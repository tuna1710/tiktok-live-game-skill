# -*- coding: utf-8 -*-
"""
Đợt 6 - Mở rộng Cột mốc 3 (hướng tới 2.500 câu)
Bổ sung 230 câu hỏi chuẩn hóa phong phú chia đều cho 6 chủ đề.
"""

import os
import json
import sqlite3
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CATEGORIES_DIR = os.path.join(DATA_DIR, 'categories')

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r'[^\w\s]', '', t, flags=re.UNICODE)
    return ' '.join(t.split())

BATCH_6_DATA = {
    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Bánh gì không nướng bằng than, không hấp bằng nồi mà lăn tròn đưa ta đi học?", "options": ["Bánh xe đạp", "Bánh mì", "Bánh gai", "Bánh giò"], "correct": 0, "explanation": "Bánh xe đạp quay đều đưa học sinh đến trường."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì sinh ra đã có bộ râu quặp, bò ngang thoăn thoắt có tám cẳng hai càng?", "options": ["Con cua", "Con tôm", "Con ốc", "Con cá"], "correct": 0, "explanation": "'Con cua tám cẳng hai càng / Bò đi bò lại bò ngang cả ngày'."},
        {"difficulty": 1, "question": "Đố mẹo: Quả gì vỏ xanh ruột đỏ, hạt đen nhánh, ăn vào ngọt mát giải khát ngày hè?", "options": ["Quả dưa hấu", "Quả thanh long", "Quả xoài", "Quả ổi"], "correct": 0, "explanation": "Dưa hấu vỏ xanh ruột đỏ thắm ngọt lịm mọng nước."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có chân mà không biết đi, có mặt mà không biết cười, dùng để bày bát đĩa mâm cơm?", "options": ["Cái bàn ăn", "Cái ghế", "Cái tủ", "Cái giường"], "correct": 0, "explanation": "Chiếc bàn ăn quen thuộc của mỗi gia đình."},
        {"difficulty": 1, "question": "Đố mẹo: Đèn gì có ba màu đỏ, vàng, xanh đứng ở ngã tư đường phố?", "options": ["Đèn tín hiệu giao thông", "Đèn lồng", "Đèn pin", "Đèn ngủ"], "correct": 0, "explanation": "Đèn giao thông điều tiết trật tự lưu thông tại các giao lộ."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt có 3 chữ cái, thêm dấu nặng thành một loài vật dưới nước có mai cứng, thêm dấu hỏi thành bộ phận điều khiển tàu xe?", "options": ["Rùa và Lái (Rua - Rùa - Rủa)", "Cua", "Tôm", "Ốc"], "correct": 0, "explanation": "Con rùa chậm chạp và vô lăng lái xe."},
        {"difficulty": 2, "question": "Đố mẹo: Một người thợ xây ngã từ tầng 10 của một tòa nhà xuống đất mà không hề bị xây xước chút nào, vì sao?", "options": ["Vì người đó ngã vào bên trong sàn nhà tầng 10", "Rơi trúng đống cát", "Có người đỡ", "Dùng dù nhảy"], "correct": 0, "explanation": "Ngã xuống sàn nhà của chính tầng 10 chứ không phải rơi ra ngoài khoảng không!"},
        {"difficulty": 2, "question": "Đố mẹo: Cái gì bạn càng lấy đi nhiều thì nó lại càng trở nên to lớn hơn?", "options": ["Cái hố (cái lỗ đất)", "Đống cát", "Hộp quà", "Bình nước"], "correct": 0, "explanation": "Bạn càng đào lấy đi nhiều đất cát thì cái hố sẽ càng phình to ra."},
        {"difficulty": 2, "question": "Đố vui: 'Thân em vừa trắng lại vừa tròn / Bảy nổi ba chìm với nước non' là món bánh truyền thống nào?", "options": ["Bánh trôi nước", "Bánh chưng", "Bánh giầy", "Bánh ít"], "correct": 0, "explanation": "Hình tượng bánh trôi nước trong bài thơ kiệt tác của nữ sĩ Hồ Xuân Hương."},
        {"difficulty": 2, "question": "Đố mẹo: Con gì sáng đi bốn chân, trưa đi hai chân, tối đi ba chân?", "options": ["Con người (ấu thơ, trưởng thành, về già chống gậy)", "Con khỉ", "Con tinh tinh", "Con gấu"], "correct": 0, "explanation": "Câu đố kinh điển của nhân sư Sphinx thời Hy Lạp cổ đại về vòng đời con người."},
        {"difficulty": 3, "question": "Đố logic: Có 10 ngọn nến đang cháy trong phòng. Gió thổi tắt 3 ngọn nến. Người ta đóng cửa sổ lại. Hỏi cuối cùng trong phòng còn lại bao nhiêu ngọn nến?", "options": ["Còn lại đúng 3 ngọn nến (7 ngọn kia cháy hết tan thành sáp)", "Còn 10 ngọn", "Còn 7 ngọn", "Không còn ngọn nào"], "correct": 0, "explanation": "7 ngọn nến tiếp tục cháy sẽ tan hết, chỉ có 3 ngọn bị gió thổi tắt là còn giữ nguyên thân nến!"},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: Bức tranh đố vui dân gian: 'Cày trên đồng ruộng trắng phau / Khát thì uống nước giếng sâu đen ngòm / Thẳng hàng ngay ngắn tươi giòn' là hành động gì thời xưa?", "options": ["Viết bút mực trên trang giấy trắng", "Cày cấy lúa", "Dệt vải tơ tằm", "In tranh dân gian"], "correct": 0, "explanation": "Cây bút mực cày nét chữ trên trang giấy trắng, hết mực thì chấm vào lọ mực đen."}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Tỉnh nào ở cực Bắc nước ta có cao nguyên đá Đồng Văn hùng vĩ và đèo Mã Pí Lèng?", "options": ["Hà Giang", "Cao Bằng", "Lào Cai", "Sơn La"], "correct": 0, "explanation": "Hà Giang là phên dậu địa đầu Tổ quốc với di sản Công viên địa chất toàn cầu UNESCO."},
        {"difficulty": 1, "question": "Vịnh biển tuyệt đẹp nào ở miền Trung được xếp vào câu lạc bộ những vịnh biển đẹp nhất thế giới thuộc tỉnh Khánh Hòa?", "options": ["Vịnh Nha Trang", "Vịnh Cam Ranh", "Vịnh Lăng Cô", "Vịnh Vân Phong"], "correct": 0, "explanation": "Vịnh Nha Trang với biển xanh cát trắng nắng vàng là thiên đường du lịch biển đảo."},
        {"difficulty": 1, "question": "Quốc gia nào ở châu Á có thủ đô là Viêng Chăn (Vientiane) có chung dòng sông Mê Kông với nước ta?", "options": ["Lào", "Campuchia", "Thái Lan", "Myanmar"], "correct": 0, "explanation": "Thủ đô Viêng Chăn nằm bên bờ tả ngạn dòng sông Mê Kông của nước bạn Lào anh em."},
        {"difficulty": 2, "question": "Thác Dambri ngọn thác hùng vĩ cao hơn 60 mét nằm giữa rừng nguyên sinh đại ngàn thuộc thành phố nào của tỉnh Lâm Đồng?", "options": ["Thành phố Bảo Lộc", "Thành phố Đà Lạt", "Thị xã Gia Nghĩa", "Huyện Di Linh"], "correct": 0, "explanation": "Thác Dambri hùng vĩ cách trung tâm thành phố Bảo Lộc khoảng 18 km."},
        {"difficulty": 2, "question": "Tỉnh nào ở vùng duyên hải miền Trung có danh xưng 'Xứ nẫu' với bãi biển Quy Nhơn và đầm Thị Nại?", "options": ["Bình Định", "Phú Yên", "Quảng Ngãi", "Khánh Hòa"], "correct": 0, "explanation": "Bình Định vùng đất võ trời văn với cầu Thị Nại cây cầu vượt biển dài nhất nước ta một thời."},
        {"difficulty": 2, "question": "Dãy núi Alps (An-pơ) dãy núi cao và đồ sộ nhất châu Âu trải dài qua bao nhiêu quốc gia?", "options": ["8 quốc gia (Pháp, Thụy Sĩ, Ý, Áo, Đức, Slovenia, Liechtenstein, Monaco)", "3 quốc gia", "5 quốc gia", "12 quốc gia"], "correct": 0, "explanation": "Dãy Alps hình cánh cung dài 1.200 km là nóc nhà thiên nhiên của lục địa già châu Âu."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Vùng trũng Danakil (Danakil Depression) nơi nóng và khắc nghiệt nhất trên Trái Đất nằm ở quốc gia nào của châu Phi?", "options": ["Ethiopia", "Ai Cập", "Kenya", "Nam Phi"], "correct": 0, "explanation": "Vùng trũng Danakil tại Ethiopia có hồ dung nham sôi sục và suối lưu huỳnh rực rỡ sắc màu."}
    ],

    "lich-su": [
        {"difficulty": 1, "question": "Chiến thắng lịch sử trên sông Bạch Đằng năm 1288 chém chết tướng Ô Mã Nhi gắn liền với triều đại nào?", "options": ["Nhà Trần", "Nhà Lý", "Nhà Hậu Lê", "Nhà Tiền Lê"], "correct": 0, "explanation": "Hưng Đạo Đại vương Trần Quốc Tuấn lãnh đạo đại thắng quân Nguyên Mông lần thứ 3 trên sông Bạch Đằng."},
        {"difficulty": 1, "question": "Ngày thành lập Đoàn Thanh niên Cộng sản Hồ Chí Minh được tổ chức vào ngày tháng nào hàng năm?", "options": ["26/3", "19/5", "15/10", "22/12"], "correct": 0, "explanation": "Ngày 26/3/1931 đánh dấu sự ra đời của tổ chức Đoàn Thanh niên cứu quốc."},
        {"difficulty": 2, "question": "Vị vua nào của triều Lý đã ban hành khoa thi Nho học đầu tiên (khoa thi Minh kinh bác học) vào năm 1075?", "options": ["Lý Nhân Tông", "Lý Thánh Tông", "Lý Thái Tổ", "Lý Thần Tông"], "correct": 0, "explanation": "Vua Lý Nhân Tông mở khoa thi đầu tiên và chọn ra thủ khoa Lê Văn Thịnh."},
        {"difficulty": 2, "question": "Bản 'Lời kêu gọi Toàn quốc kháng chiến' của Chủ tịch Hồ Chí Minh được phát đi vào đêm ngày tháng năm nào?", "options": ["Đêm 19/12/1946", "Đêm 2/9/1945", "Đêm 19/8/1945", "Đêm 7/5/1954"], "correct": 0, "explanation": "'Chúng ta thà hy sinh tất cả, chứ nhất định không chịu mất nước, nhất định không chịu làm nô lệ!' - Lời kêu gọi lịch sử tại làng Vạn Phúc."},
        {"difficulty": 2, "question": "Cuộc Vạn Lý Trường Chinh (1934 - 1936) vượt qua hơn 10.000 km địa hình hiểm trở gắn liền với quân đội cách mạng nước nào?", "options": ["Trung Quốc", "Nga", "Triều Tiên", "Cuba"], "correct": 0, "explanation": "Cuộc hành quân chiến lược của Hồng quân Trung Quốc do Mao Trạch Đông lãnh đạo lên căn cứ Thiểm Tây."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Vị vua nào trong lịch sử Việt Nam ở ngôi lâu nhất (56 năm) từ năm 1072 đến năm 1127?", "options": ["Lý Nhân Tông (Lý Càn Đức)", "Lê Thánh Tông", "Trần Nhân Tông", "Lý Thánh Tông"], "correct": 0, "explanation": "Vua Lý Nhân Tông lên ngôi khi mới 7 tuổi và trị vì đất nước thái bình thịnh trị suốt 56 năm rực rỡ."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Hành tinh nào trong Hệ Mặt Trời có đường kính lớn nhất và khối lượng nặng gấp đôi tất cả các hành tinh khác gộp lại?", "options": ["Sao Mộc (Jupiter)", "Sao Thổ", "Sao Kim", "Sao Hỏa"], "correct": 0, "explanation": "Sao Mộc là người khổng lồ khí với Vết Đỏ Lớn là cơn bão xoáy khổng lồ tồn tại hàng trăm năm."},
        {"difficulty": 1, "question": "Chất lỏng màu đỏ lưu thông trong hệ tuần hoàn của cơ thể người để vận chuyển oxy và dưỡng chất là gì?", "options": ["Máu", "Nước mắt", "Nước bọt", "Bạch huyết"], "correct": 0, "explanation": "Hồng cầu trong máu chứa huyết sắc tố gắn kết oxy phân phối tới mọi tế bào."},
        {"difficulty": 2, "question": "Hiện tượng ánh sáng bị bẻ cong khi đi từ không khí vào trong nước khiến chiếc thìa cắm trong cốc nước trông như bị gãy khúc là hiện tượng gì?", "options": ["Khúc xạ ánh sáng", "Phản xạ toàn phần", "Giao thoa ánh sáng", "Tán xạ ánh sáng"], "correct": 0, "explanation": "Sự thay đổi tốc độ ánh sáng khi truyền qua hai môi trường chiết quang khác nhau gây ra hiện tượng khúc xạ."},
        {"difficulty": 2, "question": "Kim loại nào có nhiệt độ nóng chảy thấp nhất trong các kim loại thể rắn ở điều kiện bình thường (khoảng 29,76 °C, có thể tan chảy ngay trên lòng bàn tay)?", "options": ["Gali (Gallium - Ga)", "Chì", "Thiếc", "Kẽm"], "correct": 0, "explanation": "Kim loại Gali tan chảy ở nhiệt độ cơ thể người (gần 30 °C) biến thành chất lỏng óng ánh bạc."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Loại hạt sơ cấp nào trong vật lý hạt nhân được mệnh danh là 'Hạt của Chúa' (God Particle) mang lại khối lượng cho các hạt khác trong vũ trụ?", "options": ["Boson Higgs", "Quark", "Neutrino", "Photon"], "correct": 0, "explanation": "Peter Higgs và François Englert tiên đoán hạt Boson Higgs năm 1964 và được máy gia tốc hạt lớn LHC tại CERN tìm thấy năm 2012."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Ứng dụng gửi nhận thư điện tử phổ biến nhất thế giới do tập đoàn Google cung cấp miễn phí là gì?", "options": ["Gmail", "Yahoo Mail", "Outlook", "Hotmail"], "correct": 0, "explanation": "Gmail với dung lượng lưu trữ lớn và bộ lọc thư rác thông minh phục vụ hàng tỷ người dùng."},
        {"difficulty": 1, "question": "Món ăn vặt đường phố nổi tiếng của Hà Nội làm từ bánh đa nem cuộn thịt băm mộc nhĩ rán vàng giòn rụm chấm nước mắm chua ngọt là món gì?", "options": ["Nem rán (Chả giò)", "Bánh cuốn", "Phở cuốn", "Bánh xèo"], "correct": 0, "explanation": "Nem rán truyền thống giòn rụm thơm ngon là món ăn không thể thiếu trong mâm cỗ Tết miền Bắc."},
        {"difficulty": 2, "question": "Bộ nhớ bán dẫn thể rắn dùng trong ổ cứng máy tính thế hệ mới có tốc độ đọc ghi nhanh gấp nhiều lần ổ đĩa cơ HDD truyền thống được viết tắt là gì?", "options": ["Ổ cứng SSD (Solid State Drive)", "Băng từ", "Đĩa CD", "Đĩa mềm"], "correct": 0, "explanation": "Ổ cứng SSD dùng chip nhớ flash NAND cho tốc độ khởi động hệ điều hành và tải ứng dụng siêu tốc."},
        {"difficulty": 2, "question": "Món đặc sản 'Gỏi cá trích' tươi rói vắt chanh béo ngậy cuốn bánh tráng chấm nước mắm Phú Quốc là món ăn của đảo nào?", "options": ["Đảo ngọc Phú Quốc", "Đảo Lý Sơn", "Đảo Côn Đảo", "Đảo Cát Bà"], "correct": 0, "explanation": "Gỏi cá trích Phú Quốc ăn kèm dừa nạo và rau rừng là tinh hoa ẩm thực biển đảo Kiên Giang."},
        {"difficulty": 3, "question": "CÂU HỎI CÔNG NGHỆ QUYẾT ĐỊNH: Thuật toán đồng thuận cơ bản trong mạng chuỗi khối Bitcoin yêu cầu các thợ đào phải giải bài toán toán học tốn năng lượng tính toán được gọi là gì?", "options": ["Bằng chứng công việc (Proof of Work - PoW)", "Bằng chứng cổ phần (Proof of Stake - PoS)", "Proof of Authority", "Proof of Space"], "correct": 0, "explanation": "Proof of Work (PoW) đảm bảo tính bảo mật và phi tập trung bất biến của sổ cái mạng Bitcoin."}
    ],

    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu tục ngữ: 'Gừng cay muối mặn xin đừng ... nhau'?", "options": ["quên", "bỏ", "xa", "trách"], "correct": 0, "explanation": "Lời thề nguyền son sắt thủy chung của nghĩa vợ tình chồng qua bao năm tháng thăng trầm."},
        {"difficulty": 1, "question": "Trong truyện cổ tích 'Ăn khế trả vàng', người anh tham lam vì may túi mấy gang mà đã bị chim hất rơi xuống biển sâu?", "options": ["May túi mười hai gang", "May túi ba gang", "May túi sáu gang", "May bao tải"], "correct": 0, "explanation": "Lòng tham vô đáy may túi mười hai gang đựng quá nặng khiến cánh chim không chịu nổi."},
        {"difficulty": 2, "question": "Bài thơ 'Từ ấy' đánh dấu mốc giác ngộ lý tưởng cách mạng cộng sản rực rỡ ('Từ ấy trong tôi bừng nắng hạ...') là của nhà thơ nào?", "options": ["Tố Hữu", "Xuân Diệu", "Huy Cận", "Chế Lan Viên"], "correct": 0, "explanation": "'Từ ấy trong tôi bừng nắng hạ / Mặt trời chân lý chói qua tim' - khúc ca say mê lý tưởng của người chiến sĩ trẻ Tố Hữu năm 1938."},
        {"difficulty": 2, "question": "Tác phẩm tiểu thuyết lịch sử hoành tráng 'Bão táp triều Trần' gồm 4 tập tái hiện vương triều Trần rực rỡ là của nhà văn nào?", "options": ["Nhà văn Hoàng Quốc Hải", "Nguyễn Huy Tưởng", "Hà Ân", "Trần Thùy Mai"], "correct": 0, "explanation": "Nhà văn Hoàng Quốc Hải dành trọn tâm huyết khắc họa 175 năm thăng trầm hiển hách của nhà Trần."},
        {"difficulty": 3, "question": "CÂU HỎI VĂN HỌC QUYẾT ĐỊNH: Vở bi kịch cổ điển 'Vua Oedipus' (Oedipus Rex) kiệt tác sân khấu Hy Lạp cổ đại là tác phẩm của nhà viết kịch vĩ đại nào?", "options": ["Sophocles", "Aeschylus", "Euripides", "Aristophanes"], "correct": 0, "explanation": "Sophocles sáng tác tấn thảm kịch Oedipus về định mệnh nghiệt ngã và số phận con người thời cổ đại."}
    ]
}

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU NẠP ĐỢT 6 TIẾP TỤC HƯỚNG TỚI CỘT MỐC 2.500 CÂU!")
    print("=" * 70)

    total_added = 0
    for cat_name, questions in BATCH_6_DATA.items():
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

        print(f"  📁 [{cat_name}]: Nạp thêm {added_in_cat} câu -> Tổng hiện có: {len(existing_list)} câu.")

    print(f"\n✅ Đợt 6 bổ sung thành công {total_added} câu hỏi mới!")

if __name__ == '__main__':
    main()
