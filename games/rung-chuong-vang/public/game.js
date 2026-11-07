/* ===================================================
   RUNG CHUÔNG VÀNG TIKTOK LIVE - GAME CLIENT ENGINE
   =================================================== */

// Khởi tạo Socket.IO
const socket = io();

// Các phần tử DOM chính
const stage = document.getElementById('game-stage');
const fxCanvas = document.getElementById('fx-canvas');
const ctx = fxCanvas.getContext('2d');

const aliveCountEl = document.getElementById('alive-count');
const totalCountEl = document.getElementById('total-count');
const roundBadgeEl = document.getElementById('round-badge');
const diffBadgeEl = document.getElementById('difficulty-badge');
const timerCircleEl = document.getElementById('timer-circle');
const timerNumEl = document.getElementById('timer-num');
const energyPercentEl = document.getElementById('energy-percent');
const energyBarFillEl = document.getElementById('energy-bar-fill');

const questionTextEl = document.getElementById('question-text');
const optBtns = [
  document.getElementById('opt-0'),
  document.getElementById('opt-1'),
  document.getElementById('opt-2'),
  document.getElementById('opt-3')
];
const optTexts = [
  document.getElementById('opt-text-0'),
  document.getElementById('opt-text-1'),
  document.getElementById('opt-text-2'),
  document.getElementById('opt-text-3')
];
const optCounts = [
  document.getElementById('opt-count-0'),
  document.getElementById('opt-count-1'),
  document.getElementById('opt-count-2'),
  document.getElementById('opt-count-3')
];

const arenaGrid = document.getElementById('arena-grid');
const topScholarsEl = document.getElementById('top-scholars');
const topRescuersEl = document.getElementById('top-rescuers');

// Modals
const revealOverlay = document.getElementById('reveal-overlay');
const revealLetterEl = document.getElementById('reveal-letter');
const revealExplainEl = document.getElementById('reveal-explain');
const statSurvivedEl = document.getElementById('stat-survived');
const statEliminatedEl = document.getElementById('stat-eliminated');

const rescueOverlay = document.getElementById('rescue-overlay');
const rescueTimerNumEl = document.getElementById('rescue-timer-num');

const victoryOverlay = document.getElementById('victory-overlay');
const winnersContainer = document.getElementById('winners-container');

// Dữ liệu nội bộ
let currentState = null;
const seats = []; // Mảng 100 ghế DOM
let particles = [];
let animFrameId = null;

// ===================================================
// 1. TỰ ĐỘNG CO GIÃN MÀN HÌNH (RESPONSIVE FIT 1080x1920)
// ===================================================
function resizeStage() {
  const targetW = 1080;
  const targetH = 1920;
  const windowW = window.innerWidth;
  const windowH = window.innerHeight;

  const scale = Math.min(windowW / targetW, windowH / targetH);
  stage.style.transform = `scale(${scale})`;

  fxCanvas.width = targetW;
  fxCanvas.height = targetH;
}

window.addEventListener('resize', resizeStage);
window.addEventListener('load', resizeStage);
resizeStage();

// ===================================================
// 2. TẠO 100 Ô GHẾ TRÊN SÀN ĐẤU (10 x 10)
// ===================================================
function initArenaSeats() {
  arenaGrid.innerHTML = '';
  for (let i = 0; i < 100; i++) {
    const seat = document.createElement('div');
    seat.className = 'arena-seat';
    seat.id = `seat-${i}`;
    seat.innerHTML = `<span class="seat-num">${(i + 1).toString().padStart(2, '0')}</span>`;
    arenaGrid.appendChild(seat);
    seats.push(seat);
  }
}
initArenaSeats();

// ===================================================
// 3. TỔNG HỢP ÂM THANH (WEB AUDIO API & TTS)
// ===================================================
let audioCtx = null;
function getAudioContext() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  return audioCtx;
}

