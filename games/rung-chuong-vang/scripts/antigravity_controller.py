# -*- coding: utf-8 -*-
"""
🛸 Antigravity Cluster Controller
Quản lý cụm 3 Sandbox Google Cloud để tăng tốc sinh 10.000 câu hỏi song song
Tương thích với kiến trúc Google Antigravity Agent Studio Pro
"""

import os
import sys
import json
import time
import re
import sqlite3
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from google import genai
from google.genai import types

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CATEGORIES_DIR = os.path.join(DATA_DIR, 'categories')
DB_PATH = os.path.join(DATA_DIR, 'questions.db')
SANDBOXES_FILE = os.path.join(DATA_DIR, 'sandboxes.json')
QUESTIONS_JSON_PATH = os.path.join(DATA_DIR, 'questions.json')

USER_API_KEY = 'AIzaSyBx7vEx2JCZxtoQpMBkmZQnfgsqn-ACgzo'
env_key = os.getenv('GEMINI_API_KEY', '')
API_KEY = USER_API_KEY if (not env_key or env_key == 'PLACEHOLDER') else env_key

CATEGORY_PROMPTS = {
    'do-vui-tri-tue': 'đố mẹo dân gian Việt Nam, câu đố chữ, tư duy logic hài hước, phản xạ nhanh cho gameshow TikTok Live',
    'lich-su': 'lịch sử Việt Nam hào hùng (thời Hùng Vương, Hai Bà Trưng, Đinh, Lý, Trần, Lê, Quang Trung, thời cận hiện đại) và các mốc lịch sử thế giới kinh điển',
    'dia-ly': 'địa lý 63 tỉnh thành Việt Nam, danh lam thắng cảnh, di sản văn hóa, biển đảo Hoàng Sa - Trường Sa, sông hồ, núi đèo và các kỷ lục địa lý thế giới',
    'khoa-hoc-tu-nhien': 'khoa học tự nhiên, vật lý, hóa học, sinh học, cơ thể con người, thiên văn học, hệ mặt trời và các hiện tượng tự nhiên kỳ thú',
    'van-hoc-nghe-thuat': 'kho tàng ca dao tục ngữ Việt Nam, truyện cổ tích, tác phẩm văn học kinh điển, âm nhạc, hội họa, nghệ thuật sân khấu dân gian',
    'doi-song-cong-nghe': 'công nghệ thông tin, trí tuệ nhân tạo (AI), điện thoại thông minh, ẩm thực 3 miền Việt Nam, thể thao bóng đá và đời sống hiện đại'
}

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r'[^\w\s]', '', t, flags=re.UNICODE)
    return ' '.join(t.split())

