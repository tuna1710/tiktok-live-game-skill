const socket = io();

// Canvas hiệu ứng cánh hoa rơi & kim tuyến
const canvas = document.getElementById('fx-canvas');
const ctx = canvas.getContext('2d');

// DOM Elements
const congDucValEl = document.getElementById('cong-duc-val');
const shakerContainer = document.getElementById('shaker-container');
const shakerStatusText = document.getElementById('shaker-status-text');
const scrollWrapper = document.getElementById('scroll-wrapper');

// Scroll elements
const seekerAvatar = document.getElementById('seeker-avatar');
const seekerName = document.getElementById('seeker-name');
const seekerBadge = document.getElementById('seeker-badge');
const sealStamp = document.getElementById('seal-stamp');
const fortuneTitle = document.getElementById('fortune-title');
const fortunePoem = document.getElementById('fortune-poem');
const aspectTaiLoc = document.getElementById('aspect-tailoc');
const aspectTinhDuyen = document.getElementById('aspect-tinhduyen');
const aspectCongDanh = document.getElementById('aspect-congdanh');
const aspectSucKhoe = document.getElementById('aspect-suckhoe');
const luckyNumEl = document.getElementById('lucky-num');
const shortAdviceEl = document.getElementById('short-advice');

// Queue lists
const vipQueueList = document.getElementById('vip-queue-list');
const normalQueueList = document.getElementById('normal-queue-list');
const historyList = document.getElementById('history-list');

// Hệ thống cánh hoa đào / mai rơi
let petals = [];
class Petal {
  constructor() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * -canvas.height;
    this.size = Math.random() * 12 + 8;
    this.speedY = Math.random() * 2 + 1.2;
    this.speedX = Math.random() * 2 - 1;
    this.rotation = Math.random() * 360;
    this.rotSpeed = Math.random() * 2 - 1;
    // Màu cánh hoa đào hồng hoặc hoa mai vàng
    this.isMai = Math.random() > 0.4;
    this.color = this.isMai ? '#ffd700' : '#ff758f';
  }
  update() {
    this.y += this.speedY;
    this.x += Math.sin(this.y * 0.01) * 1.5 + this.speedX;
    this.rotation += this.rotSpeed;
    if (this.y > canvas.height + 20) {
      this.y = -20;
      this.x = Math.random() * canvas.width;
    }
  }
  draw() {
    ctx.save();
    ctx.translate(this.x, this.y);
    ctx.rotate((this.rotation * Math.PI) / 180);
    ctx.fillStyle = this.color;
    ctx.beginPath();
    ctx.ellipse(0, 0, this.size, this.size * 0.55, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }
}

for (let i = 0; i < 45; i++) {
  petals.push(new Petal());
}

// Quản lý âm thanh & TTS
const audioQueue = [];
let isPlayingTts = false;

function playAudioTts(text) {
  audioQueue.push(text);
  processNextTts();
}

function processNextTts() {
  if (isPlayingTts || audioQueue.length === 0) return;
  isPlayingTts = true;
  const text = audioQueue.shift();
  const audio = new Audio(`/api/tts?text=${encodeURIComponent(text)}`);
  audio.onended = () => {
    isPlayingTts = false;
    setTimeout(processNextTts, 500);
  };
  audio.onerror = () => {
    isPlayingTts = false;
    processNextTts();
  };
  audio.play().catch(() => {
    isPlayingTts = false;
    processNextTts();
  });
}

// Socket.IO Lắng nghe sự kiện
socket.on('gameState', state => {
  congDucValEl.textContent = state.totalCongDuc.toLocaleString();

  // Cập nhật hàng VIP
  if (state.vipQueue && state.vipQueue.length > 0) {
    vipQueueList.innerHTML = state.vipQueue.map(u => `
      <div class="vip-chip">
        <span>⭐ ${u.nickname}</span>
        <span>(${u.giftName || 'VIP'})</span>
      </div>
    `).join('');
  } else {
    vipQueueList.innerHTML = '<span class="empty-hint">Chưa có ai trong hàng VIP (Tặng quà để ưu tiên)</span>';
  }

  // Cập nhật hàng thường
  if (state.normalQueue && state.normalQueue.length > 0) {
    normalQueueList.innerHTML = state.normalQueue.map((u, i) => `
      <div class="queue-item">#${i + 1} ${u.nickname}</div>
    `).join('');
  } else {
    normalQueueList.innerHTML = '<div class="queue-empty">Gõ "Xin quẻ" để vào hàng đợi</div>';
  }

  // Cập nhật lịch sử
  if (state.historyFortunes && state.historyFortunes.length > 0) {
    historyList.innerHTML = state.historyFortunes.map(h => `
      <div class="history-item">
        <span>${h.user.nickname}</span>
        <strong>${h.fortune.type}</strong>
      </div>
    `).join('');
  } else {
    historyList.innerHTML = '<div class="history-empty">Chưa có quẻ nào</div>';
  }

  // Đồng bộ trạng thái hiển thị chuẩn xác
  if (state.currentFortune) {
    displayRevealedFortune(state.currentFortune);
  } else if (state.isDrawing) {
    scrollWrapper.classList.add('hidden');
    shakerContainer.classList.remove('hidden');
    shakerContainer.classList.add('shaking');
    shakerStatusText.textContent = '🎋 Đang lắc ống xăm cầu phúc...';
  } else {
    shakerContainer.classList.remove('hidden', 'shaking');
    scrollWrapper.classList.add('hidden');
    shakerStatusText.textContent = 'Thành tâm gõ "Xin quẻ" để rút thẻ...';
  }
});

function displayRevealedFortune(data) {
  shakerContainer.classList.remove('shaking');
  shakerContainer.classList.add('hidden');

  const u = data.user;
  const f = data.fortune;

  seekerAvatar.src = u.avatar || 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg';
  seekerName.textContent = u.nickname;
  seekerBadge.textContent = data.isVip ? '🌟 QUẺ VIP ĐẦU XUÂN' : '🎋 QUẺ ĐẦU NĂM';
  sealStamp.textContent = f.type;

  fortuneTitle.textContent = f.title;
  fortunePoem.textContent = f.poem;
  aspectTaiLoc.textContent = f.taiLoc;
  aspectTinhDuyen.textContent = f.tinhDuyen;
  aspectCongDanh.textContent = f.congDanh;
  aspectSucKhoe.textContent = f.sucKhoe;
  luckyNumEl.textContent = f.luckyNumber;
  shortAdviceEl.textContent = f.shortAdvice;

  scrollWrapper.classList.remove('hidden');
}

// Bắt đầu rung lắc ống xăm
socket.on('draw:start', data => {
  scrollWrapper.classList.add('hidden');
  shakerContainer.classList.remove('hidden');
  shakerContainer.classList.add('shaking');
  shakerStatusText.textContent = `🎋 Đang lắc quẻ cho: ${data.user.nickname} ${data.isVip ? '⭐ (QUẺ VIP)' : ''}...`;
});

// Bung mở thẻ quẻ
socket.on('draw:reveal', data => {
  displayRevealedFortune(data);
});

socket.on('playTts', data => {
  playAudioTts(data.text);
});

socket.on('game:reset', () => {
  shakerContainer.classList.remove('hidden', 'shaking');
  scrollWrapper.classList.add('hidden');
  shakerStatusText.textContent = 'Thành tâm gõ "Xin quẻ" để rút thẻ...';
});

// Canvas Render Loop
function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = 0; i < petals.length; i++) {
    petals[i].update();
    petals[i].draw();
  }
  requestAnimationFrame(render);
}
render();
