// ============================================================
// GAME TIKTOK LIVE: GHÉ THĂM 63 TỈNH THÀNH VIỆT NAM
// ============================================================

const socket = io();

// DOM Elements
const gameContainer = document.getElementById('gameContainer');
const mapZoomContainer = document.getElementById('mapZoomContainer');
const svgContainer = document.getElementById('svgContainer');
const provincePin = document.getElementById('provincePin');
const pinAvatar = document.getElementById('pinAvatar');
const pinName = document.getElementById('pinName');
const pinBadge = document.getElementById('pinBadge');
const visitorSpotlight = document.getElementById('visitorSpotlight');
const spotlightAvatar = document.getElementById('spotlightAvatar');
const spotlightNickname = document.getElementById('spotlightNickname');

// Header HUD Elements
const roundNumberEl = document.getElementById('roundNumber');
const roundTimerEl = document.getElementById('roundTimer');
const currentProvinceNameEl = document.getElementById('currentProvinceName');
const visitCountdownEl = document.getElementById('visitCountdown');
const totalViewersEl = document.getElementById('totalViewers');
const followersCountEl = document.getElementById('followersCount');
const goalPercentageEl = document.getElementById('goalPercentage');
const circleProgressPath = document.getElementById('circleProgressPath');
const queueCardsWrapper = document.getElementById('queueCardsWrapper');
const toastContainer = document.getElementById('toastContainer');
const ttsAudio = document.getElementById('ttsAudio');

// FX Canvas
const fxCanvas = document.getElementById('fxCanvas');
const ctx = fxCanvas.getContext('2d');

let svgDoc = null;
let currentProvinceData = null;
let provincesMetadata = [];
let ttsQueue = [];
let isPlayingTts = false;

// ============================================================
// 1. AUTO-SCALE 9:16 RESPONSIVE FIT
// ============================================================
function handleResize() {
  const windowW = window.innerWidth;
  const windowH = window.innerHeight;
  const targetW = 1080;
  const targetH = 1920;

  const scale = Math.min(windowW / targetW, windowH / targetH);
  gameContainer.style.transform = `scale(${scale})`;
  gameContainer.style.transformOrigin = 'center center';
}

window.addEventListener('resize', handleResize);
handleResize();

// ============================================================
// 2. TẢI BẢN ĐỒ SVG VIỆT NAM VÀ KHỞI TẠO
// ============================================================
async function initMap() {
  try {
    const [svgRes, provRes] = await Promise.all([
      fetch('/vietnam.svg'),
      fetch('/api/provinces')
    ]);

    const svgText = await svgRes.text();
    svgContainer.innerHTML = svgText;
    provincesMetadata = await provRes.json();

    const svg = svgContainer.querySelector('svg');
    if (svg) {
      svg.setAttribute('id', 'vietnamSvg');
      svg.style.width = '900px';
      svg.style.height = '1150px';

      // Gắn sự kiện click thử nghiệm trên từng tỉnh
      svg.querySelectorAll('path').forEach(path => {
        path.addEventListener('click', () => {
          const pathId = path.getAttribute('id');
          socket.emit('mock:set_province', pathId);
        });
      });
    }

    console.log('Vietnam Map SVG initialized successfully');

    // Nếu đã có dữ liệu tỉnh ban đầu, zoom ngay
    if (currentProvinceData) {
      focusProvince(currentProvinceData);
    }
  } catch (err) {
    console.error('Failed to load map assets:', err);
  }
}

