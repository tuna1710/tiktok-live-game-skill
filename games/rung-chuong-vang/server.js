require('dotenv').config();
const path = require('path');
const http = require('http');
const express = require('express');
const cors = require('cors');
const { Server } = require('socket.io');
const { TikTokLiveConnection } = require('tiktok-live-connector');
const fs = require('fs');

const PORT = Number(process.env.PORT) || 3000;
const TIKTOK_USERNAME = process.env.TIKTOK_USERNAME || '';
const QUESTION_DURATION = Number(process.env.QUESTION_DURATION) || 20;
const RESCUE_DURATION = 20;
const TOTAL_QUESTIONS = Number(process.env.TOTAL_QUESTIONS) || 15;

// Load questions database
const questionsFilePath = path.join(__dirname, 'data', 'questions.json');
let allQuestions = [];
try {
  allQuestions = JSON.parse(fs.readFileSync(questionsFilePath, 'utf8'));
  console.log(`[RungChuongVang] Loaded ${allQuestions.length} questions from data/questions.json`);
} catch (err) {
  console.error('[RungChuongVang] Error loading questions:', err);
  allQuestions = [
    {
      id: 1,
      difficulty: 1,
      question: "Thủ đô của Việt Nam là gì?",
      options: ["Hà Nội", "Đà Nẵng", "TP. Hồ Chí Minh", "Cần Thơ"],
      correct: 0,
      explanation: "Hà Nội là thủ đô của Việt Nam."
    }
  ];
}

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

const https = require('https');
const ttsCache = new Map();

