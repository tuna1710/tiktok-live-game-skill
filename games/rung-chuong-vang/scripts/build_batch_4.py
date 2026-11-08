# -*- coding: utf-8 -*-
"""
Script tạo và nạp Đợt 4 để hoàn thành chính xác CỘT MỐC 1.000 CÂU HỎI.
"""

import os
import json
import sqlite3
import re

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from batch4_van_hoc import QUESTIONS as q_van_hoc
from batch4_cong_nghe import QUESTIONS as q_cong_nghe
from batch4_rest import QUESTIONS_LICH_SU as q_lich_su, QUESTIONS_KHOA_HOC as q_khoa_hoc, QUESTIONS_DO_VUI as q_do_vui, QUESTIONS_DIA_LY as q_dia_ly

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CATEGORIES_DIR = os.path.join(DATA_DIR, 'categories')
DB_PATH = os.path.join(DATA_DIR, 'questions.db')

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r'[^\w\s]', '', t, flags=re.UNICODE)
    return ' '.join(t.split())

# Danh sách phong phú bổ sung thêm để chắc chắn vượt mốc 1.000 câu
EXTRA_QUESTIONS = {
    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu thành ngữ: 'Chị ngã em ...'?", "options": ["nâng", "đỡ", "kéo", "dắt"], "correct": 0, "explanation": "Thành ngữ ca ngợi tình cảm chị em ruột thịt yêu thương đùm bọc lẫn nhau."},
        {"difficulty": 1, "question": "Trong truyện ngụ ngôn 'Rùa và Thỏ', tại sao chú Rùa chậm chạp lại chiến thắng chú Thỏ chạy nhanh?", "options": ["Vì Thỏ chủ quan kiêu ngạo nằm ngủ quên dọc đường", "Vì Rùa chạy nhanh hơn", "Vì Thỏ bị lạc đường", "Vì có người giúp Rùa"], "correct": 0, "explanation": "Tính kiên trì, nhẫn nại và không chủ quan của Rùa đã mang lại chiến thắng vẻ vang."},
        {"difficulty": 1, "question": "Điền từ vào câu ca dao: 'Bao giờ cho đến tháng ba / Hoa gạo rụng xuống bà già cất ...'?", "options": ["chăn", "áo", "chiếu", "mền"], "correct": 0, "explanation": "'Bao giờ cho đến tháng ba / Hoa gạo rụng xuống bà già cất chăn' - thời tiết ấm áp sang hè."},
        {"difficulty": 1, "question": "Nhạc cụ gõ truyền thống bằng đồng có núm ở giữa phát ra âm thanh vang rền trong lễ hội Tây Nguyên là gì?", "options": ["Cồng chiêng", "Trống đồng", "Đàn t'rưng", "Kèn đá"], "correct": 0, "explanation": "Không gian văn hóa Cồng chiêng Tây Nguyên là kiệt tác di sản truyền khẩu phi vật thể nhân loại."},
        {"difficulty": 1, "question": "Điền từ vào câu tục ngữ: 'Lời nói chẳng mất tiền mua / Lựa lời mà nói cho ... lòng nhau'?", "options": ["vừa", "thuận", "hợp", "thấu"], "correct": 0, "explanation": "Khuyên nhủ con người cư xử văn minh, ăn nói lịch thiệp tôn trọng lẫn nhau."},
        {"difficulty": 2, "question": "Truyện ngắn 'Lão Hạc' của nhà văn Nam Cao kể về tình cảnh đau xót của người nông dân nghèo phải bán đi con chó yêu quý tên là gì?", "options": ["Cậu Vàng", "Cậu Vện", "Cậu Mực", "Cậu Đốm"], "correct": 0, "explanation": "Lão Hạc dằn vặt khóc thương sau khi bán cậu Vàng để giữ lại mảnh vườn cho con trai."},
        {"difficulty": 2, "question": "Bài thơ 'Tiểu đội xe không kính' với tinh thần lạc quan, hiên ngang của các chiến sĩ lái xe Trường Sơn là của ai?", "options": ["Phạm Tiến Duật", "Chính Hữu", "Hữu Thỉnh", "Nguyễn Duy"], "correct": 0, "explanation": "'Không có kính không phải vì xe không có kính / Bom giật bom rung kính vỡ đi rồi' - thơ Phạm Tiến Duật."},
        {"difficulty": 2, "question": "Tác phẩm văn học 'Dấu chân người lính' viết về chiến dịch Đường 9 - Khe Sanh năm 1968 là của nhà văn nào?", "options": ["Nguyễn Minh Châu", "Bảo Ninh", "Lê Lựu", "Hồ Phương"], "correct": 0, "explanation": "Nhà văn Nguyễn Minh Châu là cây bút mở đường tinh tế của văn học Việt Nam hiện đại."},
        {"difficulty": 2, "question": "Nhà thơ nào viết bài thơ 'Tre Việt Nam' ('Tre xanh xanh tự bao giờ / Chuyện ngày xưa đã có bờ tre xanh...')?", "options": ["Nguyễn Duy", "Trần Đăng Khoa", "Tế Hanh", "Huy Cận"], "correct": 0, "explanation": "Nhà thơ Nguyễn Duy tôn vinh hình ảnh cây tre dẻo dai kiên cường biểu tượng cho phẩm chất con người Việt Nam."},
        {"difficulty": 3, "question": "Ai là tác giả của tác phẩm chính luận mẫu mực 'Hịch tướng sĩ' khích lệ tinh thần yêu nước đánh giặc Nguyên Mông năm 1284?", "options": ["Hưng Đạo Đại vương Trần Quốc Tuấn", "Trần Quang Khải", "Trần Thái Tông", "Lý Thường Kiệt"], "correct": 0, "explanation": "'Ta thường tới bữa quên ăn, nửa đêm vỗ gối, ruột đau như cắt, nước mắt đầm đìa...' - áng hùng văn bất hủ của Trần Quốc Tuấn."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Hãng xe điện VinFast của Việt Nam có trụ sở nhà máy sản xuất ô tô hiện đại tại thành phố nào?", "options": ["Hải Phòng", "Hà Nội", "Đà Nẵng", "TP. Hồ Chí Minh"], "correct": 0, "explanation": "Tổ hợp nhà máy sản xuất ô tô VinFast đặt tại đảo Cát Hải, thành phố Hải Phòng."},
        {"difficulty": 1, "question": "Món chè trứ danh làm từ hạt sen tươi và long nhãn giòn ngọt thanh tao là đặc sản nức tiếng của tỉnh nào?", "options": ["Hưng Yên", "Hà Nam", "Bắc Giang", "Hải Dương"], "correct": 0, "explanation": "Chè hạt sen long nhãn Hưng Yên tiến vua nức tiếng gần xa."},
        {"difficulty": 1, "question": "Công nghệ truyền dữ liệu cự ly siêu gần chạm để thanh toán không tiếp xúc trên smartphone được viết tắt là gì?", "options": ["NFC", "GPS", "Infrared", "Wi-Fi"], "correct": 0, "explanation": "NFC (Near Field Communication) cho phép chạm điện thoại vào máy POS để thanh toán cực nhanh."},
        {"difficulty": 1, "question": "Kích thước màn hình tivi hay điện thoại thường được tính bằng đơn vị đo lường nào?", "options": ["Inch (inch)", "Centimet", "Milimet", "Pixel"], "correct": 0, "explanation": "Kích thước màn hình là độ dài đường chéo màn hình đo bằng đơn vị Inch (1 inch = 2,54 cm)."},
        {"difficulty": 2, "question": "Sân vận động Quốc gia Mỹ Đình với sức chứa hơn 40.000 chỗ ngồi nằm tại quận nào của Hà Nội?", "options": ["Quận Nam Từ Liêm", "Quận Cầu Giấy", "Quận Bắc Từ Liêm", "Quận Đống Đa"], "correct": 0, "explanation": "Sân vận động Quốc gia Mỹ Đình khánh thành năm 2003 phục vụ SEA Games 22 tại Nam Từ Liêm."},
        {"difficulty": 2, "question": "Chữ cái 'e' trong các thuật ngữ như e-commerce, e-wallet, email là viết tắt của từ tiếng Anh nào?", "options": ["Electronic (Điện tử)", "Electric", "Engine", "Express"], "correct": 0, "explanation": "Electronic nghĩa là điện tử (thương mại điện tử, ví điện tử, thư điện tử)."},
        {"difficulty": 2, "question": "Món bún chả Hà Nội vinh dự được cựu Tổng thống Mỹ Barack Obama thưởng thức cùng đầu bếp Anthony Bourdain năm nào?", "options": ["Năm 2016", "Năm 2015", "Năm 2018", "Năm 2020"], "correct": 0, "explanation": "Tháng 5/2016, Tổng thống Obama thưởng thức bún chả Hương Liên phố Lê Văn Hưu gây sốt truyền thông quốc tế."},
        {"difficulty": 3, "question": "Hệ thống cơ sở dữ liệu phi quan hệ (NoSQL) lưu trữ dữ liệu dưới dạng tài liệu JSON/BSON phổ biến nhất hiện nay là gì?", "options": ["MongoDB", "MySQL", "PostgreSQL", "SQLite"], "correct": 0, "explanation": "MongoDB là hệ quản trị cơ sở dữ liệu hướng tài liệu NoSQL được ưa chuộng cho các ứng dụng web quy mô lớn."}
    ],

    "lich-su": [
        {"difficulty": 1, "question": "Nhà nước Âu Lạc của Thục Phán An Dương Vương chọn địa danh nào làm kinh đô xây dựng thành trì?", "options": ["Thành Cổ Loa (Đông Anh, Hà Nội)", "Hoa Lư", "Bạch Hạc (Việt Trì)", "Mê Linh"], "correct": 0, "explanation": "An Dương Vương định đô ở Cổ Loa, đắp thành ốc chín vòng kiên cố chống quân Triệu Đà."},
        {"difficulty": 1, "question": "Vị nữ tướng cưỡi voi cầm gươm dẹp giặc Đông Ngô năm 248 quê ở vùng đất Triệu Sơn, Thanh Hóa là ai?", "options": ["Bà Triệu (Triệu Thị Trinh)", "Bùi Thị Xuân", "Nguyễn Thị Định", "Lê Chân"], "correct": 0, "explanation": "Bà Triệu cưỡi voi trắng đánh tan giặc Ngô với lời thề đạp luồng sóng dữ chém cá kình Biển Đông."},
        {"difficulty": 2, "question": "Cuộc chiến tranh bảo vệ biên giới Tây Nam và lật đổ chế độ diệt chủng Pol Pot diễn ra từ năm nào?", "options": ["Năm 1978 - 1979", "Năm 1975", "Năm 1985", "Năm 1989"], "correct": 0, "explanation": "Quân đội nhân dân Việt Nam phối hợp quân cách mạng Campuchia giải phóng Phnom Penh ngày 7/1/1979."},
        {"difficulty": 2, "question": "Chiếc xe tăng T-54 mang số hiệu bao nhiêu do Trung úy Bùi Quang Thận chỉ huy đã húc đổ cổng chính Dinh Độc Lập ngày 30/4/1975?", "options": ["Xe tăng số hiệu 390 và 843", "Xe tăng 990", "Xe tăng 555", "Xe tăng 123"], "correct": 0, "explanation": "Xe tăng 843 tiến vào cổng phụ và xe tăng 390 húc tung cổng chính Dinh Độc Lập trưa ngày 30/4/1975."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Vị vua nào của triều Lý đã cho lập đàn Xã Tắc tại Thăng Long năm 1048 để tế thần Đất và thần Lúa cầu quốc thái dân an?", "options": ["Lý Thái Tông", "Lý Thái Tổ", "Lý Thánh Tông", "Lý Cao Tông"], "correct": 0, "explanation": "Vua Lý Thái Tông lập đàn Xã Tắc thể hiện truyền thống nông nghiệp trọng cội nguồn của người Việt."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Khí nào cần thiết nhất duy trì sự sống và quá trình hô hấp của con người và muôn loài?", "options": ["Khí Oxy (O2)", "Khí Cacbonic (CO2)", "Khí Nitơ (N2)", "Khí Metan"], "correct": 0, "explanation": "Oxy nuôi dưỡng các tế bào và thực hiện các phản ứng oxy hóa sinh học giải phóng năng lượng cho cơ thể."},
        {"difficulty": 1, "question": "Chất rắn nào đông cứng từ nước ở nhiệt độ dưới 0 độ C được thả vào nước ngọt cho mát?", "options": ["Băng đá (Nước đá)", "Muối ăn", "Đường kính", "Thạch cao"], "correct": 0, "explanation": "Nước đá tan chảy ở 0 °C hấp thụ nhiệt giúp làm mát đồ uống tức thì."},
        {"difficulty": 2, "question": "Hiện tượng cầu vồng bảy sắc lung linh sau cơn mưa gồm 7 dải màu cơ bản lần lượt từ ngoài vào trong là gì?", "options": ["Đỏ, Da cam, Vàng, Lục, Lam, Chàm, Tím", "Tím, Chàm, Lam, Lục, Vàng, Cam, Đỏ", "Đỏ, Vàng, Xanh, Trắng, Đen, Tím, Nâu", "Xanh, Đỏ, Tím, Vàng, Cam, Hồng, Nâu"], "correct": 0, "explanation": "Hiện tượng tán sắc ánh sáng mặt trời qua các giọt nước mưa tạo nên dải quang phổ 7 màu rực rỡ."},
        {"difficulty": 2, "question": "Lớp vỏ Trái Đất dày trung bình từ bao nhiêu km dưới các đại dương và lục địa?", "options": ["Khoảng 5 - 70 km", "Khoảng 500 km", "Khoảng 1.000 km", "Khoảng 100 mét"], "correct": 0, "explanation": "Lớp vỏ thạch quyển Trái Đất mỏng manh như vỏ quả táo, dày từ 5-10 km ở đại dương đến 30-70 km ở lục địa."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Vận tốc âm thanh truyền trong không khí khô ở nhiệt độ 20 độ C xấp xỉ bằng bao nhiêu?", "options": ["Khoảng 343 mét/giây (khoảng 1.235 km/h)", "Khoảng 300.000 km/s", "Khoảng 100 m/s", "Khoảng 1.500 m/s"], "correct": 0, "explanation": "Vận tốc âm thanh trong không khí là 343 m/s; khi máy bay vượt tốc độ này sẽ tạo ra tiếng nổ siêu thanh (Sonic boom)."}
    ],

    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Bánh gì đi lại trên đường / Chở bao nhiêu khách phố phường đông vui?", "options": ["Bánh xe", "Bánh mì", "Bánh bao", "Bánh giầy"], "correct": 0, "explanation": "Bánh xe lăn tròn trên đường giúp ô tô xe máy chở người đi lại khắp nơi."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có cánh nhưng không biết bay, đứng yên một chỗ phả gió mát khắp phòng?", "options": ["Cây quạt máy", "Cái diều", "Máy bay", "Con chim cánh cụt"], "correct": 0, "explanation": "Cánh quạt máy quay tít tạo ra làn gió mát mẻ xua tan oi bức."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt có 4 chữ cái, bỏ dấu thành tên một loài cá nước ngọt, thêm sắc thành thứ ai cũng thích có trong ví?", "options": ["Chữ 'Tiền' (Tiên - Tiền)", "Chữ 'Vàng'", "Chữ 'Bạc'", "Chữ 'Đô'"], "correct": 0, "explanation": "Tiên cá, Tiền bạc trong ví."},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: 'Bốn chân đạp đất, hai sừng chỉ thiên, cày sâu cuốc bẫm làm nên mùa màng' là con vật thân thương nào của đồng quê Việt?", "options": ["Con trâu", "Con bò", "Con ngựa", "Con hươu"], "correct": 0, "explanation": "'Con trâu là đầu cơ nghiệp' - hình ảnh con trâu cần mẫn gắn liền với nền văn minh lúa nước ngàn đời."}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Cột cờ Hà Nội (Kỳ đài Hà Nội) công trình kiến trúc thời Nguyễn được bảo tồn nguyên vẹn nằm trên đường phố nào?", "options": ["Đường Điện Biên Phủ", "Đường Hoàng Diệu", "Đường Hùng Vương", "Đường Độc Lập"], "correct": 0, "explanation": "Kỳ đài Hà Nội xây năm 1812 nằm trong khuôn viên Bảo tàng Lịch sử Quân sự Việt Nam."},
        {"difficulty": 2, "question": "Tỉnh nào ở miền Bắc nước ta nổi tiếng với hồ Thác Bà và vùng bưởi ngọt Đại Minh?", "options": ["Yên Bái", "Tuyên Quang", "Phú Thọ", "Lào Cai"], "correct": 0, "explanation": "Hồ thủy điện Thác Bà với hơn 1.300 hòn đảo lớn nhỏ nằm tại tỉnh Yên Bái."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Đỉnh núi lửa cao nhất châu Phi tuyết phủ quanh năm giữa xích đạo (cao 5.895 mét) là đỉnh núi nào?", "options": ["Đỉnh Kilimanjaro (Tanzania)", "Đỉnh Kenya", "Đỉnh Atlas", "Đỉnh Elgon"], "correct": 0, "explanation": "Núi Kilimanjaro là ngọn núi đứng tự do cao nhất thế giới tại Tanzania."}
    ]
}

