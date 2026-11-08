# -*- coding: utf-8 -*-
"""
Đợt 8 - Tiếp tục tăng tốc tích lũy Cột mốc 3 (hướng tới 2.500 câu)
Bổ sung 120 câu hỏi chuẩn hóa phong phú chia đều cho 6 chủ đề (mỗi chủ đề ~20 câu).
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

BATCH_8_DATA = {
    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Bánh gì không ăn được mà xoay tít trên mặt nước đẩy cano lướt sóng?", "options": ["Chân vịt (chân vịt tàu)", "Bánh lái", "Bánh xe", "Bánh bao"], "correct": 0, "explanation": "Chân vịt tàu thủy quay tít dưới nước tạo lực đẩy tàu thuyền tiến lên."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì sinh ra đã có đôi cánh mỏng rực rỡ, thích bay lượn hút mật hoa ngày xuân?", "options": ["Con bướm", "Con chuồn chuồn", "Con ong", "Con ruồi"], "correct": 0, "explanation": "Bướm hoa với đôi cánh nhiều màu sắc sặc sỡ bay rập rờn bên khóm hoa."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có lưng mà không có bụng, dùng để tựa mỗi khi ta ngồi nghỉ mỏi mệt?", "options": ["Lưng ghế tựa", "Chiếc gối", "Bức tường", "Cái bàn"], "correct": 0, "explanation": "Chiếc ghế có phần lưng tựa êm ái nâng đỡ cột sống."},
        {"difficulty": 1, "question": "Đố mẹo: Quả gì nhiều mắt xung quanh, khi chín vỏ vàng thơm ngát gọt bỏ mắt ăn ngọt lịm?", "options": ["Quả dứa (Quả khóm / Thơm)", "Quả mít", "Quả chuối", "Quả dưa hấu"], "correct": 0, "explanation": "Quả dứa có nhiều mắt nhỏ trên lớp vỏ gai dày."},
        {"difficulty": 1, "question": "Đố mẹo: Đồ vật nào dùng để quét nhà mỗi sớm mai cho sàn nhà sạch bóng?", "options": ["Cây chổi quét nhà", "Cây lau nhà", "Cái xẻng", "Cái cào"], "correct": 0, "explanation": "Cây chổi rơm, chổi đót quét sạch bụi bẩn trong nhà."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt có 4 chữ cái, bỏ dấu thành tên một loài cá nước ngọt, thêm sắc thành thứ để trả tiền mua hàng?", "options": ["Tiền và Tiên (Tiên - Tiền)", "Vàng", "Bạc", "Đô"], "correct": 0, "explanation": "Nàng tiên cá xinh đẹp và tiền bạc chi tiêu hàng ngày."},
        {"difficulty": 2, "question": "Đố mẹo: Cái gì của bạn nhưng người khác lại gọi nó và dùng nó nhiều hơn chính bản thân bạn?", "options": ["Tên gọi của bạn", "Điện thoại của bạn", "Đôi giày", "Cái áo"], "correct": 0, "explanation": "Tên riêng của bạn chủ yếu để bạn bè, người thân gọi khi giao tiếp."},
        {"difficulty": 2, "question": "Đố mẹo: Một người đứng dưới trời mưa tầm tã không có ô hay áo mưa nhưng sợi tóc nào cũng không ướt, tại sao?", "options": ["Người đó bị hói đầu", "Người đó đi quá nhanh", "Trời mưa nhỏ", "Người đó ở ngoài đường"], "correct": 0, "explanation": "Người đàn ông hói đầu không có sợi tóc nào nên tóc không thể bị ướt!"},
        {"difficulty": 2, "question": "Đố vui: 'Da cóc mà bọc trứng gà / Bổ ra thơm phức cả nhà muốn ăn' là quả gì thơm ngọt?", "options": ["Quả mít chín", "Quả sầu riêng", "Quả na", "Quả bưởi"], "correct": 0, "explanation": "Quả mít chín cây vỏ sần sùi như da cóc, bên trong múi vàng thơm lừng."},
        {"difficulty": 2, "question": "Đố mẹo: Con gì sinh ra đã có bộ ria mép dài nhưng lại thích trèo cây bắt chuột?", "options": ["Con mèo", "Con cún", "Con thỏ", "Con lợn"], "correct": 0, "explanation": "Chú mèo với hàng ria mép định vị thính nhạy trong bóng đêm."},
        {"difficulty": 3, "question": "Đố logic: Có 5 quả táo trong giỏ, làm sao chia đều cho 5 bạn mà trong giỏ vẫn còn nguyên 1 quả táo?", "options": ["Đưa quả táo cuối cùng kèm theo chiếc giỏ cho bạn thứ năm", "Cắt đôi táo", "Không chia được", "Giấu 1 quả"], "correct": 0, "explanation": "4 bạn nhận 4 quả táo rời, bạn thứ 5 nhận cả chiếc giỏ bên trong có quả táo còn lại!"},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: Bức tranh đố vui dân gian: 'Trùng trục như con bò thui / Chín mắt, chín mũi, chín đuôi, chín đầu' là gì trong thực tế?", "options": ["Chín con bò thui", "Con quái vật chín đầu", "Con sâu đo", "Con rồng biển"], "correct": 0, "explanation": "Từ 'chín' ở đây là số đếm số 9 (gồm 9 con bò thui), không phải thức ăn nấu chín!"}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Thành phố Đà Lạt thành phố ngàn thông reo và sương mù mộng mơ là tỉnh lỵ của tỉnh nào?", "options": ["Lâm Đồng", "Đắk Lắk", "Gia Lai", "Kon Tum"], "correct": 0, "explanation": "Đà Lạt nằm trên cao nguyên Lâm Viên ở độ cao 1.500m thuộc tỉnh Lâm Đồng."},
        {"difficulty": 1, "question": "Chợ Bến Thành ngôi chợ biểu tượng sầm uất hơn 100 năm tuổi với chiếc tháp đồng hồ bốn mặt nằm ở trung tâm thành phố nào?", "options": ["TP. Hồ Chí Minh", "Hà Nội", "Đà Nẵng", "Cần Thơ"], "correct": 0, "explanation": "Chợ Bến Thành tọa lạc tại Quận 1, TP. Hồ Chí Minh."},
        {"difficulty": 1, "question": "Vịnh Hạ Long di sản thiên nhiên thế giới kỳ vĩ với hàng ngàn đảo đá vôi nhấp nhô thuộc tỉnh nào?", "options": ["Quảng Ninh", "Hải Phòng", "Thái Bình", "Nam Định"], "correct": 0, "explanation": "Vịnh Hạ Long là báu vật ngoại hạng toàn cầu của tỉnh Quảng Ninh."},
        {"difficulty": 2, "question": "Đèo Pha Đin con đèo huyền thoại trong chiến dịch Điện Biên Phủ nằm trên ranh giới giữa hai tỉnh nào?", "options": ["Sơn La và Điện Biên", "Hòa Bình và Sơn La", "Lào Cai và Lai Châu", "Yên Bái và Tuyên Quang"], "correct": 0, "explanation": "'Dốc Pha Đin, chị gánh anh thồ...' - con đèo dài 32 km nối Sơn La và Điện Biên."},
        {"difficulty": 2, "question": "Quần thể danh thắng Tràng An di sản hỗn hợp Văn hóa và Thiên nhiên thế giới đầu tiên của Đông Nam Á thuộc tỉnh nào?", "options": ["Ninh Bình", "Thanh Hóa", "Hà Nam", "Nam Định"], "correct": 0, "explanation": "Tràng An (Ninh Bình) được UNESCO vinh danh năm 2014 nhờ vẻ đẹp karst đá vôi tráng lệ."},
        {"difficulty": 2, "question": "Quốc gia nào ở châu Âu nổi tiếng với đồng hồ chính xác, sô-cô-la hảo hạng và dãy núi Alps phủ tuyết?", "options": ["Thụy Sĩ", "Áo", "Bỉ", "Hà Lan"], "correct": 0, "explanation": "Thụy Sĩ là quốc gia trung lập giàu có bậc nhất châu Âu."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Dãy núi nào dài nhất Nam Mỹ (hơn 7.000 km) chạy dọc theo bờ biển Thái Bình Dương?", "options": ["Dãy Andes", "Dãy Rocky", "Dãy Alps", "Dãy Himalaya"], "correct": 0, "explanation": "Dãy Andes chạy qua 7 quốc gia Nam Mỹ với nhiều đỉnh núi lửa cao trên 6.000 mét."}
    ],

    "lich-su": [
        {"difficulty": 1, "question": "Vua Lý Thái Tổ ban Chiếu dời đô dời kinh thành từ Hoa Lư về thành Đại La vào mùa thu năm nào?", "options": ["Năm Canh Tuất 1010", "Năm 938", "Năm 1070", "Năm 1258"], "correct": 0, "explanation": "Năm 1010, vua Lý Thái Tổ thấy rồng vàng bay lên nên đổi tên Đại La thành Thăng Long."},
        {"difficulty": 1, "question": "Hai Bà Trưng cưỡi voi ra trận khởi nghĩa chống quân xâm lược của triều đại phong kiến phương Bắc nào?", "options": ["Nhà Đông Hán (thái thú Tô Định)", "Nhà Đường", "Nhà Tống", "Nhà Minh"], "correct": 0, "explanation": "Hai Bà Trưng phất cờ khởi nghĩa mùa xuân năm 40 sau Công nguyên trừng trị tên thái thú bạo tàn Tô Định."},
        {"difficulty": 2, "question": "Hội nghị Diên Hồng lịch sử biểu thị ý chí toàn dân muôn người cùng hô vang một lời 'Đánh!' diễn ra dưới triều vua nào?", "options": ["Trần Nhân Tông", "Trần Thái Tông", "Trần Thánh Tông", "Trần Anh Tông"], "correct": 0, "explanation": "Năm 1284, vua Trần Nhân Tông triệu tập các bô lão tại thềm điện Diên Hồng hỏi kế đánh giặc Nguyên Mông."},
        {"difficulty": 2, "question": "Chiến thắng Điện Biên Phủ ngày 7/5/1954 đã buộc thực dân Pháp phải ký kết văn kiện quốc tế nào lập lại hòa bình ở Đông Dương?", "options": ["Hiệp định Geneva", "Hiệp định Paris", "Hiệp định Sơ bộ", "Tạm ước 14/9"], "correct": 0, "explanation": "Hiệp định Geneva năm 1954 công nhận độc lập, chủ quyền, thống nhất và toàn vẹn lãnh thổ của Việt Nam."},
        {"difficulty": 2, "question": "Vị hoàng đế nào của nhà Hậu Lê sáng lập ra Hội Tao Đàn gồm 28 vị đại thần trí thức ('Nhị thập bát tú')?", "options": ["Lê Thánh Tông", "Lê Thái Tổ", "Lê Nhân Tông", "Lê Thái Tông"], "correct": 0, "explanation": "Vua Lê Thánh Tông là tao đàn đô nguyên súy phát triển văn học Nho giáo thịnh trị."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Vị tướng nào của khởi nghĩa Lam Sơn đã dùng mưu mai phục chém chết Liễu Thăng tại ải Chi Lăng ngày 10/10/1427?", "options": ["Tướng quân Trần Lựu và Lê Sát", "Đinh Liệt", "Nguyễn Xí", "Lê Ngân"], "correct": 0, "explanation": "Trần Lựu vờ thua nhử Liễu Thăng vào đầm lầy Mã Yên để phục binh Lê Sát tung đòn quyết định chém đầu tướng giặc."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Cơ thể con người cần hít thở chất khí nào từ không khí để duy trì sự sống mỗi giây?", "options": ["Khí Oxy (O2)", "Khí Cacbonic", "Khí Nitơ", "Khí Hydro"], "correct": 0, "explanation": "Oxy được phổi hấp thụ đưa vào hồng cầu đi nuôi dưỡng toàn bộ tế bào cơ thể."},
        {"difficulty": 1, "question": "Hành tinh nào trong Hệ Mặt Trời được con người đặt chân lên thám hiểm đầu tiên vào năm 1969?", "options": ["Mặt Trăng (vệ tinh của Trái Đất)", "Sao Hỏa", "Sao Kim", "Sao Mộc"], "correct": 0, "explanation": "Phi hành gia Neil Armstrong đặt bước chân lịch sử đầu tiên lên Mặt Trăng trên tàu Apollo 11."},
        {"difficulty": 2, "question": "Hiện tượng cầu vồng bảy sắc sau cơn mưa xuất hiện do ánh sáng mặt trời bị giọt nước mưa làm gì?", "options": ["Tán sắc và khúc xạ ánh sáng", "Phản xạ gương", "Hấp thụ nhiệt", "Giao thoa sóng"], "correct": 0, "explanation": "Giọt nước mưa như lăng kính tán sắc chùm sáng trắng thành 7 dải màu quang phổ rực rỡ."},
        {"difficulty": 2, "question": "Kim loại nào có tính dẫn điện và dẫn nhiệt tốt nhất trong tất cả các kim loại trong tự nhiên?", "options": ["Bạc (Ag)", "Đồng (Cu)", "Vàng (Au)", "Nhôm (Al)"], "correct": 0, "explanation": "Bạc dẫn điện tốt nhất, tiếp theo là đồng, vàng và nhôm."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Thuyết Vạn vật Hấp dẫn nổi tiếng do nhà bác học vĩ đại người Anh nào phát minh khi quan sát quả táo rụng?", "options": ["Sir Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"], "correct": 0, "explanation": "Isaac Newton công bố định luật vạn vật hấp dẫn năm 1687 đặt nền móng cơ học cổ điển."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Món phở truyền thống trứ danh của Việt Nam thường được thưởng thức với nước dùng hầm từ xương bò và loại gia vị thơm nào?", "options": ["Hoa hồi, quế, thảo quả, gừng nướng", "Lá chanh, ớt bột", "Hạt tiêu xanh, thì là", "Nghệ tươi"], "correct": 0, "explanation": "Hồi, quế, thảo quả tạo nên hương thơm đặc trưng nồng nàn quyến rũ của bát phở bò."},
        {"difficulty": 1, "question": "Hệ điều hành di động mã nguồn mở phổ biến nhất thế giới trên điện thoại Samsung, Xiaomi do Google phát triển là gì?", "options": ["Android", "iOS", "Windows Phone", "BlackBerry OS"], "correct": 0, "explanation": "Android chiếm hơn 70% thị phần hệ điều hành smartphone toàn cầu."},
        {"difficulty": 2, "question": "Cầu thủ bóng đá nào đang nắm giữ kỷ lục ghi nhiều bàn thắng nhất trong lịch sử các kỳ World Cup (16 bàn thắng)?", "options": ["Miroslav Klose (Đức)", "Ronaldo Nazario (Brazil)", "Lionel Messi", "Pele"], "correct": 0, "explanation": "Tiền đạo Miroslav Klose ghi 16 bàn thắng qua 4 kỳ World Cup (2002, 2006, 2010, 2014)."},
        {"difficulty": 2, "question": "Món 'Cơm tấm sườn bì chả' thơm lừng chan mỡ hành là món ăn sáng đặc sản biểu tượng của thành phố nào?", "options": ["TP. Hồ Chí Minh", "Hà Nội", "Đà Nẵng", "Hải Phòng"], "correct": 0, "explanation": "Hạt tấm dẻo ngọt, sườn nướng than hoa thơm nức mũi là tinh hoa ẩm thực đường phố Sài Gòn."},
        {"difficulty": 3, "question": "CÂU HỎI CÔNG NGHỆ QUYẾT ĐỊNH: Mô hình mạng nơ-ron học sâu tích chập (CNN - Convolutional Neural Network) được ứng dụng phổ biến và tối ưu nhất trong lĩnh vực nào của AI?", "options": ["Thị giác máy tính và nhận diện hình ảnh (Computer Vision)", "Dịch văn bản", "Xử lý âm thanh giọng nói", "Dự báo thời tiết"], "correct": 0, "explanation": "Mạng CNN bắt chước vỏ não thị giác trích xuất các đặc trưng không gian hình ảnh cực kỳ chính xác."}
    ],

    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu tục ngữ: 'Lời nói gói ...'?", "options": ["vàng", "bạc", "tiền", "đồng"], "correct": 0, "explanation": "Khuyên con người quý trọng lời nói chân thành, có giá trị như gói vàng mười."},
        {"difficulty": 1, "question": "Trong truyện cổ tích 'Thạch Sanh', chàng Thạch Sanh đã dùng vũ khí thần kỳ nào để đẩy lùi đội quân 18 nước chư hầu mà không tốn một mũi tên?", "options": ["Cây đàn thần (và niêu cơm thần)", "Cung tên vàng", "Thanh bảo kiếm", "Gậy sắt"], "correct": 0, "explanation": "Tiếng đàn thần Thạch Sanh gảy lên nỗi niềm hòa bình cảm hóa quân giặc buông vũ khí quy hàng."},
        {"difficulty": 2, "question": "Đoạn thơ 'Sông Mã xa rồi Tây Tiến ơi! / Nhớ về rừng núi nhớ chơi vơi...' mở đầu kiệt tác thơ hào hoa nào của Quang Dũng?", "options": ["Tây Tiến", "Đồng chí", "Việt Bắc", "Bài thơ về tiểu đội xe không kính"], "correct": 0, "explanation": "Bài thơ 'Tây Tiến' khắc họa bức tượng đài bi tráng, hào hoa của người chiến sĩ Hà thành vệ quốc."},
        {"difficulty": 2, "question": "Ai là tác giả của tác phẩm truyện ngắn 'Chí Phèo' với hình ảnh bát cháo hành ấm áp tình người của Thị Nở?", "options": ["Nhà văn Nam Cao", "Ngô Tất Tố", "Vũ Trọng Phụng", "Nguyễn Công Hoan"], "correct": 0, "explanation": "Nam Cao thức tỉnh lương tri người nông dân bị bần cùng hóa qua bát cháo hành cứu rỗi linh hồn Chí Phèo."},
        {"difficulty": 3, "question": "CÂU HỎI VĂN HỌC QUYẾT ĐỊNH: Vở nhạc kịch 'Cô Sao' vở opera kinh điển đầu tiên của nền âm nhạc hàn lâm cách mạng Việt Nam do nhạc sĩ nào chắp bút năm 1965?", "options": ["Nhạc sĩ Đỗ Nhuận", "Văn Cao", "Lưu Hữu Phước", "Hoàng Việt"], "correct": 0, "explanation": "Nhạc sĩ Đỗ Nhuận viết vở opera Cô Sao tái hiện cuộc đời kiên trung của cô gái Thái dưới ngọn cờ cách mạng."}
    ]
}

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU NẠP ĐỢT 8: TIẾP TỤC TÍCH LŨY CỘT MỐC 3 CỤC BỘ (LOCAL)!")
    print("=" * 70)

    total_added = 0
    for cat_name, questions in BATCH_8_DATA.items():
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

    print(f"\n✅ Đợt 8 bổ sung thành công {total_added} câu hỏi mới!")

if __name__ == '__main__':
    main()
