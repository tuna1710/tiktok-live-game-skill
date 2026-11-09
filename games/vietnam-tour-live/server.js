require('dotenv').config();
const path = require('path');
const fs = require('fs');
const http = require('http');
const https = require('https');
const crypto = require('crypto');
const express = require('express');
const cors = require('cors');
const { Server } = require('socket.io');
const { TikTokLiveConnection, WebcastEvent, ControlEvent } = require('tiktok-live-connector');

const PORT = Number(process.env.PORT) || 3000;
const TIKTOK_USERNAME = process.env.TIKTOK_USERNAME || '';
const TOTAL_VIEWERS_START = process.env.TOTAL_VIEWERS_START !== undefined ? Number(process.env.TOTAL_VIEWERS_START) : 0;
const FOLLOWERS_START = process.env.FOLLOWERS_START !== undefined ? Number(process.env.FOLLOWERS_START) : 0;
const FOLLOWERS_TARGET = process.env.FOLLOWERS_TARGET !== undefined ? Number(process.env.FOLLOWERS_TARGET) : 10000;



const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// ============================================================
// ⚙️ BẢNG CẤU HÌNH THAM SỐ TÍNH ĐIỂM (CÓ THỂ CHỈNH TRỰC TIẾP HOẶC QUA ADMIN)
// ============================================================
const GAME_CONFIG = {
  COINS_TO_POINTS_RATE: Number(process.env.COINS_TO_POINTS_RATE) || 30, // 1 Xu = 30 Điểm Yêu thương
  LIKES_PER_POINT: Number(process.env.LIKES_PER_POINT) || 100,          // 100 Tim = +1 Điểm
  SHARES_PER_POINT: Number(process.env.SHARES_PER_POINT) || 10,        // 10 Chia sẻ = +1 Điểm
  FOLLOW_POINTS: Number(process.env.FOLLOW_POINTS) || 1,              // 1 Follow = +1 Điểm
  COMMENT_POINTS: Number(process.env.COMMENT_POINTS) || 1,            // 1 Comment tỉnh = +1 Điểm (1 lần duy nhất/hiệp)
  VIP_COIN_THRESHOLD: Number(process.env.VIP_COIN_THRESHOLD) || 20,   // Mốc VIP Hoàng Kim
  FAST_PASS_COIN_THRESHOLD: Number(process.env.FAST_PASS_COIN_THRESHOLD) || 5 // Mốc Đọc Nhanh
};

// Giữ các biến tham chiếu tương thích ngược
let COINS_TO_POINTS_RATE = GAME_CONFIG.COINS_TO_POINTS_RATE;
let VIP_COIN_THRESHOLD = GAME_CONFIG.VIP_COIN_THRESHOLD;
let FAST_PASS_COIN_THRESHOLD = GAME_CONFIG.FAST_PASS_COIN_THRESHOLD;

