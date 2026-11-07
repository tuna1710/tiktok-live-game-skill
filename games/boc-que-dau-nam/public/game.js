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

// Web Audio API Sound Engine cho SFX & BGM Tết thuần Việt
class TetSoundEngine {
  constructor() {
    this.ctx = null;
    this.bgmPlaying = false;
    this.bgmTimer = null;
    this.isMuted = false;
  }

  ensureContext() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  // 1. Tiếng lắc ống xăm tre (nhiều tiếng va chạm gỗ chân thực)
  playBambooShake() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;

    for (let i = 0; i < 9; i++) {
      setTimeout(() => {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        const filter = this.ctx.createBiquadFilter();

        osc.type = 'triangle';
        osc.frequency.setValueAtTime(480 + Math.random() * 600, now);

        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(1100 + Math.random() * 350, now);
        filter.Q.setValueAtTime(7, now);

        gain.gain.setValueAtTime(0.32, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);

        osc.start(now);
        osc.stop(now + 0.08);
      }, i * 95);
    }
  }

  // 2. Tiếng Chiêng Đồng ngân vang cổ truyền
  playGong() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;

    const now = this.ctx.currentTime;
    const freqs = [220, 440, 660, 880];
    freqs.forEach((f, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(f, now);
      
      const vol = 0.38 / (idx + 1);
      gain.gain.setValueAtTime(vol, now);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 3.2);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now);
      osc.stop(now + 3.2);
    });
  }

  // 3. Tiếng Pháo Nổ rộn ràng khi bốc trúng quẻ Đại Cát
  playFirecrackers() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;

    for (let i = 0; i < 12; i++) {
      setTimeout(() => {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const bufferSize = this.ctx.sampleRate * 0.12;
        const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let j = 0; j < bufferSize; j++) {
          data[j] = Math.random() * 2 - 1;
        }

        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;

        const filter = this.ctx.createBiquadFilter();
        filter.type = 'highpass';
        filter.frequency.setValueAtTime(750, now);

        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(0.45, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.11);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);

        noise.start(now);
      }, i * 110 + Math.random() * 40);
    }
  }

  // 4. Tiếng Chuông Chime may mắn khi có người vào hàng
  playChime() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;
    [1046.5, 1318.5, 1567.98].forEach((f, idx) => {
      setTimeout(() => {
        if (!this.ctx) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(f, this.ctx.currentTime);
        gain.gain.setValueAtTime(0.18, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + 0.8);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.8);
      }, idx * 90);
    });
  }

  // 5. Nhạc nền BGM Ngũ Cung Ngày Xuân (Điệu đàn tranh du dương)
  startBgm() {
    if (this.bgmPlaying || this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;
    this.bgmPlaying = true;

    // Giai điệu ngũ cung Việt Nam: C4, D4, F4, G4, A4, C5
    const pentatonicNotes = [261.63, 293.66, 349.23, 392.00, 440.00, 523.25, 392.00, 349.23];
    let noteIdx = 0;

    const playNextNote = () => {
      if (!this.bgmPlaying || this.isMuted || !this.ctx) return;
      const now = this.ctx.currentTime;
      const freq = pentatonicNotes[noteIdx % pentatonicNotes.length];
      noteIdx++;

      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, now);

      gain.gain.setValueAtTime(0.05, now);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.7);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now);
      osc.stop(now + 0.7);

      this.bgmTimer = setTimeout(playNextNote, 600);
    };

    playNextNote();
  }

  stopBgm() {
    this.bgmPlaying = false;
    if (this.bgmTimer) {
      clearTimeout(this.bgmTimer);
      this.bgmTimer = null;
    }
  }

  toggleSound() {
    this.isMuted = !this.isMuted;
    if (this.isMuted) {
      this.stopBgm();
    } else {
      this.startBgm();
    }
    return !this.isMuted;
  }
}

const soundEngine = new TetSoundEngine();

// Tự động bật BGM sau lần click đầu tiên của người dùng (tránh chính sách Autoplay của trình duyệt)
document.addEventListener('click', () => {
  soundEngine.ensureContext();
  if (!soundEngine.bgmPlaying && !soundEngine.isMuted) {
    soundEngine.startBgm();
  }
}, { once: true });

// Nút bấm Bật/Tắt âm thanh trên giao diện
const btnSoundToggle = document.getElementById('btn-sound-toggle');
const soundLabel = document.getElementById('sound-label');
const soundIcon = document.getElementById('sound-icon');

