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
const pinCohortBadge = document.getElementById('pinCohortBadge');
const visitorSpotlight = document.getElementById('visitorSpotlight');
const spotlightAvatar = document.getElementById('spotlightAvatar');
const spotlightNickname = document.getElementById('spotlightNickname');
const spotlightRole = document.getElementById('spotlightRole');
const spotlightCrown = document.getElementById('spotlightCrown');
const spotlightCohort = document.getElementById('spotlightCohort');

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

// Chat Feed Elements
const chatFeedList = document.getElementById('chatFeedList');
const chatCountBadge = document.getElementById('chatCountBadge');
let chatCount = 0;

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

  const leader = visitData.leader || visitData.user || {};
  const visitors = Array.isArray(visitData.visitors) && visitData.visitors.length > 0 
    ? visitData.visitors 
    : [leader];

  pinAvatar.src = leader.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=100&fit=crop&crop=face';
  pinName.textContent = visitData.provinceName;
  pinBadge.textContent = `+${visitData.visitCount !== undefined ? visitData.visitCount : 0}`;

  if (pinCohortBadge) {
    if (visitors.length > 1) {
      pinCohortBadge.style.display = 'inline-block';
      pinCohortBadge.textContent = `👥 ${visitors.length}`;
    } else {
      pinCohortBadge.style.display = 'none';
    }
  }

  // Cập nhật Spotlight Avatar lớn ở dưới
  spotlightAvatar.src = leader.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&h=120&fit=crop&crop=face';
  spotlightNickname.textContent = leader.nickname || 'Khán giả';

  if (spotlightRole) {
    if (visitors.length > 1) {
      spotlightRole.textContent = `👑 TRƯỞNG ĐOÀN (${visitors.length} NGƯỜI)`;
    } else {
      spotlightRole.textContent = `🚩 ĐỒNG HƯƠNG`;
    }
  }

  if (spotlightCohort) {
    if (visitors.length > 1) {
      const otherVisitors = visitors.filter(v => v.uniqueId !== leader.uniqueId);
      const displayVisitors = otherVisitors.slice(0, 4);
      let cohortHtml = displayVisitors.map(v => `
        <div class="cohort-member-pill">
          <img src="${v.profilePictureUrl || 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=60&h=60&fit=crop&crop=face'}" alt="Avatar">
          <span>${escapeHtml(v.nickname || 'Bạn')}</span>
        </div>
      `).join('');
      if (otherVisitors.length > 4) {
        cohortHtml += `<span class="cohort-more-pill">+${otherVisitors.length - 4}</span>`;
      }
      spotlightCohort.innerHTML = cohortHtml;
    } else {
      spotlightCohort.innerHTML = '';
    }
  }
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
  // Cập nhật mùa giải và thời gian đếm ngược 15 phút Bảng Vàng
  roundNumberEl.textContent = `#${state.roundNumber}`;
  const seasonFormatted = formatTime(state.roundTimeLeft || 900);
  roundTimerEl.textContent = seasonFormatted;
  const lbCountdown = document.getElementById('lbCountdown');
  if (lbCountdown) lbCountdown.textContent = seasonFormatted;
  const rulesCountdown = document.getElementById('rulesCountdown');
  if (rulesCountdown) rulesCountdown.textContent = seasonFormatted;

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

  // Khởi tạo danh sách comment ban đầu nếu có
  if (state.recentChats && Array.isArray(state.recentChats) && chatCount === 0) {
    state.recentChats.slice().reverse().forEach(c => addChatToFeed(c));
  }
});

