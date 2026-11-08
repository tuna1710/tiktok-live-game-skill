# -*- coding: utf-8 -*-
"""
Chính thức đưa ngân hàng câu hỏi vượt qua 1.000 CÂU HỎI (30 câu cuối cùng).
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES_DIR = os.path.join(BASE_DIR, 'data', 'categories')

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r'[^\w\s]', '', t, flags=re.UNICODE)
    return ' '.join(t.split())

DATA_30 = {
    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Bánh gì không nướng, không chiên, mà trẻ em nào cũng thích thổi bong bóng?", "options": ["Kẹo cao su (Kẹo sing-gum)", "Bánh rán", "Bánh nếp", "Bánh quy"], "correct": 0, "explanation": "Kẹo cao su thổi thành những quả bong bóng tròn xoe vui mắt."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có lưng nhưng không có bụng, dùng để dựa mỗi khi mỏi lưng?", "options": ["Lưng ghế tựa", "Chiếc giường", "Cái gối", "Bức tường"], "correct": 0, "explanation": "Chiếc ghế có phần lưng tựa êm ái."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt có 3 chữ cái, thêm dấu huyền thành thứ để soi rọi, thêm dấu sắc thành thứ để uống nước?", "options": ["Đèn và Chén (Đen - Đèn - Đén)", "Ly", "Cốc", "Bát"], "correct": 0, "explanation": "Cây đèn thắp sáng ban đêm và chén trà thơm."},
        {"difficulty": 2, "question": "Đố mẹo: Có một người phụ nữ lái xe máy đi ngược chiều trên đường một chiều nhưng cảnh sát giao thông không xử phạt. Tại sao?", "options": ["Vì người phụ nữ đó đang đi bộ dắt xe trên vỉa hè", "Cảnh sát không nhìn thấy", "Người quen cảnh sát", "Đường vắng"], "correct": 0, "explanation": "Người đi bộ dắt xe trên vỉa hè không vi phạm luật giao thông đường bộ."},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: Bức tranh đố mẹo dân gian: 'Tròn vành vạnh như đĩa xôi, chiếu sáng muôn nơi, vầng trăng rằm tháng Tám' là dịp tết nào?", "options": ["Tết Trung Thu", "Tết Nguyên Đán", "Tết Hàn Thực", "Tết Đoan Ngọ"], "correct": 0, "explanation": "Tết Trung Thu rằm tháng Tám ngắm trăng tròn, phá cỗ rước đèn lồng."}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Vịnh Cam Ranh vịnh nước sâu kín gió chiến lược quân sự hàng đầu thế giới thuộc tỉnh nào?", "options": ["Khánh Hòa", "Bình Thuận", "Ninh Thuận", "Phú Yên"], "correct": 0, "explanation": "Vịnh Cam Ranh là cảng nước sâu tự nhiên kín gió lý tưởng của thế giới."},
        {"difficulty": 1, "question": "Tỉnh nào ở miền Bắc nước ta có danh thắng Chùa Ba Vàng và di tích Yên Tử linh thiêng?", "options": ["Quảng Ninh (TP. Uông Bí)", "Hải Dương", "Bắc Giang", "Hải Phòng"], "correct": 0, "explanation": "Thành phố Uông Bí (Quảng Ninh) là cái nôi thiền phái Trúc Lâm Yên Tử."},
        {"difficulty": 2, "question": "Hồ Lak hồ nước ngọt tự nhiên lớn thứ nhì Việt Nam (sau hồ Ba Bể) thuộc huyện nào tỉnh Đắk Lắk?", "options": ["Huyện Lắk", "Huyện Krông Pắc", "Huyện Cư M'gar", "Huyện Buôn Đôn"], "correct": 0, "explanation": "Hồ Lắk thơ mộng gắn liền với truyền thuyết của người M'Nông và biệt điện vua Bảo Đại."},
        {"difficulty": 2, "question": "Cù Lao Chàm khu dự trữ sinh quyển thế giới với những rạn san hô tuyệt đẹp cách bờ biển Cửa Đại (Hội An) bao nhiêu hải lý?", "options": ["Khoảng 8 - 10 hải lý", "Khoảng 50 hải lý", "Khoảng 1 hải lý", "Khoảng 100 hải lý"], "correct": 0, "explanation": "Cù Lao Chàm gồm 8 hòn đảo nhỏ tuyệt đẹp thuộc thành phố Hội An, Quảng Nam."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Dãy núi Bạch Mã là ranh giới khí hậu tự nhiên phân chia giữa vùng khí hậu nhiệt đới gió mùa có mùa đông lạnh ở phía Bắc và vùng khí hậu nào ở phía Nam?", "options": ["Vùng khí hậu nhiệt đới gió mùa cận xích đạo nóng quanh năm", "Vùng khí hậu ôn đới", "Vùng khí hậu khô hạn", "Vùng khí hậu cận cực"], "correct": 0, "explanation": "Dãy Bạch Mã ngăn cản gió mùa Đông Bắc tràn sâu vào phương Nam, tạo ranh giới khí hậu rõ rệt."}
    ],

    "lich-su": [
        {"difficulty": 1, "question": "Vị hoàng đế nào của nhà Trần đã lãnh đạo nhân dân giành thắng lợi vang dội trong cuộc kháng chiến chống quân Nguyên Mông lần thứ nhất năm 1258?", "options": ["Trần Thái Tông (Trần Cảnh)", "Trần Thánh Tông", "Trần Nhân Tông", "Trần Anh Tông"], "correct": 0, "explanation": "Vua Trần Thái Tông cùng Thái sư Trần Thủ Độ chỉ huy trận Đông Bộ Đầu quét sạch quân Mông Cổ."},
        {"difficulty": 1, "question": "Đại hội Đại biểu toàn quốc lần thứ III của Đảng Cộng sản Việt Nam (năm 1960) đã bầu ai làm Tổng Bí thư?", "options": ["Đồng chí Lê Duẩn", "Đồng chí Trường Chinh", "Đồng chí Nguyễn Văn Linh", "Đồng chí Đỗ Mười"], "correct": 0, "explanation": "Đồng chí Lê Duẩn giữ trọng trách Tổng Bí thư lãnh đạo kháng chiến chống Mỹ cứu nước thắng lợi."},
        {"difficulty": 2, "question": "Vị trạng nguyên nào nổi tiếng với giai thoại 'Trạng Quỳnh' dùng sự hóm hỉnh trào phúng để châm biếm bọn quan lại phong kiến?", "options": ["Nguyễn Quỳnh (Trạng Quỳnh)", "Nguyễn Hiền", "Lương Thế Vinh", "Lê Quý Đôn"], "correct": 0, "explanation": "Trạng Quỳnh là nhân vật văn học dân gian biểu trưng cho trí tuệ thông minh và tinh thần phản kháng của nhân dân."},
        {"difficulty": 2, "question": "Chiến thắng Việt Bắc Thu - Đông năm 1947 đã đập tan hoàn toàn chiến lược quân sự nào của thực dân Pháp?", "options": ["Chiến lược 'Đánh nhanh thắng nhanh'", "Chiến lược 'Chiến tranh đặc biệt'", "Chiến lược 'Chiến tranh cục bộ'", "Chiến lược 'Việt Nam hóa chiến tranh'"], "correct": 0, "explanation": "Thực dân Pháp thất bại thảm hại ở sông Lô, đèo Bông Lau buộc phải chuyển sang đánh lâu dài."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Bộ quốc sử đầu tiên của nước Đại Việt do nhà sử học Lê Văn Hưu biên soạn vào năm 1272 dưới thời Trần có tên là gì?", "options": ["Đại Việt sử ký", "Đại Việt sử ký toàn thư", "Khâm định Việt sử thông giám cương mục", "Việt sử tiêu án"], "correct": 0, "explanation": "Bảng nhãn Lê Văn Hưu hoàn thành 30 quyển 'Đại Việt sử ký' đặt nền móng vững chắc cho nền sử học nước nhà."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Bộ phận nào của quả trứng gia cầm chứa nhiều protein và khoáng chất bảo vệ phôi thai?", "options": ["Lòng trắng và Lòng đỏ", "Vỏ trứng canxi", "Màng vỏ", "Buồng khí"], "correct": 0, "explanation": "Lòng đỏ giàu lipid và vitamin, lòng trắng giàu albumin cung cấp dinh dưỡng trọn vẹn."},
        {"difficulty": 1, "question": "Loài côn trùng nào có khả năng bay phát ra ánh sáng lung linh lập lòe trong đêm tối mùa hè?", "options": ["Con đom đóm", "Con ve sầu", "Con bướm đêm", "Con muỗi"], "correct": 0, "explanation": "Phản ứng sinh học giữa enzym luciferase và phân tử luciferin tạo ra ánh sáng lạnh kỳ diệu."},
        {"difficulty": 2, "question": "Quá trình thoát hơi nước qua khí khổng ở lá cây có vai trò sinh lý quan trọng nào?", "options": ["Tạo lực hút kéo dòng nước và muối khoáng từ rễ lên và hạ nhiệt độ cho lá", "Làm héo lá", "Thải độc tố", "Hấp thụ oxy"], "correct": 0, "explanation": "Thoát hơi nước là động lực đầu trên hút dòng nhựa nguyên từ rễ lên nuôi cây."},
        {"difficulty": 2, "question": "Trong vật lý, âm thanh không thể truyền được qua môi trường nào sau đây?", "options": ["Môi trường chân không", "Môi trường chất lỏng (nước)", "Môi trường chất rắn (thép)", "Môi trường chất khí (không khí)"], "correct": 0, "explanation": "Âm thanh là sóng cơ học đòi hỏi môi trường vật chất có hạt phân tử để lan truyền dao động."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Bán kính trung bình của Trái Đất (tính từ tâm Trái Đất ra xích đạo) xấp xỉ bằng bao nhiêu km?", "options": ["Khoảng 6.371 km", "Khoảng 10.000 km", "Khoảng 1.000 km", "Khoảng 3.000 km"], "correct": 0, "explanation": "Bán kính Trái Đất khoảng 6.371 km, chu vi đường xích đạo khoảng 40.075 km."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Món lẩu riêu cua đồng thanh mát thơm mùi giấm bỗng thường được ăn kèm loại rau ghém nào?", "options": ["Hoa chuối thái mỏng, rau muống chẻ, tía tô", "Rau bina", "Cải xoong luộc", "Rau mồng tơi"], "correct": 0, "explanation": "Vị chua thanh của giấm bỗng hòa quyện với vị béo ngậy của gạch cua và rau sống giòn ngọt."},
        {"difficulty": 1, "question": "Đơn vị đo dung lượng dữ liệu bộ nhớ máy tính gồm 1 Gigabyte (1GB) tương đương với bao nhiêu Megabyte (MB)?", "options": ["1.024 MB", "1.000 MB", "100 MB", "512 MB"], "correct": 0, "explanation": "Trong hệ nhị phân (hệ đếm cơ số 2), 1 GB = 2^10 MB = 1.024 MB."},
        {"difficulty": 2, "question": "Kỳ đại hội Thể thao Đông Nam Á (SEA Games 31) lần thứ hai được tổ chức thành công rực rỡ tại Việt Nam vào năm nào?", "options": ["Năm 2022 (tại Hà Nội)", "Năm 2019", "Năm 2021", "Năm 2023"], "correct": 0, "explanation": "SEA Games 31 diễn ra vào tháng 5/2022 tại Hà Nội và 11 tỉnh lân cận, đoàn Việt Nam đứng nhất toàn đoàn."},
        {"difficulty": 2, "question": "Thiết bị chuyển đổi tín hiệu quang sang tín hiệu điện internet lắp đặt trong mỗi hộ gia đình được gọi là gì?", "options": ["Modem quang (ONT)", "Switch chia mạng", "Card mạng LAN", "Hub"], "correct": 0, "explanation": "Modem quang chuyển đổi xung ánh sáng trên sợi cáp quang thành tín hiệu số Ethernet cho router phát Wi-Fi."},
        {"difficulty": 3, "question": "CÂU HỎI CÔNG NGHỆ QUYẾT ĐỊNH: Hệ điều hành nhân Linux (Linux Kernel) mã nguồn mở thống trị máy chủ và smartphone (Android) do kỹ sư người Phần Lan nào sáng lập năm 1991?", "options": ["Linus Torvalds", "Richard Stallman", "Dennis Ritchie", "Ken Thompson"], "correct": 0, "explanation": "Linus Torvalds phát hành phiên bản hạt nhân Linux 0.01 năm 1991, đặt nền tảng cho cuộc cách mạng phần mềm nguồn mở thế giới."}
    ],

    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu tục ngữ: 'Đi một ngày đàng, học một ... khôn'?", "options": ["sàng", "gánh", "bồ", "thúng"], "correct": 0, "explanation": "Khuyên con người nên chịu khó đi ra ngoài trải nghiệm để mở rộng tầm hiểu biết tri thức."},
        {"difficulty": 1, "question": "Trong truyện 'Sự tích trầu cau', ba nhân vật chính sau khi chết đã biến thành những vật gì tượng trưng cho tình nghĩa thủy chung gắn bó?", "options": ["Cây cau, cây trầu không và tảng đá vôi", "Cây đa, giếng nước, sân đình", "Cây bàng, cây phượng", "Ba đóa hoa sen"], "correct": 0, "explanation": "Khi hòa quyện trầu, cau và vôi tạo nên màu đỏ son thắm đượm tình nghĩa anh em, vợ chồng son sắt."},
        {"difficulty": 2, "question": "Bài thơ 'Mẹ và quả' với câu thơ xúc động 'Và chúng tôi, một thứ quả trên đời / Bảy mươi tuổi mẹ đợi chờ được hái' là của nhà thơ nào?", "options": ["Nguyễn Khoa Điềm", "Nguyễn Duy", "Hữu Thỉnh", "Trần Đăng Khoa"], "correct": 0, "explanation": "Nhà thơ Nguyễn Khoa Điềm viết về sự hy sinh thầm lặng của người mẹ nuôi con khôn lớn."},
        {"difficulty": 2, "question": "Làng tranh khắc gỗ dân gian Hàng Trống nổi tiếng đất kinh kỳ Thăng Long với bức tranh tứ bình nào tiêu biểu?", "options": ["Bộ tranh Tứ bình: Tố nữ, Tứ quý (Tùng - Cúc - Trúc - Mai)", "Tranh Gà lợn", "Tranh Đám cưới chuột", "Tranh Đánh ghen"], "correct": 0, "explanation": "Tranh Hàng Trống tinh tế với kỹ thuật vờn màu nước điêu luyện và nét khắc mảnh mai tao nhã."},
        {"difficulty": 3, "question": "CÂU HỎI VĂN HỌC QUYẾT ĐỊNH: Tác phẩm thơ trào phúng 'Vịnh khoa thi Hương' với câu thơ chua chát: 'Lọng cắm rợp trời quan sứ đến / Váy lê quét đất mụ đầm ra' là kiệt tác của nhà thơ nào?", "options": ["Tú Xương (Trần Tế Xương)", "Nguyễn Khuyến", "Ba Giai - Tú Xuất", "Hồ Xuân Hương"], "correct": 0, "explanation": "Nhà thơ Tú Xương xót xa trước cảnh khoa cử Nho học suy đồi thời thực dân nửa phong kiến ở trường thi Nam Định năm Đinh Dậu 1897."}
    ]
}

def main():
    total_added = 0
    for cat_name, questions in DATA_30.items():
        cat_file = os.path.join(CATEGORIES_DIR, f"{cat_name}.json")
        existing_list = []
        if os.path.exists(cat_file):
            try:
                with open(cat_file, 'r', encoding='utf-8') as f:
                    existing_list = json.load(f)
            except Exception as e:
                pass

        existing_normalized = set()
        for item in existing_list:
            existing_normalized.add(normalize_text(item.get('question', '')))

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
                total_added += 1

        with open(cat_file, 'w', encoding='utf-8') as f:
            json.dump(existing_list, f, ensure_ascii=False, indent=2)

    print(f"✅ Bổ sung thêm {total_added} câu hỏi.")

if __name__ == '__main__':
    main()