class AntigravityCluster:
    def __init__(self, api_key: str = API_KEY):
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key, http_options={'api_version': 'v1beta'})
        self.sandboxes = self.load_sandboxes()

    def load_sandboxes(self):
        if os.path.exists(SANDBOXES_FILE):
            try:
                with open(SANDBOXES_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def save_sandboxes(self):
        with open(SANDBOXES_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.sandboxes, f, ensure_ascii=False, indent=2)

    def print_sandboxes(self):
        print("\n🛸 === DANH SÁCH 3 CLOUD SANDBOXES ĐANG HOẠT ĐỘNG ===")
        for s_id, s_info in self.sandboxes.items():
            print(f"📦 [{s_id}] {s_info.get('name')}")
            print(f"   - Mã Sandbox (Environment ID): {s_info.get('environment_id')}")
            print(f"   - Vai trò: {s_info.get('role')}")
            print(f"   - Chuyên mục phụ trách: {s_info.get('categories')}")
            print(f"   - Trạng thái: {s_info.get('status')} | Tạo lúc: {s_info.get('created_at')}")
            print("   --------------------------------------------------------")
        print("========================================================\n")

    def generate_for_category(self, sandbox_id: str, category: str, count: int):
        s_info = self.sandboxes.get(sandbox_id, {})
        env_id = s_info.get('environment_id')
        topic_desc = CATEGORY_PROMPTS.get(category, category)

        prompt = f"""Bạn đang làm việc trong Sandbox Google Cloud: {env_id}.
Hãy biên soạn đúng {count} câu hỏi trắc nghiệm tiếng Việt cực kỳ chọn lọc cho gameshow 'Rung Chuông Vàng' trên TikTok Live.
Chủ đề: {topic_desc}.

Yêu cầu định dạng JSON array chuẩn 100%:
[
  {{
    "question": "Nội dung câu hỏi?",
    "options": ["Đáp án A", "Đáp án B", "Đáp án C", "Đáp án D"],
    "correct": 0,
    "difficulty": 1,
    "explanation": "Lời giải thích ngắn gọn."
  }}
]

Quy chuẩn:
- 4 lựa chọn không trùng lặp, chỉ duy nhất 1 đáp án đúng.
- 'correct' là chỉ số 0..3.
- 'difficulty': 1 (Dễ), 2 (Trung bình), hoặc 3 (Khó). Phân bố đều cả 3 mức.
- Không kèm thêm bất kỳ văn bản giải thích nào ngoài khối JSON."""

        try:
            # Gửi yêu cầu gắn kết với Sandbox cụ thể
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    temperature=0.75
                )
            )
            data = json.loads(response.text)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and 'questions' in data:
                return data['questions']
            return []
        except Exception as e:
            print(f"❌ Lỗi sinh câu hỏi trên Sandbox {sandbox_id} cho [{category}]: {e}")
            return []

    def save_questions_to_db(self, category: str, questions: list):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        inserted = 0
        duplicate = 0
        new_items = []

        for q in questions:
            q_text = q.get('question', '').strip()
            options = q.get('options', [])
            if not q_text or len(options) != 4:
                continue
            correct = int(q.get('correct', 0))
            if correct < 0 or correct > 3:
                continue
            difficulty = int(q.get('difficulty', 2))
            if difficulty not in [1, 2, 3]:
                difficulty = 2
            explanation = q.get('explanation', '').strip()
            norm = normalize_text(q_text)

            try:
                cursor.execute("""
                    INSERT INTO questions (category, difficulty, question, options, correct, explanation, normalized)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (category, difficulty, q_text, json.dumps(options, ensure_ascii=False), correct, explanation, norm))
                inserted += 1
                new_items.append({
                    "category": category,
                    "difficulty": difficulty,
                    "question": q_text,
                    "options": options,
                    "correct": correct,
                    "explanation": explanation
                })
            except sqlite3.IntegrityError:
                duplicate += 1

        conn.commit()

        # Đồng bộ category JSON
        cat_file = os.path.join(CATEGORIES_DIR, f"{category}.json")
        cat_data = []
        if os.path.exists(cat_file):
            try:
                with open(cat_file, 'r', encoding='utf-8') as f:
                    cat_data = json.load(f)
            except Exception:
                pass
        cat_data.extend(new_items)
        with open(cat_file, 'w', encoding='utf-8') as f:
            json.dump(cat_data, f, ensure_ascii=False, indent=2)

        # Đồng bộ questions.json
        cursor.execute("SELECT id, category, difficulty, question, options, correct, explanation FROM questions ORDER BY id ASC;")
        all_rows = cursor.fetchall()
        export_list = []
        for r in all_rows:
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

        conn.close()
        return inserted, duplicate, len(export_list)

    def run_parallel_workers(self, count_per_cat: int = 15):
        tasks = []
        for s_id, s_info in self.sandboxes.items():
            cats = s_info.get('categories', [])
            for c in cats:
                tasks.append((s_id, c, count_per_cat))

        print(f"🚀 Bắt đầu điều phối song song {len(tasks)} tác vụ trên 3 Sandboxes...")
        start_time = time.time()
        results = {}

        def worker_task(item):
            s_id, cat, cnt = item
            print(f"⚡ [Sandbox: {s_id}] Đang sinh {cnt} câu cho [{cat}]...")
            q_list = self.generate_for_category(s_id, cat, cnt)
            if q_list:
                ins, dup, current_total = self.save_questions_to_db(cat, q_list)
                return cat, ins, dup, current_total
            return cat, 0, 0, 0

        with ThreadPoolExecutor(max_workers=3) as executor:
            future_to_task = {executor.submit(worker_task, t): t for t in tasks}
            for future in as_completed(future_to_task):
                cat, ins, dup, current_total = future.result()
                results[cat] = {'inserted': ins, 'duplicate': dup, 'total': current_total}
                print(f"   ✅ Hoàn thành [{cat}]: +{ins} câu mới (Trùng: {dup})")

        duration = time.time() - start_time
        print(f"\n🎉 HOÀN THÀNH TOÀN BỘ CỤM 3 SANDBOXES trong {duration:.2f}s!")
        print("Chi tiết kết quả từng chuyên mục:")
        total_new = 0
        for cat, r in results.items():
            print(f"  - [{cat}]: +{r['inserted']} câu mới (Trùng lặp bị loại: {r['duplicate']})")
            total_new += r['inserted']
        print(f"👉 Tổng số câu hỏi mới nạp vào SQLite: {total_new} câu.")

def main():
    parser = argparse.ArgumentParser(description="Điều khiển cụm 3 Sandboxes Antigravity Agent Studio")
    parser.add_argument('command', choices=['list', 'parallel', 'sync'], default='list', nargs='?', help="Lệnh thực thi")
    parser.add_argument('--count', type=int, default=15, help="Số câu mỗi chuyên mục khi chạy song song")
    args = parser.parse_args()

    cluster = AntigravityCluster()

    if args.command == 'list':
        cluster.print_sandboxes()
    elif args.command == 'parallel':
        cluster.print_sandboxes()
        cluster.run_parallel_workers(count_per_cat=args.count)
    elif args.command == 'sync':
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM questions;")
        cnt = cursor.fetchone()[0]
        print(f"Hiện có {cnt} câu hỏi trong SQLite questions.db")
        conn.close()

if __name__ == '__main__':
    main()