// ============================================================
// 3. ĐỘNG CƠ CAMERA PAN & ZOOM (DYNAMIC CAMERA)
// ============================================================
function focusProvince(visitData) {
  if (!svgContainer) return;
  const svg = svgContainer.querySelector('svg');
  if (!svg) return;

  // Hỗ trợ cả 34 tỉnh mới (nhiều svgIds) và tỉnh đơn lẻ
  const rawIds = visitData.svgIds || [visitData.svgId || visitData.provinceId.replace(/-/g, '')];
  const svgIds = Array.isArray(rawIds) ? rawIds : [rawIds];

  // Xóa class active của các tỉnh cũ
  svg.querySelectorAll('.active-province').forEach(p => p.classList.remove('active-province'));

  let activePaths = [];
  svgIds.forEach(id => {
    const p = svg.querySelector(`#${id}`);
    if (p) {
      p.classList.add('active-province');
      p.parentNode.appendChild(p);
      activePaths.push(p);
    }
  });

  if (activePaths.length === 0) {
    const fallbackPath = svg.querySelector(`[name*="${visitData.provinceName}"]`);
    if (fallbackPath) {
      fallbackPath.classList.add('active-province');
      fallbackPath.parentNode.appendChild(fallbackPath);
      activePaths.push(fallbackPath);
    } else {
      console.warn(`Province paths not found for:`, svgIds);
      return;
    }
  }

  // Group chứa bản đồ trong SVG
  const mapGroup = svg.querySelector('#mapGroup') || svg;

  // Tính toán Bounding Box gộp chung của tất cả các đơn vị sáp nhập
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  activePaths.forEach(path => {
    try {
      const b = path.getBBox();
      if (b.x < minX) minX = b.x;
      if (b.y < minY) minY = b.y;
      if (b.x + b.width > maxX) maxX = b.x + b.width;
      if (b.y + b.height > maxY) maxY = b.y + b.height;
    } catch (e) {}
  });

  const bboxW = maxX - minX;
  const bboxH = maxY - minY;
  const cx = minX + bboxW / 2;
  const cy = minY + bboxH / 2;

  // Zoom scale trong SVG (giữ tỉnh vừa vặn vùng hiển thị)
  const provinceSize = Math.max(bboxW, bboxH);
  const zoomScale = Math.min(3.2, Math.max(1.9, 270 / Math.max(provinceSize, 45)));

  // Căn tâm tỉnh vào vị trí trên của bản đồ (351.5, 380) để chừa chỗ cho avatar spotlight ở dưới
  const targetSvgX = 351.5;
  const targetSvgY = 380;

  const translateX = targetSvgX - cx * zoomScale;
  const translateY = targetSvgY - cy * zoomScale;

  // Áp dụng transform cho group trong SVG
  mapGroup.style.transform = `translate(${translateX}px, ${translateY}px) scale(${zoomScale})`;
  mapGroup.style.transformOrigin = '0 0';
  mapGroup.style.transition = 'transform 1.2s cubic-bezier(0.25, 1, 0.5, 1)';

  // Cập nhật vị trí ghim Avatar trên tỉnh (ngay tại điểm tâm đã zoom)
  const renderedSvgH = svg.clientHeight || 1250;
  const pinScreenY = targetSvgY * (renderedSvgH / 900);

  provincePin.style.left = `540px`;
  provincePin.style.top = `${pinScreenY}px`;
  provincePin.classList.add('visible');

  pinAvatar.src = visitData.user.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face';
  pinName.textContent = visitData.provinceName;
  pinBadge.textContent = `+${visitData.visitCount !== undefined ? visitData.visitCount : 0}`;


  // Cập nhật Spotlight Avatar lớn ở dưới
  spotlightAvatar.src = visitData.user.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&h=120&fit=crop&crop=face';
  spotlightNickname.textContent = visitData.user.nickname || 'Khán giả';
}

// ============================================================
// 4. ĐỒNG BỘ DỮ LIỆU & GIAO DIỆN (SOCKET.IO)
// ============================================================
function formatTime(seconds) {
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m < 10 ? '0' : ''}${m}:${s < 10 ? '0' : ''}${s}`;
}

socket.on('gameState', state => {
  // Cập nhật vòng và thời gian live
  roundNumberEl.textContent = `#${state.roundNumber}`;
  roundTimerEl.textContent = formatTime(state.roundTimeLeft || 70);

  // Cập nhật tỉnh đang thăm
  if (state.currentVisit) {
    currentProvinceData = state.currentVisit;
    currentProvinceNameEl.textContent = state.currentVisit.provinceName;
    visitCountdownEl.textContent = `15:${state.currentVisit.timeLeft < 10 ? '0' : ''}${state.currentVisit.timeLeft}`;
    focusProvince(state.currentVisit);
  }

  // Cập nhật thống kê
  if (state.stats) {
    totalViewersEl.textContent = state.stats.totalViewers.toLocaleString();
    followersCountEl.textContent = state.stats.followersGoal.toLocaleString();

    const percentage = Math.min(100, Math.round((state.stats.followersGoal / state.stats.followersTarget) * 100));
    goalPercentageEl.textContent = `${percentage}%`;
    circleProgressPath.setAttribute('stroke-dasharray', `${percentage}, 100`);
  }

  // Cập nhật hàng đợi
  renderQueue(state.queue);

  // Cập nhật bảng xếp hạng Đua Top tỉnh thành
  if (state.leaderboard) {
    renderLeaderboard(state.leaderboard);
  }
});