// TTS Proxy tiếng Việt trực tiếp (Tránh lỗi CORS/Referer của Google Translate)
app.get('/api/tts', (req, res) => {
  const text = (req.query.text || '').toString().trim().slice(0, 180);
  if (!text) return res.status(400).send('Missing text');

  // Kiểm tra bộ nhớ đệm
  if (ttsCache.has(text)) {
    const cachedBuffer = ttsCache.get(text);
    res.setHeader('Content-Type', 'audio/mpeg');
    res.setHeader('Content-Length', cachedBuffer.length);
    res.setHeader('Cache-Control', 'public, max-age=86400');
    return res.end(cachedBuffer);
  }

  const googleTtsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=vi&client=tw-ob&q=${encodeURIComponent(text)}`;
  https.get(googleTtsUrl, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
      'Referer': 'https://translate.google.com/'
    }
  }, (ttsRes) => {
    if (ttsRes.statusCode !== 200) {
      console.error(`[TTS] Lỗi phản hồi Google TTS status: ${ttsRes.statusCode}`);
      return res.status(502).send('TTS upstream error');
    }

    const chunks = [];
    ttsRes.on('data', chunk => chunks.push(chunk));
    ttsRes.on('end', () => {
      const audioBuffer = Buffer.concat(chunks);
      if (audioBuffer.length > 500) {
        ttsCache.set(text, audioBuffer);
      }
      res.setHeader('Content-Type', 'audio/mpeg');
      res.setHeader('Content-Length', audioBuffer.length);
      res.setHeader('Cache-Control', 'public, max-age=86400');
      res.end(audioBuffer);
    });
  }).on('error', err => {
    console.error('[TTS] Network error:', err.message);
    res.status(500).send('TTS fetch error');
  });
});

// API lấy thông tin câu hỏi
app.get('/api/questions', (req, res) => {
  res.json({ total: allQuestions.length, data: allQuestions });
});

// ==========================================
// GAME MANAGER (Quản lý logic Rung Chuông Vàng)
// ==========================================
class GoldenBellGame {
  constructor(ioInstance) {
    this.io = ioInstance;
    this.status = 'WAITING'; // WAITING, QUESTION, REVEAL, RESCUE, VICTORY, GAME_OVER
    this.currentQuestionIndex = 0;
    this.totalQuestions = Math.min(TOTAL_QUESTIONS, allQuestions.length);
    this.questionTimer = QUESTION_DURATION;
    this.rescueTimer = RESCUE_DURATION;
    this.rescueEnergy = 0; // 0 - 1000
    this.maxEnergy = 1000;
    this.timerInterval = null;

    // Danh sách thí sinh: uniqueId -> Player Object
    // Player: { uniqueId, nickname, profilePictureUrl, seatIndex, status: 'alive'|'eliminated', answer: null, streak: 0, score: 0 }
    this.players = new Map();
    this.nextSeat = 0;
    this.maxSeats = 100;

    // Thống kê & Quán quân
    this.bellWinners = [];
    this.rescuers = new Map(); // uniqueId -> { nickname, count }
    this.rescuedInThisRound = 0; // Đếm chính xác số người thực tế được cứu trong vòng cứu trợ

    // Xáo trộn câu hỏi
    this.gameQuestions = this.pickQuestions();
    this.currentQuestion = null;
  }

  pickQuestions() {
    // Sắp xếp câu hỏi theo độ khó tăng dần
    const easy = allQuestions.filter(q => q.difficulty === 1).sort(() => 0.5 - Math.random());
    const medium = allQuestions.filter(q => q.difficulty === 2).sort(() => 0.5 - Math.random());
    const hard = allQuestions.filter(q => q.difficulty === 3).sort(() => 0.5 - Math.random());

    const result = [
      ...easy.slice(0, 5),
      ...medium.slice(0, 6),
      ...hard.slice(0, 4)
    ];

    // Bổ sung nếu chưa đủ
    if (result.length < this.totalQuestions) {
      const remaining = allQuestions.filter(q => !result.includes(q));
      result.push(...remaining.slice(0, this.totalQuestions - result.length));
    }
    return result.slice(0, this.totalQuestions);
  }

  getAliveCount() {
    let count = 0;
    for (const p of this.players.values()) {
      if (p.status === 'alive') count++;
    }
    return count;
  }

  getTotalPlayers() {
    return this.players.size;
  }

  registerPlayer(uniqueId, nickname, avatar) {
    if (!uniqueId) return null;
    let player = this.players.get(uniqueId);
    if (!player) {
      const seat = this.nextSeat < this.maxSeats ? this.nextSeat++ : Math.floor(Math.random() * this.maxSeats);
      // QUY TẮC RUNG CHUÔNG VÀNG:
      // Thí sinh chỉ được vào trạng thái 'alive' khi ván đang ở trạng thái WAITING hoặc ở CÂU 1.
      // Nếu ván đấu đã qua câu 1 hoặc đang diễn ra, người mới vào sẽ ở trạng thái 'eliminated' (chờ ván sau hoặc tặng quà để vào).
      const isAtInitialRound = (this.status === 'WAITING' || this.currentQuestionIndex === 0);
      const initialStatus = isAtInitialRound ? 'alive' : 'eliminated';

      player = {
        uniqueId,
        nickname: nickname || `Thí sinh ${seat + 1}`,
        profilePictureUrl: avatar || 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7339798083893821445~c5_100x100.jpeg',
        seatIndex: seat,
        status: initialStatus,
        answer: null,
        streak: 0,
        score: 0
      };
      this.players.set(uniqueId, player);
      this.broadcastState();
      this.io.emit('player_joined', player);
    }
    return player;
  }

  submitAnswer(uniqueId, rawText) {
    if (this.status !== 'QUESTION') return;
    const player = this.players.get(uniqueId);
    if (!player || player.status !== 'alive') return;

    const clean = rawText.toString().trim().toUpperCase();
    let choice = null;
    if (['A', '1', 'ĐÁP ÁN A', 'CÂU A'].includes(clean)) choice = 0;
    else if (['B', '2', 'ĐÁP ÁN B', 'CÂU B'].includes(clean)) choice = 1;
    else if (['C', '3', 'ĐÁP ÁN C', 'CÂU C'].includes(clean)) choice = 2;
    else if (['D', '4', 'ĐÁP ÁN D', 'CÂU D'].includes(clean)) choice = 3;

    if (choice !== null) {
      player.answer = choice;
      this.io.emit('player_answered', {
        uniqueId: player.uniqueId,
        seatIndex: player.seatIndex,
        answer: choice
      });
    }
  }

  addLikes(count) {
    this.rescueEnergy = Math.min(this.maxEnergy, this.rescueEnergy + count);
    this.io.emit('energy_update', {
      rescueEnergy: this.rescueEnergy,
      maxEnergy: this.maxEnergy
    });

    // Tự động cứu người khi đầy bình năng lượng (1.000 tim)
    if (this.rescueEnergy >= this.maxEnergy) {
      this.rescueEnergy = 0;
      this.triggerEnergyRescue();
    }
  }

  triggerEnergyRescue() {
    const eliminated = Array.from(this.players.values()).filter(p => p.status === 'eliminated');
    if (eliminated.length === 0) return;

    // Cứu tối đa 3 người ngẫu nhiên
    const rescued = eliminated.sort(() => 0.5 - Math.random()).slice(0, 3);
    rescued.forEach(p => {
      p.status = 'alive';
      p.answer = null;
    });

    this.rescuedInThisRound += rescued.length;

    this.io.emit('rescue_occurred', {
      type: 'energy',
      rescuedCount: rescued.length,
      rescuedPlayers: rescued.map(p => ({ uniqueId: p.uniqueId, nickname: p.nickname, seatIndex: p.seatIndex }))
    });
    this.broadcastState();
  }

  handleGift(uniqueId, nickname, giftName, diamondCount, avatar) {
    // Đảm bảo người chơi tồn tại
    let player = this.registerPlayer(uniqueId, nickname, avatar);

    // Cập nhật bảng vinh danh người cứu trợ
    const rescuer = this.rescuers.get(uniqueId) || { nickname, count: 0, diamonds: 0 };
    rescuer.count += 1;
    rescuer.diamonds += (diamondCount || 1);
    this.rescuers.set(uniqueId, rescuer);

    // Logic hồi sinh bằng quà tặng
    if (diamondCount >= 100 || giftName.includes('Pháo hoa') || giftName.includes('Sư tử')) {
      // Quà VIP: CỨU TẤT CẢ
      const count = this.rescueAll();
      this.io.emit('rescue_occurred', {
        type: 'vip',
        rescuer: nickname,
        giftName,
        rescuedCount: count
      });
    } else {
      // Quà bình thường: Hồi sinh bản thân nếu bị loại
      if (player && player.status === 'eliminated') {
        player.status = 'alive';
        player.answer = null;
        this.rescuedInThisRound += 1;
        this.io.emit('rescue_occurred', {
          type: 'self',
          rescuer: nickname,
          giftName,
          rescuedPlayers: [{ uniqueId: player.uniqueId, nickname: player.nickname, seatIndex: player.seatIndex }]
        });
      } else if (player) {
        // Tặng điểm khích lệ nếu đang còn sống
        player.score += 50;
      }
    }
    this.broadcastState();
  }

  rescueAll() {
    let count = 0;
    for (const p of this.players.values()) {
      if (p.status === 'eliminated') {
        p.status = 'alive';
        p.answer = null;
        count++;
      }
    }
    this.rescuedInThisRound += count;
    this.broadcastState();
    return count;
  }

  startGame() {
    console.log('[Game] Bắt đầu ván chơi mới từ CÂU 1!');
    this.status = 'WAITING';
    this.currentQuestionIndex = 0;
    this.gameQuestions = this.pickQuestions();
    this.bellWinners = [];
    this.rescuedInThisRound = 0;
    this.rescueEnergy = 0;

    // Reset toàn bộ thí sinh quay lại sàn đấu với trạng thái 'alive'
    for (const p of this.players.values()) {
      p.status = 'alive';
      p.answer = null;
      p.streak = 0;
      p.score = 0;
    }

    this.broadcastState();
    this.io.emit('game_reset', { message: "Ván mới bắt đầu lại từ CÂU 1! Tất cả thí sinh trở lại sàn đấu." });
    this.nextQuestion();
  }

  nextQuestion() {
    if (this.currentQuestionIndex >= this.totalQuestions) {
      this.finishGame();
      return;
    }

    // Xóa đáp án vòng trước của thí sinh còn sống
    for (const p of this.players.values()) {
      if (p.status === 'alive') {
        p.answer = null;
      }
    }

    this.status = 'QUESTION';
    this.currentQuestion = this.gameQuestions[this.currentQuestionIndex];
    this.questionTimer = QUESTION_DURATION;

    // Phát câu hỏi cho client (LƯỢC BỎ đáp án đúng để client không gian lận)
    const publicQuestion = {
      id: this.currentQuestion.id,
      index: this.currentQuestionIndex + 1,
      total: this.totalQuestions,
      question: this.currentQuestion.question,
      options: this.currentQuestion.options,
      difficulty: this.currentQuestion.difficulty
    };

    this.io.emit('question_start', {
      question: publicQuestion,
      timer: this.questionTimer,
      aliveCount: this.getAliveCount(),
      totalPlayers: this.getTotalPlayers()
    });

    this.startQuestionTimer();
  }

  startQuestionTimer() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    this.timerInterval = setInterval(() => {
      this.questionTimer--;
      this.io.emit('timer_tick', { timer: this.questionTimer });

      if (this.questionTimer <= 0) {
        clearInterval(this.timerInterval);
        this.revealAnswer();
      }
    }, 1000);
  }

  revealAnswer() {
    if (this.timerInterval) clearInterval(this.timerInterval);
    this.status = 'REVEAL';

    const correctIdx = this.currentQuestion.correct;
    const correctLetter = ['A', 'B', 'C', 'D'][correctIdx];
    const newlyEliminated = [];
    const correctPlayers = [];

    for (const p of this.players.values()) {
      if (p.status === 'alive') {
        if (p.answer === correctIdx) {
          p.streak += 1;
          p.score += 10 * p.streak;
          correctPlayers.push(p);
        } else {
          p.status = 'eliminated';
          p.streak = 0;
          newlyEliminated.push(p);
        }
      }
    }

    const aliveCount = this.getAliveCount();

    this.io.emit('question_reveal', {
      correctIndex: correctIdx,
      correctLetter,
      explanation: this.currentQuestion.explanation,
      eliminated: newlyEliminated.map(p => ({ uniqueId: p.uniqueId, nickname: p.nickname, seatIndex: p.seatIndex, answer: p.answer })),
      corrects: correctPlayers.map(p => ({ uniqueId: p.uniqueId, nickname: p.nickname, seatIndex: p.seatIndex })),
      aliveCount,
      totalPlayers: this.getTotalPlayers()
    });

    // Chờ 5 giây xem kết quả, sau đó quyết định bước tiếp theo
    setTimeout(() => {
      this.handlePostReveal(aliveCount);
    }, 5000);
  }

  handlePostReveal(aliveCount) {
    // 1. Nếu không còn ai sống sót: Kích hoạt Vòng Cứu Trợ
    if (aliveCount === 0) {
      this.startRescueRound();
      return;
    }

    // 2. Nếu đã hoàn thành câu hỏi cuối cùng: RUNG CHUÔNG VÀNG
    if (this.currentQuestionIndex === this.totalQuestions - 1) {
      this.finishGame();
      return;
    }

    // 3. Nếu số người còn lại quá ít (<= 2 người) ở mốc câu 5, 10: Có thể kích hoạt cứu trợ nhanh
    if (aliveCount <= 2 && (this.currentQuestionIndex === 4 || this.currentQuestionIndex === 9)) {
      this.startRescueRound();
      return;
    }

    // Tiếp tục câu tiếp theo
    this.currentQuestionIndex++;
    this.nextQuestion();
  }

  startRescueRound() {
    this.status = 'RESCUE';
    this.rescueTimer = RESCUE_DURATION;
    this.rescuedInThisRound = 0; // Đặt lại số người thực tế được cứu

    this.io.emit('rescue_round_start', {
      timer: this.rescueTimer,
      message: "SÀN ĐẤU THẤT THỦ! Hãy Thả Tim hoặc Tặng Quà để HỒI SINH các thí sinh!"
    });

    if (this.timerInterval) clearInterval(this.timerInterval);
    this.timerInterval = setInterval(() => {
      this.rescueTimer--;
      this.io.emit('rescue_timer_tick', { timer: this.rescueTimer });

      if (this.rescueTimer <= 0) {
        clearInterval(this.timerInterval);
        const aliveCount = this.getAliveCount();

        // CHỈ TIẾP TỤC NẾU CÓ NGƯỜI THỰC SỰ ĐƯỢC CỨU (qua Tim hoặc Quà)
        if (this.rescuedInThisRound > 0 && aliveCount > 0) {
          console.log(`[Rescue] Cứu trợ thành công: ${this.rescuedInThisRound} người được cứu.`);
          this.io.emit('rescue_round_end', { success: true, aliveCount });
          setTimeout(() => {
            this.currentQuestionIndex++;
            this.nextQuestion();
          }, 3000);
        } else {
          // KHÔNG CÓ AI HỒI SINH -> SÀN ĐẤU THẤT THỦ HOÀN TOÀN -> BẮT BUỘC RESET VỀ CÂU 1
          console.log('[Rescue] Không có ai được cứu trợ. Reset ván chơi về CÂU 1!');
          this.status = 'GAME_OVER';
          this.io.emit('game_over', {
            message: "KHÔNG CÓ AI HỒI SINH! Sàn đấu thất thủ. Trò chơi bắt đầu lại từ CÂU 1!",
            topScores: this.getTopPlayers()
          });
          setTimeout(() => {
            this.startGame(); // Reset hoàn toàn về CÂU 1
          }, 5000);
        }
      }
    }, 1000);
  }

  finishGame() {
    this.status = 'VICTORY';
    const winners = Array.from(this.players.values()).filter(p => p.status === 'alive');
    this.bellWinners = winners;

    this.io.emit('bell_ringing', {
      winners: winners.map(w => ({
        uniqueId: w.uniqueId,
        nickname: w.nickname,
        avatar: w.profilePictureUrl,
        score: w.score,
        streak: w.streak
      })),
      message: "CHÚC MỪNG QUÁN QUÂN ĐÃ RUNG CHUÔNG VÀNG THÀNH CÔNG!"
    });

    // Tự động chuyển ván mới sau 12 giây vinh danh
    setTimeout(() => {
      this.startGame();
    }, 12000);
  }

  getTopPlayers() {
    return Array.from(this.players.values())
      .sort((a, b) => b.score - a.score)
      .slice(0, 5)
      .map(p => ({ nickname: p.nickname, score: p.score, streak: p.streak, avatar: p.profilePictureUrl }));
  }

  getTopRescuers() {
    return Array.from(this.rescuers.values())
      .sort((a, b) => b.diamonds - a.diamonds)
      .slice(0, 5);
  }

  getState() {
    return {
      status: this.status,
      currentQuestionIndex: this.currentQuestionIndex,
      totalQuestions: this.totalQuestions,
      questionTimer: this.questionTimer,
      rescueTimer: this.rescueTimer,
      rescueEnergy: this.rescueEnergy,
      maxEnergy: this.maxEnergy,
      aliveCount: this.getAliveCount(),
      totalPlayers: this.getTotalPlayers(),
      currentQuestion: this.currentQuestion ? {
        id: this.currentQuestion.id,
        index: this.currentQuestionIndex + 1,
        total: this.totalQuestions,
        question: this.currentQuestion.question,
        options: this.currentQuestion.options,
        difficulty: this.currentQuestion.difficulty
      } : null,
      players: Array.from(this.players.values()).map(p => ({
        uniqueId: p.uniqueId,
        nickname: p.nickname,
        avatar: p.profilePictureUrl,
        seatIndex: p.seatIndex,
        status: p.status,
        answer: p.answer,
        score: p.score,
        streak: p.streak
      })),
      topPlayers: this.getTopPlayers(),
      topRescuers: this.getTopRescuers()
    };
  }

  broadcastState() {
    this.io.emit('game_state', this.getState());
  }
}

// Khởi tạo Game Manager
const game = new GoldenBellGame(io);

// ==========================================
// KẾT NỐI TIKTOK LIVE REALTIME
// ==========================================
let tiktokLive = null;
if (TIKTOK_USERNAME) {
  try {
    const cleanUsername = TIKTOK_USERNAME.replace('@', '').trim();
    tiktokLive = new TikTokLiveConnection(cleanUsername, {});
    tiktokLive.connect()
      .then(state => {
        console.log(`[TikTokLive] Đã kết nối phòng Live: ${state.roomId} (User: @${cleanUsername})`);
      })
      .catch(err => {
        console.log(`[TikTokLive] Không thể kết nối TikTok Live: ${err.message}`);
      });

    tiktokLive.on('chat', data => {
      const uniqueId = data.user?.displayId || data.user?.id || data.uniqueId || `user_${Date.now()}`;
      const nickname = data.user?.nickname || data.nickname || 'Khán giả';
      const comment = data.content || data.comment || '';
      const avatar = data.user?.avatarThumb?.urlList?.[0] || data.profilePictureUrl || `https://api.dicebear.com/7.x/bottts/svg?seed=${uniqueId}`;

      // Tự động đăng ký người xem vào sàn đấu
      game.registerPlayer(uniqueId, nickname, avatar);
      // Xử lý câu trả lời
      game.submitAnswer(uniqueId, comment);
      io.emit('chat', {
        uniqueId,
        nickname,
        comment,
        profilePictureUrl: avatar
      });
    });

    tiktokLive.on('gift', data => {
      const uniqueId = data.user?.displayId || data.user?.id || data.uniqueId || `donor_${Date.now()}`;
      const nickname = data.user?.nickname || data.nickname || 'Khán giả';
      const giftName = data.gift?.name || data.giftDetails?.giftName || data.giftName || 'Hoa Hồng';
      const diamondCount = Number(data.gift?.diamondCount) || Number(data.diamondCount) || 1;
      const avatar = data.user?.avatarThumb?.urlList?.[0] || data.profilePictureUrl || `https://api.dicebear.com/7.x/bottts/svg?seed=${uniqueId}`;

      game.handleGift(uniqueId, nickname, giftName, diamondCount, avatar);
      io.emit('gift', {
        uniqueId,
        nickname,
        giftName,
        diamondCount,
        profilePictureUrl: avatar
      });
    });

    tiktokLive.on('like', data => {
      const count = Number(data.count) || Number(data.likeCount) || 1;
      const nickname = data.user?.nickname || data.nickname || 'Khán giả';
      const totalLikes = data.total || data.totalLikes || 0;

      game.addLikes(count);
      io.emit('like', {
        uniqueId: data.user?.id,
        nickname,
        likeCount: count,
        totalLikes
      });
    });

    tiktokLive.on('member', data => {
      const uniqueId = data.user?.displayId || data.user?.id || data.uniqueId;
      const nickname = data.user?.nickname || data.nickname;
      const avatar = data.user?.avatarThumb?.urlList?.[0] || data.profilePictureUrl;
      if (uniqueId) {
        game.registerPlayer(uniqueId, nickname, avatar);
      }
    });

  } catch (err) {
    console.error('[TikTokLive] Lỗi khởi tạo TikTok Live:', err);
  }
}