function escapeHtml(str) {
  if (!str) return '';
  return String(str).replace(/[&<>'"]/g, 
    tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
  );
}

function addChatToFeed(chat) {
  if (!chatFeedList) return;
  chatCount++;
  if (chatCountBadge) chatCountBadge.textContent = chatCount > 99 ? '99+' : `${chatCount}`;

  const emptyEl = chatFeedList.querySelector('.cf-empty');
  if (emptyEl) emptyEl.remove();

  const isMatched = !!chat.matchedProvince;
  const tagHtml = isMatched
    ? `<span class="cf-tag tag-match">🚩 ${chat.matchedProvince}</span>`
    : `<span class="cf-tag tag-normal">💬 Chat</span>`;

  const itemEl = document.createElement('div');
  itemEl.className = `cf-item ${isMatched ? 'cf-matched' : ''}`;
  itemEl.innerHTML = `
    <img class="cf-avatar" src="${chat.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=60&h=60&fit=crop&crop=face'}" alt="User">
    <div class="cf-content">
      <div class="cf-user-row">
        <span class="cf-user-name">${escapeHtml(chat.nickname || 'Khán giả')}</span>
        ${tagHtml}
      </div>
      <div class="cf-comment-text">${escapeHtml(chat.comment || '')}</div>
    </div>
  `;

  chatFeedList.insertBefore(itemEl, chatFeedList.firstChild);

  while (chatFeedList.children.length > 5) {
    chatFeedList.removeChild(chatFeedList.lastChild);
  }
}

socket.on('chat', chat => {
  addChatToFeed(chat);
});

// Sự kiện đếm giây
socket.on('tick', data => {
  visitCountdownEl.textContent = `15:${data.timeLeft < 10 ? '0' : ''}${data.timeLeft}`;
  const seasonFormatted = formatTime(data.roundTimeLeft);
  roundTimerEl.textContent = seasonFormatted;
  const lbCountdown = document.getElementById('lbCountdown');
  if (lbCountdown) lbCountdown.textContent = seasonFormatted;
  const rulesCountdown = document.getElementById('rulesCountdown');
  if (rulesCountdown) rulesCountdown.textContent = seasonFormatted;
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
    let themeClass = CARD_THEMES[idx % CARD_THEMES.length];
    let badgeHtml = '<span class="q-badge q-free">💬 Thường</span>';

    const coins = item.coins || 0;
    const visitors = item.visitors && item.visitors.length > 0 ? item.visitors : (item.user ? [item.user] : []);
    const leader = item.leader || item.user || {};

    if (coins >= 20 || item.perkType === 'vip') {
      themeClass = 'card-vip';
      badgeHtml = `<span class="q-badge q-vip">👑 ${coins} xu</span>`;
    } else if (coins >= 5 || item.perkType === 'fast') {
      themeClass = 'card-fast';
      badgeHtml = `<span class="q-badge q-fast">⚡ ${coins} xu</span>`;
    } else if (coins > 0 || item.perkType === 'gift') {
      themeClass = 'card-gift';
      badgeHtml = `<span class="q-badge q-gift">🌹 ${coins} xu</span>`;
    } else if (visitors.length >= 2 || item.perkType === 'cohort') {
      badgeHtml = `<span class="q-badge q-cohort">👥 Đoàn ${visitors.length}</span>`;
    } else if (item.perkType === 'follower') {
      badgeHtml = '<span class="q-badge q-follower">⭐ Follower</span>';
    } else if (item.perkType === 'share') {
      badgeHtml = '<span class="q-badge q-share">🔁 Share</span>';
    } else if (item.priorityScore >= 20) {
      badgeHtml = '<span class="q-badge q-follower">❤️ Like 20+</span>';
    }

    const orderStr = (idx + 1) < 10 ? `0${idx + 1}` : `${idx + 1}`;
    
    // Stacked avatars HTML
    let avatarStackHtml = '';
    if (visitors.length > 0) {
      const stackImgs = visitors.slice(0, 4).map(v => 
        `<img class="queue-avatar-stack-item" src="${v.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=50&h=50&fit=crop&crop=face'}" title="${escapeHtml(v.nickname || 'Khán giả')}" alt="User">`
      ).join('');
      const countTag = visitors.length > 1 ? `<span class="queue-cohort-count">👥 ${visitors.length}</span>` : '';
      avatarStackHtml = `
        <div class="queue-avatar-row">
          <div class="queue-avatar-stack">${stackImgs}</div>
          ${countTag}
        </div>
      `;
    }

    const leaderName = leader.nickname ? escapeHtml(leader.nickname) : 'Khán giả';
    const subText = visitors.length > 1 
      ? `👑 ${leaderName} + ${visitors.length - 1} bạn`
      : leaderName;

    return `
      <div class="queue-card ${themeClass}">
        <div class="queue-card-top">
          <span class="order">${orderStr}</span>
          ${badgeHtml}
        </div>
        <div class="queue-card-body">
          <span class="name">${item.provinceName}</span>
          <span class="user-sub">${subText}</span>
          ${avatarStackHtml}
        </div>
      </div>
    `;
  }).join('');
}

// Sự kiện Nhập đoàn tức thì (Instant Drop-in)
socket.on('visitorDropIn', data => {
  // 1. Hiển thị banner nổi bật
  const banner = document.createElement('div');
  banner.className = 'drop-in-banner';
  banner.innerHTML = `
    <img src="${data.user.profilePictureUrl || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=60&h=60&fit=crop&crop=face'}" alt="Avatar">
    <span>${data.isLeader ? '👑 ' : '✨ '}<b>${escapeHtml(data.user.nickname)}</b> vừa ${data.isLeader ? 'làm TRƯỞNG ĐOÀN' : 'nhập đoàn'} ${escapeHtml(data.provinceName)}! (Tổng: ${data.totalVisitors} người)</span>
  `;
  document.body.appendChild(banner);
  setTimeout(() => {
    if (banner.parentNode) banner.parentNode.removeChild(banner);
  }, 3000);

  // 2. Hiệu ứng hạt tim
  createHeartBurst(540, 750);

  // 3. Cập nhật ngay spotlight nếu đang chiếu cùng tỉnh
  if (currentProvinceData && currentProvinceData.provinceId === data.provinceId) {
    if (!currentProvinceData.visitors) {
      currentProvinceData.visitors = [];
    }
    const idx = currentProvinceData.visitors.findIndex(v => v.uniqueId === data.user.uniqueId);
    if (idx >= 0) {
      currentProvinceData.visitors[idx] = data.user;
    } else {
      currentProvinceData.visitors.push(data.user);
    }
    if (data.isLeader || data.leader) {
      currentProvinceData.leader = data.leader || data.user;
      currentProvinceData.user = currentProvinceData.leader;
    }
    focusProvince(currentProvinceData);
  }
});

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

