// Khởi tạo kết nối Socket.IO
const socket = io();

// Canvas & Context
const canvas = document.getElementById('game-canvas');
const ctx = canvas.getContext('2d');

// DOM Elements
const likeCountEl = document.getElementById('like-count');
const giftCountEl = document.getElementById('gift-count');
const scoreCountEl = document.getElementById('score-count');
const tiktokUserEl = document.getElementById('tiktok-user');
const leaderboardListEl = document.getElementById('leaderboard-list');
const chatMessagesEl = document.getElementById('chat-messages');

// Gift Alert Banner
const giftBannerEl = document.getElementById('gift-alert-banner');
const giftAvatarEl = document.getElementById('gift-user-avatar');
const giftUserNameEl = document.getElementById('gift-user-name');
const giftActionDescEl = document.getElementById('gift-action-desc');

// Quản lý hạt hiệu ứng (Particles)
let particles = [];
let balls = [];

class Particle {
  constructor(x, y, color) {
    this.x = x;
    this.y = y;
    this.color = color;
    this.radius = Math.random() * 6 + 3;
    this.speedX = (Math.random() - 0.5) * 12;
    this.speedY = (Math.random() - 0.5) * 12 - 4;
    this.alpha = 1;
    this.decay = Math.random() * 0.02 + 0.015;
  }
  update() {
    this.x += this.speedX;
    this.y += this.speedY;
    this.speedY += 0.3; // trọng lực
    this.alpha -= this.decay;
  }
  draw() {
    ctx.save();
    ctx.globalAlpha = Math.max(0, this.alpha);
    ctx.fillStyle = this.color;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }
}

// Thả bóng tương tác khi có comment hoặc like
class InteractiveBall {
  constructor(nickname, text, color) {
    this.nickname = nickname;
    this.text = text;
    this.x = Math.random() * (canvas.width - 200) + 100;
    this.y = 50;
    this.radius = 45;
    this.color = color;
    this.vy = 2;
    this.vx = (Math.random() - 0.5) * 4;
  }
  update() {
    this.y += this.vy;
    this.x += this.vx;
    this.vy += 0.25;

    // Va chạm đáy
    if (this.y + this.radius > canvas.height - 20) {
      this.y = canvas.height - 20 - this.radius;
      this.vy = -this.vy * 0.6;
    }
    // Va chạm tường
    if (this.x - this.radius < 20 || this.x + this.radius > canvas.width - 20) {
      this.vx = -this.vx;
    }
  }
  draw() {
    ctx.save();
    ctx.fillStyle = this.color;
    ctx.shadowBlur = 15;
    ctx.shadowColor = this.color;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fill();

    ctx.shadowBlur = 0;
    ctx.fillStyle = "#ffffff";
    ctx.font = "bold 16px sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(this.nickname.slice(0, 10), this.x, this.y - 5);
    ctx.font = "14px sans-serif";
    ctx.fillText(this.text.slice(0, 12), this.x, this.y + 15);
    ctx.restore();
  }
}

// Quản lý âm thanh & TTS
const audioQueue = [];
let isPlayingAudio = false;

function playTts(text) {
  audioQueue.push(text);
  processAudioQueue();
}

function processAudioQueue() {
  if (isPlayingAudio || audioQueue.length === 0) return;
  isPlayingAudio = true;
  const text = audioQueue.shift();
  const audio = new Audio(`/api/tts?text=${encodeURIComponent(text)}`);
  audio.onended = () => {
    isPlayingAudio = false;
    setTimeout(processAudioQueue, 300);
  };
  audio.onerror = () => {
    isPlayingAudio = false;
    processAudioQueue();
  };
  audio.play().catch(() => {
    isPlayingAudio = false;
    processAudioQueue();
  });
}

// Bùng nổ hạt pháo hoa
function triggerExplosion(x, y, count = 30, color = "#ffd700") {
  for (let i = 0; i < count; i++) {
    particles.push(new Particle(x, y, color));
  }
}

// Hiển thị Gift Banner
let bannerTimeout = null;
function showGiftAlert(nickname, giftName, count, avatar) {
  giftAvatarEl.src = avatar || "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg";
  giftUserNameEl.textContent = nickname;
  giftActionDescEl.textContent = `đã tặng ${count}x ${giftName}! 🎁`;
  giftBannerEl.classList.remove('hidden');

  if (bannerTimeout) clearTimeout(bannerTimeout);
  bannerTimeout = setTimeout(() => {
    giftBannerEl.classList.add('hidden');
  }, 3500);
}

// Cập nhật BXH
function updateLeaderboard(topContributors) {
  const sorted = Object.entries(topContributors || {})
    .sort((a, b) => b[1].diamonds - a[1].diamonds)
    .slice(0, 5);

  if (sorted.length === 0) {
    leaderboardListEl.innerHTML = '<li class="empty-state">Chưa có đóng góp nào</li>';
    return;
  }

  leaderboardListEl.innerHTML = sorted.map(([id, user], index) => `
    <li class="leaderboard-item ${index === 0 ? 'rank-1' : ''}">
      <span>#${index + 1} ${user.nickname}</span>
      <span>⭐ ${user.diamonds} xu</span>
    </li>
  `).join('');
}

// Thêm tin nhắn Chat
function addChatMessage(user, comment) {
  const item = document.createElement('div');
  item.className = 'chat-item';
  item.innerHTML = `<span class="chat-user">${user}:</span> ${comment}`;
  chatMessagesEl.appendChild(item);
  chatMessagesEl.scrollTop = chatMessagesEl.scrollHeight;

  // Giới hạn 20 tin gần nhất
  if (chatMessagesEl.children.length > 20) {
    chatMessagesEl.removeChild(chatMessagesEl.firstChild);
  }
}

// Lắng nghe sự kiện từ Socket.IO
socket.on('gameState', state => {
  likeCountEl.textContent = state.totalLikes.toLocaleString();
  giftCountEl.textContent = state.totalGifts.toLocaleString();
  scoreCountEl.textContent = state.score.toLocaleString();
  updateLeaderboard(state.topContributors);
});

socket.on('tiktok:status', status => {
  if (status.connected) {
    tiktokUserEl.textContent = `@${status.username}`;
  }
});

socket.on('chat', data => {
  addChatMessage(data.nickname, data.comment);
  balls.push(new InteractiveBall(data.nickname, data.comment, "#00f2fe"));
  if (balls.length > 25) balls.shift();
});

socket.on('gift', data => {
  showGiftAlert(data.nickname, data.giftName, data.repeatCount, data.profilePictureUrl);
  triggerExplosion(canvas.width / 2, canvas.height / 3, 50, "#ff007f");
  playTts(`Cảm ơn ${data.nickname} đã tặng ${data.giftName}`);
});

socket.on('like', data => {
  triggerExplosion(Math.random() * canvas.width, canvas.height - 100, 6, "#ff3b5c");
});

socket.on('game:reset', () => {
  balls = [];
  particles = [];
  chatMessagesEl.innerHTML = '<div class="chat-item system">Ván chơi đã được đặt lại!</div>';
});

// Game Loop
function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Vẽ các bóng tương tác
  for (let i = balls.length - 1; i >= 0; i--) {
    balls[i].update();
    balls[i].draw();
  }

  // Vẽ các hạt pháo hoa
  for (let i = particles.length - 1; i >= 0; i--) {
    particles[i].update();
    particles[i].draw();
    if (particles[i].alpha <= 0) {
      particles.splice(i, 1);
    }
  }

  requestAnimationFrame(render);
}

render();