// Bảng tra cứu Biển số xe 63 Tỉnh Thành Việt Nam (cho phép gửi số như 36, 29, 89...)
const LICENSE_PLATE_MAP = {
  // Miền Bắc
  '11': { sub: 'Cao Bằng', provId: 'cao-bang' },
  '12': { sub: 'Lạng Sơn', provId: 'lang-son' },
  '14': { sub: 'Quảng Ninh', provId: 'quang-ninh' },
  '15': { sub: 'Hải Phòng', provId: 'hai-phong' },
  '16': { sub: 'Hải Phòng', provId: 'hai-phong' },
  '17': { sub: 'Thái Bình', provId: 'hung-yen' },
  '18': { sub: 'Nam Định', provId: 'ninh-binh' },
  '19': { sub: 'Phú Thọ', provId: 'phu-tho' },
  '20': { sub: 'Thái Nguyên', provId: 'thai-nguyen' },
  '21': { sub: 'Yên Bái', provId: 'lao-cai' },
  '22': { sub: 'Tuyên Quang', provId: 'tuyen-quang' },
  '23': { sub: 'Hà Giang', provId: 'tuyen-quang' },
  '24': { sub: 'Lào Cai', provId: 'lao-cai' },
  '25': { sub: 'Lai Châu', provId: 'lai-chau' },
  '26': { sub: 'Sơn La', provId: 'son-la' },
  '27': { sub: 'Điện Biên', provId: 'dien-bien' },
  '28': { sub: 'Hòa Bình', provId: 'phu-tho' },
  '29': { sub: 'Hà Nội', provId: 'ha-noi' },
  '30': { sub: 'Hà Nội', provId: 'ha-noi' },
  '31': { sub: 'Hà Nội', provId: 'ha-noi' },
  '32': { sub: 'Hà Nội', provId: 'ha-noi' },
  '33': { sub: 'Hà Nội', provId: 'ha-noi' },
  '40': { sub: 'Hà Nội', provId: 'ha-noi' },
  '34': { sub: 'Hải Dương', provId: 'hai-phong' },
  '35': { sub: 'Ninh Bình', provId: 'ninh-binh' },
  '88': { sub: 'Vĩnh Phúc', provId: 'phu-tho' },
  '89': { sub: 'Hưng Yên', provId: 'hung-yen' },
  '90': { sub: 'Hà Nam', provId: 'ninh-binh' },
  '97': { sub: 'Bắc Kạn', provId: 'thai-nguyen' },
  '98': { sub: 'Bắc Giang', provId: 'bac-ninh' },
  '99': { sub: 'Bắc Ninh', provId: 'bac-ninh' },

  // Miền Trung & Tây Nguyên
  '36': { sub: 'Thanh Hóa', provId: 'thanh-hoa' },
  '37': { sub: 'Nghệ An', provId: 'nghe-an' },
  '38': { sub: 'Hà Tĩnh', provId: 'ha-tinh' },
  '43': { sub: 'Đà Nẵng', provId: 'da-nang' },
  '47': { sub: 'Đắk Lắk', provId: 'dak-lak' },
  '48': { sub: 'Đắk Nông', provId: 'lam-dong' },
  '49': { sub: 'Lâm Đồng', provId: 'lam-dong' },
  '73': { sub: 'Quảng Bình', provId: 'quang-tri' },
  '74': { sub: 'Quảng Trị', provId: 'quang-tri' },
  '75': { sub: 'Huế', provId: 'hue' },
  '76': { sub: 'Quảng Ngãi', provId: 'quang-ngai' },
  '77': { sub: 'Bình Định', provId: 'gia-lai' },
  '78': { sub: 'Phú Yên', provId: 'dak-lak' },
  '79': { sub: 'Khánh Hòa', provId: 'khanh-hoa' },
  '81': { sub: 'Gia Lai', provId: 'gia-lai' },
  '82': { sub: 'Kon Tum', provId: 'quang-ngai' },
  '85': { sub: 'Ninh Thuận', provId: 'khanh-hoa' },
  '86': { sub: 'Bình Thuận', provId: 'lam-dong' },
  '92': { sub: 'Quảng Nam', provId: 'da-nang' },

  // Miền Nam
  '39': { sub: 'Đồng Nai', provId: 'dong-nai' },
  '41': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '50': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '51': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '52': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '53': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '54': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '55': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '56': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '57': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '58': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '59': { sub: 'TP. Hồ Chí Minh', provId: 'ho-chi-minh' },
  '60': { sub: 'Đồng Nai', provId: 'dong-nai' },
  '61': { sub: 'Bình Dương', provId: 'ho-chi-minh' },
  '62': { sub: 'Long An', provId: 'tay-ninh' },
  '63': { sub: 'Tiền Giang', provId: 'dong-thap' },
  '64': { sub: 'Vĩnh Long', provId: 'vinh-long' },
  '65': { sub: 'Cần Thơ', provId: 'can-tho' },
  '66': { sub: 'Đồng Tháp', provId: 'dong-thap' },
  '67': { sub: 'An Giang', provId: 'an-giang' },
  '68': { sub: 'Kiên Giang', provId: 'an-giang' },
  '69': { sub: 'Cà Mau', provId: 'ca-mau' },
  '70': { sub: 'Tây Ninh', provId: 'tay-ninh' },
  '71': { sub: 'Bến Tre', provId: 'vinh-long' },
  '72': { sub: 'Bà Rịa - Vũng Tàu', provId: 'ho-chi-minh' },
  '83': { sub: 'Sóc Trăng', provId: 'can-tho' },
  '84': { sub: 'Trà Vinh', provId: 'vinh-long' },
  '93': { sub: 'Bình Phước', provId: 'dong-nai' },
  '94': { sub: 'Bạc Liêu', provId: 'ca-mau' },
  '95': { sub: 'Hậu Giang', provId: 'can-tho' }
};

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

  // 3. Khớp theo Biển số xe (Ví dụ: "36", "29", "89", "bien 36", "em 29 nha"...)
  const numMatches = norm.match(/\b(1[124-9]|2[0-9]|3[0-9]|4[013789]|5[0-9]|6[0-9]|7[0-9]|8[1-689]|9[0-5789])\b/g);
  if (numMatches) {
    for (const num of numMatches) {
      const plate = LICENSE_PLATE_MAP[num];
      if (plate) {
        const p = PROVINCES.find(item => item.id === plate.provId);
        if (p) {
          const sub = plate.sub;
          return {
            province: p,
            displayName: sub === p.name ? `${p.name} (Biển ${num})` : `${sub} (${p.name} - Biển ${num})`,
            ttsName: sub
          };
        }
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

// API cấu hình điểm thưởng & tương tác Realtime
app.get('/api/config', (req, res) => {
  res.json(GAME_CONFIG);
});

app.post('/api/config', (req, res) => {
  const newConfig = req.body;
  if (newConfig && typeof newConfig === 'object') {
    if (newConfig.COINS_TO_POINTS_RATE !== undefined) GAME_CONFIG.COINS_TO_POINTS_RATE = Math.max(1, Number(newConfig.COINS_TO_POINTS_RATE) || 30);
    if (newConfig.LIKES_PER_POINT !== undefined) GAME_CONFIG.LIKES_PER_POINT = Math.max(1, Number(newConfig.LIKES_PER_POINT) || 100);
    if (newConfig.SHARES_PER_POINT !== undefined) GAME_CONFIG.SHARES_PER_POINT = Math.max(1, Number(newConfig.SHARES_PER_POINT) || 10);
    if (newConfig.FOLLOW_POINTS !== undefined) GAME_CONFIG.FOLLOW_POINTS = Math.max(0, Number(newConfig.FOLLOW_POINTS) || 1);
    if (newConfig.COMMENT_POINTS !== undefined) GAME_CONFIG.COMMENT_POINTS = Math.max(0, Number(newConfig.COMMENT_POINTS) || 1);
    if (newConfig.VIP_COIN_THRESHOLD !== undefined) GAME_CONFIG.VIP_COIN_THRESHOLD = Math.max(1, Number(newConfig.VIP_COIN_THRESHOLD) || 20);
    if (newConfig.FAST_PASS_COIN_THRESHOLD !== undefined) GAME_CONFIG.FAST_PASS_COIN_THRESHOLD = Math.max(1, Number(newConfig.FAST_PASS_COIN_THRESHOLD) || 5);

    COINS_TO_POINTS_RATE = GAME_CONFIG.COINS_TO_POINTS_RATE;
    VIP_COIN_THRESHOLD = GAME_CONFIG.VIP_COIN_THRESHOLD;
    FAST_PASS_COIN_THRESHOLD = GAME_CONFIG.FAST_PASS_COIN_THRESHOLD;

    io.emit('configUpdated', GAME_CONFIG);
  }
  res.json({ success: true, config: GAME_CONFIG });
});

// API kết nối TikTok Live động
app.post('/api/tiktok/connect', async (req, res) => {
  const { username } = req.body;
  if (!username) {
    return res.status(400).json({ success: false, message: 'Thiếu username hoặc link TikTok' });
  }
  try {
    const status = await connectTikTokLive(username);
    res.json({ success: true, status });
  } catch (err) {
    res.status(500).json({ success: false, message: err.message, status: gameState.tiktok });
  }
});

app.post('/api/tiktok/disconnect', async (req, res) => {
  try {
    const status = await disconnectTikTokLive();
    res.json({ success: true, status });
  } catch (err) {
    res.status(500).json({ success: false, message: err.message });
  }
});

app.get('/api/tiktok/status', (req, res) => {
  res.json(gameState.tiktok);
});

// Khởi tạo Game State
const PROVINCE_VISIT_DURATION = 15; // Mỗi tỉnh ghé thăm 15 giây
const LEADERBOARD_SEASON_DURATION = 15 * 60; // 15 phút = 900 giây tự động reset Bảng Vàng

let gameState = {
  roundNumber: 1, // Mùa giải đua top #1
  roundTimeLeft: LEADERBOARD_SEASON_DURATION, // 15:00
  currentVisit: {
    provinceId: 'lao-cai',
    svgId: 'laocai',
    provinceName: 'Lào Cai',
    ttsName: 'Lào Cai',
    user: {
      uniqueId: 'toi_ech',
      nickname: 'TỚI Ếch',
      profilePictureUrl: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face'
    },
    leader: {
      uniqueId: 'toi_ech',
      nickname: 'TỚI Ếch',
      profilePictureUrl: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face',
      coins: 0
    },
    visitors: [
      {
        uniqueId: 'toi_ech',
        nickname: 'TỚI Ếch',
        profilePictureUrl: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face',
        coins: 0,
        joinedAt: Date.now()
      }
    ],
    timeLeft: PROVINCE_VISIT_DURATION,
    visitCount: 0
  },
  queue: [
    {
      id: 'q1',
      provinceId: 'da-nang',
      svgId: 'danang',
      provinceName: 'Đà Nẵng',
      ttsName: 'Đà Nẵng',
      user: {
        uniqueId: 'danang_lover',
        nickname: 'Biển Mỹ Khê',
        profilePictureUrl: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face'
      },
      leader: {
        uniqueId: 'danang_lover',
        nickname: 'Biển Mỹ Khê',
        profilePictureUrl: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face',
        coins: 0
      },
      visitors: [
        {
          uniqueId: 'danang_lover',
          nickname: 'Biển Mỹ Khê',
          profilePictureUrl: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face',
          coins: 0,
          joinedAt: Date.now()
        }
      ],
      coins: 0,
      priorityScore: 0,
      perkType: 'normal',
      addedAt: Date.now()
    },
    {
      id: 'q2',
      provinceId: 'tay-ninh',
      svgId: 'tayninh',
      provinceName: 'Tây Ninh',
      ttsName: 'Tây Ninh',
      user: {
        uniqueId: 'alo_vu',
        nickname: 'Alo vũ à vũ...',
        profilePictureUrl: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop&crop=face'
      },
      leader: {
        uniqueId: 'alo_vu',
        nickname: 'Alo vũ à vũ...',
        profilePictureUrl: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop&crop=face',
        coins: 0
      },
      visitors: [
        {
          uniqueId: 'alo_vu',
          nickname: 'Alo vũ à vũ...',
          profilePictureUrl: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&h=100&fit=crop&crop=face',
          coins: 0,
          joinedAt: Date.now()
        }
      ],
      coins: 0,
      priorityScore: 0,
      perkType: 'normal',
      addedAt: Date.now()
    },
    {
      id: 'q3',
      provinceId: 'cao-bang',
      svgId: 'caobang',
      provinceName: 'Cao Bằng',
      ttsName: 'Cao Bằng',
      user: {
        uniqueId: 'thac_ban_gioc',
        nickname: 'Cao Bằng Quê Tôi',
        profilePictureUrl: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop&crop=face'
      },
      leader: {
        uniqueId: 'thac_ban_gioc',
        nickname: 'Cao Bằng Quê Tôi',
        profilePictureUrl: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop&crop=face',
        coins: 0
      },
      visitors: [
        {
          uniqueId: 'thac_ban_gioc',
          nickname: 'Cao Bằng Quê Tôi',
          profilePictureUrl: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop&crop=face',
          coins: 0,
          joinedAt: Date.now()
        }
      ],
      coins: 0,
      priorityScore: 0,
      perkType: 'normal',
      addedAt: Date.now()
    }
  ],
  stats: {
    totalViewers: TOTAL_VIEWERS_START,
    followersGoal: FOLLOWERS_START,
    followersTarget: FOLLOWERS_TARGET,
    totalLikes: 0
  },
  provinceStats: {},
  leaderboard: [],
  recentNotifications: [],
  recentChats: [],
  tiktok: {
    connected: false,
    connecting: false,
    username: TIKTOK_USERNAME ? TIKTOK_USERNAME.replace(/^@/, '') : '',
    roomId: null,
    viewerCount: 0,
    lastError: null
  }
};

// Hàm lấy Top tỉnh thành được yêu quý / donate nhiều nhất
function getTopProvinces(limit = 5) {
  const entries = Object.entries(gameState.provinceStats);
  if (entries.length === 0) {
    // Khởi đầu buổi live = 0 điểm cho tất cả các tỉnh thành
    return PROVINCES.slice(0, limit).map(p => ({
      id: p.id,
      name: p.name,
      score: 0
    }));
  }
  return entries
    .map(([id, score]) => {
      const p = PROVINCES.find(prov => prov.id === id);
      return {
        id,
        name: p ? p.name : id,
        score
      };
    })
    .sort((a, b) => b.score - a.score)
    .slice(0, limit);
}

// Khởi tạo leaderboard ban đầu
gameState.leaderboard = getTopProvinces(5);

const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

// Hàm chuyển sang tỉnh tiếp theo trong hàng đợi
function nextProvince() {
  if (gameState.queue.length > 0) {
    const nextItem = gameState.queue.shift();
    const currentCount = (gameState.provinceStats[nextItem.provinceId] || 0) + 1;
    gameState.provinceStats[nextItem.provinceId] = currentCount;

    const visitors = nextItem.visitors && nextItem.visitors.length > 0 ? nextItem.visitors : [nextItem.user];
    const leader = nextItem.leader || nextItem.user;

    // Reset vé ưu tiên của các thành viên trong đoàn sau khi đã được ghé thăm
    visitors.forEach(v => {
      if (v && v.uniqueId) {
        const uState = getUserInteraction(v.uniqueId);
        uState.pendingCoins = 0;
        uState.lastProvinceId = null;
        uState.lastDisplayName = null;
      }
    });

    gameState.currentVisit = {
      provinceId: nextItem.provinceId,
      svgIds: nextItem.svgIds || [nextItem.provinceId.replace(/-/g, '')],
      provinceName: nextItem.provinceName,
      ttsName: nextItem.ttsName || nextItem.provinceName,
      user: leader,
      leader: leader,
      visitors: visitors,
      timeLeft: visitors.length >= 3 ? 20 : PROVINCE_VISIT_DURATION,
      visitCount: currentCount
    };

    io.emit('queueUpdated', gameState.queue);

    // Thông báo TTS chuyển tỉnh đa dạng theo quy mô đoàn
    let ttsText;
    if (visitors.length >= 5) {
      ttsText = getRandomLine('cohortMega', {
        province: nextItem.ttsName || nextItem.provinceName,
        leader: leader.nickname,
        count: visitors.length
      }) || `Đại gia đình đồng hương ${nextItem.ttsName || nextItem.provinceName} hôm nay quá đông đảo! Chào mừng trưởng đoàn ${leader.nickname} cùng hơn ${visitors.length} anh em đã tề tựu!`;
    } else if (visitors.length >= 2) {
      const otherNames = visitors.filter(v => v.uniqueId !== leader.uniqueId).slice(0, 3).map(v => v.nickname).join(', ');
      ttsText = getRandomLine('cohortSmall', {
        province: nextItem.ttsName || nextItem.provinceName,
        leader: leader.nickname,
        count: visitors.length,
        members: otherNames || 'các anh em'
      }) || `Đoàn ${nextItem.ttsName || nextItem.provinceName} hôm nay quá đông vui! Chào mừng trưởng đoàn ${leader.nickname} cùng các bạn ${otherNames} đã về với quê hương!`;
    } else {
      ttsText = getRandomLine('visitUser', {
        nickname: leader.nickname,
        province: nextItem.ttsName || nextItem.provinceName
      }) || `Đang cùng bạn ${leader.nickname} ghé thăm quê hương ${nextItem.ttsName || nextItem.provinceName}`;
    }
    io.emit('playTts', { text: ttsText });
  } else {
    // Nếu hết hàng đợi, tự động chọn một tỉnh ngẫu nhiên trong 34 tỉnh để không bị khoảng lặng (Anti-Dead Air)
    const randomProv = PROVINCES[Math.floor(Math.random() * PROVINCES.length)];
    const currentCount = (gameState.provinceStats[randomProv.id] || 0) + 1;
    gameState.provinceStats[randomProv.id] = currentCount;

    const defaultVisitor = {
      uniqueId: 'tiktok_live',
      nickname: 'Du khách TikTok',
      profilePictureUrl: 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&h=100&fit=crop&crop=face',
      coins: 0,
      joinedAt: Date.now()
    };

    gameState.currentVisit = {
      provinceId: randomProv.id,
      svgIds: randomProv.svgIds || [randomProv.id.replace(/-/g, '')],
      provinceName: randomProv.name,
      ttsName: randomProv.name,
      user: defaultVisitor,
      leader: defaultVisitor,
      visitors: [defaultVisitor],
      timeLeft: PROVINCE_VISIT_DURATION,
      visitCount: currentCount
    };

    const deadAirTts = getRandomLine('antiDeadAir', {
      province: randomProv.name
    }) || `Mời cả nhà cùng ngắm nhìn vẻ đẹp của ${randomProv.name}`;
    io.emit('playTts', { text: deadAirTts });
  }

  gameState.leaderboard = getTopProvinces(5);
  io.emit('leaderboardUpdated', gameState.leaderboard);
  io.emit('provinceChanged', gameState.currentVisit);
  io.emit('gameState', gameState);
}

// Xử lý Chốt Bảng Vàng 15 phút & Bắt đầu Mùa giải mới
function resetLeaderboardSeason(manualTrigger = false) {
  // 1. Xác định Quán quân Bảng Vàng (Top 1)
  const currentLeaderboard = getTopProvinces(5);
  const winner = currentLeaderboard.find(p => (p.score || 0) > 0);

  if (winner) {
    const winnerTts = `Thời gian 15 phút đã khép lại! Xin chúc mừng tỉnh ${winner.name} đã xuất sắc giành Quán Quân Bảng Vàng mùa này với ${winner.score} điểm! Bắt đầu mùa đua mới ngay bây giờ!`;
    io.emit('playTts', { text: winnerTts });
    io.emit('seasonWinner', {
      provinceName: winner.name,
      score: winner.score,
      roundNumber: gameState.roundNumber
    });
  } else {
    const freshTts = `Hết 15 phút mùa giải! Bắt đầu vòng đua Top mới, cả nhà cùng gõ tên tỉnh và tặng quà để đưa quê hương mình lên đỉnh Bảng Vàng nhé!`;
    io.emit('playTts', { text: freshTts });
  }

  // 2. Tăng số thứ tự vòng/mùa giải
  gameState.roundNumber++;
  gameState.roundTimeLeft = LEADERBOARD_SEASON_DURATION;

  // 3. Reset toàn bộ điểm Bảng Vàng về 0 và làm mới cờ tương tác mùa giải của người xem
  for (const provId in gameState.provinceStats) {
    gameState.provinceStats[provId] = 0;
  }
  for (const uid in userInteractions) {
    if (userInteractions[uid]) {
      userInteractions[uid].hasCommentedInSeason = false;
      userInteractions[uid].hasFollowRewarded = false;
      userInteractions[uid].accumulatedLikes = 0;
      userInteractions[uid].accumulatedShares = 0;
    }
  }
  gameState.currentVisit.visitCount = 0;
  gameState.leaderboard = getTopProvinces(5);

  // 4. Đồng bộ cho toàn bộ client
  io.emit('roundReset', {
    roundNumber: gameState.roundNumber,
    roundTimeLeft: gameState.roundTimeLeft,
    winner: winner || null
  });
  io.emit('provinceChanged', gameState.currentVisit);
  io.emit('leaderboardUpdated', gameState.leaderboard);
  io.emit('gameState', gameState);
}


let lastCtaTime = Date.now();
let lastDropInTtsTime = 0;

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

  // Đếm ngược thời gian mùa giải Đua Top Bảng Vàng (15 phút)
  if (gameState.roundTimeLeft > 0) {
    gameState.roundTimeLeft--;
  } else {
    resetLeaderboardSeason();
  }

  // Kêu gọi tương tác / Đua top định kỳ (Call to action) khi hàng đợi trống
  if (Date.now() - lastCtaTime > 35000 && gameState.queue.length === 0) {
    lastCtaTime = Date.now();
    const cat = Math.random() < 0.5 ? 'cta' : 'duaTop';
    const ctaTts = getRandomLine(cat);
    if (ctaTts) io.emit('playTts', { text: ctaTts });
  }
}, 1000);

// Bộ nhớ tương tác người dùng phục vụ tính điểm ưu tiên
const userInteractions = {};

function getUserInteraction(uniqueId) {
  if (!userInteractions[uniqueId]) {
    userInteractions[uniqueId] = {
      isFollower: false,
      hasFollowRewarded: false,
      shared: false,
      shareCount: 0,
      accumulatedShares: 0,
      likeCount: 0,
      accumulatedLikes: 0,
      hasCommentedInSeason: false,
      pendingCoins: 0,
      lastProvinceId: null,
      lastDisplayName: null,
      lastTtsName: null,
      lastSvgIds: null
    };
  }
  return userInteractions[uniqueId];
}

// Công thức tính điểm ưu tiên: (Số xu * 1000) + Điểm tương tác
function calculatePriority(coins, userState) {
  const c = Number(coins) || 0;
  let interactionScore = 0;
  if (userState.isFollower) interactionScore += 100;
  if (userState.shared) interactionScore += 50;
  if (userState.likeCount >= 20) interactionScore += 20;

  return (c * 1000) + interactionScore;
}

// Sắp xếp hàng đợi theo thứ tự ưu tiên
function sortQueue() {
  gameState.queue.sort((a, b) => {
    if (b.priorityScore !== a.priorityScore) {
      return b.priorityScore - a.priorityScore; // Điểm cao hơn đứng trước
    }
    return a.addedAt - b.addedAt; // Cùng điểm thì ai đến trước đứng trước
  });
}

// Xử lý khi có người yêu cầu ghé thăm tỉnh qua chat hoặc mock
function handleProvinceRequest(user, comment, isVip = false, coins = 0) {
  const matched = matchProvince(comment);
  if (!matched) return null;

  const targetProvince = matched.province;
  const uid = user.uniqueId || 'user_' + Date.now();
  const uState = getUserInteraction(uid);

  // Ghi nhớ tỉnh mà người xem này quan tâm
  uState.lastProvinceId = targetProvince.id;
  uState.lastDisplayName = matched.displayName;
  uState.lastTtsName = matched.ttsName;
  uState.lastSvgIds = targetProvince.svgIds || [targetProvince.id.replace(/-/g, '')];

  const totalItemCoins = (Number(coins) || 0) + (uState.pendingCoins || 0);
  uState.pendingCoins = 0; // Đã tiêu thụ xu chờ

  const userObj = {
    uniqueId: uid,
    nickname: user.nickname || 'Khán giả',
    profilePictureUrl: user.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face',
    coins: totalItemCoins,
    joinedAt: Date.now()
  };

  // Tính điểm thưởng: Comment tỉnh chỉ cộng điểm 1 lần duy nhất trong mỗi mùa giải 15 phút (chống spam)
  let commentPointsToAdd = 0;
  if (!uState.hasCommentedInSeason) {
    uState.hasCommentedInSeason = true;
    commentPointsToAdd = GAME_CONFIG.COMMENT_POINTS;
  }
  const pointsToAdd = (totalItemCoins * GAME_CONFIG.COINS_TO_POINTS_RATE) + commentPointsToAdd;

  // TRƯỜNG HỢP 1: Tỉnh này ĐANG ĐƯỢC CHIẾU TRÊN MÀN HÌNH (Nhập đoàn tức thì - Instant Drop-in)
  if (gameState.currentVisit && gameState.currentVisit.provinceId === targetProvince.id) {
    if (!gameState.currentVisit.visitors) {
      gameState.currentVisit.visitors = [gameState.currentVisit.user || userObj];
    }
    const existingVisitor = gameState.currentVisit.visitors.find(v => v.uniqueId === uid);
    if (existingVisitor) {
      existingVisitor.coins = (existingVisitor.coins || 0) + totalItemCoins;
    } else {
      gameState.currentVisit.visitors.push(userObj);
    }

    // Xác định Trưởng đoàn theo số xu cao nhất
    gameState.currentVisit.visitors.sort((a, b) => (b.coins || 0) - (a.coins || 0) || a.joinedAt - b.joinedAt);
    const newLeader = gameState.currentVisit.visitors[0];
    const becameLeader = (newLeader.uniqueId === uid && gameState.currentVisit.leader?.uniqueId !== uid);
    gameState.currentVisit.leader = newLeader;
    gameState.currentVisit.user = newLeader;

    // Cộng điểm danh vọng cho tỉnh
    gameState.currentVisit.visitCount += pointsToAdd;
    gameState.provinceStats[targetProvince.id] = gameState.currentVisit.visitCount;

    // Phát sự kiện Nhập đoàn tức thì (Drop-in) cho Client
    io.emit('visitorDropIn', {
      provinceId: targetProvince.id,
      provinceName: matched.displayName,
      user: userObj,
      leader: newLeader,
      isLeader: becameLeader,
      totalVisitors: gameState.currentVisit.visitors.length,
      coins: totalItemCoins
    });

    // Lời thoại MC chúc mừng nhập đoàn (cooldown 8s chống nghẽn âm thanh)
    const now = Date.now();
    if (becameLeader) {
      const leaderTts = `Chúc mừng bạn ${userObj.nickname} vừa vươn lên làm Trưởng đoàn ${matched.ttsName || matched.displayName}!`;
      io.emit('playTts', { text: leaderTts });
      lastDropInTtsTime = now;
    } else if (!existingVisitor && (now - lastDropInTtsTime > 8000)) {
      lastDropInTtsTime = now;
      const dropInTts = getRandomLine('visitorDropIn', {
        nickname: userObj.nickname,
        province: matched.ttsName || matched.displayName,
        leader: newLeader.nickname,
        count: gameState.currentVisit.visitors.length
      }) || `Hoan nghênh ${userObj.nickname} vừa nhập đoàn ${matched.ttsName || matched.displayName}!`;
      io.emit('playTts', { text: dropInTts });
    }

    gameState.leaderboard = getTopProvinces(5);
    io.emit('leaderboardUpdated', gameState.leaderboard);
    io.emit('gameState', gameState);

    return matched;
  }

  // TRƯỜNG HỢP 2: Tỉnh này ĐÃ CÓ trong hàng đợi (Gộp vào đoàn đồng hương)
  const existingProvinceItem = gameState.queue.find(item => item.provinceId === targetProvince.id);

  if (existingProvinceItem) {
    if (!existingProvinceItem.visitors) {
      existingProvinceItem.visitors = [existingProvinceItem.user || userObj];
    }

    const existingVisitor = existingProvinceItem.visitors.find(v => v.uniqueId === uid);
    if (existingVisitor) {
      existingVisitor.coins = (existingVisitor.coins || 0) + totalItemCoins;
    } else {
      existingProvinceItem.visitors.push(userObj);
    }

    // Sắp xếp tìm Trưởng đoàn: Ai nhiều xu nhất đứng đầu
    existingProvinceItem.visitors.sort((a, b) => (b.coins || 0) - (a.coins || 0) || a.joinedAt - b.joinedAt);
    existingProvinceItem.leader = existingProvinceItem.visitors[0];
    existingProvinceItem.user = existingProvinceItem.leader; // Tương thích ngược

    // Tổng số xu của đoàn
    existingProvinceItem.coins = existingProvinceItem.visitors.reduce((sum, v) => sum + (v.coins || 0), 0);

    // Tính điểm ưu tiên: Điểm xu + Điểm tương tác + Bonus mỗi thành viên +20 điểm
    const basePriority = calculatePriority(existingProvinceItem.coins, uState);
    const cohortBonus = (existingProvinceItem.visitors.length - 1) * 20;
    existingProvinceItem.priorityScore = basePriority + cohortBonus;

    if (existingProvinceItem.coins >= GAME_CONFIG.VIP_COIN_THRESHOLD) existingProvinceItem.perkType = 'vip';
    else if (existingProvinceItem.coins >= GAME_CONFIG.FAST_PASS_COIN_THRESHOLD) existingProvinceItem.perkType = 'fast';
    else if (existingProvinceItem.coins > 0) existingProvinceItem.perkType = 'gift';
    else if (existingProvinceItem.visitors.length >= 3) existingProvinceItem.perkType = 'cohort';
    else if (uState.isFollower) existingProvinceItem.perkType = 'follower';
    else if (uState.shared) existingProvinceItem.perkType = 'share';
    else existingProvinceItem.perkType = 'normal';

    // Cộng điểm danh vọng cho tỉnh
    gameState.provinceStats[targetProvince.id] = (gameState.provinceStats[targetProvince.id] || 0) + pointsToAdd;

    sortQueue();
  } else {
    // TRƯỜNG HỢP 3: Tỉnh này CHƯA CÓ trong hàng đợi -> Khởi tạo đoàn mới
    const basePriority = calculatePriority(totalItemCoins, uState);
    let perkType = 'normal';
    if (totalItemCoins >= GAME_CONFIG.VIP_COIN_THRESHOLD) perkType = 'vip';
    else if (totalItemCoins >= GAME_CONFIG.FAST_PASS_COIN_THRESHOLD) perkType = 'fast';
    else if (totalItemCoins > 0) perkType = 'gift';
    else if (uState.isFollower) perkType = 'follower';
    else if (uState.shared) perkType = 'share';

    const queueItem = {
      id: 'req_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4),
      provinceId: targetProvince.id,
      svgIds: targetProvince.svgIds || [targetProvince.id.replace(/-/g, '')],
      provinceName: matched.displayName,
      ttsName: matched.ttsName,
      leader: userObj,
      user: userObj, // Tương thích ngược
      visitors: [userObj],
      coins: totalItemCoins,
      priorityScore: basePriority,
      perkType: perkType,
      addedAt: Date.now()
    };
    gameState.queue.push(queueItem);

    // Cộng điểm danh vọng cho tỉnh
    gameState.provinceStats[targetProvince.id] = (gameState.provinceStats[targetProvince.id] || 0) + pointsToAdd;

    sortQueue();
  }

  gameState.stats.totalViewers++;
  gameState.leaderboard = getTopProvinces(5);
  io.emit('leaderboardUpdated', gameState.leaderboard);
  io.emit('queueUpdated', gameState.queue);
  io.emit('gameState', gameState);

  return matched;
}

// Xử lý tặng quà (Gift)
function handleGiftEvent(giftData) {
  const { uniqueId, nickname, giftName, diamondCount, repeatCount, profilePictureUrl } = giftData;
  const totalCoins = (diamondCount || 1) * (repeatCount || 1);
  const uid = uniqueId || 'donor_' + Date.now();
  const uState = getUserInteraction(uid);

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

  const pointsFromGift = totalCoins * COINS_TO_POINTS_RATE;
  let targetProvinceId = null;
  let targetProvinceName = null;

  // 1. Kiểm tra nếu user thuộc tỉnh đang ghé thăm trên màn hình
  const isVisitingCurrent = gameState.currentVisit && (
    (gameState.currentVisit.visitors && gameState.currentVisit.visitors.some(v => v.uniqueId === uid || (nickname && v.nickname === nickname))) ||
    (uState.lastProvinceId && gameState.currentVisit.provinceId === uState.lastProvinceId)
  );

  if (isVisitingCurrent) {
    targetProvinceId = gameState.currentVisit.provinceId;
    targetProvinceName = gameState.currentVisit.provinceName;

    if (!gameState.currentVisit.visitors) gameState.currentVisit.visitors = [];
    let curVis = gameState.currentVisit.visitors.find(v => v.uniqueId === uid || (nickname && v.nickname === nickname));
    if (curVis) {
      curVis.coins = (curVis.coins || 0) + totalCoins;
    } else {
      curVis = {
        uniqueId: uid,
        nickname: nickname || 'Khán giả',
        profilePictureUrl: profilePictureUrl || 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face',
        coins: totalCoins,
        joinedAt: Date.now()
      };
      gameState.currentVisit.visitors.push(curVis);
    }

    gameState.currentVisit.visitors.sort((a, b) => (b.coins || 0) - (a.coins || 0) || a.joinedAt - b.joinedAt);
    gameState.currentVisit.leader = gameState.currentVisit.visitors[0];
    gameState.currentVisit.user = gameState.currentVisit.leader;

    gameState.currentVisit.visitCount += pointsFromGift;
    gameState.provinceStats[targetProvinceId] = gameState.currentVisit.visitCount;
    io.emit('provinceChanged', gameState.currentVisit);
  } else {
    // 2. Kiểm tra trong hàng đợi (Queue)
    const queueItemWithUser = gameState.queue.find(item => 
      (item.visitors && item.visitors.some(v => v.uniqueId === uid || (nickname && v.nickname === nickname))) ||
      (uState.lastProvinceId && item.provinceId === uState.lastProvinceId)
    );

    if (queueItemWithUser) {
      targetProvinceId = queueItemWithUser.provinceId;
      targetProvinceName = queueItemWithUser.provinceName;

      if (!queueItemWithUser.visitors) queueItemWithUser.visitors = [];
      let vObj = queueItemWithUser.visitors.find(v => v.uniqueId === uid || (nickname && v.nickname === nickname));
      if (vObj) {
        vObj.coins = (vObj.coins || 0) + totalCoins;
      } else {
        vObj = {
          uniqueId: uid,
          nickname: nickname || 'Khán giả',
          profilePictureUrl: profilePictureUrl || 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face',
          coins: totalCoins,
          joinedAt: Date.now()
        };
        queueItemWithUser.visitors.push(vObj);
      }

      queueItemWithUser.visitors.sort((a, b) => (b.coins || 0) - (a.coins || 0) || a.joinedAt - b.joinedAt);
      queueItemWithUser.leader = queueItemWithUser.visitors[0];
      queueItemWithUser.user = queueItemWithUser.leader;
      queueItemWithUser.coins = queueItemWithUser.visitors.reduce((s, v) => s + (v.coins || 0), 0);

      const basePriority = calculatePriority(queueItemWithUser.coins, uState);
      const cohortBonus = (queueItemWithUser.visitors.length - 1) * 20;
      queueItemWithUser.priorityScore = basePriority + cohortBonus;

      if (queueItemWithUser.coins >= VIP_COIN_THRESHOLD) queueItemWithUser.perkType = 'vip';
      else if (queueItemWithUser.coins >= FAST_PASS_COIN_THRESHOLD) queueItemWithUser.perkType = 'fast';
      else queueItemWithUser.perkType = 'gift';

      gameState.provinceStats[targetProvinceId] = (gameState.provinceStats[targetProvinceId] || 0) + pointsFromGift;
    } else if (uState.lastProvinceId) {
      // User chưa trong hàng đợi nhưng trước đó ĐÃ comment tên tỉnh: Tạo vé ưu tiên ngay lập tức!
      targetProvinceId = uState.lastProvinceId;
      targetProvinceName = uState.lastDisplayName;
      const priorityScore = calculatePriority(totalCoins, uState);
      let perkType = totalCoins >= VIP_COIN_THRESHOLD ? 'vip' : (totalCoins >= FAST_PASS_COIN_THRESHOLD ? 'fast' : 'gift');
      const donorObj = {
        uniqueId: uid,
        nickname: nickname || 'Khán giả',
        profilePictureUrl: profilePictureUrl || 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=100&fit=crop&crop=face',
        coins: totalCoins,
        joinedAt: Date.now()
      };
      const queueItem = {
        id: 'req_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4),
        provinceId: uState.lastProvinceId,
        svgIds: uState.lastSvgIds || [uState.lastProvinceId.replace(/-/g, '')],
        provinceName: uState.lastDisplayName,
        ttsName: uState.lastTtsName,
        leader: donorObj,
        user: donorObj,
        visitors: [donorObj],
        coins: totalCoins,
        priorityScore: priorityScore,
        perkType: perkType,
        addedAt: Date.now()
      };
      gameState.queue.push(queueItem);
      gameState.provinceStats[targetProvinceId] = (gameState.provinceStats[targetProvinceId] || 0) + pointsFromGift;
    } else {
      // 3. User CHƯA TỪNG comment tỉnh: Tạm lưu pendingCoins, khi họ comment tên tỉnh sẽ tự động cộng dồn
      uState.pendingCoins = (uState.pendingCoins || 0) + totalCoins;
    }
  }

  sortQueue();
  io.emit('queueUpdated', gameState.queue);

  // 4. Hiệu ứng & Lời thoại MC
  if (totalCoins >= VIP_COIN_THRESHOLD) {
    io.emit('vipSpecialEffect', { nickname, giftName, coins: totalCoins });
    const tts = getRandomLine('vipGift', { nickname, giftName, coins: totalCoins, province: targetProvinceName || '' }) ||
      `Cảm ơn đại gia ${nickname} đã tặng ${giftName}! Nhận đặc quyền ưu tiên đọc trước!`;
    io.emit('playTts', { text: tts });
  } else if (totalCoins >= FAST_PASS_COIN_THRESHOLD) {
    const tts = getRandomLine('fastPassGift', { nickname, giftName, coins: totalCoins, province: targetProvinceName || '' }) ||
      `Cảm ơn ${nickname} đã tặng ${giftName} để đọc nhanh!`;
    io.emit('playTts', { text: tts });
  } else {
    if (!targetProvinceId) {
      const tts = `Cảm ơn ${nickname} đã tặng ${giftName || 'quà'}! Bạn hãy bình luận tên tỉnh hoặc số biển số để cộng điểm cho quê hương nhé!`;
      io.emit('playTts', { text: tts });
    } else if (Math.random() < 0.6) {
      const tts = getRandomLine('smallGift', { nickname, giftName: giftName || 'hoa hồng' });
      if (tts) io.emit('playTts', { text: tts });
    }
  }

  gameState.stats.followersGoal += Math.floor(totalCoins / 2) + 1;
  gameState.leaderboard = getTopProvinces(5);
  io.emit('leaderboardUpdated', gameState.leaderboard);
  io.emit('gameState', gameState);
}

// Xử lý sự kiện Follow kênh
function handleFollowEvent(userData) {
  const uid = userData.uniqueId;
  if (uid) {
    const uState = getUserInteraction(uid);
    uState.isFollower = true;
    const item = gameState.queue.find(q => q.user.uniqueId === uid);
    if (item) {
      item.priorityScore = calculatePriority(item.coins, uState);
      if (!item.coins) item.perkType = 'follower';
      sortQueue();
      io.emit('queueUpdated', gameState.queue);
    }

    // Cộng điểm cho tỉnh khi Follow (1 lần duy nhất trong mùa giải)
    if (!uState.hasFollowRewarded && GAME_CONFIG.FOLLOW_POINTS > 0) {
      uState.hasFollowRewarded = true;
      const targetProvId = uState.lastProvinceId || gameState.currentVisit?.provinceId;
      if (targetProvId) {
        gameState.provinceStats[targetProvId] = (gameState.provinceStats[targetProvId] || 0) + GAME_CONFIG.FOLLOW_POINTS;
        if (gameState.currentVisit?.provinceId === targetProvId) {
          gameState.currentVisit.visitCount = gameState.provinceStats[targetProvId];
          io.emit('provinceChanged', gameState.currentVisit);
        }
        gameState.leaderboard = getTopProvinces(5);
        io.emit('leaderboardUpdated', gameState.leaderboard);
      }
    }
  }

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

// Xử lý sự kiện Chia sẻ Live (Share)
function handleShareEvent(userData) {
  const uid = userData.uniqueId;
  if (uid) {
    const uState = getUserInteraction(uid);
    uState.shared = true;
    uState.shareCount = (uState.shareCount || 0) + 1;
    uState.accumulatedShares = (uState.accumulatedShares || 0) + 1;

    const item = gameState.queue.find(q => q.user.uniqueId === uid);
    if (item) {
      item.priorityScore = calculatePriority(item.coins, uState);
      if (!item.coins && !uState.isFollower) item.perkType = 'share';
      sortQueue();
      io.emit('queueUpdated', gameState.queue);
    }

    // Kiểm tra mốc đổi lượt chia sẻ thành Điểm Yêu thương (mặc định 10 share = +1 điểm)
    if (uState.accumulatedShares >= GAME_CONFIG.SHARES_PER_POINT) {
      const pointsEarned = Math.floor(uState.accumulatedShares / GAME_CONFIG.SHARES_PER_POINT);
      uState.accumulatedShares %= GAME_CONFIG.SHARES_PER_POINT;

      const targetProvId = uState.lastProvinceId || gameState.currentVisit?.provinceId;
      if (targetProvId) {
        gameState.provinceStats[targetProvId] = (gameState.provinceStats[targetProvId] || 0) + pointsEarned;
        if (gameState.currentVisit?.provinceId === targetProvId) {
          gameState.currentVisit.visitCount = gameState.provinceStats[targetProvId];
          io.emit('provinceChanged', gameState.currentVisit);
        }
        gameState.leaderboard = getTopProvinces(5);
        io.emit('leaderboardUpdated', gameState.leaderboard);
        io.emit('gameState', gameState);
      }
    }
  }
}

// Xử lý sự kiện thả tim (Like)
function handleLikeEvent(count, userData) {
  const uid = typeof userData === 'object' ? userData.uniqueId : null;
  const nickname = typeof userData === 'object' ? (userData.nickname || 'Người xem') : (userData || 'Người xem');

  if (uid) {
    const uState = getUserInteraction(uid);
    uState.likeCount = (uState.likeCount || 0) + count;
    uState.accumulatedLikes = (uState.accumulatedLikes || 0) + count;

    if (uState.likeCount >= 20) {
      const item = gameState.queue.find(q => q.user.uniqueId === uid);
      if (item) {
        item.priorityScore = calculatePriority(item.coins, uState);
        sortQueue();
        io.emit('queueUpdated', gameState.queue);
      }
    }

    // Kiểm tra mốc đổi tim thành Điểm Yêu thương (mặc định 100 tim = +1 điểm)
    if (uState.accumulatedLikes >= GAME_CONFIG.LIKES_PER_POINT) {
      const pointsEarned = Math.floor(uState.accumulatedLikes / GAME_CONFIG.LIKES_PER_POINT);
      uState.accumulatedLikes %= GAME_CONFIG.LIKES_PER_POINT;

      const targetProvId = uState.lastProvinceId || gameState.currentVisit?.provinceId;
      if (targetProvId) {
        gameState.provinceStats[targetProvId] = (gameState.provinceStats[targetProvId] || 0) + pointsEarned;
        if (gameState.currentVisit?.provinceId === targetProvId) {
          gameState.currentVisit.visitCount = gameState.provinceStats[targetProvId];
          io.emit('provinceChanged', gameState.currentVisit);
        }
        gameState.leaderboard = getTopProvinces(5);
        io.emit('leaderboardUpdated', gameState.leaderboard);
        io.emit('gameState', gameState);
      }
    }
  }

  const prevLikes = gameState.stats.totalLikes;
  gameState.stats.totalLikes += count;
  io.emit('like', {
    nickname: nickname,
    likeCount: count,
    totalLikes: gameState.stats.totalLikes
  });

  if (Math.floor(gameState.stats.totalLikes / 150) > Math.floor(prevLikes / 150)) {
    const tts = getRandomLine('likeMilestone');
    if (tts) io.emit('playTts', { text: tts });
  }
}

// Hàm chuẩn hóa username TikTok từ chuỗi hoặc link
async function resolveTikTokUsername(rawInput) {
  let input = String(rawInput || '').trim();
  if (!input) {
    throw new Error('Vui lòng nhập @username hoặc link TikTok Live cần kết nối');
  }
  if (input.startsWith('http://') || input.startsWith('https://') || input.includes('tiktok.com/')) {
    const urlToFetch = input.startsWith('http') ? input : `https://${input}`;
    const directMatch = urlToFetch.match(/tiktok\.com\/@([^/?#]+)/i);
    if (directMatch && directMatch[1]) {
      return directMatch[1];
    }
    try {
      const resp = await fetch(urlToFetch, { redirect: 'follow' });
      const finalUrl = resp.url || '';
      const resolvedMatch = finalUrl.match(/tiktok\.com\/@([^/?#]+)/i);
      if (resolvedMatch && resolvedMatch[1]) {
        return resolvedMatch[1];
      }
    } catch (e) {
      console.warn('[TikTok URL Resolve Warning]', e.message);
    }
  }
  return input.replace(/^@/, '').split(/[/?#]/)[0].trim();
}

function processChatMessage(user, comment, isMock = false) {
  const matched = handleProvinceRequest(user, comment, false, 0);
  const prefix = isMock ? '[Mock Chat]' : '[TikTok Chat]';
  if (matched) {
    console.log(`${prefix} 💬 ${user.nickname}: "${comment}" -> ✅ Khớp tỉnh: ${matched.displayName}`);
  } else {
    console.log(`${prefix} 💬 ${user.nickname}: "${comment}" (Không chứa tên tỉnh)`);
  }

  const chatEntry = {
    id: 'c_' + Date.now() + '_' + Math.random().toString(36).substr(2, 4),
    uniqueId: user.uniqueId,
    nickname: user.nickname,
    profilePictureUrl: user.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face',
    comment: comment,
    matchedProvince: matched ? matched.displayName : null,
    timestamp: Date.now()
  };

  if (!gameState.recentChats) gameState.recentChats = [];
  gameState.recentChats.unshift(chatEntry);
  if (gameState.recentChats.length > 30) gameState.recentChats.pop();

  io.emit('chat', chatEntry);
  return chatEntry;
}

// Kết nối TikTok Live chuẩn mới
let tiktokLive = null;

async function connectTikTokLive(usernameOrUrl) {
  const cleanUser = await resolveTikTokUsername(usernameOrUrl);
  if (!cleanUser) {
    throw new Error('Không tìm thấy @username hợp lệ từ dữ liệu nhập vào');
  }

  if (tiktokLive) {
    try {
      await tiktokLive.disconnect();
    } catch (_) {}
    tiktokLive = null;
  }

  gameState.tiktok.connected = false;
  gameState.tiktok.connecting = true;
  gameState.tiktok.username = cleanUser;
  gameState.tiktok.roomId = null;
  gameState.tiktok.lastError = null;
  io.emit('tiktok:status', gameState.tiktok);

  console.log(`[TikTok Live] Đang bắt đầu kết nối tới @${cleanUser}...`);

  try {
    tiktokLive = new TikTokLiveConnection(cleanUser, {
      processInitialData: true,
      fetchRoomInfoOnConnect: false,
      enableExtendedGiftInfo: false,
      sessionId: process.env.TIKTOK_SESSION_ID || undefined
    });

    tiktokLive.on(ControlEvent.CONNECTED, state => {
      gameState.tiktok.connected = true;
      gameState.tiktok.connecting = false;
      gameState.tiktok.roomId = state?.roomId || tiktokLive?.roomId || null;
      gameState.tiktok.lastError = null;
      console.log(`[TikTok Live] ✅ Đã kết nối thành công phòng @${cleanUser} (RoomId: ${gameState.tiktok.roomId})`);
      io.emit('tiktok:status', gameState.tiktok);
      io.emit('gameState', gameState);
    });

    tiktokLive.on(ControlEvent.DISCONNECTED, () => {
      gameState.tiktok.connected = false;
      gameState.tiktok.connecting = false;
      console.log(`[TikTok Live] 🔌 Đã ngắt kết nối phòng @${cleanUser}`);
      io.emit('tiktok:status', gameState.tiktok);
      io.emit('gameState', gameState);
    });

    tiktokLive.on(ControlEvent.ERROR, err => {
      gameState.tiktok.lastError = err?.message || String(err);
      console.warn(`[TikTok Live Cảnh báo] ${gameState.tiktok.lastError}`);
      io.emit('tiktok:status', gameState.tiktok);
    });

    tiktokLive.on(WebcastEvent.ROOM_USER, data => {
      const viewerCount = Number(data?.total ?? data?.viewerCount ?? 0);
      if (viewerCount > 0) {
        gameState.tiktok.viewerCount = viewerCount;
        gameState.stats.totalViewers = Math.max(gameState.stats.totalViewers, viewerCount);
        io.emit('tiktok:status', gameState.tiktok);
        io.emit('gameState', gameState);
      }
    });

    tiktokLive.on(WebcastEvent.CHAT, data => {
      const user = {
        uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
        nickname: data.user?.nickname || data.nickname || 'Khán giả',
        profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || data.profilePictureUrl
      };
      const comment = data.content || data.comment || '';
      processChatMessage(user, comment, false);
    });

    tiktokLive.on(WebcastEvent.GIFT, data => {
      handleGiftEvent({
        uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
        nickname: data.user?.nickname || data.nickname || 'Khán giả',
        giftName: data.gift?.name || data.giftName || 'Hoa hồng',
        diamondCount: Number(data.gift?.diamondCount) || Number(data.diamondCount) || 1,
        repeatCount: Number(data.repeatCount) || 1,
        profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || data.profilePictureUrl
      });
    });

    tiktokLive.on(WebcastEvent.LIKE, data => {
      const count = Number(data.count) || Number(data.likeCount) || 1;
      const user = {
        uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
        nickname: data.user?.nickname || data.nickname || 'Người xem'
      };
      handleLikeEvent(count, user);
    });

    const handleSocial = data => {
      const user = {
        uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
        nickname: data.user?.nickname || data.nickname || 'Khán giả',
        profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || ''
      };
      const action = String(data?.action || '');
      const disp = String(data?.common?.displayText?.displayType || data?.displayType || '').toLowerCase();
      if (action === '3' || disp.includes('share')) {
        handleShareEvent(user);
      } else {
        handleFollowEvent(user);
      }
    };

    tiktokLive.on(WebcastEvent.FOLLOW, data => {
      handleFollowEvent({
        uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
        nickname: data.user?.nickname || data.nickname || 'Khán giả',
        profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || ''
      });
    });

    tiktokLive.on(WebcastEvent.SHARE, data => {
      handleShareEvent({
        uniqueId: data.user?.displayId || data.user?.id || data.uniqueId,
        nickname: data.user?.nickname || data.nickname || 'Khán giả',
        profilePictureUrl: data.user?.avatarThumb?.urlList?.[0] || ''
      });
    });

    tiktokLive.on(WebcastEvent.SOCIAL, handleSocial);

    await tiktokLive.connect();
    return gameState.tiktok;
  } catch (err) {
    gameState.tiktok.connected = false;
    gameState.tiktok.connecting = false;
    gameState.tiktok.lastError = err?.message || String(err);
    console.error(`[TikTok Live Lỗi kết nối] ${gameState.tiktok.lastError}`);
    io.emit('tiktok:status', gameState.tiktok);
    throw err;
  }
}

async function disconnectTikTokLive() {
  if (tiktokLive) {
    try {
      await tiktokLive.disconnect();
    } catch (_) {}
    tiktokLive = null;
  }
  gameState.tiktok.connected = false;
  gameState.tiktok.connecting = false;
  gameState.tiktok.roomId = null;
  io.emit('tiktok:status', gameState.tiktok);
  io.emit('gameState', gameState);
  console.log('[TikTok Live] Đã chủ động ngắt kết nối');
  return gameState.tiktok;
}

// Tự động kết nối lúc khởi động nếu có TIKTOK_USERNAME
if (TIKTOK_USERNAME) {
  connectTikTokLive(TIKTOK_USERNAME).catch(err => {
    console.log(`[TikTok Live Khởi động] Thông báo: ${err.message}`);
  });
}

// Xử lý sự kiện Socket.IO từ Frontend & Admin Mock Simulator
io.on('connection', socket => {
  // Gửi trạng thái ban đầu ngay khi client kết nối
  socket.emit('gameState', gameState);
  socket.emit('leaderboardUpdated', getTopProvinces(5));
  socket.emit('tiktok:status', gameState.tiktok);
  socket.emit('configUpdated', GAME_CONFIG);

  // Cập nhật cấu hình điểm thưởng Realtime từ admin
  socket.on('config:update', newConfig => {
    if (newConfig && typeof newConfig === 'object') {
      if (newConfig.COINS_TO_POINTS_RATE !== undefined) GAME_CONFIG.COINS_TO_POINTS_RATE = Math.max(1, Number(newConfig.COINS_TO_POINTS_RATE) || 30);
      if (newConfig.LIKES_PER_POINT !== undefined) GAME_CONFIG.LIKES_PER_POINT = Math.max(1, Number(newConfig.LIKES_PER_POINT) || 100);
      if (newConfig.SHARES_PER_POINT !== undefined) GAME_CONFIG.SHARES_PER_POINT = Math.max(1, Number(newConfig.SHARES_PER_POINT) || 10);
      if (newConfig.FOLLOW_POINTS !== undefined) GAME_CONFIG.FOLLOW_POINTS = Math.max(0, Number(newConfig.FOLLOW_POINTS) || 1);
      if (newConfig.COMMENT_POINTS !== undefined) GAME_CONFIG.COMMENT_POINTS = Math.max(0, Number(newConfig.COMMENT_POINTS) || 1);
      if (newConfig.VIP_COIN_THRESHOLD !== undefined) GAME_CONFIG.VIP_COIN_THRESHOLD = Math.max(1, Number(newConfig.VIP_COIN_THRESHOLD) || 20);
      if (newConfig.FAST_PASS_COIN_THRESHOLD !== undefined) GAME_CONFIG.FAST_PASS_COIN_THRESHOLD = Math.max(1, Number(newConfig.FAST_PASS_COIN_THRESHOLD) || 5);

      COINS_TO_POINTS_RATE = GAME_CONFIG.COINS_TO_POINTS_RATE;
      VIP_COIN_THRESHOLD = GAME_CONFIG.VIP_COIN_THRESHOLD;
      FAST_PASS_COIN_THRESHOLD = GAME_CONFIG.FAST_PASS_COIN_THRESHOLD;

      io.emit('configUpdated', GAME_CONFIG);
      console.log('[Config] ✅ Đã cập nhật cấu hình tham số mới:', GAME_CONFIG);
    }
  });

  // Đổi kênh TikTok Live trực tiếp từ client/admin
  socket.on('tiktok:connect', async data => {
    const username = data?.username || data;
    try {
      await connectTikTokLive(username);
    } catch (_) {}
  });

  socket.on('tiktok:disconnect', async () => {
    await disconnectTikTokLive();
  });

  // Mock Comment từ admin.html
  socket.on('mock:chat', data => {
    const user = {
      uniqueId: data.uniqueId || 'mock_user_' + Math.floor(Math.random() * 1000),
      nickname: data.nickname || 'Khán giả Demo',
      profilePictureUrl: data.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face'
    };
    processChatMessage(user, data.comment, true);
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
    const user = {
      uniqueId: data.uniqueId || 'mock_user_' + (data.nickname || 'Fan'),
      nickname: data.nickname || 'Fan cứng'
    };
    handleLikeEvent(count, user);
  });

  // Mock Follow
  socket.on('mock:follow', data => {
    handleFollowEvent({
      uniqueId: data.uniqueId || 'mock_user_' + (data.nickname || 'Fan'),
      nickname: data.nickname || 'Bảo săn bão',
      profilePictureUrl: data.profilePictureUrl || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&h=100&fit=crop&crop=face'
    });
  });

  // Mock Share
  socket.on('mock:share', data => {
    handleShareEvent({
      uniqueId: data.uniqueId || 'mock_user_' + (data.nickname || 'Fan'),
      nickname: data.nickname || 'Fan chia sẻ',
      profilePictureUrl: data.profilePictureUrl || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=100&h=100&fit=crop&crop=face'
    });
  });

  // Buff điểm trực tiếp cho tỉnh (dùng để test realtime Biểu đồ Đua Top)
  socket.on('mock:buff_province', data => {
    const provinceId = (data && data.provinceId) || gameState.currentVisit.provinceId;
    const points = Number(data && data.points) || 10;
    gameState.provinceStats[provinceId] = (gameState.provinceStats[provinceId] || 0) + points;
    if (gameState.currentVisit.provinceId === provinceId) {
      gameState.currentVisit.visitCount = gameState.provinceStats[provinceId];
      io.emit('provinceChanged', gameState.currentVisit);
    }
    gameState.leaderboard = getTopProvinces(5);
    io.emit('leaderboardUpdated', gameState.leaderboard);
    io.emit('gameState', gameState);
  });

  // Chuyển tỉnh ngay lập tức
  socket.on('mock:next', () => {
    nextProvince();
  });

  // Reset hàng đợi / vòng chơi
  socket.on('mock:reset', () => {
    gameState.queue = [];
    resetLeaderboardSeason(true);
  });

  // Chốt Bảng Vàng 15 phút ngay lập tức (Test / Admin)
  socket.on('mock:season_reset', () => {
    resetLeaderboardSeason(true);
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
      gameState.leaderboard = getTopProvinces(5);
      io.emit('leaderboardUpdated', gameState.leaderboard);
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
