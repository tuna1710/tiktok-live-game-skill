# -*- coding: utf-8 -*-
"""
Khởi tạo và đồng bộ Ngân hàng câu hỏi SQLite (questions.db)
Chuyển đổi toàn bộ ngân hàng câu hỏi từ JSON sang SQLite với Indexing & Chống trùng lặp.
"""

import sqlite3
import json
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CATEGORIES_DIR = os.path.join(DATA_DIR, 'categories')
DB_PATH = os.path.join(DATA_DIR, 'questions.db')
QUESTIONS_JSON_PATH = os.path.join(DATA_DIR, 'questions.json')

def normalize_text(text: str) -> str:
    """Chuẩn hóa chuỗi văn bản tiếng Việt để so sánh trùng lặp"""
    t = text.lower()
    t = re.sub(r'[^\w\s]', '', t, flags=re.UNICODE)
    return ' '.join(t.split())

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Bật WAL mode để truy vấn đồng thời nhanh hơn gấp nhiều lần
    cursor.execute("PRAGMA journal_mode=WAL;")

    # Tạo bảng questions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        difficulty INTEGER NOT NULL CHECK (difficulty IN (1, 2, 3)),
        question TEXT NOT NULL,
        options TEXT NOT NULL, -- Lưu chuỗi JSON array 4 phần tử
        correct INTEGER NOT NULL CHECK (correct IN (0, 1, 2, 3)),
        explanation TEXT,
        normalized TEXT UNIQUE NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Tạo chỉ mục tối ưu hóa truy vấn ngẫu nhiên theo độ khó & chuyên mục
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_cat_diff ON questions (category, difficulty);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_diff ON questions (difficulty);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_normalized ON questions (normalized);")

    conn.commit()
    return conn

def import_from_categories(conn):
    cursor = conn.cursor()
    inserted = 0
    skipped = 0

    if not os.path.exists(CATEGORIES_DIR):
        print(f"Thư mục {CATEGORIES_DIR} không tồn tại.")
        return

    for filename in sorted(os.listdir(CATEGORIES_DIR)):
        if not filename.endswith('.json'):
            continue
        cat_name = filename.replace('.json', '')
        file_path = os.path.join(CATEGORIES_DIR, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                items = json.load(f)
            
            for item in items:
                q_text = item.get('question', '').strip()
                if not q_text:
                    continue
                norm = normalize_text(q_text)
                options = json.dumps(item.get('options', []), ensure_ascii=False)
                correct = int(item.get('correct', 0))
                difficulty = int(item.get('difficulty', 1))
                category = item.get('category', cat_name)
                explanation = item.get('explanation', '').strip()

                try:
                    cursor.execute("""
                        INSERT INTO questions (category, difficulty, question, options, correct, explanation, normalized)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (category, difficulty, q_text, options, correct, explanation, norm))
                    inserted += 1
                except sqlite3.IntegrityError:
                    skipped += 1
        except Exception as e:
            print(f"Lỗi khi đọc file {filename}: {e}")

    conn.commit()
    print(f"✅ Đã nạp vào SQLite questions.db: {inserted} câu hỏi mới (Bỏ qua {skipped} câu trùng lặp).")

def export_to_json(conn):
    """Xuất từ SQLite ra questions.json để bảo đảm tính tương thích với server"""
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, difficulty, question, options, correct, explanation FROM questions ORDER BY id ASC;")
    rows = cursor.fetchall()

    export_list = []
    for r in rows:
        export_list.append({
            "id": r[0],
            "category": r[1],
            "difficulty": r[2],
            "question": r[3],
            "options": json.loads(r[4]),
            "correct": r[5],
            "explanation": r[6]
        })

    with open(QUESTIONS_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(export_list, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã đồng bộ {len(export_list)} câu hỏi từ SQLite ra {QUESTIONS_JSON_PATH}")

def print_stats(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM questions;")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT difficulty, COUNT(*) FROM questions GROUP BY difficulty ORDER BY difficulty;")
    diff_stats = cursor.fetchall()

    cursor.execute("SELECT category, COUNT(*) FROM questions GROUP BY category ORDER BY COUNT(*) DESC;")
    cat_stats = cursor.fetchall()

    print("\n📊 === THỐNG KÊ CƠ SỞ DỮ LIỆU SQLITE (questions.db) ===")
    print(f"📌 Tổng số câu hỏi: {total} câu")
    print("\nPhân bố theo độ khó:")
    for d, c in diff_stats:
        labels = {1: 'Cấp 1 (Dễ)', 2: 'Cấp 2 (Trung bình)', 3: 'Cấp 3 (Khó)'}
        print(f"  - {labels.get(d, d)}: {c} câu ({c/total*100:.1f}%)")
    print("\nPhân bố theo chuyên mục:")
    for cat, c in cat_stats:
        print(f"  - [{cat}]: {c} câu")
    print("=====================================================\n")

if __name__ == '__main__':
    conn = init_db()
    import_from_categories(conn)
    export_to_json(conn)
    print_stats(conn)
    conn.close()