// Phát TTS tiếng Việt
let currentAudio = null;
function playTts(text) {
  try {
    if (!text) return;
    if (currentAudio) {
      currentAudio.pause();
      currentAudio = null;
    }
    const url = `/api/tts?text=${encodeURIComponent(text)}`;
    currentAudio = new Audio(url);
    currentAudio.play().catch(() => {});
  } catch (e) {}
}

// Âm thanh tích tắc đếm ngược
function soundTick() {
  try {
    const ctx = getAudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(800, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(400, ctx.currentTime + 0.04);
    gain.gain.setValueAtTime(0.12, ctx.currentTime);
    gain.gain.linearRampToValueAtTime(0, ctx.currentTime + 0.04);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.04);
  } catch (e) {}
}

// Âm thanh Chuông Đồng Vàng ngân vang
function soundBell() {
  try {
    const ctx = getAudioContext();
    const freqs = [587.33, 880, 1174.66, 1760]; // Hòa âm chuông vàng
    freqs.forEach(f => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.value = f;
      gain.gain.setValueAtTime(0.2, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 2.5);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 2.5);
    });
  } catch (e) {}
}

// Âm thanh trả lời đúng
function soundCorrect() {
  try {
    const ctx = getAudioContext();
    const now = ctx.currentTime;
    [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.frequency.value = freq;
      gain.gain.setValueAtTime(0.15, now + idx * 0.08);
      gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.3);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now + idx * 0.08);
      osc.stop(now + idx * 0.08 + 0.3);
    });
  } catch (e) {}
}

// Âm thanh loại / sét đánh
function soundBuzzer() {
  try {
    const ctx = getAudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(160, ctx.currentTime);
    osc.frequency.linearRampToValueAtTime(80, ctx.currentTime + 0.4);
    gain.gain.setValueAtTime(0.2, ctx.currentTime);
    gain.gain.linearRampToValueAtTime(0.01, ctx.currentTime + 0.4);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.4);
  } catch (e) {}
}

// Âm thanh hồi sinh
function soundRevive() {
  try {
    const ctx = getAudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(200, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(1200, ctx.currentTime + 0.6);
    gain.gain.setValueAtTime(0.25, ctx.currentTime);
    gain.gain.linearRampToValueAtTime(0.01, ctx.currentTime + 0.6);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.6);
  } catch (e) {}
}

// ===================================================
// 4. HIỆU ỨNG HẠT PARTICLE (CANVAS PHÁO HOA & SPARKLES)
// ===================================================
class Particle {
  constructor(x, y, color) {
    this.x = x;
    this.y = y;
    this.color = color;
    this.radius = Math.random() * 6 + 3;
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 12 + 4;
    this.vx = Math.cos(angle) * speed;
    this.vy = Math.sin(angle) * speed;
    this.gravity = 0.35;
    this.alpha = 1;
    this.decay = Math.random() * 0.02 + 0.012;
  }
  update() {
    this.vx *= 0.98;
    this.vy += this.gravity;
    this.x += this.vx;
    this.y += this.vy;
    this.alpha -= this.decay;
  }
  draw(ctx) {
    ctx.save();
    ctx.globalAlpha = Math.max(0, this.alpha);
    ctx.fillStyle = this.color;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }
}

function spawnFireworks(x, y, count = 60) {
  const colors = ['#ffd700', '#ff3b5c', '#00f2fe', '#2ecc71', '#ffffff', '#ff9900'];
  for (let i = 0; i < count; i++) {
    const col = colors[Math.floor(Math.random() * colors.length)];
    particles.push(new Particle(x, y, col));
  }
}

function loopFX() {
  ctx.clearRect(0, 0, fxCanvas.width, fxCanvas.height);
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.update();
    p.draw(ctx);
    if (p.alpha <= 0) particles.splice(i, 1);
  }
  animFrameId = requestAnimationFrame(loopFX);
}
loopFX();

