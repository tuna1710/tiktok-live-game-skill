require('dotenv').config();
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const http = require('http');
const express = require('express');
const cors = require('cors');
const { Server } = require('socket.io');
const { TikTokLiveConnection } = require('tiktok-live-connector');

const PORT = Number(process.env.PORT) || 3005;
let TIKTOK_USERNAME = process.env.TIKTOK_USERNAME || '';

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Cache thư mục cho âm thanh TTS
const TTS_CACHE_DIR = path.join(__dirname, 'data', 'tts-cache');
if (!fs.existsSync(TTS_CACHE_DIR)) {
  fs.mkdirSync(TTS_CACHE_DIR, { recursive: true });
}

// Endpoint TTS tiếng Việt có MD5 disk-cache
app.get('/api/tts', (req, res) => {
  const text = (req.query.text || '').toString().trim().slice(0, 160);
  if (!text) return res.status(400).send('Missing text parameter');

  const hash = crypto.createHash('md5').update(text).digest('hex');
  const cacheFile = path.join(TTS_CACHE_DIR, `${hash}.mp3`);

  if (fs.existsSync(cacheFile)) {
    res.setHeader('Content-Type', 'audio/mpeg');
    return fs.createReadStream(cacheFile).pipe(res);
  }

  const googleTtsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=vi&client=tw-ob&q=${encodeURIComponent(text)}`;
  const https = require('https');
  https.get(googleTtsUrl, {
    headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' }
  }, (ttsRes) => {
    if (ttsRes.statusCode === 200) {
      const fileStream = fs.createWriteStream(cacheFile);
      ttsRes.pipe(fileStream);
      ttsRes.pipe(res);
      res.setHeader('Content-Type', 'audio/mpeg');
    } else {
      res.status(500).send('TTS fetch failed');
    }
  }).on('error', () => {
    res.status(500).send('TTS error');
  });
});

// Endpoint REST API tiện lợi để Giả lập / Test nhanh qua cURL hoặc Webhook
app.get('/api/mock/chat', (req, res) => {
  const user = (req.query.user || 'NguoiChoi_Test').toString();
  const comment = (req.query.comment || 'Xin quẻ').toString();
  handleComment({
    uniqueId: user.toLowerCase().replace(/\s+/g, '_'),
    nickname: user,
    comment: comment,
    profilePictureUrl: 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg'
  });
  res.json({ success: true, message: `Mock chat: ${user} -> ${comment}` });
});

app.get('/api/mock/gift', (req, res) => {
  const user = (req.query.user || 'DaiGia_Test').toString();
  const giftName = (req.query.gift || 'Hoa Hồng').toString();
  const count = Number(req.query.count) || 1;
  const diamonds = Number(req.query.diamonds) || 1;
  handleGift({
    uniqueId: user.toLowerCase().replace(/\s+/g, '_'),
    nickname: user,
    giftName: giftName,
    diamondCount: diamonds,
    repeatCount: count,
    profilePictureUrl: 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg'
  });
  res.json({ success: true, message: `Mock gift: ${user} -> ${giftName} (x${count})` });
});

// Nạp danh sách quẻ xăm
const queDbPath = path.join(__dirname, 'data', 'que_database.json');
let fortunes = [];
try {
  fortunes = JSON.parse(fs.readFileSync(queDbPath, 'utf8'));
} catch (e) {
  console.error('Không thể đọc que_database.json:', e);
}

// Quản lý hàng đợi và trạng thái game
let vipQueue = [];       // Người tặng quà được ưu tiên rút ngay
let normalQueue = [];    // Người bình luận xếp hàng
let isDrawing = false;   // Đang lắc ống / mở quẻ
let currentFortune = null;
let historyFortunes = [];
let totalCongDuc = 0;    // Điểm công đức từ quà và tim

const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

// Hàm đồng bộ trạng thái
function broadcastState() {
  io.emit('gameState', {
    vipQueue: vipQueue.map(u => ({ nickname: u.nickname, avatar: u.avatar, giftName: u.giftName })),
    normalQueue: normalQueue.map(u => ({ nickname: u.nickname, avatar: u.avatar })),
    isDrawing,
    currentFortune,
    historyFortunes: historyFortunes.slice(-6).reverse(),
    totalCongDuc
  });
}

// Hàm thực hiện bốc quẻ cho người tiếp theo trong hàng đợi
function processNextInQueue() {
  if (isDrawing) return;

  let nextUser = null;
  let isVip = false;

  if (vipQueue.length > 0) {
    nextUser = vipQueue.shift();
    isVip = true;
  } else if (normalQueue.length > 0) {
    nextUser = normalQueue.shift();
    isVip = false;
  }

  if (!nextUser) return;

  isDrawing = true;

  let picked = null;
  if (isVip && nextUser.vipTier === 'diamond') {
    // 🥇 VIP Kim Cương: 100% mở ra Quẻ Hoàng Kim Vạn Lộc độc bản (Đại Đại Cát)
    const hoangKimList = fortunes.filter(f => f.category === 'hoang_kim');
    picked = hoangKimList[Math.floor(Math.random() * hoangKimList.length)] || fortunes[0];
  } else if (isVip && nextUser.vipTier === 'gold') {
    // 🥈 VIP Vàng: 100% ra quẻ Thượng Cát hoặc Đại Cát
    const goldEligible = fortunes.filter(f => f.type === 'ĐẠI CÁT' || f.type === 'THƯỢNG CÁT');
    picked = goldEligible[Math.floor(Math.random() * goldEligible.length)] || fortunes[0];
  } else if (isVip) {
    // 🥉 VIP Bạc: cam kết không bao giờ dính quẻ Hạ Hạ
    const silverEligible = fortunes.filter(f => f.type !== 'HẠ HẠ');
    picked = silverEligible[Math.floor(Math.random() * silverEligible.length)] || fortunes[0];
  } else if (nextUser.forceCrisis) {
    const crisisFortunes = fortunes.filter(f => f.type === 'HẠ HẠ');
    picked = crisisFortunes[Math.floor(Math.random() * crisisFortunes.length)] || fortunes[0];
  } else {
    // Người xem thường: Lọc theo chủ đề đã chọn
    const userCat = nextUser.category || 'tong_hop';
    let eligibleFortunes = fortunes.filter(f => f.category === userCat);
    if (eligibleFortunes.length === 0) eligibleFortunes = fortunes;
    picked = eligibleFortunes[Math.floor(Math.random() * eligibleFortunes.length)];
  }

  currentFortune = {
    user: nextUser,
    isVip,
    fortune: picked,
    drawnAt: new Date().toLocaleTimeString('vi-VN')
  };

  // Bước 1: Phát lệnh rung lắc ống xăm
  io.emit('draw:start', { user: nextUser, isVip });
  broadcastState();

  // Bước 2: Sau 3 giây rung lắc, kiểm tra nếu trúng Quẻ Đại Hạn (Hạ Hạ) ➔ Bắt đầu Thử Thách Cả Phòng Giải Cứu
  setTimeout(() => {
    if (!isVip && picked.type === 'HẠ HẠ') {
      startCrisisChallenge(nextUser, picked);
      return;
    }

    io.emit('draw:reveal', currentFortune);
    historyFortunes.push(currentFortune);
    broadcastState();

    // Chuẩn bị câu thoại TTS cá nhân hóa theo Tên & Tuổi Can Chi
    const agePhrase = nextUser.canChi ? `tuổi ${nextUser.canChi}` : '';
    const catPhrase = picked.categoryName ? `về ${picked.categoryName}` : '';
    const ttsMessage = `Chúc mừng ${nextUser.nickname} ${agePhrase} đã rút được quẻ ${catPhrase} ${picked.type}, ${picked.title}. ${picked.shortAdvice}`;
    io.emit('playTts', { text: ttsMessage });

    // Bước 3: Giữ quẻ trên màn hình trong 9 giây để khán giả đọc rồi chuyển người tiếp theo
    setTimeout(() => {
      isDrawing = false;
      broadcastState();
      // Chờ 1 giây rồi bốc người tiếp theo
      setTimeout(processNextInQueue, 1000);
    }, 9000);

  }, 3000);
}

// Quản lý sự kiện Quẻ Đại Hạn & Thử Thách Cả Phòng Giải Cứu (Co-op Crisis)
let crisisState = null;

function startCrisisChallenge(nextUser, badFortune) {
  if (crisisState) return;

  crisisState = {
    active: true,
    victim: nextUser,
    fortune: badFortune,
    goalLikes: 30, // 30 tim là mục tiêu phù hợp để giải cứu
    currentLikes: 0,
    countdown: 15,
    timer: null,
    isResolved: false
  };

  io.emit('crisis:start', {
    victim: nextUser,
    fortune: badFortune,
    goalLikes: crisisState.goalLikes,
    currentLikes: 0,
    countdown: 15
  });

  const ageStr = nextUser.canChi ? `tuổi ${nextUser.canChi}` : '';
  const alertTts = `Báo động nguy cấp! Thí chủ ${nextUser.nickname} ${ageStr} đã bốc phải quẻ Đại Hạn ${badFortune.title}! Cả phòng hãy mau mau thả 30 tim hoặc tặng 1 hoa hồng để giải cứu trong 15 giây!`;
  io.emit('playTts', { text: alertTts });

  crisisState.timer = setInterval(() => {
    if (!crisisState || crisisState.isResolved) {
      clearInterval(crisisState?.timer);
      return;
    }
    crisisState.countdown--;
    io.emit('crisis:tick', {
      countdown: crisisState.countdown,
      currentLikes: crisisState.currentLikes,
      goalLikes: crisisState.goalLikes
    });

    if (crisisState.countdown <= 0) {
      clearInterval(crisisState.timer);
      resolveCrisis(false);
    }
  }, 1000);
}

function resolveCrisis(success, reason = 'likes', giftData = null) {
  if (!crisisState || crisisState.isResolved) return;
  crisisState.isResolved = true;
  clearInterval(crisisState.timer);

  if (success) {
    const convertedFortune = {
      id: 999,
      category: 'tong_hop',
      categoryName: '🌟 Hóa Hung Thành Cát',
      type: 'ĐẠI CÁT',
      title: 'THOÁT NẠN THÀNH CÔNG',
      poem: 'Hiệp lực đồng lòng vạn cánh tay\nGian nan vận hạn thảy tan bay\nCả phòng cứu nạn tròn công đức\nPhúc ấm đầu xuân rực rỡ này.',
      taiLoc: 'Tai qua nạn khỏi, tiền tài vào gấp bội.',
      tinhDuyen: 'Được cả cộng đồng yêu quý, đào hoa ngập tràn.',
      congDanh: 'Vượt ải gian nan, bước sang trang mới huy hoàng.',
      sucKhoe: 'Khỏe mạnh, thoát khỏi mọi ưu phiền.',
      luckyNumber: 99,
      shortAdvice: 'Tình cảm tương thân tương ái của mọi người đã cứu bạn!'
    };

    io.emit('crisis:resolved', {
      success: true,
      reason,
      savior: giftData ? giftData.nickname : 'Cả Phòng Live',
      victim: crisisState.victim,
      fortune: convertedFortune
    });

    historyFortunes.push({
      user: crisisState.victim,
      isVip: true,
      fortune: convertedFortune,
      drawnAt: new Date().toLocaleTimeString('vi-VN')
    });

    const saviorPhrase = giftData 
      ? `Đại gia ${giftData.nickname} đã hào phóng tặng ${giftData.giftName} giải cứu thần tốc cho ${crisisState.victim.nickname}!`
      : `Cả phòng Live đã chung sức thả đủ 30 tim giải cứu thành công cho ${crisisState.victim.nickname}!`;
    const ttsSuccess = `${saviorPhrase} Hóa hung thành cát! Chúc mừng bạn vạn sự bình an!`;
    io.emit('playTts', { text: ttsSuccess });
  } else {
    io.emit('crisis:resolved', {
      success: false,
      victim: crisisState.victim,
      fortune: crisisState.fortune
    });

    const ttsFail = `Hết giờ! Giải cứu bất thành! Thí chủ ${crisisState.victim.nickname} đành chịu hạn ${crisisState.fortune.title}, nhớ làm lành tích đức nhé!`;
    io.emit('playTts', { text: ttsFail });
  }

  // Kết thúc thử thách và quay lại hàng đợi sau 8 giây
  setTimeout(() => {
    crisisState = null;
    isDrawing = false;
    broadcastState();
    setTimeout(processNextInQueue, 1000);
  }, 8000);
}

// Xử lý khi có Comment
function handleComment(data) {
  const comment = (data.comment || '').trim().toLowerCase();
  // Nếu bình luận chứa từ khóa xin quẻ
  if (comment.includes('quẻ') || comment.includes('que') || comment.includes('xin') || comment.includes('bốc') || comment.includes('boc') || comment === '1') {
    // 1. Phân loại chủ đề cầu xin
    let category = 'tong_hop';
    let categoryName = '🎋 Toàn Diện';
    if (/tinh duyen|tinh cam|nguoi yeu|ny|thoat e|chong|vo|yeu/i.test(comment)) {
      category = 'tinh_duyen';
      categoryName = '💖 Tình Duyên';
    } else if (/tai loc|lam an|kinh doanh|buon ban|tien|giau|phat tai/i.test(comment)) {
      category = 'tai_loc';
      categoryName = '💰 Tài Lộc';
    } else if (/cong danh|hoc hanh|thi cu|su nghiep|thang chuc|viec lam|do dat/i.test(comment)) {
      category = 'cong_danh';
      categoryName = '📚 Công Danh';
    } else if (/gia dao|binh an|suc khoe|gia dinh/i.test(comment)) {
      category = 'gia_dao';
      categoryName = '🏡 Gia Đạo';
    }

    // 2. Trích xuất năm sinh & tính Can Chi tự động
    const yearMatch = comment.match(/\b(19[5-9]\d|20[0-2]\d)\b/);
    let canChi = '';
    let birthYear = null;
    if (yearMatch) {
      birthYear = parseInt(yearMatch[1], 10);
      const CAN = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ'];
      const CHI = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi'];
      canChi = `${CAN[birthYear % 10]} ${CHI[birthYear % 12]} (${birthYear})`;
    }

    // Tránh spam trùng lặp trong hàng đợi
    const exists = normalQueue.some(u => u.uniqueId === data.uniqueId) || vipQueue.some(u => u.uniqueId === data.uniqueId);
    if (!exists) {
      normalQueue.push({
        uniqueId: data.uniqueId,
        nickname: data.nickname || data.uniqueId,
        avatar: data.profilePictureUrl || 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg',
        comment: data.comment,
        category,
        categoryName,
        canChi,
        birthYear
      });
      totalCongDuc += 1;
      broadcastState();
      processNextInQueue();
    }
  }
  io.emit('chat', data);
}

// Xử lý khi có Gift (Quà tặng)
function handleGift(data) {
  const diamonds = Number(data.diamondCount) || 1;
  const count = Number(data.repeatCount) || 1;
  const totalValue = diamonds * count;
  totalCongDuc += totalValue * 10;

  // Xác định cấp bậc VIP (Tier) theo giá trị xu
  let vipTier = 'silver'; // 🥉 VIP Bạc (1 - 9 xu)
  let vipBadge = '🥉 VIP Bạc';
  if (totalValue >= 100) {
    vipTier = 'diamond';  // 🥇 VIP Kim Cương (100+ xu - Triệu hồi Thần Tài)
    vipBadge = '👑 VIP Kim Cương';
  } else if (totalValue >= 10) {
    vipTier = 'gold';     // 🥈 VIP Vàng (10 - 99 xu)
    vipBadge = '🥈 VIP Vàng';
  }

  // Nếu đang trong thử thách Đại Hạn, quà tặng sẽ giải cứu tức thì!
  if (crisisState && crisisState.active && !crisisState.isResolved) {
    resolveCrisis(true, 'gift', data);
  }

  const newVipUser = {
    uniqueId: data.uniqueId,
    nickname: data.nickname || data.uniqueId,
    avatar: data.profilePictureUrl || 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg',
    giftName: data.giftName,
    diamondCount: totalValue,
    vipTier,
    vipBadge
  };

  // Nếu là VIP Kim Cương (>= 100 xu): Kích hoạt sự kiện Triệu Hồi Thần Tài ngay!
  if (vipTier === 'diamond') {
    vipQueue.unshift(newVipUser); // Ưu tiên số 1
    io.emit('thantai:summon', {
      user: newVipUser,
      giftName: data.giftName,
      diamonds: totalValue
    });
    const ttsThantai = `Bái kiến Đại Gia ${newVipUser.nickname} đã dâng tặng ${data.giftName}! Thần Tài Hoàng Kim giáng thế ban phúc lộc vạn niên!`;
    io.emit('playTts', { text: ttsThantai });
  } else if (vipTier === 'gold') {
    // Chèn sau các VIP Kim Cương, nhưng trước VIP Bạc
    const firstNonDiamondIndex = vipQueue.findIndex(u => u.vipTier !== 'diamond');
    if (firstNonDiamondIndex === -1) {
      vipQueue.push(newVipUser);
    } else {
      vipQueue.splice(firstNonDiamondIndex, 0, newVipUser);
    }
    const ttsGold = `Chào mừng Phú Hộ ${newVipUser.nickname} đã tặng ${data.giftName} gia nhập hàng VIP Vàng!`;
    io.emit('playTts', { text: ttsGold });
  } else {
    // VIP Bạc: thêm vào cuối hàng VIP
    vipQueue.push(newVipUser);
  }

  io.emit('gift', { ...data, vipTier, vipBadge });
  broadcastState();
  processNextInQueue();
}

// Xử lý khi có Like (Thả tim)
function handleLike(data) {
  totalCongDuc += (data.likeCount || 1);

  // Nếu đang trong thử thách Đại Hạn, lượt like sẽ tích lũy giải cứu
  if (crisisState && crisisState.active && !crisisState.isResolved) {
    crisisState.currentLikes += (data.likeCount || 1);
    io.emit('crisis:tick', {
      countdown: crisisState.countdown,
      currentLikes: crisisState.currentLikes,
      goalLikes: crisisState.goalLikes
    });
    if (crisisState.currentLikes >= crisisState.goalLikes) {
      resolveCrisis(true, 'likes');
    }
  }

  io.emit('like', data);
  broadcastState();
}

// Kết nối TikTok Live nếu có Username
if (TIKTOK_USERNAME) {
  try {
    const cleanUser = TIKTOK_USERNAME.replace('@', '');
    const tiktokLive = new TikTokLiveConnection(cleanUser);
    tiktokLive.connect()
      .then(state => console.log(`✅ Kết nối TikTok Live: ${cleanUser}`))
      .catch(err => console.log(`⚠️ Lỗi kết nối: ${err.message}`));

    tiktokLive.on('chat', data => handleComment(data));
    tiktokLive.on('gift', data => handleGift(data));
    tiktokLive.on('like', data => handleLike(data));
  } catch (err) {
    console.error('Lỗi khởi tạo TikTok connector:', err);
  }
}

// Socket.IO kết nối
io.on('connection', socket => {
  socket.emit('gameState', {
    vipQueue: vipQueue.map(u => ({ nickname: u.nickname, avatar: u.avatar, giftName: u.giftName })),
    normalQueue: normalQueue.map(u => ({ nickname: u.nickname, avatar: u.avatar })),
    isDrawing,
    currentFortune,
    historyFortunes: historyFortunes.slice(-6).reverse(),
    totalCongDuc
  });

  socket.on('mock:chat', data => handleComment(data));
  socket.on('mock:gift', data => handleGift(data));
  socket.on('mock:like', data => handleLike(data));
  socket.on('mock:crisis', data => {
    const name = data?.name || 'NguoiXuiXe_01';
    normalQueue.unshift({
      uniqueId: name.toLowerCase(),
      nickname: name,
      avatar: 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg',
      comment: 'Xin quẻ đầu năm',
      category: 'tong_hop',
      categoryName: '🎋 May Mắn',
      canChi: 'Mậu Thân (1968)',
      forceCrisis: true
    });
    broadcastState();
    processNextInQueue();
  });
  socket.on('admin:sfx', data => io.emit('audio:sfx', data));
  socket.on('admin:bgm:toggle', () => io.emit('audio:bgm:toggle'));

  socket.on('game:reset', () => {
    vipQueue = [];
    normalQueue = [];
    isDrawing = false;
    currentFortune = null;
    historyFortunes = [];
    totalCongDuc = 0;
    broadcastState();
    io.emit('game:reset');
  });
});

server.listen(PORT, () => {
  console.log(`🎋 GAME BỐC QUẺ ĐẦU NĂM ĐANG CHẠY TRÊN CỔNG: ${PORT}`);
  console.log(`👉 Màn hình game chính: http://localhost:${PORT}/index.html`);
  console.log(`👉 Bảng giả lập Admin: http://localhost:${PORT}/admin.html`);
});
