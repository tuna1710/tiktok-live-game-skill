const path = require('path');
const QuestionBank = require('../data/questionBank');

const qb = new QuestionBank(path.join(__dirname, '..', 'data'));
const cmd = process.argv[2] || 'stats';

if (cmd === 'stats') {
  const stats = qb.getStats();
  console.log('\n📊 === THỐNG KÊ NGÂN HÀNG CÂU HỎI RUNG CHUÔNG VÀNG ===');
  console.log(`📌 Tổng số câu hỏi hiện có: ${stats.total}`);
  console.log('\nPhân bố theo độ khó:');
  console.log(`  - Cấp 1 (Dễ):        ${stats.byDifficulty[1]} câu`);
  console.log(`  - Cấp 2 (Trung bình): ${stats.byDifficulty[2]} câu`);
  console.log(`  - Cấp 3 (Khó):       ${stats.byDifficulty[3]} câu`);
  console.log('\nPhân bố theo chủ đề:');
  for (const [cat, count] of Object.entries(stats.byCategory)) {
    console.log(`  - [${cat}]: ${count} câu`);
  }
  console.log('===================================================\n');
} else if (cmd === 'sync') {
  qb.syncToLegacyFile();
} else if (cmd === 'lint') {
  console.log('🔍 Đang kiểm tra tính hợp lệ toàn bộ ngân hàng câu hỏi...');
  const all = qb.getAll();
  const seenTexts = new Map();
  let errors = 0;

  all.forEach((q, idx) => {
    const norm = qb.normalizeText(q.question);
    if (seenTexts.has(norm)) {
      console.warn(`⚠️ [TRÙNG LẶP] Câu ${q.id} trùng với câu ${seenTexts.get(norm)}: "${q.question}"`);
      errors++;
    } else {
      seenTexts.set(norm, q.id);
    }

    if (!q.options || q.options.length !== 4) {
      console.error(`❌ [LỖI ĐÁP ÁN] Câu ${q.id} không có đúng 4 đáp án`);
      errors++;
    }
    if (q.correct < 0 || q.correct > 3) {
      console.error(`❌ [LỖI ĐÁP ÁN ĐÚNG] Câu ${q.id} có đáp án đúng ngoài khoảng 0..3`);
      errors++;
    }
    if (!q.explanation || q.explanation.trim().length === 0) {
      console.warn(`⚠️ [THIẾU GIẢI THÍCH] Câu ${q.id} chưa có lời giải thích`);
      errors++;
    }
  });

  if (errors === 0) {
    console.log(`✅ Toàn bộ ${all.length} câu hỏi đạt chuẩn 100%, không phát hiện lỗi!`);
  } else {
    console.log(`⚠️ Phát hiện ${errors} vấn đề cần lưu ý.`);
  }
} else {
  console.log('Cách dùng: node manage_questions.js [stats|lint|sync]');
}
