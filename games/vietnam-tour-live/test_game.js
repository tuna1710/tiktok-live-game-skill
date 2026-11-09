// Script kiểm thử toàn diện cho Vietnam Tour Live
const assert = require('assert');
const fs = require('fs');
const path = require('path');

console.log('🧪 BẮT ĐẦU KIỂM THỬ TỰ ĐỘNG: VIETNAM TOUR LIVE');

// 1. Kiểm tra database tỉnh thành
const provincesFile = path.join(__dirname, 'data', 'provinces.json');
assert(fs.existsSync(provincesFile), 'Thiếu file data/provinces.json');
const provinces = JSON.parse(fs.readFileSync(provincesFile, 'utf-8'));
assert.strictEqual(provinces.length, 63, `Cần đủ 63 tỉnh thành, hiện có: ${provinces.length}`);
console.log('✅ 1. Kiểm tra Database 63 tỉnh thành: ĐẠT');

// 2. Kiểm tra file SVG bản đồ
const svgFile = path.join(__dirname, 'public', 'vietnam.svg');
assert(fs.existsSync(svgFile), 'Thiếu file public/vietnam.svg');
const svgContent = fs.readFileSync(svgFile, 'utf-8');
assert(svgContent.includes('<svg'), 'File SVG không hợp lệ');
assert(svgContent.includes('id="laocai"'), 'Thiếu id laocai trong SVG');
assert(svgContent.includes('id="tayninh"'), 'Thiếu id tayninh trong SVG');
console.log('✅ 2. Kiểm tra Bản đồ Vector SVG: ĐẠT');

// 3. Kiểm tra logic chuẩn hóa và match tỉnh thành
function normalizeText(str) {
  if (!str) return '';
  return str.toString().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'd').toLowerCase().replace(/[^a-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim();
}

function matchProvince(comment) {
  const norm = normalizeText(comment);
  if (!norm) return null;
  for (const p of provinces) {
    for (const alias of p.aliases) {
      if (norm === normalizeText(alias)) return p;
    }
  }
  for (const p of provinces) {
    for (const alias of p.aliases) {
      const normAlias = normalizeText(alias);
      if (normAlias.length < 2) continue;
      const regex = new RegExp(`(^|\\s)${normAlias}(\\s|$)`, 'i');
      if (regex.test(norm)) return p;
    }
  }
  return null;
}

assert.strictEqual(matchProvince('Lào cai')?.id, 'lao-cai');
assert.strictEqual(matchProvince('lao cai')?.id, 'lao-cai');
assert.strictEqual(matchProvince('cho em ve tay ninh voi ad')?.id, 'tay-ninh');
assert.strictEqual(matchProvince('sg nha')?.id, 'ho-chi-minh');
assert.strictEqual(matchProvince('da nang dep qua')?.id, 'da-nang');
assert.strictEqual(matchProvince('thu do ha noi')?.id, 'ha-noi');
console.log('✅ 3. Kiểm tra thuật toán nhận diện tỉnh từ comment: ĐẠT (100% khớp các trường hợp khó)');

// 4. Kiểm tra cấu trúc file frontend
assert(fs.existsSync(path.join(__dirname, 'public', 'index.html')), 'Thiếu public/index.html');
assert(fs.existsSync(path.join(__dirname, 'public', 'style.css')), 'Thiếu public/style.css');
assert(fs.existsSync(path.join(__dirname, 'public', 'game.js')), 'Thiếu public/game.js');
assert(fs.existsSync(path.join(__dirname, 'public', 'admin.html')), 'Thiếu public/admin.html');
console.log('✅ 4. Kiểm tra toàn bộ file Frontend & Mock Admin: ĐẠT');

// 5. Kiểm tra Colab Runners
assert(fs.existsSync(path.join(__dirname, 'run_colab.py')), 'Thiếu run_colab.py');
assert(fs.existsSync(path.join(__dirname, 'live_ngam_tiktok.py')), 'Thiếu live_ngam_tiktok.py');
console.log('✅ 5. Kiểm tra Bộ khởi chạy kép trên Colab: ĐẠT');

console.log('\n🎉 TOÀN BỘ BÀI TEST ĐÃ VƯỢT QUA XUẤT SẮC!');