// ===================================================
// 5. CẬP NHẬT TRẠNG THÁI SÀN ĐẤU & GIAO DIỆN
// ===================================================
function renderPlayers(players) {
  // Xóa sạch trạng thái cũ của các ghế
  seats.forEach((seat, idx) => {
    seat.className = 'arena-seat';
    seat.innerHTML = `<span class="seat-num">${(idx + 1).toString().padStart(2, '0')}</span>`;
  });

  if (!players || !Array.isArray(players)) return;

  const letterLabels = ['A', 'B', 'C', 'D'];
  const answerCounts = [0, 0, 0, 0];
  let aliveTally = 0;

  players.forEach(p => {
    const idx = p.seatIndex;
    if (idx < 0 || idx >= 100) return;
    const seatEl = seats[idx];

    let cls = 'arena-seat occupied';
    if (p.status === 'eliminated') {
      cls += ' eliminated';
    } else {
      aliveTally++;
      if (p.answer !== null && p.answer !== undefined) {
        answerCounts[p.answer]++;
      }
    }

    seatEl.className = cls;
    let inner = `<img class="seat-avatar" src="${p.avatar}" alt="${p.nickname}" onerror="this.src='https://api.dicebear.com/7.x/bottts/svg?seed=${p.uniqueId}'">`;
    if (p.status === 'alive' && p.answer !== null && p.answer !== undefined) {
      inner += `<div class="seat-ans-tag">${letterLabels[p.answer]}</div>`;
    }
    seatEl.innerHTML = inner;
  });

  aliveCountEl.innerText = aliveTally;
  totalCountEl.innerText = players.length;

  // Tính phần trăm đáp án chọn
  const totalAnswers = answerCounts.reduce((a, b) => a + b, 0);
  for (let i = 0; i < 4; i++) {
    const pct = totalAnswers > 0 ? Math.round((answerCounts[i] / totalAnswers) * 100) : 0;
    optCounts[i].innerText = `${pct}%`;
  }
}

function updateLeaderboard(topScholars, topRescuers) {
  // Top Thần Đồng
  if (topScholars && topScholars.length > 0) {
    topScholarsEl.innerHTML = topScholars.slice(0, 3).map((s, i) => `
      <div class="lb-item">
        <span class="lb-name">
          <img class="lb-avatar" src="${s.avatar}" onerror="this.src='https://api.dicebear.com/7.x/bottts/svg?seed=${s.nickname}'">
          #${i + 1} ${s.nickname}
        </span>
        <span class="lb-val">${s.score}đ (🔥${s.streak})</span>
      </div>
    `).join('');
  } else {
    topScholarsEl.innerHTML = '<span class="lb-empty">Chưa có bảng vàng</span>';
  }

  // Top Cứu Trợ
  if (topRescuers && topRescuers.length > 0) {
    topRescuersEl.innerHTML = topRescuers.slice(0, 3).map((r, i) => `
      <div class="lb-item">
        <span class="lb-name">❤️ #${i + 1} ${r.nickname}</span>
        <span class="lb-val">${r.diamonds} 💎</span>
      </div>
    `).join('');
  } else {
    topRescuersEl.innerHTML = '<span class="lb-empty">Thả tim & Tặng quà</span>';
  }
}

// ===================================================
// 6. XỬ LÝ CÁC SỰ KIỆN SOCKET.IO
// ===================================================

