require('dotenv').config();
const path = require('path');
const fs = require('fs');
const http = require('http');
const https = require('https');
const crypto = require('crypto');
const express = require('express');
const cors = require('cors');
const { Server } = require('socket.io');
const { TikTokLiveConnection } = require('tiktok-live-connector');

const PORT = Number(process.env.PORT) || 3000;
const TIKTOK_USERNAME = process.env.TIKTOK_USERNAME || '';

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Tạo thư mục cache cho TTS tiếng Việt (MD5 disk-cache)
const TTS_CACHE_DIR = path.join(__dirname, 'data', 'tts-cache');
if (!fs.existsSync(TTS_CACHE_DIR)) {
  fs.mkdirSync(TTS_CACHE_DIR, { recursive: true });
}

// Tải dữ liệu 63 tỉnh thành Việt Nam
const PROVINCES_DATA_FILE = path.join(__dirname, 'data', 'provinces.json');
let PROVINCES = [];
if (fs.existsSync(PROVINCES_DATA_FILE)) {
  PROVINCES = JSON.parse(fs.readFileSync(PROVINCES_DATA_FILE, 'utf-8'));
} else {
  console.warn('provinces.json not found, using fallback list');
}

// Tải kịch bản lời thoại MC phong phú & hài hước
const MC_LINES_FILE = path.join(__dirname, 'data', 'mc-lines.json');
let MC_LINES = {};
if (fs.existsSync(MC_LINES_FILE)) {
  MC_LINES = JSON.parse(fs.readFileSync(MC_LINES_FILE, 'utf-8'));
}

const lastSpokenIndexes = {};
function getRandomLine(category, vars = {}) {
  const lines = MC_LINES[category];
  if (!lines || lines.length === 0) return '';
  let index = Math.floor(Math.random() * lines.length);
  if (lines.length > 1 && lastSpokenIndexes[category] === index) {
    index = (index + 1) % lines.length;
  }
  lastSpokenIndexes[category] = index;
  let text = lines[index];
  for (const [key, val] of Object.entries(vars)) {
    text = text.replace(new RegExp(`\\{${key}\\}`, 'g'), val || '');
  }
  return text;
}

// Hàm chuẩn hóa chuỗi tiếng Việt (loại bỏ dấu và ký tự đặc biệt)
function normalizeText(str) {
  if (!str) return '';
  return str
    .toString()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/đ/g, 'd')
    .replace(/Đ/g, 'd')
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

// Hàm tìm tỉnh thành từ comment của người xem (Hỗ trợ 34 tỉnh mới & 63 tỉnh truyền thống)
function matchProvince(comment) {
  const norm = normalizeText(comment);
  if (!norm) return null;

  // 1. Khớp chính xác tên hoặc quê hương con (subProvinces)
  for (const p of PROVINCES) {
    for (const sub of (p.subProvinces || [])) {
      const normSub = normalizeText(sub);
      if (norm === normSub) {
        return {
          province: p,
          displayName: sub === p.name ? p.name : `${sub} (${p.name})`,
          ttsName: sub
        };
      }
    }
    for (const alias of p.aliases) {
      const normAlias = normalizeText(alias);
      if (norm === normAlias) {
        return {
          province: p,
          displayName: p.name,
          ttsName: p.name
        };
      }
    }
  }

  // 2. Khớp từ ngữ có ranh giới từ (word boundary)
  for (const p of PROVINCES) {
    for (const sub of (p.subProvinces || [])) {
      const normSub = normalizeText(sub);
      if (normSub.length < 2) continue;
      const regex = new RegExp(`(^|\\s)${normSub}(\\s|$)`, 'i');
      if (regex.test(norm)) {
        return {
          province: p,
          displayName: sub === p.name ? p.name : `${sub} (${p.name})`,
          ttsName: sub
        };
      }
    }
    for (const alias of p.aliases) {
      const normAlias = normalizeText(alias);
      if (normAlias.length < 2) continue;
      const regex = new RegExp(`(^|\\s)${normAlias}(\\s|$)`, 'i');
      if (regex.test(norm)) {
        return {
          province: p,
          displayName: p.name,
          ttsName: p.name
        };
      }
    }
  }

  return null;
}