if (btnSoundToggle) {
  btnSoundToggle.addEventListener('click', () => {
    const isNowActive = soundEngine.toggleSound();
    if (isNowActive) {
      btnSoundToggle.classList.remove('muted');
      soundLabel.textContent = 'BGM: Bật';
      soundIcon.textContent = '🏮';
    } else {
      btnSoundToggle.classList.add('muted');
      soundLabel.textContent = 'BGM: Tắt';
      soundIcon.textContent = '🔇';
    }
  });
}

// Quản lý Thiệp Chúc Tết Lưu Niệm Chụp Màn Hình
const fortuneShareCard = document.getElementById('fortune-share-card');
const cardAvatar = document.getElementById('card-avatar');
const cardName = document.getElementById('card-name');
const cardBadge = document.getElementById('card-badge');
const cardSeal = document.getElementById('card-seal');
const cardTitle = document.getElementById('card-title');
const cardPoem = document.getElementById('card-poem');
const cardTaiLoc = document.getElementById('card-tailoc');
const cardTinhDuyen = document.getElementById('card-tinhduyen');
const cardTimerEl = document.getElementById('card-timer');
let cardCountdownInterval = null;

function showShareCard(data) {
  const u = data.user;
  const f = data.fortune;
  cardAvatar.src = u.avatar || 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg';
  cardName.textContent = u.nickname;
  cardBadge.textContent = data.isVip ? '🌟 Quẻ VIP Đầu Xuân' : '🎋 Quẻ Lộc Đầu Xuân';
  cardSeal.textContent = f.type;
  cardTitle.textContent = f.title;
  cardPoem.textContent = f.poem;
  cardTaiLoc.textContent = f.taiLoc || 'Hưng Vượng';
  cardTinhDuyen.textContent = f.tinhDuyen || 'Viên Mãn';

  fortuneShareCard.classList.remove('hidden');

  let seconds = 6;
  cardTimerEl.textContent = seconds;
  if (cardCountdownInterval) clearInterval(cardCountdownInterval);
  cardCountdownInterval = setInterval(() => {
    seconds--;
    cardTimerEl.textContent = seconds;
    if (seconds <= 0) {
      clearInterval(cardCountdownInterval);
      fortuneShareCard.classList.add('hidden');
    }
  }, 1000);
}

// Quản lý âm thanh TTS
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
  if (fortuneShareCard) fortuneShareCard.classList.add('hidden');
  scrollWrapper.classList.add('hidden');
  shakerContainer.classList.remove('hidden');
  shakerContainer.classList.add('shaking');
  shakerStatusText.textContent = `🎋 Đang lắc quẻ cho: ${data.user.nickname} ${data.isVip ? '⭐ (QUẺ VIP)' : ''}...`;

  // Phát tiếng lắc tre chân thực
  soundEngine.playBambooShake();
});

// Bung mở thẻ quẻ
socket.on('draw:reveal', data => {
  displayRevealedFortune(data);

  // Phát tiếng chiêng đồng ngân vang
  soundEngine.playGong();

  // Nếu là Đại Cát hoặc VIP: bắn pháo nổ rộn ràng
  if (data.isVip || (data.fortune && data.fortune.type && data.fortune.type.includes('ĐẠI CÁT'))) {
    setTimeout(() => soundEngine.playFirecrackers(), 350);
  }

  // Tự động mở Tấm Thiệp Kỷ Niệm Chụp Màn Hình (6s)
  setTimeout(() => {
    showShareCard(data);
  }, 1000);
});

// Sự kiện âm thanh trực tiếp từ Admin
socket.on('audio:sfx', data => {
  if (!data || !data.type) return;
  if (data.type === 'shake') soundEngine.playBambooShake();
  else if (data.type === 'gong') soundEngine.playGong();
  else if (data.type === 'firecracker') soundEngine.playFirecrackers();
  else if (data.type === 'chime') soundEngine.playChime();
  else if (data.type === 'test_card') {
    showShareCard({
      user: { nickname: 'Thí Chủ May Mắn', avatar: '' },
      fortune: { type: 'ĐẠI CÁT', title: 'TIẾN BẢO CHIÊU TÀI', poem: 'Xuân về hoa nở thắm tươi\nTài danh đắc ý trọn mười phần vui', taiLoc: 'Đại Hưng', tinhDuyen: 'Viên Mãn' },
      isVip: true
    });
  }
});

socket.on('audio:bgm:toggle', () => {
  if (btnSoundToggle) btnSoundToggle.click();
});

socket.on('playTts', data => {
  playAudioTts(data.text);
});

socket.on('game:reset', () => {
  if (fortuneShareCard) fortuneShareCard.classList.add('hidden');
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