// Sự kiện đếm giây
socket.on('tick', data => {
  visitCountdownEl.textContent = `15:${data.timeLeft < 10 ? '0' : ''}${data.timeLeft}`;
  roundTimerEl.textContent = formatTime(data.roundTimeLeft);
});

// Chuyển tỉnh
socket.on('provinceChanged', visitData => {
  currentProvinceData = visitData;
  currentProvinceNameEl.textContent = visitData.provinceName;
  focusProvince(visitData);
});

// Cập nhật hàng đợi
socket.on('queueUpdated', queue => {
  renderQueue(queue);
});

// Cập nhật bảng xếp hạng Đua Top tỉnh thành
const leaderboardListEl = document.getElementById('leaderboardList');
function renderLeaderboard(topProvinces) {
  if (!leaderboardListEl || !Array.isArray(topProvinces) || topProvinces.length === 0) return;
  
  const maxScore = Math.max(...topProvinces.map(p => p.score), 0);
  
  leaderboardListEl.innerHTML = topProvinces.map((prov, index) => {
    const rank = index + 1;
    const rankClass = rank === 1 ? 'lb-rank-1' : rank === 2 ? 'lb-rank-2' : rank === 3 ? 'lb-rank-3' : 'lb-rank-other';
    const fillClass = rank === 1 ? 'lb-fill-1' : rank === 2 ? 'lb-fill-2' : rank === 3 ? 'lb-fill-3' : 'lb-fill-other';
    const percent = maxScore > 0 ? Math.min(100, Math.max(8, Math.round((prov.score / maxScore) * 100))) : 0;
    const medal = rank === 1 ? '🥇' : rank === 2 ? '🥈' : rank === 3 ? '🥉' : rank;


    return `
      <div class="lb-item" data-id="${prov.id}">
        <div class="lb-item-info">
          <div class="lb-item-left">
            <span class="lb-rank-badge ${rankClass}">${medal}</span>
            <span class="lb-item-name">${prov.name}</span>
          </div>
          <div class="lb-item-score">${prov.score} ❤️</div>
        </div>
        <div class="lb-bar-track">
          <div class="lb-bar-fill ${fillClass}" style="width: ${percent}%;"></div>
        </div>
      </div>
    `;
  }).join('');
}

socket.on('leaderboardUpdated', renderLeaderboard);


// Render danh sách thẻ hàng đợi
const CARD_THEMES = ['card-blue', 'card-teal', 'card-gold'];
function renderQueue(queue) {
  if (!queue || queue.length === 0) {
    queueCardsWrapper.innerHTML = `
      <div class="queue-card card-teal" style="flex: 1; text-align: center; justify-content: center;">
        <span class="name" style="font-size: 24px; opacity: 0.8;">Bình luận tên tỉnh để vào hàng đợi...</span>
      </div>
    `;
    return;
  }

  queueCardsWrapper.innerHTML = queue.slice(0, 5).map((item, idx) => {
    const isVip = item.isVip || item.priority >= 50;
    const themeClass = isVip ? 'card-vip' : CARD_THEMES[idx % CARD_THEMES.length];
    const orderStr = (idx + 1) < 10 ? `0${idx + 1}` : `${idx + 1}`;

    return `
      <div class="queue-card ${themeClass}">
        <span class="order">${orderStr} ${isVip ? '👑' : ''}</span>
        <span class="name">${item.provinceName}</span>
      </div>
    `;
  }).join('');
}

// ============================================================
// 5. HIỆU ỨNG THÔNG BÁO NỔI (TOAST NOTIFICATIONS)
// ============================================================
socket.on('followNotification', notif => {
  showToast(`🕊️ ${notif.nickname} đã bắt đầu follow bạn`);
});

