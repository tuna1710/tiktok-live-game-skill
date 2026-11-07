# -*- coding: utf-8 -*-
"""
Công cụ sinh câu hỏi tự động bằng AI (Google Gemini 2.5 Flash)
Tích hợp Antigravity Agent Studio & Gemini Interactions API
Tự động kiểm tra trùng lặp và lưu trữ vào SQLite questions.db
"""

import os
import sys
import json
import sqlite3
import argparse
import re
from google import genai
from google.genai import types

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CATEGORIES_DIR = os.path.join(DATA_DIR, 'categories')
DB_PATH = os.path.join(DATA_DIR, 'questions.db')
QUESTIONS_JSON_PATH = os.path.join(DATA_DIR, 'questions.json')

USER_API_KEY = 'AIzaSyBx7vEx2JCZxtoQpMBkmZQnfgsqn-ACgzo'
env_key = os.getenv('GEMINI_API_KEY', '')
DEFAULT_API_KEY = USER_API_KEY if (not env_key or env_key == 'PLACEHOLDER') else env_key

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

def generate_questions(category: str, count: int, difficulty: str = 'all', api_key: str = DEFAULT_API_KEY):
    topic_desc = CATEGORY_PROMPTS.get(category, category)
    diff_instruction = ""
    if difficulty in ['1', '2', '3']:
        diff_instruction = f"Tất cả câu hỏi phải có độ khó đúng mức {difficulty} (1: Dễ, 2: Trung bình, 3: Khó)."
    else:
        diff_instruction = "Phân bổ độ khó cân đối: khoảng 30% Dễ (độ khó 1), 40% Trung bình (độ khó 2), 30% Khó (độ khó 3)."

    prompt = f"""Bạn là chuyên gia biên soạn ngân hàng câu hỏi chuẩn cho gameshow 'Rung Chuông Vàng' trên TikTok Live.
Hãy tạo đúng {count} câu hỏi trắc nghiệm tiếng Việt đặc sắc thuộc chủ đề: {topic_desc}.

Yêu cầu chất lượng khắt khe:
1. Câu hỏi và đáp án hoàn toàn bằng tiếng Việt chuẩn xác, văn phong hấp dẫn, không gây hiểu lầm.
2. {diff_instruction}
3. Mỗi câu hỏi phải có đúng 4 lựa chọn (options) phân biệt rõ ràng, không có đáp án trùng lặp, chỉ duy nhất 1 đáp án đúng 100%.
4. 'correct' là chỉ số (0, 1, 2, hoặc 3) của đáp án đúng trong mảng options.
5. 'explanation' là lời giải thích ngắn gọn, súc tích (1-2 câu) giúp MC đọc giải thích ngay trên sóng live.
6. Tuyệt đối không sinh câu hỏi nhảm nhí, bạo lực hay vi phạm tiêu chuẩn cộng đồng TikTok.

Trả về kết quả ở định dạng JSON array chuẩn (không kèm văn bản dẫn nhập), cấu trúc mỗi đối tượng:
[
  {{
    "question": "Nội dung câu hỏi?",
    "options": ["Đáp án A", "Đáp án B", "Đáp án C", "Đáp án D"],
    "correct": 0,
    "difficulty": 1,
    "explanation": "Lời giải thích ngắn gọn."
  }}
]"""

    client = genai.Client(api_key=api_key, http_options={'api_version': 'v1beta'})
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.7
            )
        )
        data = json.loads(response.text)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'questions' in data:
            return data['questions']
        return []
    except Exception as e:
        print(f"❌ Lỗi gọi Gemini API: {e}")
        return []

def save_to_db_and_sync(questions, category):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    inserted = 0
    duplicate = 0
    new_items_for_json = []

    for q in questions:
        q_text = q.get('question', '').strip()
        options = q.get('options', [])
        if not q_text or len(options) != 4:
            continue
        correct = int(q.get('correct', 0))
        if correct < 0 or correct > 3:
            continue
        difficulty = int(q.get('difficulty', 1))
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
            new_items_for_json.append({
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

    # Cập nhật tệp categories/<category>.json
    cat_file = os.path.join(CATEGORIES_DIR, f"{category}.json")
    existing_cat = []
    if os.path.exists(cat_file):
        try:
            with open(cat_file, 'r', encoding='utf-8') as f:
                existing_cat = json.load(f)
        except Exception:
            existing_cat = []
    existing_cat.extend(new_items_for_json)
    with open(cat_file, 'w', encoding='utf-8') as f:
        json.dump(existing_cat, f, ensure_ascii=False, indent=2)

    # Đồng bộ toàn bộ SQLite ra questions.json
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

def main():
    parser = argparse.ArgumentParser(description="Sinh câu hỏi Rung Chuông Vàng bằng AI Gemini")
    parser.add_argument('--category', type=str, default='all', choices=list(CATEGORY_PROMPTS.keys()) + ['all'], help="Chuyên mục")
    parser.add_argument('--count', type=int, default=10, help="Số câu mỗi chuyên mục")
    parser.add_argument('--difficulty', type=str, default='all', choices=['1', '2', '3', 'all'], help="Độ khó")
    args = parser.parse_args()

    target_cats = list(CATEGORY_PROMPTS.keys()) if args.category == 'all' else [args.category]

    print(f"🚀 Bắt đầu sinh câu hỏi tự động với AI Gemini 2.5 Flash...")
    print(f"📋 Các chuyên mục: {target_cats}")
    print(f"🎯 Số lượng: {args.count} câu / chuyên mục\n")

    total_inserted = 0
    total_duplicate = 0

    for cat in target_cats:
        print(f"⏳ Đang sinh {args.count} câu hỏi cho [{cat}]...")
        items = generate_questions(cat, args.count, args.difficulty)
        if items:
            ins, dup, current_total = save_to_db_and_sync(items, cat)
            total_inserted += ins
            total_duplicate += dup
            print(f"   ✅ [{cat}]: Thêm thành công {ins} câu (Trùng lặp: {dup}). Tổng ngân hàng: {current_total} câu.")
        else:
            print(f"   ⚠️ Không nhận được câu hỏi từ AI cho [{cat}].")

    print(f"\n🎉 HOÀN THÀNH ĐỢT SINH CÂU HỎI:")
    print(f"   - Tổng số câu mới nạp vào SQLite: {total_inserted}")
    print(f"   - Số câu trùng lặp bị lọc bỏ: {total_duplicate}")

if __name__ == '__main__':
    main()