// Endpoint TTS tiếng Việt trực tiếp (Lọc emoji + MD5 Disk Cache)
app.get('/api/tts', (req, res) => {
  const text = (req.query.text || '').toString().trim();
  if (!text) return res.status(400).send('Missing text parameter');

  const cleanText = text
    .replace(/[\u{1F600}-\u{1F64F}\u{1F300}-\u{1F5FF}\u{1F680}-\u{1F6FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '')
    .slice(0, 180).trim();
  if (!cleanText) return res.status(400).send('Empty clean text');

  const hash = crypto.createHash('md5').update(cleanText).digest('hex');
  const cacheFile = path.join(TTS_CACHE_DIR, `${hash}.mp3`);

  if (fs.existsSync(cacheFile)) {
    res.setHeader('Content-Type', 'audio/mpeg');
    res.setHeader('Cache-Control', 'public, max-age=604800');
    return fs.createReadStream(cacheFile).pipe(res);
  }

  const googleTtsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=vi&client=tw-ob&q=${encodeURIComponent(cleanText)}`;
  https.get(googleTtsUrl, {
    headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' }
  }, (ttsRes) => {
    if (ttsRes.statusCode === 200) {
      res.writeHead(200, {
        'Content-Type': 'audio/mpeg',
        'Cache-Control': 'public, max-age=604800'
      });
      const fileStream = fs.createWriteStream(cacheFile);
      ttsRes.pipe(fileStream);
      ttsRes.pipe(res);
    } else {
      res.status(500).send('TTS fetch failed');
    }
  }).on('error', () => res.status(500).send('TTS error'));
});

// API lấy danh sách tỉnh thành
app.get('/api/provinces', (req, res) => {
  res.json(PROVINCES);
});

// Khởi tạo Game State
const PROVINCE_VISIT_DURATION = 15; // Mỗi tỉnh ghé thăm 15 giây

let gameState = {
  roundNumber: 19,
  roundTimeLeft: 70, // 01:10
  currentVisit: {
    provinceId: 'lao-cai',
    svgId: 'laocai',
    provinceName: 'Lào Cai',
    user: {
      uniqueId: 'toi_ech',
      nickname: 'TỚI Ếch',
      profilePictureUrl: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face'
    },
    timeLeft: PROVINCE_VISIT_DURATION,
    visitCount: 5
  },
  queue: [
    {
      id: 'q1',
      provinceId: 'da-nang',
      svgId: 'danang',
      provinceName: 'Đà Nẵng',
      user: {
        uniqueId: 'danang_lover',
        nickname: 'Biển Mỹ Khê',
        profilePictureUrl: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face'
      },
      isVip: false,
      priority: 0,
      addedAt: Date.now()
    },
    {
      id: 'q2',
      provinceId: 'tay-ninh',
      svgId: 'tayninh',
      provinceName: 'Tây Ninh',
      user: {
        uniqueId: 'alo_vu',
        nickname: 'Alo vũ à vũ...',
        profilePictureUrl: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop&crop=face'
      },
      isVip: false,
      priority: 0,
      addedAt: Date.now()
    },
    {
      id: 'q3',
      provinceId: 'cao-bang',
      svgId: 'caobang',
      provinceName: 'Cao Bằng',
      user: {
        uniqueId: 'thac_ban_gioc',
        nickname: 'Cao Bằng Quê Tôi',
        profilePictureUrl: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop&crop=face'
      },
      isVip: false,
      priority: 0,
      addedAt: Date.now()
    }
  ],
  stats: {
    totalViewers: 341,
    followersGoal: 1751,
    followersTarget: 10000,
    totalLikes: 2286
  },
  provinceStats: {
    'lao-cai': 5,
    'da-nang': 8,
    'tay-ninh': 3,
    'cao-bang': 4
  },
  recentNotifications: []
};

const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

// Hàm chuyển sang tỉnh tiếp theo trong hàng đợi
function nextProvince() {
  if (gameState.queue.length > 0) {
    const nextItem = gameState.queue.shift();
    const currentCount = (gameState.provinceStats[nextItem.provinceId] || 0) + 1;
    gameState.provinceStats[nextItem.provinceId] = currentCount;

    gameState.currentVisit = {
      provinceId: nextItem.provinceId,
      svgIds: nextItem.svgIds || [nextItem.provinceId.replace(/-/g, '')],
      provinceName: nextItem.provinceName,
      user: nextItem.user,
      timeLeft: PROVINCE_VISIT_DURATION,
      visitCount: currentCount
    };

    // Thông báo TTS chuyển tỉnh đa dạng & hài hước
    const ttsText = getRandomLine('visitUser', {
      nickname: nextItem.user.nickname,
      province: nextItem.ttsName || nextItem.provinceName
    }) || `Đang cùng bạn ${nextItem.user.nickname} ghé thăm quê hương ${nextItem.ttsName || nextItem.provinceName}`;
    io.emit('playTts', { text: ttsText });
  } else {
    // Nếu hết hàng đợi, tự động chọn một tỉnh ngẫu nhiên trong 34 tỉnh để không bị khoảng lặng (Anti-Dead Air)
    const randomProv = PROVINCES[Math.floor(Math.random() * PROVINCES.length)];
    const currentCount = (gameState.provinceStats[randomProv.id] || 0) + 1;
    gameState.provinceStats[randomProv.id] = currentCount;

    gameState.currentVisit = {
      provinceId: randomProv.id,
      svgIds: randomProv.svgIds || [randomProv.id.replace(/-/g, '')],
      provinceName: randomProv.name,
      user: {
        uniqueId: 'tiktok_live',
        nickname: 'Du khách TikTok',
        profilePictureUrl: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&h=100&fit=crop&crop=face'
      },
      timeLeft: PROVINCE_VISIT_DURATION,
      visitCount: currentCount
    };

    const deadAirTts = getRandomLine('antiDeadAir', {
      province: randomProv.name
    }) || `Mời cả nhà cùng ngắm nhìn vẻ đẹp của ${randomProv.name}`;
    io.emit('playTts', { text: deadAirTts });
  }

  io.emit('provinceChanged', gameState.currentVisit);
  io.emit('gameState', gameState);
}

let lastCtaTime = Date.now();

// Vòng lặp đếm ngược thời gian (Ticker) mỗi giây
setInterval(() => {
  // Đếm ngược thời gian ghé thăm tỉnh
  if (gameState.currentVisit.timeLeft > 0) {
    gameState.currentVisit.timeLeft--;
    io.emit('tick', {
      timeLeft: gameState.currentVisit.timeLeft,
      roundTimeLeft: gameState.roundTimeLeft
    });
  } else {
    nextProvince();
  }

  // Đếm ngược thời gian vòng phiên Live
  if (gameState.roundTimeLeft > 0) {
    gameState.roundTimeLeft--;
  } else {
    gameState.roundNumber++;
    gameState.roundTimeLeft = 70;
    io.emit('roundReset', { roundNumber: gameState.roundNumber });
  }

  // Kêu gọi tương tác / Đua top định kỳ (Call to action) khi hàng đợi trống
  if (Date.now() - lastCtaTime > 35000 && gameState.queue.length === 0) {
    lastCtaTime = Date.now();
    const cat = Math.random() < 0.5 ? 'cta' : 'duaTop';
    const ctaTts = getRandomLine(cat);
    if (ctaTts) io.emit('playTts', { text: ctaTts });
  }
}, 1000);

// Xử lý khi có người yêu cầu ghé thăm tỉnh qua chat hoặc mock
function handleProvinceRequest(user, comment, isVip = false, coins = 0) {
  const matched = matchProvince(comment);
  if (!matched) return null;

  const targetProvince = matched.province;
  const queueItem = {
    id: 'req_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4),
    provinceId: targetProvince.id,
    svgIds: targetProvince.svgIds || [targetProvince.id.replace(/-/g, '')],
    provinceName: matched.displayName,
    ttsName: matched.ttsName,
    user: {
      uniqueId: user.uniqueId || 'user_' + Date.now(),
      nickname: user.nickname || 'Khán giả',
      profilePictureUrl: user.profilePictureUrl || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&h=100&fit=crop&crop=face'
    },
    isVip: isVip,
    priority: coins,
    addedAt: Date.now()
  };

  // Cơ chế VIP Jump: Tặng quà lớn (>=200 xu) hoặc mốc VIP nhảy ngay lên đầu hàng đợi
  if (coins >= 200 || (isVip && coins >= 100)) {
    gameState.queue.unshift(queueItem);
  } else if (coins >= 50) {
    // Mốc "Đọc nhanh" (50 xu): chen lên trước các yêu cầu thường
    const firstNormalIndex = gameState.queue.findIndex(item => !item.isVip && item.priority < 50);
    if (firstNormalIndex !== -1) {
      gameState.queue.splice(firstNormalIndex, 0, queueItem);
    } else {
      gameState.queue.push(queueItem);
    }
  } else {
    // Yêu cầu thường (Comment): xếp vào cuối hàng đợi
    // Tránh spam trùng lặp liên tiếp cùng 1 user cho cùng 1 tỉnh
    const isDuplicate = gameState.queue.some(
      item => item.user.uniqueId === queueItem.user.uniqueId && item.provinceId === queueItem.provinceId
    );
    if (!isDuplicate) {
      gameState.queue.push(queueItem);
    }
  }

  gameState.stats.totalViewers++;
  io.emit('queueUpdated', gameState.queue);
  io.emit('gameState', gameState);

  return matched;
}

// Xử lý tặng quà (Gift)
function handleGiftEvent(giftData) {
  const { uniqueId, nickname, giftName, diamondCount, repeatCount, profilePictureUrl } = giftData;
  const totalCoins = (diamondCount || 1) * (repeatCount || 1);

  // Thêm notification popup
  const notif = {
    id: 'gift_' + Date.now(),
    type: 'gift',
    nickname,
    profilePictureUrl,
    giftName,
    coins: totalCoins,
    time: Date.now()
  };
  gameState.recentNotifications.unshift(notif);
  if (gameState.recentNotifications.length > 5) gameState.recentNotifications.pop();

  io.emit('giftNotification', notif);

  // 1. Quà mốc VIP "Đọc trước" (>= 200 xu): Kích hoạt hiệu ứng đặc biệt + VIP queue jump
  if (totalCoins >= 200) {
    io.emit('vipSpecialEffect', { nickname, giftName, coins: totalCoins });
    const tts = getRandomLine('vipGift', { nickname, giftName, coins: totalCoins }) ||
      `Cảm ơn đại gia ${nickname} đã tặng ${giftName}! Nhận đặc quyền ưu tiên đọc trước!`;
    io.emit('playTts', { text: tts });
  } 
  // 2. Quà mốc "Đọc nhanh" (50 - 199 xu)
  else if (totalCoins >= 50) {
    const tts = getRandomLine('fastPassGift', { nickname, giftName, coins: totalCoins }) ||
      `Cảm ơn ${nickname} đã tặng ${giftName} để đọc nhanh!`;
    io.emit('playTts', { text: tts });
  }
  // 3. Quà nhỏ (Hoa hồng, 1 - 49 xu): Cộng điểm lượt thăm cho tỉnh hiện tại
  else {
    gameState.currentVisit.visitCount += totalCoins;
    gameState.provinceStats[gameState.currentVisit.provinceId] = gameState.currentVisit.visitCount;
    if (Math.random() < 0.6) {
      const tts = getRandomLine('smallGift', { nickname, giftName: giftName || 'hoa hồng' });
      if (tts) io.emit('playTts', { text: tts });
    }
  }

  gameState.stats.followersGoal += Math.floor(totalCoins / 2) + 1;
  io.emit('gameState', gameState);
}

// Xử lý sự kiện thả tim (Like)
function handleLikeEvent(count, nickname) {
  const prevLikes = gameState.stats.totalLikes;
  gameState.stats.totalLikes += count;
  io.emit('like', {
    nickname: nickname || 'Người xem',
    likeCount: count,
    totalLikes: gameState.stats.totalLikes
  });

  if (Math.floor(gameState.stats.totalLikes / 150) > Math.floor(prevLikes / 150)) {
    const tts = getRandomLine('likeMilestone');
    if (tts) io.emit('playTts', { text: tts });
  }
}

// Xử lý sự kiện Follow kênh
function handleFollowEvent(userData) {
  const notif = {
    id: 'fol_' + Date.now(),
    type: 'follow',
    nickname: userData.nickname || 'Khán giả',
    profilePictureUrl: userData.profilePictureUrl || '',
    time: Date.now()
  };
  gameState.stats.followersGoal++;
  gameState.recentNotifications.unshift(notif);
  if (gameState.recentNotifications.length > 5) gameState.recentNotifications.pop();
  io.emit('followNotification', notif);
  io.emit('gameState', gameState);

  if (Math.random() < 0.6) {
    const tts = getRandomLine('follow', { nickname: notif.nickname });
    if (tts) io.emit('playTts', { text: tts });
  }
}

// Kết nối TikTok Live chuẩn 2.x
let tiktokLive = null;
if (TIKTOK_USERNAME) {
  try {
    const cleanUsername = TIKTOK_USERNAME.replace('@', '').trim();
    tiktokLive = new TikTokLiveConnection(cleanUsername, {
      processInitialData: false,
      enableExtendedGiftInfo: true,
      requestPollingIntervalMs: 1000,
      sessionId: process.env.TIKTOK_SESSION_ID || undefined
    });

    tiktokLive.connect()
      .then(state => console.log(`[TikTok Live] Connected successfully to roomId: ${state.roomId}`))
      .catch(err => console.log(`[TikTok Live] Connect notice: ${err.message}`));

    tiktokLive.on('chat', data => {
      const user = {
        uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
        nickname: data.user?.nickname || data.nickname || 'Khán giả',
        profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || data.profilePictureUrl
      };
      const comment = data.content || data.comment || '';
      handleProvinceRequest(user, comment, false, 0);
      io.emit('chat', { ...user, comment });
    });

    tiktokLive.on('gift', data => {
      handleGiftEvent({
        uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
        nickname: data.user?.nickname || data.nickname || 'Khán giả',
        giftName: data.gift?.name || data.giftName || 'Hoa hồng',
        diamondCount: Number(data.gift?.diamondCount) || Number(data.diamondCount) || 1,
        repeatCount: Number(data.repeatCount) || 1,
        profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || data.profilePictureUrl
      });
    });

    tiktokLive.on('like', data => {
      const count = Number(data.count) || Number(data.likeCount) || 1;
      handleLikeEvent(count, data.user?.nickname || data.nickname);
    });

    tiktokLive.on('follow', data => {
      handleFollowEvent({
        nickname: data.user?.nickname || data.nickname || 'Khán giả',
        profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || ''
      });
    });

  } catch (e) {
    console.error('Failed to initialize TikTok Live connection:', e);
  }
}

// Xử lý sự kiện Socket.IO từ Frontend & Admin Mock Simulator
io.on('connection', socket => {
  // Gửi trạng thái ban đầu ngay khi client kết nối
  socket.emit('gameState', gameState);

  // Mock Comment từ admin.html
  socket.on('mock:chat', data => {
    const user = {
      uniqueId: data.uniqueId || 'mock_user_' + Math.floor(Math.random() * 1000),
      nickname: data.nickname || 'Khán giả Demo',
      profilePictureUrl: data.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face'
    };
    handleProvinceRequest(user, data.comment, data.isVip || false, data.coins || 0);
    io.emit('chat', { ...user, comment: data.comment });
  });

  // Mock Gift từ admin.html
  socket.on('mock:gift', data => {
    handleGiftEvent({
      uniqueId: data.uniqueId || 'mock_donor',
      nickname: data.nickname || 'Đại gia TikTok',
      giftName: data.giftName || 'Hoa hồng',
      diamondCount: Number(data.diamondCount) || 1,
      repeatCount: Number(data.repeatCount) || 1,
      profilePictureUrl: data.profilePictureUrl || 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face'
    });
  });

  // Mock Like
  socket.on('mock:like', data => {
    const count = Number(data.count) || 15;
    handleLikeEvent(count, data.nickname || 'Fan cứng');
  });

  // Mock Follow
  socket.on('mock:follow', data => {
    handleFollowEvent({
      nickname: data.nickname || 'Bảo săn bão',
      profilePictureUrl: data.profilePictureUrl || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&h=100&fit=crop&crop=face'
    });
  });

  // Chuyển tỉnh ngay lập tức
  socket.on('mock:next', () => {
    nextProvince();
  });

  // Reset hàng đợi / vòng chơi
  socket.on('mock:reset', () => {
    gameState.queue = [];
    gameState.roundTimeLeft = 70;
    io.emit('gameState', gameState);
  });

  // Chọn thẳng một tỉnh để ghé thăm
  socket.on('mock:set_province', provinceId => {
    const p = PROVINCES.find(item => item.id === provinceId);
    if (p) {
      const count = (gameState.provinceStats[p.id] || 0) + 1;
      gameState.provinceStats[p.id] = count;
      gameState.currentVisit = {
        provinceId: p.id,
        provinceName: p.name,
        user: {
          uniqueId: 'admin',
          nickname: 'Chủ phòng',
          profilePictureUrl: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face'
        },
        timeLeft: PROVINCE_VISIT_DURATION,
        visitCount: count
      };
      io.emit('provinceChanged', gameState.currentVisit);
      io.emit('gameState', gameState);
      io.emit('playTts', { text: `Đang ghé thăm tỉnh ${p.name}` });
    }
  });
});

server.listen(PORT, () => {
  console.log(`====================================================`);
  console.log(`🇻🇳 Game Vietnam Tour Live Server is running!`);
  console.log(`📡 URL màn hình chính (OBS): http://localhost:${PORT}/index.html`);
  console.log(`🎛️ Bảng giả lập Mock Admin: http://localhost:${PORT}/admin.html`);
  console.log(`====================================================`);
});