// ==========================================
// SOCKET.IO & MOCK ADMIN ENGINE
// ==========================================
io.on('connection', socket => {
  // Gửi toàn bộ trạng thái hiện tại khi client kết nối
  socket.emit('game_state', game.getState());

  // Nhận yêu cầu từ client / admin
  socket.on('get_state', () => {
    socket.emit('game_state', game.getState());
  });

  // Sự kiện giả lập từ admin.html
  socket.on('mock:chat', data => {
    game.registerPlayer(data.uniqueId, data.nickname, data.profilePictureUrl);
    game.submitAnswer(data.uniqueId, data.comment);
    io.emit('chat', data);
  });

  socket.on('mock:gift', data => {
    game.handleGift(
      data.uniqueId,
      data.nickname,
      data.giftName || 'Hoa Hồng',
      data.diamondCount || 1,
      data.profilePictureUrl
    );
    io.emit('gift', data);
  });

  socket.on('mock:like', data => {
    const count = Number(data.likeCount) || 100;
    game.addLikes(count);
    io.emit('like', { likeCount: count });
  });

  socket.on('mock:start_game', () => {
    game.startGame();
  });

  socket.on('mock:next_question', () => {
    if (game.status === 'QUESTION') {
      game.questionTimer = 1; // Rút ngắn đếm ngược để công bố ngay
    } else {
      game.currentQuestionIndex++;
      game.nextQuestion();
    }
  });

  socket.on('mock:rescue_all', () => {
    game.rescueAll();
    io.emit('rescue_occurred', {
      type: 'admin',
      rescuer: 'Quản trị viên',
      giftName: 'Đặc xá',
      rescuedCount: game.getAliveCount()
    });
  });

  socket.on('mock:reset_game', () => {
    game.startGame();
  });

  // Thêm một số bot giả lập để kiểm thử sàn đấu 100 người
  socket.on('mock:add_bots', count => {
    const botCount = Math.min(Number(count) || 20, 80);
    const vietnameseNames = [
      "Nguyễn Văn An", "Trần Thị Mai", "Lê Hoàng Nam", "Phạm Minh Tuấn", "Vũ Phương Thảo",
      "Đặng Quốc Bảo", "Bùi Thu Hà", "Đỗ Hải Đăng", "Hồ Bích Ngọc", "Ngô Trọng Hiếu",
      "Dương Thùy Linh", "Lý Thanh Tùng", "Trương Mỹ Duyên", "Mai Anh Khoa", "Võ Kim Yến",
      "Đinh Gia Huy", "Lâm Khánh Chi", "Chu Hữu Phước", "Phan Thảo Vy", "Cao Tiến Đạt"
    ];

    for (let i = 0; i < botCount; i++) {
      const id = `bot_${Date.now()}_${i}`;
      const name = vietnameseNames[i % vietnameseNames.length] + ` (#${i + 1})`;
      const avatar = `https://api.dicebear.com/7.x/bottts/svg?seed=${id}`;
      game.registerPlayer(id, name, avatar);
    }
    game.broadcastState();
  });

  // Bot ngẫu nhiên chọn đáp án A, B, C, D
  socket.on('mock:bots_answer', () => {
    for (const p of game.players.values()) {
      if (p.uniqueId.startsWith('bot_') && p.status === 'alive') {
        const randomAnswer = ['A', 'B', 'C', 'D'][Math.floor(Math.random() * 4)];
        game.submitAnswer(p.uniqueId, randomAnswer);
      }
    }
  });
});

// Tự động khởi động ván đầu tiên
setTimeout(() => {
  if (game.status === 'WAITING' && game.currentQuestionIndex === 0) {
    game.startGame();
  }
}, 3000);

server.listen(PORT, () => {
  console.log(`[RungChuongVang] Server is running at http://localhost:${PORT}`);
  console.log(`[RungChuongVang] Mở bảng giả lập tại http://localhost:${PORT}/admin.html`);
});
