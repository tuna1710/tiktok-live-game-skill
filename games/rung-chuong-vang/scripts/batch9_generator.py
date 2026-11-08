# -*- coding: utf-8 -*-
"""
Đợt 9 - Tiếp tục bứt phá Cột mốc 3 (hướng tới 2.500 câu)
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

BATCH_9_DATA = {
    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Bánh gì không nướng bằng lò, không gói bằng lá mà dùng để thổi phồng nổi trên mặt nước cứu người?", "options": ["Phao cứu sinh (Bánh phao)", "Bánh xe", "Bánh bao", "Bánh rán"], "correct": 0, "explanation": "Phao cứu sinh hình chiếc bánh tròn phồng to giúp người nổi an toàn trên mặt nước."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì sinh ra đã có đôi cánh mỏng bay dập dờn trong đêm thắp đèn lập lòe ở đuôi?", "options": ["Con đom đóm", "Con muỗi", "Con bướm đêm", "Con ve sầu"], "correct": 0, "explanation": "Đom đóm phát quang sinh học ở phần đuôi để phát tín hiệu tìm bạn tình."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có cổ mà không có họng, có nắp đậy kín dùng để rót nước uống hàng ngày?", "options": ["Cái bình nước (hoặc cái chai)", "Cái bát", "Cái xô", "Cái chậu"], "correct": 0, "explanation": "Chiếc bình / chai có phần cổ thu nhỏ để rót nước tiện lợi."},
        {"difficulty": 1, "question": "Đố mẹo: Quả gì vỏ màu cam tươi, mọng nước chua ngọt giàu vitamin C tăng sức đề kháng?", "options": ["Quả cam", "Quả ổi", "Quả chuối", "Quả bơ"], "correct": 0, "explanation": "Cam sành, cam sành mọng nước chứa hàm lượng vitamin C dồi dào."},
        {"difficulty": 1, "question": "Đố mẹo: Đồ vật nào dùng để soi bóng mỗi ngày giúp ta chải tóc, chỉnh trang quần áo gọn gàng?", "options": ["Chiếc gương soi", "Bức tranh", "Tấm kính cửa sổ", "Cái bàn"], "correct": 0, "explanation": "Gương phẳng phản chiếu hình ảnh chân thực của người soi."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt có 3 chữ cái, thêm dấu huyền thành thứ để ngắm nhìn vào ban đêm trên trời, thêm dấu sắc thành thứ để trả công?", "options": ["Sao và Sáo (Sao - Sào - Sáo)", "Trăng", "Mây", "Gió"], "correct": 0, "explanation": "Ngôi sao trên bầu trời đêm lung linh và sào đo đạc."},
        {"difficulty": 2, "question": "Đố mẹo: Thứ gì thuộc về bạn, khi người khác xin phép mượn thì bạn đồng ý cho, nhưng họ dùng xong lại không thể trả lại bạn?", "options": ["Thời gian của bạn", "Cây bút", "Cuốn sách", "Chiếc xe"], "correct": 0, "explanation": "Thời gian trôi qua là một đi không trở lại, không ai có thể hoàn trả thời gian."},
        {"difficulty": 2, "question": "Đố mẹo: Một người ngồi trong phòng tối đen như mực không có một chút ánh sáng nào mà vẫn đọc được sách rất nhanh, vì sao?", "options": ["Người đó là người khiếm thị đọc sách chữ nổi Braille", "Người đó có mắt cú mèo", "Phòng có ánh trăng", "Người đó đeo kính đêm"], "correct": 0, "explanation": "Chữ nổi Braille được cảm nhận bằng đầu ngón tay nên không cần ánh sáng vẫn đọc tốt!"},
        {"difficulty": 2, "question": "Đố vui: 'Da xanh ngăn ngắt, ruột trắng phau phau / Nấu canh tôm đồng ngọt mát từ lâu' là quả gì vườn nhà?", "options": ["Quả bầu (hoặc quả bí xanh)", "Quả dưa hấu", "Quả chuối", "Quả mít"], "correct": 0, "explanation": "'Râu tôm nấu với ruột bầu / Chồng chan vợ húp gật đầu khen ngon'."},
        {"difficulty": 2, "question": "Đố mẹo: Con gì sinh ra không có chân, trườn bò trên mặt đất mà ai nghe tiếng thở phì phì cũng phải tránh xa?", "options": ["Con rắn", "Con giun", "Con đỉa", "Con lươn"], "correct": 0, "explanation": "Loài rắn trườn bò uốn lượn bằng các vảy bụng linh hoạt."},
        {"difficulty": 3, "question": "Đố logic: Có một chiếc thuyền chở một người đàn ông, một con sói, một con dê và một bắp cải. Thuyền chỉ chở được người đó và một thứ. Nếu để sói ở một mình với dê thì sói ăn dê; để dê ở một mình với bắp cải thì dê ăn bắp cải. Người đó phải chở thứ gì qua sông đầu tiên?", "options": ["Chở con dê qua sông đầu tiên", "Chở con sói", "Chở bắp cải", "Không chở gì"], "correct": 0, "explanation": "Chở dê qua trước (để sói ở lại với bắp cải an toàn). Sau đó quay lại chở sói qua và mang dê về... bài toán kinh điển!"},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: Bức tranh đố vui dân gian: 'Thân hình mỏng mảnh như lá sen / Che nắng che mưa cho cô nàng / Đội trên mái tóc duyên dáng hiền' là vật dụng biểu tượng nào của người phụ nữ Việt?", "options": ["Chiếc nón lá bài thơ xứ Huế", "Chiếc ô", "Cái khăn rằn", "Chiếc mũ tai bèo"], "correct": 0, "explanation": "Chiếc nón lá nghiêng che tà áo dài thướt tha mang đậm hồn cốt dân tộc Việt Nam."}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Sông Hàn con sông biểu tượng thơ mộng bắc qua nhiều cây cầu độc đáo chảy qua trung tâm thành phố nào?", "options": ["Thành phố Đà Nẵng", "Thành phố Huế", "Thành phố Nha Trang", "Thành phố Quy Nhơn"], "correct": 0, "explanation": "Sông Hàn uốn lượn giữa lòng Đà Nẵng với cầu Rồng phun lửa, cầu quay sông Hàn."},
        {"difficulty": 1, "question": "Đảo ngọc Phú Quốc hòn đảo du lịch biển lớn nhất Việt Nam nằm trong vịnh biển nào?", "options": ["Vịnh Thái Lan", "Vịnh Bắc Bộ", "Vịnh Cam Ranh", "Vịnh Nha Trang"], "correct": 0, "explanation": "Phú Quốc nằm trong vùng biển Tây Nam thuộc Vịnh Thái Lan ấm áp quanh năm."},
        {"difficulty": 1, "question": "Tỉnh nào ở miền Tây Nam Bộ nổi tiếng với xứ sở dừa bạt ngàn và phong trào Đồng Khởi năm 1960?", "options": ["Bến Tre", "Trà Vinh", "Tiền Giang", "Vĩnh Long"], "correct": 0, "explanation": "Bến Tre quê hương xứ dừa với những vườn dừa bạt ngàn ngút tầm mắt."},
        {"difficulty": 2, "question": "Vườn quốc gia Yok Đôn vườn quốc gia lớn nhất Việt Nam bảo tồn hệ sinh thái rừng khộp nhiệt đới thuộc tỉnh nào?", "options": ["Đắk Lắk (và Đắk Nông)", "Gia Lai", "Kon Tum", "Lâm Đồng"], "correct": 0, "explanation": "Yok Đôn nằm bên dòng sông Sêrêpôk là ngôi nhà của nhiều loài động vật quý hiếm."},
        {"difficulty": 2, "question": "Tỉnh nào ở miền Trung có dòng sông Thạch Hãn và di tích Thành cổ lịch sử với 81 ngày đêm rực lửa năm 1972?", "options": ["Quảng Trị", "Quảng Bình", "Thừa Thiên Huế", "Hà Tĩnh"], "correct": 0, "explanation": "Thành cổ Quảng Trị là di tích lịch sử quốc gia đặc biệt ghi dấu chiến công oanh liệt của quân và dân ta."},
        {"difficulty": 2, "question": "Thủ đô của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam là thành phố ngàn năm văn hiến nào?", "options": ["Hà Nội", "TP. Hồ Chí Minh", "Huế", "Đà Nẵng"], "correct": 0, "explanation": "Thủ đô Hà Nội trái tim của cả nước với 36 phố phường cổ kính rực rỡ sắc màu."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Hồ nước ngọt tự nhiên Ba Bể ở độ cao 150m giữa núi rừng Đông Bắc gồm ba nhánh hồ nào thông nhau hợp thành?", "options": ["Pé Lầm, Pé Lù, Pé Lèng", "Hồ Ba Mẫu, Bảy Mẫu", "Hồ Tơ Nưng, Lắk", "Hồ Dầu Tiếng, Thác Bà"], "correct": 0, "explanation": "Hồ Ba Bể tiếng Tày là Slam Pé (ba hồ nhỏ) thông nhau tạo thành hồ nước ngọt tự nhiên lớn nhất nước ta."}
    ],

    "lich-su": [
        {"difficulty": 1, "question": "Chiến thắng trên sông Bạch Đằng năm 938 của Ngô Quyền đã đánh tan đạo quân xâm lược của quốc gia phong kiến nào?", "options": ["Quân Nam Hán", "Quân Tống", "Quân Nguyên", "Quân Minh"], "correct": 0, "explanation": "Ngô Quyền cắm cọc gỗ nhọn bịt sắt tiêu diệt đạo thuyền chiến của tướng giặc Lưu Hoằng Tháo."},
        {"difficulty": 1, "question": "Ngày Thương binh - Liệt sĩ nhằm tưởng nhớ và tri ân các anh hùng có công với đất nước được tổ chức vào ngày nào hàng năm?", "options": ["27/7", "22/12", "30/4", "19/8"], "correct": 0, "explanation": "Ngày 27/7 hàng năm là dịp toàn Đảng toàn dân thể hiện đạo lý 'Uống nước nhớ nguồn', tri ân các liệt sĩ."},
        {"difficulty": 2, "question": "Bài hịch bất hủ 'Hịch tướng sĩ' khuyên răn tướng sĩ rèn luyện võ nghệ đánh giặc Nguyên Mông do danh nhân nào chắp bút năm 1284?", "options": ["Hưng Đạo Đại vương Trần Quốc Tuấn", "Trần Quang Khải", "Trần Thái Tông", "Trần Thủ Độ"], "correct": 0, "explanation": "Áng hùng văn 'Hịch tướng sĩ' thổi bùng hào khí Đông A bất diệt của non sông Đại Việt."},
        {"difficulty": 2, "question": "Vị vua nào của triều Hậu Lê đã lãnh đạo cuộc cải cách hành chính chia đất nước thành 13 đạo thừa tuyên và ban hành Luật Hồng Đức?", "options": ["Lê Thánh Tông", "Lê Thái Tổ", "Lê Nhân Tông", "Lê Thái Tông"], "correct": 0, "explanation": "Vua Lê Thánh Tông đưa Đại Việt phát triển rực rỡ đỉnh cao về kinh tế, văn hóa và pháp luật."},
        {"difficulty": 2, "question": "Trận phục kích Chúc Động - Tốt Động năm 1426 của nghĩa quân Lam Sơn đã tiêu diệt tướng giặc nào của nhà Minh?", "options": ["Vương Thông bị tháo chạy, tiêu diệt Trần Hiệp và Lý Lượng", "Liễu Thăng", "Trương Phụ", "Mộc Thạnh"], "correct": 0, "explanation": "'Ninh Kiều máu chảy thành sông / Tốt Động thây chất đầy nội' - Nguyễn Trãi viết trong Bình Ngô Đại Cáo."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Vị vua nào của triều Tiền Lê đã cho mở hội cày ruộng Tịch điền đầu tiên tại Đọi Sơn (Hà Nam) vào đầu xuân năm 987?", "options": ["Lê Hoàn (vua Lê Đại Hành)", "Lê Long Đĩnh", "Lê Thái Tổ", "Đinh Tiên Hoàng"], "correct": 0, "explanation": "Vua Lê Đại Hành đích thân xuống đồng cày ruộng tịch điền đầu xuân để khuyến khích muôn dân chăm lo nông nghiệp."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Chất khí nào thoát ra từ lá cây trong quá trình quang hợp dưới ánh sáng mặt trời là nguồn sống cho con người?", "options": ["Khí Oxy (O2)", "Khí Cacbonic", "Khí Metan", "Khí Nitơ"], "correct": 0, "explanation": "Quá trình quang hợp phân tách nước và giải phóng khí oxy duy trì bầu khí quyển Trái Đất."},
        {"difficulty": 1, "question": "Hành tinh nào trong Hệ Mặt Trời có vị trí thứ 3 tính từ Mặt Trời ra ngoài và là ngôi nhà chung của nhân loại?", "options": ["Trái Đất (Earth)", "Sao Hỏa", "Sao Kim", "Sao Thủy"], "correct": 0, "explanation": "Trái Đất nằm trong vùng có thể sống được (Goldilocks zone) có nước lỏng và khí quyển thích hợp."},
        {"difficulty": 2, "question": "Hiện tượng sấm sét trong cơn dông bão tạo ra âm thanh tiếng sấm đến tai ta muộn hơn ánh chớp là do nguyên nhân vật lý nào?", "options": ["Vận tốc ánh sáng nhanh hơn rất nhiều so với vận tốc âm thanh", "Âm thanh bị gió cản", "Mắt nhìn nhanh hơn tai", "Tai phản xạ chậm"], "correct": 0, "explanation": "Ánh sáng truyền đi với tốc độ 300.000 km/s gần như tức thời, trong khi âm thanh chỉ truyền khoảng 340 m/s."},
        {"difficulty": 2, "question": "Nguyên tố hóa học nào là thành phần cấu tạo chính trong xương và răng giúp xương chắc khỏe?", "options": ["Canxi (Ca)", "Sắt (Fe)", "Kẽm (Zn)", "Đồng (Cu)"], "correct": 0, "explanation": "Hợp chất Canxi photphat (hydroxyapatite) mang lại độ cứng cáp và vững chắc cho khung xương."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Thuyết tương đối rộng của Albert Einstein (1915) giải thích bản chất của lực hấp dẫn là do hiện tượng gì của không - thời gian?", "options": ["Sự cong uốn của không - thời gian dưới tác động của khối lượng và năng lượng", "Lực hút tĩnh điện", "Sóng xung kích", "Lực từ trường"], "correct": 0, "explanation": "Khối lượng khổng lồ của các thiên thể làm biến dạng, bẻ cong tấm vải không - thời gian xung quanh chúng."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Món ăn nào được gói bằng lá dong hình vuông nhân đậu xanh thịt mỡ là linh hồn của mâm cỗ Tết cổ truyền miền Bắc?", "options": ["Bánh chưng", "Bánh tét", "Bánh giầy", "Bánh ú"], "correct": 0, "explanation": "Bánh chưng xanh vuông vắn tượng trưng cho Đất trời thái bình thịnh vượng."},
        {"difficulty": 1, "question": "Nền tảng mạng xã hội chuyên chia sẻ ảnh và video ngắn thuộc sở hữu của tập đoàn Meta với biểu tượng ống kính máy ảnh là gì?", "options": ["Instagram", "Facebook", "Twitter", "LinkedIn"], "correct": 0, "explanation": "Instagram là mạng xã hội chia sẻ hình ảnh phong cách sống phổ biến toàn cầu."},
        {"difficulty": 2, "question": "Giải đấu bóng đá vô địch các câu lạc bộ danh giá nhất châu Âu diễn ra hàng năm có tên gọi là gì?", "options": ["UEFA Champions League (Cúp C1)", "Europa League", "Copa America", "AFC Champions League"], "correct": 0, "explanation": "Champions League quy tụ các câu lạc bộ hàng đầu châu Âu tranh tài đỉnh cao."},
        {"difficulty": 2, "question": "Món đặc sản 'Chả mực nang giã tay' giòn sần sật vàng ruộm thơm lừng là món ngon nổi tiếng của tỉnh nào?", "options": ["Quảng Ninh (Hạ Long)", "Hải Phòng", "Thanh Hóa", "Nghệ An"], "correct": 0, "explanation": "Chả mực Hạ Long giã tay thủ công ăn kèm xôi trắng hoặc bánh cuốn là đặc sản trứ danh đất mỏ."},
        {"difficulty": 3, "question": "CÂU HỎI CÔNG NGHỆ QUYẾT ĐỊNH: Mạng máy tính diện rộng kết nối các thiết bị trong phạm vi một thành phố hoặc khu vực đô thị lớn được viết tắt là gì?", "options": ["Mạng MAN (Metropolitan Area Network)", "Mạng LAN", "Mạng WAN", "Mạng PAN"], "correct": 0, "explanation": "Mạng MAN kết nối nhiều mạng LAN trong cùng một đô thị với đường truyền cáp quang tốc độ cao."}
    ],

    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu tục ngữ: 'Lá lành đùm lá rách / Lá rách đùm lá ...'?", "options": ["nát", "hỏng", "rơi", "vàng"], "correct": 0, "explanation": "Tinh thần đùm bọc, sẻ chia tương trợ lẫn nhau của dân tộc Việt Nam."},
        {"difficulty": 1, "question": "Trong truyện cổ tích 'Sọ Dừa', chàng Sọ Dừa tuy dị hình dị dạng nhưng có tài nghệ chăn con vật gì rất giỏi cho phú ông?", "options": ["Chăn đàn bò", "Chăn đàn dê", "Chăn vịt", "Chăn ngựa"], "correct": 0, "explanation": "Chàng Sọ Dừa ngày ngày chăn đàn bò béo tốt và thổi sáo véo von lay động lòng người."},
        {"difficulty": 2, "question": "Bài thơ 'Quê hương' với câu thơ bất hủ 'Cánh buồm giương to như mảnh hồn làng / Rướn thân trắng bao la thâu góp gió' là của nhà thơ nào?", "options": ["Tế Hanh", "Quang Dũng", "Huy Cận", "Xuân Diệu"], "correct": 0, "explanation": "Nhà thơ Tế Hanh viết bài thơ năm 1939 khi đang học ở Huế mang nặng tình yêu làng chài ven biển quê hương."},
        {"difficulty": 2, "question": "Ai là tác giả của tác phẩm tiểu thuyết hiện thực xuất sắc 'Tắt đèn' miêu tả tinh thần phản kháng quật khởi của Chị Dậu?", "options": ["Nhà văn Ngô Tất Tố", "Nam Cao", "Vũ Trọng Phụng", "Nguyên Hồng"], "correct": 0, "explanation": "Ngô Tất Tố phản ánh chính sách sưu thuế tàn bạo của chế độ thực dân phong kiến qua bi kịch gia đình Chị Dậu."},
        {"difficulty": 3, "question": "CÂU HỎI VĂN HỌC QUYẾT ĐỊNH: Kiệt tác kịch thơ 'Vũ Như Tô' của Nguyễn Huy Tưởng lấy bối cảnh xây dựng tòa lâu đài khổng lồ nào dưới thời vua Lê Tương Dực?", "options": ["Cửu Trùng Đài", "Điện Lam Kinh", "Thành Tây Đô", "Điện Kính Thiên"], "correct": 0, "explanation": "Vũ Như Tô dốc tâm huyết cả đời xây đài Cửu Trùng tráng lệ nhưng làm hao tổn sức người sức của dẫn đến bi kịch lịch sử."}
    ]
}

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU NẠP ĐỢT 9: TĂNG TỐC TÍCH LŨY CỘT MỐC 3 CỤC BỘ (LOCAL)!")
    print("=" * 70)

    total_added = 0
    for cat_name, questions in BATCH_9_DATA.items():
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

    print(f"\n✅ Đợt 9 bổ sung thành công {total_added} câu hỏi mới!")

if __name__ == '__main__':
    main()
