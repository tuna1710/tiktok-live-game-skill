const socket = io();

const redScoreEl = document.getElementById('red-score');
const blueScoreEl = document.getElementById('blue-score');
const redBarEl = document.getElementById('tug-bar-red');
const blueBarEl = document.getElementById('tug-bar-blue');
const pinEl = document.getElementById('tug-pin');
const winBanner = document.getElementById('win-banner');
const winText = document.getElementById('win-text');
const redLbList = document.getElementById('red-lb-list');
const blueLbList = document.getElementById('blue-lb-list');

const canvas = document.getElementById('battle-canvas');
const ctx = canvas.getContext('2d');

let particles = [];

socket.on('gameState', state => {
  redScoreEl.textContent = state.redScore;
  blueScoreEl.textContent = state.blueScore;

  const total = state.redScore + state.blueScore;
  const redPercent = total > 0 ? (state.redScore / total) * 100 : 50;
  const bluePercent = 100 - redPercent;

  redBarEl.style.width = `${redPercent}%`;
  blueBarEl.style.width = `${bluePercent}%`;
  pinEl.style.left = `${redPercent}%`;

  renderLb(redLbList, state.redContributors);
  renderLb(blueLbList, state.blueContributors);
});

socket.on('game:win', data => {
  winText.textContent = data.text;
  winBanner.classList.remove('hidden');
});

socket.on('game:reset', () => {
  winBanner.classList.add('hidden');
  particles = [];
});

socket.on('chat', data => {
  const isRed = data.comment === '1' || data.comment.toLowerCase().includes('đỏ');
  spawnFighter(isRed ? '#ff3b5c' : '#00f2fe', isRed ? 100 : canvas.width - 100, data.nickname);
});

socket.on('gift', data => {
  for (let i = 0; i < 40; i++) {
    particles.push({
      x: canvas.width / 2, y: canvas.height / 2,
      vx: (Math.random() - 0.5) * 16, vy: (Math.random() - 0.5) * 16,
      color: Math.random() > 0.5 ? '#ff3b5c' : '#00f2fe',
      alpha: 1
    });
  }
});

function spawnFighter(color, startX, name) {
  particles.push({
    x: startX, y: canvas.height * 0.7,
    vx: startX < canvas.width / 2 ? 6 : -6,
    vy: -2,
    color,
    name,
    alpha: 1
  });
}

function renderLb(el, contributors) {
  const sorted = Object.values(contributors || {}).sort((a,b) => b.points - a.points).slice(0, 3);
  if (!sorted.length) return el.innerHTML = '<li>Chưa có điểm</li>';
  el.innerHTML = sorted.map((u, i) => `<li>#${i+1} ${u.nickname}: <strong>${u.points}đ</strong></li>`).join('');
}

function loop() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.x += p.vx || 0;
    p.y += p.vy || 0;
    p.alpha -= 0.015;

    ctx.save();
    ctx.globalAlpha = Math.max(0, p.alpha);
    ctx.fillStyle = p.color;
    ctx.beginPath();
    ctx.arc(p.x, p.y, 10, 0, Math.PI * 2);
    ctx.fill();
    if (p.name) {
      ctx.fillStyle = "#fff";
      ctx.font = "bold 16px sans-serif";
      ctx.fillText(p.name.slice(0, 8), p.x - 20, p.y - 15);
    }
    ctx.restore();

    if (p.alpha <= 0) particles.splice(i, 1);
  }
  requestAnimationFrame(loop);
}
loop();
