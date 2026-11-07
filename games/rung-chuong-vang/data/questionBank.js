const fs = require('fs');
const path = require('path');

class QuestionBank {
  constructor(baseDir = __dirname) {
    this.baseDir = baseDir;
    this.categoriesDir = path.join(baseDir, 'categories');
    this.legacyFile = path.join(baseDir, 'questions.json');
    this.questions = [];
    this.categories = new Map(); // categoryName -> array of questions
    this.normalizedMap = new Set();
    this.init();
  }

  init() {
    this.questions = [];
    this.categories.clear();
    this.normalizedMap.clear();

    if (fs.existsSync(this.categoriesDir)) {
      const files = fs.readdirSync(this.categoriesDir).filter(f => f.endsWith('.json'));
      if (files.length > 0) {
        for (const file of files) {
          const catName = path.basename(file, '.json');
          const filePath = path.join(this.categoriesDir, file);
          try {
            const raw = fs.readFileSync(filePath, 'utf8');
            const list = JSON.parse(raw);
            if (Array.isArray(list)) {
              const validated = [];
              for (const item of list) {
                if (this.isValidQuestion(item)) {
                  const norm = this.normalizeText(item.question);
                  if (!this.normalizedMap.has(norm)) {
                    this.normalizedMap.add(norm);
                    item.category = item.category || catName;
                    validated.push(item);
                  }
                }
              }
              this.categories.set(catName, validated);
              this.questions.push(...validated);
            }
          } catch (err) {
            console.error(`[QuestionBank] Lỗi đọc file ${file}:`, err.message);
          }
        }
      }
    }

    // Nếu chưa có thư mục categories hoặc không có câu hỏi, nạp từ legacy questions.json
    if (this.questions.length === 0 && fs.existsSync(this.legacyFile)) {
      try {
        const raw = fs.readFileSync(this.legacyFile, 'utf8');
        const list = JSON.parse(raw);
        if (Array.isArray(list)) {
          this.questions = list.filter(q => this.isValidQuestion(q));
          this.categories.set('tong-hop', this.questions);
        }
      } catch (err) {
        console.error(`[QuestionBank] Lỗi nạp legacy questions.json:`, err.message);
      }
    }

    // Đánh lại ID chuẩn từ 1 đến N
    this.questions.forEach((q, idx) => {
      q.id = idx + 1;
    });

    console.log(`[QuestionBank] Đã khởi tạo ngân hàng câu hỏi: ${this.questions.length} câu hỏi thuộc ${this.categories.size} chủ đề.`);
  }

  isValidQuestion(q) {
    return (
      q &&
      typeof q.question === 'string' &&
      q.question.trim().length > 5 &&
      Array.isArray(q.options) &&
      q.options.length === 4 &&
      typeof q.correct === 'number' &&
      q.correct >= 0 &&
      q.correct <= 3 &&
      [1, 2, 3].includes(Number(q.difficulty))
    );
  }

  normalizeText(str) {
    return str
      .toLowerCase()
      .replace(/[^\p{L}\p{N}]/gu, '')
      .trim();
  }

  getAll() {
    return this.questions;
  }

  getStats() {
    const stats = {
      total: this.questions.length,
      byDifficulty: { 1: 0, 2: 0, 3: 0 },
      byCategory: {}
    };

    for (const q of this.questions) {
      stats.byDifficulty[q.difficulty] = (stats.byDifficulty[q.difficulty] || 0) + 1;
      const cat = q.category || 'tong-hop';
      stats.byCategory[cat] = (stats.byCategory[cat] || 0) + 1;
    }
    return stats;
  }

  pickQuestions({ total = 15, category = 'all' } = {}) {
    let pool = this.questions;
    if (category !== 'all' && this.categories.has(category)) {
      pool = this.categories.get(category);
    }

    const easy = pool.filter(q => q.difficulty === 1).sort(() => 0.5 - Math.random());
    const medium = pool.filter(q => q.difficulty === 2).sort(() => 0.5 - Math.random());
    const hard = pool.filter(q => q.difficulty === 3).sort(() => 0.5 - Math.random());

    const result = [
      ...easy.slice(0, 5),
      ...medium.slice(0, 6),
      ...hard.slice(0, 4)
    ];

    if (result.length < total) {
      const remaining = pool.filter(q => !result.includes(q)).sort(() => 0.5 - Math.random());
      result.push(...remaining.slice(0, total - result.length));
    }

    return result.slice(0, total);
  }

  // Đồng bộ toàn bộ dữ liệu ra file questions.json chuẩn
  syncToLegacyFile() {
    fs.writeFileSync(this.legacyFile, JSON.stringify(this.questions, null, 2), 'utf8');
    console.log(`[QuestionBank] Đã đồng bộ ${this.questions.length} câu hỏi ra ${this.legacyFile}`);
  }
}

module.exports = QuestionBank;
