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

// Milestone 5: Top Donors, Thanh Phúc Khí & Giờ Vàng
const topDonorsList = document.getElementById('top-donors-list');
const phucKhiBar = document.getElementById('phuc-khi-bar');
const phucKhiStatus = document.getElementById('phuc-khi-status');
const goldenHourBanner = document.getElementById('golden-hour-banner');
const goldenHourCountdown = document.getElementById('golden-hour-countdown');

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

  // 6. Tiếng Còi Báo Động Đại Hạn
  playAlarm() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;
    for (let i = 0; i < 3; i++) {
      setTimeout(() => {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(620, now);
        osc.frequency.linearRampToValueAtTime(380, now + 0.28);
        gain.gain.setValueAtTime(0.32, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.3);
      }, i * 320);
    }
  }

  // 7. Tiếng Kèn Khúc Khải Hoàn (Giải Cứu Thành Công)
  playTriumph() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const chords = [523.25, 659.25, 783.99, 1046.5];
    chords.forEach((f, idx) => {
      setTimeout(() => {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(f, now);
        gain.gain.setValueAtTime(0.28, now);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 1.2);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 1.2);
      }, idx * 120);
    });
  }

  // 8. Kèn Trận Hoàng Gia Triệu Hồi Thần Tài (VIP Kim Cương)
  playRoyalFanfare() {
    if (this.isMuted) return;
    this.ensureContext();
    if (!this.ctx) return;
    const fanfareNotes = [261.63, 329.63, 392.00, 523.25, 392.00, 523.25];
    fanfareNotes.forEach((f, idx) => {
      setTimeout(() => {
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(f, now);
        gain.gain.setValueAtTime(0.35, now);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.6);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.6);
      }, idx * 160);
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
  const ageStr = u.canChi ? ` (${u.canChi})` : '';
  cardName.textContent = `${u.nickname}${ageStr}`;
  const catStr = f.categoryName ? f.categoryName : 'Quẻ Đầu Xuân';
  cardBadge.textContent = data.isVip ? `🌟 VIP • ${catStr}` : `🎋 ${catStr}`;
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

  // Cập nhật hàng VIP đa tầng
  const hudVipEl = document.getElementById('hud-vip-content');
  const hudNormalEl = document.getElementById('hud-normal-content');

  if (state.vipQueue && state.vipQueue.length > 0) {
    const vipHtml = state.vipQueue.map((u, idx) => `
      <div class="vip-chip vip-${u.vipTier || 'silver'}">
        <span>${u.vipTier === 'diamond' ? '👑' : (u.vipTier === 'gold' ? '🥈' : '🥉')} ${u.nickname}</span>
        <span>(${u.giftName || 'VIP'})${idx === 0 ? ' 👉 BỐC NGAY' : ''}</span>
      </div>
    `).join('');
    vipQueueList.innerHTML = vipHtml;
    if (hudVipEl) hudVipEl.innerHTML = vipHtml;
  } else {
    const emptyVipHtml = '<span class="empty-hint">🎁 Tặng Hoa Hồng (1 xu) để CHEN HÀNG lên đầu bốc ngay!</span>';
    vipQueueList.innerHTML = emptyVipHtml;
    if (hudVipEl) hudVipEl.innerHTML = emptyVipHtml;
  }

  // Cập nhật hàng thường (đánh số thứ tự rõ ràng)
  if (state.normalQueue && state.normalQueue.length > 0) {
    normalQueueList.innerHTML = state.normalQueue.map((u, i) => `
      <div class="queue-item ${i === 0 ? 'queue-item-next' : ''}">
        <span class="queue-rank">#${i + 1}</span>
        <span class="queue-name">${u.nickname}</span>
        ${i === 0 ? '<span class="queue-next-badge">SẮP TỚI</span>' : ''}
      </div>
    `).join('');

    if (hudNormalEl) {
      hudNormalEl.innerHTML = `
        <span class="hud-total-tag">Tổng: ${state.normalQueue.length} người</span>
        ${state.normalQueue.slice(0, 5).map((u, i) => `
          <span class="hud-item ${i === 0 ? 'hud-item-next' : ''}">
            <strong>#${i + 1}</strong> ${u.nickname}${i === 0 ? ' (Sắp đến)' : ''}
          </span>
        `).join('')}
        ${state.normalQueue.length > 5 ? `<span class="hud-more">+${state.normalQueue.length - 5}...</span>` : ''}
      `;
    }
  } else {
    normalQueueList.innerHTML = '<div class="queue-empty">Gõ "Xin quẻ" để vào hàng đợi</div>';
    if (hudNormalEl) hudNormalEl.innerHTML = '<span class="hud-normal-empty">Chưa có ai, gõ "xin que" để xếp hàng!</span>';
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

  // Cập nhật Bảng Vinh Danh Top 3 Phú Hộ (Milestone 5)
  if (topDonorsList) {
    if (state.topDonors && state.topDonors.length > 0) {
      const crowns = ['🥇', '🥈', '🥉'];
      const ranks = ['rank-1', 'rank-2', 'rank-3'];
      topDonorsList.innerHTML = state.topDonors.map((d, idx) => `
        <div class="donor-chip ${ranks[idx] || ''}">
          <span class="donor-crown">${crowns[idx] || '⭐'}</span>
          <img class="donor-avatar" src="${d.avatar || 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg'}" alt="">
          <span class="donor-name">${d.nickname}</span>
          <span class="donor-diamonds">💎 ${d.totalDiamonds}</span>
        </div>
      `).join('');
    } else {
      topDonorsList.innerHTML = '<span class="empty-donors">Đang chờ Đại Gia phát tâm...</span>';
    }
  }

  // Cập nhật Thanh Phúc Khí Toàn Phòng (Milestone 5)
  const phucKhi = state.phucKhiCount || 0;
  const goal = state.phucKhiGoal || 100;
  const pct = Math.min(100, Math.round((phucKhi / goal) * 100));
  if (phucKhiBar) phucKhiBar.style.width = `${pct}%`;
  if (phucKhiStatus) phucKhiStatus.textContent = `${phucKhi} / ${goal} (${pct}%)`;

  // Cập nhật Giờ Vàng May Mắn (Milestone 5)
  if (goldenHourBanner) {
    if (state.isGoldenHour) {
      goldenHourBanner.classList.remove('hidden');
      if (goldenHourCountdown) goldenHourCountdown.textContent = state.goldenHourRemaining || 60;
    } else {
      goldenHourBanner.classList.add('hidden');
    }
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
  const ageStr = u.canChi ? ` (${u.canChi})` : '';
  seekerName.textContent = `${u.nickname}${ageStr}`;
  const catStr = f.categoryName ? f.categoryName.toUpperCase() : 'QUẺ ĐẦU NĂM';
  seekerBadge.textContent = data.isVip ? `🌟 VIP • ${catStr}` : `🎋 ${catStr}`;
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

// Xử lý Sự Kiện Quẻ Đại Hạn & Thử Thách Cả Phòng Giải Cứu
const crisisOverlay = document.getElementById('crisis-overlay');
const crisisVictimAvatar = document.getElementById('crisis-victim-avatar');
const crisisVictimName = document.getElementById('crisis-victim-name');
const crisisBadTitle = document.getElementById('crisis-bad-title');
const crisisBadPoem = document.getElementById('crisis-bad-poem');
const crisisTimerEl = document.getElementById('crisis-timer');
const crisisProgressBar = document.getElementById('crisis-progress-bar');
const crisisCurrentLikes = document.getElementById('crisis-current-likes');
const crisisGoalLikes = document.getElementById('crisis-goal-likes');

socket.on('crisis:start', data => {
  shakerContainer.classList.add('hidden');
  shakerContainer.classList.remove('shaking');
  scrollWrapper.classList.add('hidden');
  if (fortuneShareCard) fortuneShareCard.classList.add('hidden');

  const u = data.victim;
  const f = data.fortune;
  crisisVictimAvatar.src = u.avatar || 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7311756534241640453~c5_100x100.jpeg';
  const ageStr = u.canChi ? ` (${u.canChi})` : '';
  crisisVictimName.textContent = `${u.nickname}${ageStr}`;
  crisisBadTitle.textContent = f.title;
  crisisBadPoem.textContent = f.poem;
  crisisTimerEl.textContent = data.countdown;
  crisisCurrentLikes.textContent = 0;
  crisisGoalLikes.textContent = data.goalLikes;
  crisisProgressBar.style.width = '0%';

  crisisOverlay.classList.remove('hidden');
  soundEngine.playAlarm();
});

socket.on('crisis:tick', data => {
  if (crisisTimerEl) crisisTimerEl.textContent = data.countdown;
  if (crisisCurrentLikes) crisisCurrentLikes.textContent = data.currentLikes;
  if (crisisGoalLikes) crisisGoalLikes.textContent = data.goalLikes;
  if (crisisProgressBar) {
    const pct = Math.min(100, Math.round((data.currentLikes / data.goalLikes) * 100));
    crisisProgressBar.style.width = `${pct}%`;
  }
});

socket.on('crisis:resolved', data => {
  crisisOverlay.classList.add('hidden');
  if (data.success) {
    soundEngine.playTriumph();
    soundEngine.playFirecrackers();
    displayRevealedFortune({
      user: data.victim,
      fortune: data.fortune,
      isVip: true
    });
    setTimeout(() => {
      showShareCard({
        user: data.victim,
        fortune: data.fortune,
        isVip: true
      });
    }, 1200);
  } else {
    soundEngine.playGong();
    displayRevealedFortune({
      user: data.victim,
      fortune: data.fortune,
      isVip: false
    });
  }
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

// Sự kiện Triệu Hồi Thần Tài Hoàng Kim (VIP Kim Cương)
const thantaiBanner = document.getElementById('thantai-summon-banner');
const thantaiSponsor = document.getElementById('thantai-sponsor');

socket.on('thantai:summon', data => {
  soundEngine.playRoyalFanfare();
  soundEngine.playFirecrackers();

  if (thantaiSponsor) {
    thantaiSponsor.textContent = `ĐẠI GIA ${data.user.nickname.toUpperCase()} TẶNG ${data.giftName.toUpperCase()} BAN LỘC KIM CƯƠNG!`;
  }

  if (thantaiBanner) {
    thantaiBanner.classList.remove('hidden');
    // Khởi động lại hoạt ảnh bay
    thantaiBanner.style.animation = 'none';
    thantaiBanner.offsetHeight; // force reflow
    thantaiBanner.style.animation = 'thantaiFly 4.5s ease-in-out forwards';

    setTimeout(() => {
      thantaiBanner.classList.add('hidden');
    }, 4500);
  }
});

// Sự kiện Giờ Vàng May Mắn (Milestone 5)
socket.on('golden_hour:start', data => {
  if (goldenHourBanner) {
    goldenHourBanner.classList.remove('hidden');
    if (goldenHourCountdown) goldenHourCountdown.textContent = data.duration || 60;
  }
  soundEngine.playTriumph();
  soundEngine.playFirecrackers();
});

socket.on('golden_hour:tick', data => {
  if (goldenHourCountdown) goldenHourCountdown.textContent = data.remaining;
});

socket.on('golden_hour:end', () => {
  if (goldenHourBanner) goldenHourBanner.classList.add('hidden');
  soundEngine.playGong();
});

socket.on('audio:bgm:toggle', () => {
  if (btnSoundToggle) btnSoundToggle.click();
});

// Sự kiện Chen Hàng VIP khi tặng quà
socket.on('vip:chen_hang', data => {
  soundEngine.playChime();
  const vipJumpBanner = document.getElementById('vip-jump-banner');
  const vipJumpText = document.getElementById('vip-jump-text');
  if (vipJumpBanner && vipJumpText) {
    vipJumpText.innerHTML = `🚀 <strong style="color: #ffd700;">${data.user.nickname}</strong> vừa tặng <strong>${data.giftName}</strong> và <strong style="color: #ff3b30; text-shadow: 0 0 8px #ffd700;">CHEN HÀNG VIP THÀNH CÔNG</strong>! Sẽ được bốc trước!`;
    vipJumpBanner.classList.remove('hidden');
    setTimeout(() => {
      vipJumpBanner.classList.add('hidden');
    }, 4500);
  }
});

socket.on('playTts', data => {
  playAudioTts(data.text);
});

// Hiển thị bong bóng thoại AI MC khi MC phát biểu
let mcBubbleTimer = null;
socket.on('mc:speaking', data => {
  const bubble = document.getElementById('mc-speech-bubble');
  const textEl = document.getElementById('mc-speech-text');
  if (bubble && textEl && data?.text) {
    textEl.textContent = data.text;
    bubble.classList.remove('hidden');
    if (mcBubbleTimer) clearTimeout(mcBubbleTimer);
    mcBubbleTimer = setTimeout(() => {
      bubble.classList.add('hidden');
    }, 6000);
  }
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
