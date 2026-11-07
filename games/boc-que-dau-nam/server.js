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

  // Chọn quẻ: Nếu là VIP ưu tiên quẻ Đại Cát / Thượng Cát
  let eligibleFortunes = fortunes;
  if (isVip) {
    eligibleFortunes = fortunes.filter(f => f.type === 'ĐẠI CÁT' || f.type === 'THƯỢNG CÁT');
    if (eligibleFortunes.length === 0) eligibleFortunes = fortunes;
  }
  const picked = eligibleFortunes[Math.floor(Math.random() * eligibleFortunes.length)];

  currentFortune = {
    user: nextUser,
    isVip,
    fortune: picked,
    drawnAt: new Date().toLocaleTimeString('vi-VN')
  };

  // Bước 1: Phát lệnh rung lắc ống xăm
  io.emit('draw:start', { user: nextUser, isVip });
  broadcastState();

  // Bước 2: Sau 3 giây rung lắc, bung mở quẻ xăm và phát giọng đọc TTS
  setTimeout(() => {
    io.emit('draw:reveal', currentFortune);
    historyFortunes.push(currentFortune);
    broadcastState();

    // Chuẩn bị câu thoại TTS chúc phúc
    const ttsMessage = `Chúc mừng ${nextUser.nickname} bốc được quẻ ${picked.type}, ${picked.title}. ${picked.shortAdvice}`;
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

// Xử lý khi có Comment
function handleComment(data) {
  const comment = (data.comment || '').trim().toLowerCase();
  // Nếu bình luận chứa từ khóa xin quẻ
  if (comment.includes('quẻ') || comment.includes('que') || comment.includes('xin') || comment.includes('bốc') || comment.includes('boc') || comment === '1') {
    // Tránh spam trùng lặp trong hàng đợi
    const exists = normalQueue.some(u => u.uniqueId === data.uniqueId) || vipQueue.some(u => u.uniqueId === data.uniqueId);
    if (!exists) {
      normalQueue.push({
        uniqueId: data.uniqueId,
        nickname: data.nickname || data.uniqueId,
        avatar: data.profilePictureUrl || 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg',
        comment: data.comment
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
  const points = (data.diamondCount || 1) * (data.repeatCount || 1);
  totalCongDuc += points * 10;

  // Người tặng quà lập tức được xếp vào VIP QUEUE (Ưu tiên số 1)
  vipQueue.unshift({
    uniqueId: data.uniqueId,
    nickname: data.nickname || data.uniqueId,
    avatar: data.profilePictureUrl || 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg',
    giftName: data.giftName,
    diamondCount: points
  });

  io.emit('gift', data);
  broadcastState();
  processNextInQueue();
}

// Xử lý khi có Like (Thả tim)
function handleLike(data) {
  totalCongDuc += (data.likeCount || 1);
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