socket.on('seasonWinner', data => {
  triggerFireworks();
  showToast(`🏆 CHÚC MỪNG ${data.provinceName.toUpperCase()} ĐẠT QUÁN QUÂN BẢNG VÀNG! (${data.score} điểm)`);
});

socket.on('roundReset', data => {
  roundNumberEl.textContent = `#${data.roundNumber}`;
  const freshTime = formatTime(data.roundTimeLeft || 900);
  roundTimerEl.textContent = freshTime;
  const lbCountdown = document.getElementById('lbCountdown');
  if (lbCountdown) lbCountdown.textContent = freshTime;
  const rulesCountdown = document.getElementById('rulesCountdown');
  if (rulesCountdown) rulesCountdown.textContent = freshTime;
  if (!data.winner) {
    showToast(`🔄 BẮT ĐẦU MÙA GIẢI ĐUA TOP BẢNG VÀNG #${data.roundNumber}!`);
  }
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
  // Giới hạn hàng đợi tối đa 4 câu để tránh trôi xa tương tác thời gian thực
  if (ttsQueue.length >= 4) {
    ttsQueue.splice(1, 1);
  }
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
  ttsAudio.playbackRate = 1.25; // Đọc nhanh 1.25x giúp giọng sôi động, chuẩn nhịp live
  if ('preservesPitch' in ttsAudio) {
    ttsAudio.preservesPitch = true;
  }

  ttsAudio.play()
    .then(() => {
      ttsAudio.playbackRate = 1.25;
      ttsAudio.onended = () => {
        setTimeout(playNextTts, 100); // Rút ngắn khoảng nghỉ giữa 2 câu xuống 100ms
      };
    })
    .catch(e => {
      console.warn('TTS playback prevented or waiting for user interaction:', e);
      setTimeout(playNextTts, 500);
    });
}

// Kích hoạt audio khi người dùng chạm màn hình lần đầu
window.addEventListener('click', () => {
  if (ttsAudio.paused && ttsQueue.length > 0) {
    playNextTts();
  }
}, { once: true });

// ============================================================
// 7. HỆ THỐNG HẠT VÀ PHÁO HOA (CANVAS FX - GPU TỐI ƯU)
// ============================================================
let particles = [];
let isFxRunning = false;

class Particle {
  constructor(x, y, color) {
    this.x = x;
    this.y = y;
    this.color = color;
    this.radius = Math.random() * 3 + 2;
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 7 + 2.5;
    this.vx = Math.cos(angle) * speed;
    this.vy = Math.sin(angle) * speed;
    this.alpha = 1;
    this.decay = Math.random() * 0.025 + 0.02;
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

function startFxLoopIfNeeded() {
  if (!isFxRunning && particles.length > 0) {
    isFxRunning = true;
    requestAnimationFrame(fxLoop);
  }
}

function triggerFireworks() {
  const colors = ['#ffd700', '#ff007f', '#00f2fe', '#7000ff', '#ffffff'];
  for (let i = 0; i < 3; i++) {
    setTimeout(() => {
      const rx = Math.random() * 600 + 240;
      const ry = Math.random() * 600 + 400;
      // Tối ưu số lượng hạt từ 80 xuống 35 để không gây giật lag
      for (let j = 0; j < 35; j++) {
        const color = colors[Math.floor(Math.random() * colors.length)];
        particles.push(new Particle(rx, ry, color));
      }
      startFxLoopIfNeeded();
    }, i * 200);
  }
}

function createHeartBurst(x, y) {
  const colors = ['#ff3b5c', '#ff8800', '#ff007f'];
  // Tối ưu số lượng hạt từ 40 xuống 18
  for (let i = 0; i < 18; i++) {
    const color = colors[Math.floor(Math.random() * colors.length)];
    particles.push(new Particle(x, y, color));
  }
  startFxLoopIfNeeded();
}

function fxLoop() {
  if (particles.length === 0) {
    ctx.clearRect(0, 0, fxCanvas.width, fxCanvas.height);
    isFxRunning = false;
    return; // Dừng vòng lặp khi không còn hiệu ứng để trả CPU/GPU về 0%
  }

  ctx.clearRect(0, 0, fxCanvas.width, fxCanvas.height);
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.update();
    p.draw(ctx);
    if (p.alpha <= 0) {
      particles.splice(i, 1);
    }
  }

  if (particles.length > 0) {
    requestAnimationFrame(fxLoop);
  } else {
    ctx.clearRect(0, 0, fxCanvas.width, fxCanvas.height);
    isFxRunning = false;
  }
}

// Khởi chạy
initMap();
