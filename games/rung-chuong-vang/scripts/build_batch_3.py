# -*- coding: utf-8 -*-
"""
Script chạy Đợt 3: Nạp câu hỏi mới vào ngân hàng câu hỏi Rung Chuông Vàng
Tự động chuẩn hóa, kiểm tra trùng lặp và đồng bộ SQLite.
"""

import os
import json
import sqlite3
import re

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from batch3_dia_ly import QUESTIONS as q_dia_ly
from batch3_do_vui import QUESTIONS as q_do_vui
from batch3_khoa_hoc import QUESTIONS as q_khoa_hoc
from batch3_lich_su import QUESTIONS as q_lich_su
from batch3_van_hoc import QUESTIONS as q_van_hoc
from batch3_cong_nghe import QUESTIONS as q_cong_nghe

from expand_batch_3 import MORE_LICH_SU, MORE_VAN_HOC, MORE_CONG_NGHE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CATEGORIES_DIR = os.path.join(DATA_DIR, 'categories')

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r'[^\w\s]', '', t, flags=re.UNICODE)
    return ' '.join(t.split())

BATCH_3_DATA = {
    "dia-ly": q_dia_ly,
    "do-vui-tri-tue": q_do_vui,
    "khoa-hoc-tu-nhien": q_khoa_hoc,
    "lich-su": q_lich_su + MORE_LICH_SU,
    "van-hoc-nghe-thuat": q_van_hoc + MORE_VAN_HOC,
    "doi-song-cong-nghe": q_cong_nghe + MORE_CONG_NGHE
}

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU NẠP ĐỢT 3 VÀO NGÂN HÀNG CÂU HỎI RUNG CHUÔNG VÀNG")
    print("=" * 70)

    total_added = 0

    for cat_name, questions in BATCH_3_DATA.items():
        cat_file = os.path.join(CATEGORIES_DIR, f"{cat_name}.json")
        existing_list = []
        if os.path.exists(cat_file):
            try:
                with open(cat_file, 'r', encoding='utf-8') as f:
                    existing_list = json.load(f)
            except Exception as e:
                print(f"Lỗi đọc file {cat_name}.json: {e}")

        existing_normalized = set()
        for item in existing_list:
            existing_normalized.add(normalize_text(item.get('question', '')))

        added_in_cat = 0
        for q in questions:
            norm = normalize_text(q['question'])
            if norm not in existing_normalized:
                existing_normalized.add(norm)
                q_entry = {
                    "category": cat_name,
                    "difficulty": q["difficulty"],
                    "question": q["question"],
                    "options": q["options"],
                    "correct": q["correct"],
                    "explanation": q["explanation"]
                }
                existing_list.append(q_entry)
                added_in_cat += 1
                total_added += 1

        with open(cat_file, 'w', encoding='utf-8') as f:
            json.dump(existing_list, f, ensure_ascii=False, indent=2)

        print(f"  📁 [{cat_name}]: Đã nạp thêm {added_in_cat} câu -> Tổng danh mục: {len(existing_list)} câu.")

    print("\n" + "=" * 70)
    print(f"✅ Đợt 3 hoàn tất: Đã bổ sung thành công {total_added} câu hỏi mới!")
    print("=" * 70)

if __name__ == '__main__':
    main()