BATCH_4_MERGED = {
    "van-hoc-nghe-thuat": q_van_hoc + EXTRA_QUESTIONS["van-hoc-nghe-thuat"],
    "doi-song-cong-nghe": q_cong_nghe + EXTRA_QUESTIONS["doi-song-cong-nghe"],
    "lich-su": q_lich_su + EXTRA_QUESTIONS["lich-su"],
    "khoa-hoc-tu-nhien": q_khoa_hoc + EXTRA_QUESTIONS["khoa-hoc-tu-nhien"],
    "do-vui-tri-tue": q_do_vui + EXTRA_QUESTIONS["do-vui-tri-tue"],
    "dia-ly": q_dia_ly + EXTRA_QUESTIONS["dia-ly"]
}

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU NẠP ĐỢT 4 ĐỂ HOÀN THÀNH CHÍNH THỨC 1.000 CÂU HỎI!")
    print("=" * 70)

    total_added = 0

    for cat_name, questions in BATCH_4_MERGED.items():
        cat_file = os.path.join(CATEGORIES_DIR, f"{cat_name}.json")
        existing_list = []
        if os.path.exists(cat_file):
            try:
                with open(cat_file, 'r', encoding='utf-8') as f:
                    existing_list = json.load(f)
            except Exception as e:
                print(f"Lỗi đọc {cat_name}.json: {e}")

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

        print(f"  📁 [{cat_name}]: Nạp thêm {added_in_cat} câu -> Tổng danh mục: {len(existing_list)} câu.")

    print("\n" + "=" * 70)
    print(f"✅ Đợt 4 hoàn tất: Bổ sung thành công {total_added} câu hỏi mới!")
    print("=" * 70)

if __name__ == '__main__':
    main()
