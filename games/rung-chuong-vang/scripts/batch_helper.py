# -*- coding: utf-8 -*-
import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CATEGORIES_DIR = os.path.join(DATA_DIR, 'categories')

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r'[^\w\s]', '', t, flags=re.UNICODE)
    return ' '.join(t.split())

def add_questions_to_category(cat_name: str, questions_raw: list) -> int:
    cat_file = os.path.join(CATEGORIES_DIR, f"{cat_name}.json")
    existing_list = []
    if os.path.exists(cat_file):
        try:
            with open(cat_file, 'r', encoding='utf-8') as f:
                existing_list = json.load(f)
        except Exception as e:
            print(f"Error loading {cat_file}: {e}")

    existing_normalized = set()
    for item in existing_list:
        existing_normalized.add(normalize_text(item.get('question', '')))

    added = 0
    for idx, q in enumerate(questions_raw):
        question_text = q.get('question', '').strip()
        norm = normalize_text(question_text)
        if not norm or norm in existing_normalized:
            continue

        difficulty = int(q.get('difficulty', 1))
        explanation = q.get('explanation', '').strip()

        if 'options' in q and 'correct' in q:
            options = q['options']
            correct = int(q['correct'])
        elif 'correct_answer' in q and 'distractors' in q:
            correct_ans = q['correct_answer'].strip()
            distractors = [d.strip() for d in q['distractors']]
            if len(distractors) != 3:
                continue
            correct = idx % 4
            options = list(distractors)
            options.insert(correct, correct_ans)
        else:
            continue

        if len(options) != 4 or correct < 0 or correct > 3:
            continue

        q_entry = {
            "category": cat_name,
            "difficulty": difficulty,
            "question": question_text,
            "options": options,
            "correct": correct,
            "explanation": explanation
        }

        existing_list.append(q_entry)
        existing_normalized.add(norm)
        added += 1

    with open(cat_file, 'w', encoding='utf-8') as f:
        json.dump(existing_list, f, ensure_ascii=False, indent=2)

    print(f"✅ [{cat_name}]: Đã nạp thành công {added} câu mới -> Tổng chuyên mục: {len(existing_list)} câu.")
    return added