socket.on('giftNotification', notif => {
  showToast(`🎁 ${notif.nickname} đã gửi ${notif.giftName} (trị giá ${notif.coins} Xu)`);
  createHeartBurst(540, 960);
});

socket.on('vipSpecialEffect', data => {
  showToast(`👑 ĐẠI GIA ${data.nickname.toUpperCase()} TẶNG ${data.giftName.toUpperCase()}! ĐẶC QUYỀN ĐỌC TRƯỚC!`);
  triggerFireworks();
});

function showToast(message) {
  const toast = document.createElement('div');
  toast.className = 'toast-banner';
  toast.innerHTML = `<span>${message}</span>`;
  toastContainer.appendChild(toast);

  setTimeout(() => {
    if (toast.parentNode) {
      toast.parentNode.removeChild(toast);
    }
  }, 5000);
}

// ============================================================
// 6. GIỌNG ĐỌC AI TIẾNG VIỆT (TTS AUDIO ENGINE)
// ============================================================
socket.on('playTts', data => {
  if (data && data.text) {
    queueTts(data.text);
  }
});

function queueTts(text) {
  ttsQueue.push(text);
  if (!isPlayingTts) {
    playNextTts();
  }
}

function playNextTts() {
  if (ttsQueue.length === 0) {
    isPlayingTts = false;
    return;
  }

  isPlayingTts = true;
  const text = ttsQueue.shift();
  const url = `/api/tts?text=${encodeURIComponent(text)}`;

  ttsAudio.src = url;
  ttsAudio.play()
    .then(() => {
      ttsAudio.onended = () => {
        setTimeout(playNextTts, 400);
      };
    })
    .catch(e => {
      console.warn('TTS playback prevented or waiting for user interaction:', e);
      setTimeout(playNextTts, 1000);
    });
}

// Kích hoạt audio khi người dùng chạm màn hình lần đầu
window.addEventListener('click', () => {
  if (ttsAudio.paused && ttsQueue.length > 0) {
    playNextTts();
  }
}, { once: true });

// ============================================================
// 7. HỆ THỐNG HẠT VÀ PHÁO HOA (CANVAS FX)
// ============================================================
let particles = [];

class Particle {
  constructor(x, y, color) {
    this.x = x;
    this.y = y;
    this.color = color;
    this.radius = Math.random() * 4 + 2;
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 8 + 3;
    this.vx = Math.cos(angle) * speed;
    this.vy = Math.sin(angle) * speed;
    this.alpha = 1;
    this.decay = Math.random() * 0.02 + 0.015;
  }

  update() {
    this.x += this.vx;
    this.y += this.vy;
    this.vy += 0.15; // Trọng lực
    this.alpha -= this.decay;
  }

  draw(context) {
    context.save();
    context.globalAlpha = Math.max(0, this.alpha);
    context.fillStyle = this.color;
    context.beginPath();
    context.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    context.fill();
    context.restore();
  }
}

function triggerFireworks() {
  const colors = ['#ffd700', '#ff007f', '#00f2fe', '#7000ff', '#ffffff'];
  for (let i = 0; i < 3; i++) {
    setTimeout(() => {
      const rx = Math.random() * 600 + 240;
      const ry = Math.random() * 600 + 400;
      for (let j = 0; j < 80; j++) {
        const color = colors[Math.floor(Math.random() * colors.length)];
        particles.push(new Particle(rx, ry, color));
      }
    }, i * 250);
  }
}

function createHeartBurst(x, y) {
  const colors = ['#ff3b5c', '#ff8800', '#ff007f'];
  for (let i = 0; i < 40; i++) {
    const color = colors[Math.floor(Math.random() * colors.length)];
    particles.push(new Particle(x, y, color));
  }
}

function fxLoop() {
  ctx.clearRect(0, 0, fxCanvas.width, fxCanvas.height);
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.update();
    p.draw(ctx);
    if (p.alpha <= 0) {
      particles.splice(i, 1);
    }
  }
  requestAnimationFrame(fxLoop);
}

requestAnimationFrame(fxLoop);

// Khởi chạy
initMap();
