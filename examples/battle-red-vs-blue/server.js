require('dotenv').config();
const path = require('path');
const http = require('http');
const express = require('express');
const cors = require('cors');
const { Server } = require('socket.io');
const { TikTokLiveConnection } = require('tiktok-live-connector');

const PORT = Number(process.env.PORT) || 3001;
let TIKTOK_USERNAME = process.env.TIKTOK_USERNAME || '';

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.get('/api/tts', (req, res) => {
  const text = (req.query.text || '').toString().trim().slice(0, 160);
  if (!text) return res.status(400).send('Missing text');
  const googleTtsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=vi&client=tw-ob&q=${encodeURIComponent(text)}`;
  res.redirect(googleTtsUrl);
});

// Trạng thái Game Kéo Co Đỏ vs Xanh
let gameState = {
  redScore: 50,
  blueScore: 50,
  targetScore: 100,
  winner: null,
  redContributors: {},
  blueContributors: {},
  totalLikes: 0,
  totalGifts: 0
};

const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

function checkWinner() {
  if (gameState.redScore >= gameState.targetScore && !gameState.winner) {
    gameState.winner = 'RED';
    io.emit('game:win', { winner: 'RED', text: 'PHE ĐỎ CHIẾN THẮNG VANG DỘI!' });
  } else if (gameState.blueScore >= gameState.targetScore && !gameState.winner) {
    gameState.winner = 'BLUE';
    io.emit('game:win', { winner: 'BLUE', text: 'PHE XANH CHIẾN THẮNG VANG DỘI!' });
  }
}

function handleComment(data) {
  if (gameState.winner) return;
  const c = (data.comment || '').trim().toLowerCase();
  if (c === '1' || c === 'đỏ' || c === 'do') {
    gameState.redScore = Math.min(gameState.targetScore, gameState.redScore + 1);
    gameState.blueScore = Math.max(0, gameState.blueScore - 1);
    addContributor('RED', data.uniqueId, data.nickname, 1);
  } else if (c === '2' || c === 'xanh' || c === 'blue') {
    gameState.blueScore = Math.min(gameState.targetScore, gameState.blueScore + 1);
    gameState.redScore = Math.max(0, gameState.redScore - 1);
    addContributor('BLUE', data.uniqueId, data.nickname, 1);
  }
  checkWinner();
  io.emit('chat', data);
  io.emit('gameState', gameState);
}

function handleGift(data) {
  if (gameState.winner) return;
  const points = (data.diamondCount || 1) * (data.repeatCount || 1) * 5;
  gameState.totalGifts += points;

  // Quà chẵn hoặc Hoa Hồng tặng Đỏ, Quà lẻ hoặc Trái Tim tặng Xanh (hoặc dựa trên tên quà)
  const gName = (data.giftName || '').toLowerCase();
  if (gName.includes('hồng') || gName.includes('rose') || gName.includes('hoa') || (data.diamondCount % 2 === 0)) {
    gameState.redScore = Math.min(gameState.targetScore, gameState.redScore + points);
    gameState.blueScore = Math.max(0, gameState.blueScore - Math.floor(points / 2));
    addContributor('RED', data.uniqueId, data.nickname, points);
  } else {
    gameState.blueScore = Math.min(gameState.targetScore, gameState.blueScore + points);
    gameState.redScore = Math.max(0, gameState.redScore - Math.floor(points / 2));
    addContributor('BLUE', data.uniqueId, data.nickname, points);
  }
  checkWinner();
  io.emit('gift', data);
  io.emit('gameState', gameState);
}

function handleLike(data) {
  if (gameState.winner) return;
  gameState.totalLikes += (data.likeCount || 1);
  // Like hỗ trợ phe đang bị dẫn trước
  if (gameState.redScore < gameState.blueScore) {
    gameState.redScore += 1;
  } else {
    gameState.blueScore += 1;
  }
  checkWinner();
  io.emit('like', data);
  io.emit('gameState', gameState);
}

function addContributor(team, id, name, pts) {
  const target = team === 'RED' ? gameState.redContributors : gameState.blueContributors;
  if (!target[id]) target[id] = { nickname: name, points: 0 };
  target[id].points += pts;
}

// Kết nối TikTok Live
if (TIKTOK_USERNAME) {
  try {
    const cleanUser = TIKTOK_USERNAME.replace('@', '');
    const conn = new TikTokLiveConnection(cleanUser);
    conn.connect().then(() => console.log(`Connected to @${cleanUser}`));
    conn.on('chat', data => handleComment(data));
    conn.on('gift', data => handleGift(data));
    conn.on('like', data => handleLike(data));
  } catch (err) {
    console.error('TikTok Live err:', err);
  }
}

io.on('connection', socket => {
  socket.emit('gameState', gameState);
  socket.on('mock:chat', data => handleComment(data));
  socket.on('mock:gift', data => handleGift(data));
  socket.on('mock:like', data => handleLike(data));
  socket.on('game:reset', () => {
    gameState.redScore = 50;
    gameState.blueScore = 50;
    gameState.winner = null;
    gameState.redContributors = {};
    gameState.blueContributors = {};
    io.emit('gameState', gameState);
    io.emit('game:reset');
  });
});

server.listen(PORT, () => {
  console.log(`Battle Red vs Blue running on port ${PORT}`);
});