// Nhận đồng bộ trạng thái toàn cục
socket.on('game_state', state => {
  currentState = state;
  aliveCountEl.innerText = state.aliveCount;
  totalCountEl.innerText = state.totalPlayers;
  energyPercentEl.innerText = `${Math.round((state.rescueEnergy / state.maxEnergy) * 100)}%`;
  energyBarFillEl.style.width = `${(state.rescueEnergy / state.maxEnergy) * 100}%`;

  if (state.currentQuestion) {
    roundBadgeEl.innerText = `CÂU ${state.currentQuestion.index} / ${state.totalQuestions}`;
    questionTextEl.innerText = state.currentQuestion.question;
    state.currentQuestion.options.forEach((opt, idx) => {
      optTexts[idx].innerText = opt;
    });

    const diff = state.currentQuestion.difficulty;
    if (diff === 1) {
      diffBadgeEl.className = 'diff-badge diff-easy';
      diffBadgeEl.innerText = 'CƠ BẢN';
    } else if (diff === 2) {
      diffBadgeEl.className = 'diff-badge diff-medium';
      diffBadgeEl.innerText = 'TRUNG BÌNH';
    } else {
      diffBadgeEl.className = 'diff-badge diff-hard';
      diffBadgeEl.innerText = 'CỰC KHÓ';
    }
  }

  renderPlayers(state.players);
  updateLeaderboard(state.topPlayers, state.topRescuers);
});

// Bắt đầu một câu hỏi mới
socket.on('question_start', data => {
  revealOverlay.classList.add('hidden');
  rescueOverlay.classList.add('hidden');
  victoryOverlay.classList.add('hidden');

  // Xóa class highlight đúng/sai ở các nút chọn
  optBtns.forEach(btn => btn.className = 'option-btn');

  roundBadgeEl.innerText = `CÂU ${data.question.index} / ${data.question.total}`;
  questionTextEl.innerText = data.question.question;
  data.question.options.forEach((opt, idx) => {
    optTexts[idx].innerText = opt;
    optCounts[idx].innerText = '0%';
  });

  const diff = data.question.difficulty;
  if (diff === 1) {
    diffBadgeEl.className = 'diff-badge diff-easy';
    diffBadgeEl.innerText = 'CƠ BẢN';
  } else if (diff === 2) {
    diffBadgeEl.className = 'diff-badge diff-medium';
    diffBadgeEl.innerText = 'TRUNG BÌNH';
  } else {
    diffBadgeEl.className = 'diff-badge diff-hard';
    diffBadgeEl.innerText = 'CỰC KHÓ';
  }

  timerNumEl.innerText = data.timer;
  soundBell();

  // Đọc câu hỏi bằng giọng đọc tiếng Việt TTS
  playTts(`Câu hỏi số ${data.question.index}: ${data.question.question}`);
});

// Đếm ngược từng giây
socket.on('timer_tick', data => {
  timerNumEl.innerText = data.timer;
  if (data.timer <= 5 && data.timer > 0) {
    soundTick();
  }
});

// Cập nhật người chơi trả lời
socket.on('player_answered', data => {
  const seatEl = seats[data.seatIndex];
  if (seatEl) {
    let tag = seatEl.querySelector('.seat-ans-tag');
    const letters = ['A', 'B', 'C', 'D'];
    if (!tag) {
      tag = document.createElement('div');
      tag.className = 'seat-ans-tag';
      seatEl.appendChild(tag);
    }
    tag.innerText = letters[data.answer];
  }
});

// Công bố kết quả câu hỏi
socket.on('question_reveal', data => {
  // Highlight nút đúng / sai
  optBtns.forEach((btn, idx) => {
    if (idx === data.correctIndex) {
      btn.className = 'option-btn opt-correct';
    } else {
      btn.className = 'option-btn opt-wrong';
    }
  });

  // Hiển thị popup công bố kết quả
  revealLetterEl.innerText = data.correctLetter;
  revealExplainEl.innerText = data.explanation;
  statSurvivedEl.innerText = data.aliveCount;
  statEliminatedEl.innerText = data.eliminated.length;
  revealOverlay.classList.remove('hidden');

  // Đánh dấu người bị loại trên sàn đấu
  data.eliminated.forEach(p => {
    const seatEl = seats[p.seatIndex];
    if (seatEl) seatEl.className = 'arena-seat occupied eliminated';
  });

  // Âm thanh
  if (data.eliminated.length > 0) {
    soundBuzzer();
  } else {
    soundCorrect();
  }

  // Tự động đóng popup sau 4.5 giây
  setTimeout(() => {
    revealOverlay.classList.add('hidden');
  }, 4500);
});

