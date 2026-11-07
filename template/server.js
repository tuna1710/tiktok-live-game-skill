require('dotenv').config();
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const http = require('http');
const express = require('express');
const cors = require('cors');
const { Server } = require('socket.io');
const { TikTokLiveConnection } = require('tiktok-live-connector');

const PORT = Number(process.env.PORT) || 3000;
let TIKTOK_USERNAME = process.env.TIKTOK_USERNAME || '';
const TIKTOK_SESSION_ID = process.env.TIKTOK_SESSION_ID || '';

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

// Trạng thái Server & Game
let gameState = {
  title: "TikTok Live Interactive Game",
  score: 0,
  totalGifts: 0,
  totalLikes: 0,
  topContributors: {},
  lastEvent: null
};

const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

// Kết nối TikTok Live
let tiktokLive = null;
function connectTikTok(username) {
  if (!username) {
    console.log('⚠️ [TIKTOK] Chưa thiết lập TIKTOK_USERNAME. Chạy ở chế độ Mock / Giả lập.');
    return;
  }
  const cleanUsername = username.startsWith('@') ? username.slice(1) : username;
  console.log(`🔄 [TIKTOK] Đang kết nối tới Live của: @${cleanUsername}...`);

  const options = {
    enableExtendedGiftInfo: true
  };
  if (TIKTOK_SESSION_ID) {
    options.sessionId = TIKTOK_SESSION_ID;
  }

  tiktokLive = new TikTokLiveConnection(cleanUsername, options);

  tiktokLive.connect()
    .then(state => {
      console.log(`✅ [TIKTOK] Đã kết nối thành công tới phòng Live ID: ${state.roomId}`);
      io.emit('tiktok:status', { connected: true, roomId: state.roomId, username: cleanUsername });
    })
    .catch(err => {
      console.log(`❌ [TIKTOK] Không thể kết nối tới @${cleanUsername}: ${err.message}`);
      io.emit('tiktok:status', { connected: false, error: err.message, username: cleanUsername });
    });

  // Bắt sự kiện Comment
  tiktokLive.on('chat', data => {
    const payload = {
      uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
      nickname: data.user?.nickname || data.nickname || 'Khán giả',
      comment: data.content || data.comment || '',
      profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || data.profilePictureUrl
    };
    handleChat(payload);
  });

  // Bắt sự kiện Gift (Quà tặng)
  tiktokLive.on('gift', data => {
    // Chỉ xử lý khi chuỗi tặng quà kết thúc hoặc với quà không lặp
    if (data.giftType === 1 && !data.repeatEnd) {
      return;
    }
    const payload = {
      uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
      nickname: data.user?.nickname || data.nickname || 'Khán giả',
      giftId: data.gift?.id || data.giftId,
      giftName: data.gift?.name || data.giftName || 'Quà',
      diamondCount: Number(data.gift?.diamondCount) || Number(data.diamondCount) || 1,
      repeatCount: Number(data.repeatCount) || 1,
      profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || data.profilePictureUrl
    };
    handleGift(payload);
  });

  // Bắt sự kiện Thả tim (Like)
  tiktokLive.on('like', data => {
    const payload = {
      uniqueId: data.user?.id || data.uniqueId,
      nickname: data.user?.nickname || data.nickname || 'Khán giả',
      likeCount: Number(data.count) || Number(data.likeCount) || 1,
      totalLikes: Number(data.total) || Number(data.totalLikes) || 0
    };
    handleLike(payload);
  });

  // Bắt sự kiện người mới tham gia
  tiktokLive.on('member', data => {
    io.emit('member', {
      uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
      nickname: data.user?.nickname || data.nickname || 'Khán giả'
    });
  });

  tiktokLive.on('disconnected', () => {
    console.log('⚠️ [TIKTOK] Mất kết nối TikTok Live!');
    io.emit('tiktok:status', { connected: false, error: 'Disconnected' });
  });
}

// Xử lý logic nghiệp vụ
function handleChat(data) {
  gameState.lastEvent = { type: 'chat', data };
  io.emit('chat', data);
}

function handleGift(data) {
  const points = (data.diamondCount || 1) * (data.repeatCount || 1);
  gameState.totalGifts += points;
  gameState.score += points * 10;

  // Cập nhật BXH
  if (!gameState.topContributors[data.uniqueId]) {
    gameState.topContributors[data.uniqueId] = {
      nickname: data.nickname,
      avatar: data.profilePictureUrl,
      diamonds: 0
    };
  }
  gameState.topContributors[data.uniqueId].diamonds += points;

  gameState.lastEvent = { type: 'gift', data };
  io.emit('gift', data);
  io.emit('gameState', gameState);
}

function handleLike(data) {
  gameState.totalLikes += (data.likeCount || 1);
  gameState.score += (data.likeCount || 1);
  io.emit('like', data);
  io.emit('gameState', gameState);
}

// Quản lý Socket.IO
io.on('connection', socket => {
  socket.emit('gameState', gameState);

  // Nhận lệnh giả lập từ admin.html
  socket.on('mock:chat', data => handleChat(data));
  socket.on('mock:gift', data => handleGift(data));
  socket.on('mock:like', data => handleLike(data));

  socket.on('game:reset', () => {
    gameState.score = 0;
    gameState.totalGifts = 0;
    gameState.totalLikes = 0;
    gameState.topContributors = {};
    io.emit('gameState', gameState);
    io.emit('game:reset');
    console.log('🔄 Game đã được đặt lại từ Admin Panel.');
  });

  socket.on('tiktok:connect', username => {
    TIKTOK_USERNAME = username;
    connectTikTok(username);
  });
});

// Khởi chạy
if (TIKTOK_USERNAME) {
  connectTikTok(TIKTOK_USERNAME);
}

server.listen(PORT, () => {
  console.log(`=======================================================`);
  console.log(`🚀 TikTok Live Game Server is running on port: ${PORT}`);
  console.log(`🌐 Màn hình Game chính: http://localhost:${PORT}/index.html`);
  console.log(`🎮 Bảng điều khiển giả lập: http://localhost:${PORT}/admin.html`);
  console.log(`=======================================================`);
});