// Bắt đầu vòng cứu trợ
socket.on('rescue_round_start', data => {
  revealOverlay.classList.add('hidden');
  rescueTimerNumEl.innerText = data.timer;
  rescueOverlay.classList.remove('hidden');
  soundBuzzer();
  playTts("Sàn đấu thất thủ! Xin mời quý khán giả hãy thả tim hoặc tặng quà để cứu trợ các thí sinh!");
});

// Đếm ngược vòng cứu trợ
socket.on('rescue_timer_tick', data => {
  rescueTimerNumEl.innerText = data.timer;
  if (data.timer <= 5) soundTick();
});

// Kết thúc vòng cứu trợ
socket.on('rescue_round_end', data => {
  rescueOverlay.classList.add('hidden');
  if (data.success) {
    soundRevive();
    spawnFireworks(540, 960, 100);
    playTts(`Cứu trợ thành công! Hiện có ${data.aliveCount} thí sinh quay trở lại sàn thi đấu!`);
  }
});

// Sự kiện có thí sinh được hồi sinh
socket.on('rescue_occurred', data => {
  soundRevive();
  spawnFireworks(540, 960, 80);

  if (data.rescuedPlayers && Array.isArray(data.rescuedPlayers)) {
    data.rescuedPlayers.forEach(p => {
      const seatEl = seats[p.seatIndex];
      if (seatEl) {
        seatEl.className = 'arena-seat occupied revived';
        setTimeout(() => { seatEl.className = 'arena-seat occupied'; }, 1500);
      }
    });
  }

  if (data.type === 'vip') {
    playTts(`Đại hiệp ${data.rescuer} đã tặng ${data.giftName}, giải cứu toàn bộ sàn thi đấu!`);
  } else if (data.type === 'self') {
    playTts(`Thí sinh ${data.rescuer} đã tặng quà và tự hồi sinh thành công!`);
  }
});

// Cập nhật thanh năng lượng tim
socket.on('energy_update', data => {
  const pct = Math.round((data.rescueEnergy / data.maxEnergy) * 100);
  energyPercentEl.innerText = `${pct}%`;
  energyBarFillEl.style.width = `${pct}%`;
});

// ĐỈNH CAO: RUNG CHUÔNG VÀNG (VICTORY)
socket.on('bell_ringing', data => {
  revealOverlay.classList.add('hidden');
  rescueOverlay.classList.add('hidden');

  winnersContainer.innerHTML = '';
  if (data.winners && data.winners.length > 0) {
    data.winners.forEach(w => {
      const card = document.createElement('div');
      card.className = 'winner-card';
      card.innerHTML = `
        <img class="winner-avatar" src="${w.avatar}" onerror="this.src='https://api.dicebear.com/7.x/bottts/svg?seed=${w.nickname}'">
        <div class="winner-info">
          <span class="winner-name">👑 ${w.nickname}</span>
          <span class="winner-score">${w.score} Điểm (Chuỗi: ${w.streak})</span>
        </div>
      `;
      winnersContainer.appendChild(card);
    });
  }

  victoryOverlay.classList.remove('hidden');

  // Âm thanh chuông vàng liên hồi và pháo hoa rực rỡ
  soundBell();
  setTimeout(soundBell, 800);
  setTimeout(soundBell, 1600);

  // Bắn pháo hoa liên tiếp
  for (let i = 0; i < 6; i++) {
    setTimeout(() => {
      const x = 200 + Math.random() * 680;
      const y = 300 + Math.random() * 700;
      spawnFireworks(x, y, 90);
    }, i * 500);
  }

  const winnerNames = data.winners.map(w => w.nickname).join(', ');
  playTts(`Chúc mừng tân trạng nguyên: ${winnerNames} đã xuất sắc rung chuông vàng thành công!`);
});

// Tự động yêu cầu dữ liệu khi kết nối
socket.on('connect', () => {
  socket.emit('get_state');
});
