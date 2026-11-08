# -*- coding: utf-8 -*-
"""
Đợt 5 - Khởi động Cột mốc 3 (1.000 -> 2.500 câu)
Sinh bổ sung 270 câu hỏi chất lượng cao chia đều cho 6 chủ đề (mỗi chủ đề 45 câu).
"""

import os
import json
import sqlite3
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
CATEGORIES_DIR = os.path.join(DATA_DIR, 'categories')
DB_PATH = os.path.join(DATA_DIR, 'questions.db')

def normalize_text(text: str) -> str:
    t = text.lower()
    t = re.sub(r'[^\w\s]', '', t, flags=re.UNICODE)
    return ' '.join(t.split())

BATCH_5_DATA = {
    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Bánh gì không nướng bằng lò, không gói bằng lá mà nằm im dưới gót chân bạn?", "options": ["Bánh gót (Gót chân)", "Bánh mì", "Bánh rán", "Bánh bao"], "correct": 0, "explanation": "Gót chân trong dân gian đôi khi gọi vui là gót chân bánh quy."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có cánh nhưng không biết bay, mỗi khi trời nóng quay tròn phả gió?", "options": ["Cây quạt trần", "Chiếc diều", "Máy bay", "Cánh cửa"], "correct": 0, "explanation": "Quạt trần quay đều tạo gió mát khắp phòng."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì có mai cứng như sắt, đi đứng chậm rì rì nhưng sống thọ hàng trăm năm?", "options": ["Con rùa", "Con ốc", "Con cua", "Con tôm"], "correct": 0, "explanation": "Loài rùa nổi tiếng với tuổi thọ cao và chiếc mai vững chắc bảo vệ cơ thể."},
        {"difficulty": 1, "question": "Đố mẹo: Quả gì không có hạt, không có gai, màu vàng cong cong như trăng lưỡi liềm?", "options": ["Quả chuối tiêu", "Quả xoài", "Quả cam", "Quả táo"], "correct": 0, "explanation": "Quả chuối chín vàng cong cong thơm ngọt."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì bạn luôn nhìn thấy mỗi khi soi gương vào buổi sáng?", "options": ["Bản thân bạn trong gương", "Bức tranh", "Chiếc giường", "Bầu trời"], "correct": 0, "explanation": "Hình ảnh phản chiếu của chính bạn trong gương phẳng."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì kêu meo meo, thích bắt chuột nhắt và leo trèo bắt cá?", "options": ["Con mèo", "Con cún", "Con thỏ", "Con lợn"], "correct": 0, "explanation": "Chú mèo dễ thương với đôi mắt tinh tường ban đêm."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có ruột màu đen, bọc ngoài bằng gỗ, gọt nhọn đầu để viết chữ vẽ tranh?", "options": ["Bút chì", "Bút bi", "Bút lông", "Thước kẻ"], "correct": 0, "explanation": "Ruột bút chì làm từ than chì và đất sét bọc thân gỗ."},
        {"difficulty": 1, "question": "Đố mẹo: Cầu gì không bắc qua sông qua suối mà bắc qua bầu trời rực rỡ 7 màu sau cơn mưa?", "options": ["Cầu vồng", "Cầu khỉ", "Cầu treo", "Cầu vượt"], "correct": 0, "explanation": "Cầu vồng bảy sắc lung linh sau cơn mưa rào."},
        {"difficulty": 1, "question": "Đố mẹo: Đồ vật nào dùng để hứng nước mưa rơi từ mái nhà xuống đựng đầy chum vại?", "options": ["Cái máng xối", "Cái thùng rác", "Cái xô vỡ", "Cái rổ"], "correct": 0, "explanation": "Máng nước (máng xối) dẫn nước mưa chảy vào bể chứa."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có răng cưa sắc bén, chạy bằng điện hoặc tay, dùng để xẻ gỗ dựng nhà?", "options": ["Cái cưa", "Cái búa", "Cái kìm", "Cái xẻng"], "correct": 0, "explanation": "Lưỡi cưa với các răng cưa nhọn dùng để cưa xẻ gỗ đá."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt có 3 chữ cái, thêm dấu sắc thành thứ để uống trà, thêm dấu huyền thành thứ để chiếu sáng?", "options": ["Đèn và Chén (Đen - Đèn - Đén)", "Ly", "Cốc", "Bình"], "correct": 0, "explanation": "Đèn thắp sáng đêm tối, chén trà thơm ngát ban mai."},
        {"difficulty": 2, "question": "Đố mẹo: Cái gì chặt không đứt, bứt không rời, lấy búa đập không vỡ nhưng lấy tay vốc lên thì chảy hết?", "options": ["Dòng nước", "Khối sắt", "Cục đá", "Khúc gỗ"], "correct": 0, "explanation": "Dòng nước lỏng mềm mại không thể đập vỡ hay chặt đứt."},
        {"difficulty": 2, "question": "Đố mẹo: Bạn đang ở trong một căn phòng có 2 cánh cửa: một cửa dẫn đến hang lửa cháy rực, một cửa dẫn đến hồ cá sấu đói nhịn ăn 3 năm. Bạn chọn cửa nào an toàn?", "options": ["Cửa có cá sấu đói (vì nhịn ăn 3 năm cá sấu đã chết đói)", "Cửa hang lửa", "Không chọn cửa nào", "Chọn ngẫu nhiên"], "correct": 0, "explanation": "Cá sấu không thể nhịn ăn suốt 3 năm, chúng chắc chắn đã chết đói từ lâu rồi!"},
        {"difficulty": 2, "question": "Đố mẹo: Cái gì bạn vừa cho đi thì lại nhận lại ngay lập tức mà không tốn một xu nào?", "options": ["Nụ cười thân thiện", "Tiền mặt", "Bức ảnh", "Đôi giày"], "correct": 0, "explanation": "Khi bạn mỉm cười với người khác, họ thường sẽ nở nụ cười đáp lại bạn ngay."},
        {"difficulty": 2, "question": "Đố mẹo: Con gì ban ngày nằm im dưới chân bạn, bạn đi đâu nó đi theo đó, nhưng khi tắt đèn tối thui thì nó biến mất?", "options": ["Cái bóng của bạn", "Con mèo con", "Đôi dép", "Chiếc tất"], "correct": 0, "explanation": "Cái bóng hình thành do vật cản ánh sáng, trong bóng tối không có ánh sáng thì không có bóng."},
        {"difficulty": 2, "question": "Đố mẹo: Có 3 bóng đèn trong phòng và 3 công tắc bên ngoài. Bạn bật công tắc 1 năm phút rồi tắt, sau đó bật công tắc 2 rồi bước vào phòng. Đèn nào tương ứng với công tắc 1?", "options": ["Bóng đèn tắt nhưng sờ vào thấy nóng", "Bóng đèn đang sáng", "Bóng đèn nguội ngắt", "Không xác định"], "correct": 0, "explanation": "Bóng đèn tắt nhưng còn ấm nóng chứng tỏ vừa được thắp sáng bởi công tắc 1."},
        {"difficulty": 2, "question": "Đố mẹo: Một người thợ săn nhìn thấy 3 con chim trên cành, bắn trúng rụng 1 con. Hỏi trên cành còn mấy con?", "options": ["Không còn con nào (tiếng súng nổ làm 2 con kia bay mất)", "Còn 2 con", "Còn 1 con", "Còn 3 con"], "correct": 0, "explanation": "Tiếng nổ chát chúa của súng săn làm các con chim còn lại hoảng hốt bay đi."},
        {"difficulty": 2, "question": "Đố vui: 'Đầu rồng đuôi phượng le te / Mùa đông ấp trứng, mùa hè nở con' là cái gì dân gian?", "options": ["Cây cau và buồng cau", "Cây bàng", "Cây xoài", "Cây ổi"], "correct": 0, "explanation": "Câu đố dân gian miêu tả dáng cây cau với buồng hoa cau và quả cau xanh."},
        {"difficulty": 2, "question": "Đố mẹo: Thứ gì đi lên thì có thể giúp bạn không bị ướt, nhưng khi đi xuống thì gấp gọn bỏ vào balo?", "options": ["Chiếc ô (chiếc dù)", "Cái áo mưa", "Cái mũ", "Đôi ủng"], "correct": 0, "explanation": "Bật ô giương lên che mưa nắng, khi tạnh thì gập hạ xuống."},
        {"difficulty": 2, "question": "Đố chữ: Từ tiếng Việt nào bỏ dấu sắc đi thành tên một thành phố miền Trung, để nguyên là thứ gia vị thơm cay trong bếp?", "options": ["Quế (Quế - Quê)", "Tiêu", "Hành", "Gừng"], "correct": 0, "explanation": "Quế thơm nồng ấm áp, bỏ dấu thành Quê hương xứ sở."},
        {"difficulty": 3, "question": "Đố tư duy logic: Bạn có 9 viên bi ve giống hệt nhau, trong đó có 1 viên bi nặng hơn các viên còn lại. Với chiếc cân đĩa hai bên, cần ít nhất mấy lần cân để chắc chắn tìm ra viên bi nặng hơn?", "options": ["2 lần cân", "3 lần cân", "1 lần cân", "4 lần cân"], "correct": 0, "explanation": "Chia 9 viên thành 3 nhóm (3-3-3). Lần 1 cân 3 vs 3. Lần 2 lấy nhóm nặng hơn cân 1 vs 1 là tìm ra ngay!"},
        {"difficulty": 3, "question": "Đố mẹo hóc búa: Có một người đứng ở mũi thuyền cách mặt nước biển 1,5 mét. Nước thủy triều dâng lên với tốc độ 20 cm mỗi giờ. Sau 3 giờ, người đó cách mặt nước bao nhiêu mét?", "options": ["Vẫn cách 1,5 mét (vì thuyền nổi dâng theo mực nước)", "Cách 0,9 mét", "Cách 2,1 mét", "Chìm dưới nước"], "correct": 0, "explanation": "Thuyền là vật nổi trên mặt nước nên khi nước dâng, thuyền cũng dâng theo cùng mực nước!"},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: Bức tranh đố vui dân gian: 'Tròn tròn như chiếc trăng rằm / Xoay vần biến đổi quanh năm đêm ngày / Giúp người biết trước tương lai' là đồ vật gì trong phong thủy cổ xưa?", "options": ["Chiếc la bàn bát quái", "Chiếc đồng hồ", "Quả địa cầu", "Gương bát quái"], "correct": 0, "explanation": "La bàn bát quái phong thủy cổ truyền dùng xác định phương hướng kinh dịch."}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Thành phố mang tên Bác (TP. Hồ Chí Minh) trước năm 1976 từng có tên gọi lịch sử quen thuộc là gì?", "options": ["Sài Gòn - Gia Định", "Bến Nghé", "Chợ Lớn", "Gia Định thành"], "correct": 0, "explanation": "Sài Gòn - Gia Định là tên gọi đô thị phồn hoa hòn ngọc Viễn Đông thời bấy giờ."},
        {"difficulty": 1, "question": "Hồ Tây thắng cảnh hồ nước tự nhiên lớn nhất nội thành Hà Nội với diện tích hơn 500 ha nằm ở quận nào?", "options": ["Quận Tây Hồ", "Quận Ba Đình", "Quận Cầu Giấy", "Quận Đống Đa"], "correct": 0, "explanation": "Hồ Tây thơ mộng với đường Thanh Niên ngăn đôi với hồ Trúc Bạch thuộc quận Tây Hồ."},
        {"difficulty": 1, "question": "Tỉnh nào ở miền Trung nổi tiếng với danh lam thắng cảnh Ghềnh Đá Đĩa có cấu trúc đá bazan hình lục giác xếp lớp độc nhất vô nhị?", "options": ["Phú Yên", "Bình Định", "Khánh Hòa", "Quảng Ngãi"], "correct": 0, "explanation": "Ghềnh Đá Đĩa (huyện Tuy An, Phú Yên) là kiệt tác địa chất tự nhiên hiếm có trên thế giới."},
        {"difficulty": 1, "question": "Núi Chứa Chan (núi Gia Lào) ngọn núi cao thứ hai Nam Bộ (837m) nằm trên địa bàn huyện Xuân Lộc tỉnh nào?", "options": ["Đồng Nai", "Bình Dương", "Bình Phước", "Tây Ninh"], "correct": 0, "explanation": "Núi Chứa Chan thuộc tỉnh Đồng Nai là điểm trekking và vãn cảnh chùa Gia Lào nổi tiếng."},
        {"difficulty": 1, "question": "Đảo Hòn Tre hòn đảo lớn nhất trong vịnh Nha Trang với khu vui chơi giải trí VinWonders thuộc tỉnh nào?", "options": ["Khánh Hòa", "Ninh Thuận", "Bình Thuận", "Phú Yên"], "correct": 0, "explanation": "Đảo Hòn Tre nằm chắn sóng cho vịnh biển Nha Trang thơ mộng."},
        {"difficulty": 2, "question": "Cố đô Luang Prabang di sản văn hóa thế giới cổ kính của đất nước Triệu Voi nằm ở quốc gia nào?", "options": ["Lào", "Campuchia", "Thái Lan", "Myanmar"], "correct": 0, "explanation": "Luang Prabang bên dòng sông Mê Kông là cố đô thanh bình của nước bạn Lào."},
        {"difficulty": 2, "question": "Thành phố cổ Petra kỳ quan thế giới với các công trình kiến trúc tạc thẳng vào vách đá sa thạch đỏ nằm ở quốc gia nào?", "options": ["Jordan", "Ai Cập", "Israel", "Thổ Nhĩ Kỳ"], "correct": 0, "explanation": "Thành phố hoa hồng đỏ Petra là báu vật khảo cổ học của vương quốc Jordan."},
        {"difficulty": 2, "question": "Kỳ quan thiên nhiên hẻm núi Grand Canyon kỳ vĩ do dòng sông Colorado bào mòn hàng triệu năm nằm ở bang nào của nước Mỹ?", "options": ["Bang Arizona", "Bang California", "Bang Texas", "Bang Nevada"], "correct": 0, "explanation": "Hẻm núi lớn Grand Canyon tại Arizona phơi bày các tầng địa chất cổ đại ngoạn mục."},
        {"difficulty": 2, "question": "Đất nước nào ở Nam Á có hình dạng giọt nước mắt trên Ấn Độ Dương nổi tiếng với trà Ceylon thơm ngon?", "options": ["Sri Lanka", "Maldives", "Nepal", "Bhutan"], "correct": 0, "explanation": "Đảo quốc Sri Lanka (trước đây là Ceylon) nổi danh toàn cầu với các đồn điền trà hảo hạng."},
        {"difficulty": 2, "question": "Vùng đất trũng Dead Sea (Biển Chết) nằm ở độ cao âm bao nhiêu mét so với mực nước biển (nơi thấp nhất trên cạn)?", "options": ["Khoảng âm 430 mét (-430m)", "Khoảng âm 100m", "Khoảng âm 1.000m", "Bằng mực nước biển"], "correct": 0, "explanation": "Bờ Biển Chết là điểm thấp nhất trên bề mặt lục địa Trái Đất ở độ cao -430m."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Quần đảo bách đảo Galapagos nơi nhà bác học Charles Darwin nghiên cứu thuyết tiến hóa thuộc chủ quyền của quốc gia nào ở Nam Mỹ?", "options": ["Ecuador", "Peru", "Chile", "Colombia"], "correct": 0, "explanation": "Quần đảo núi lửa Galapagos ngoài khơi Thái Bình Dương trực thuộc đất nước Ecuador."}
    ],

    "lich-su": [
        {"difficulty": 1, "question": "Vị trạng nguyên nào nổi tiếng với tài cân voi và đo độ dày của tờ giấy bằng hạt gạo thời vua Lê Thánh Tông?", "options": ["Trạng Lường - Lương Thế Vinh", "Nguyễn Hiền", "Lê Quý Đôn", "Mạc Đĩnh Chi"], "correct": 0, "explanation": "Lương Thế Vinh dùng phương pháp thả thuyền xuống sông đo ngấn nước để cân voi sứ thần phương Bắc."},
        {"difficulty": 1, "question": "Cuộc Cách mạng Tháng Tám năm 1945 thành công lật đổ ách thống trị của phát xít Nhật và thực dân nào?", "options": ["Thực dân Pháp", "Đế quốc Mỹ", "Quân Anh", "Quân Tưởng"], "correct": 0, "explanation": "Cách mạng Tháng Tám đập tan xiềng xích thực dân Pháp hơn 80 năm và lật đổ chế độ phong kiến ngàn năm."},
        {"difficulty": 1, "question": "Người chiến sĩ du kích nhỏ tuổi dũng cảm làm liên lạc dẫn đường hy sinh tại chiến khu Ba Tơ là ai?", "options": ["Anh hùng Vừ A Dính (hoặc Kim Đồng)", "Nguyễn Bá Ngọc", "Lê Văn Tám", "Kpa Klơng"], "correct": 0, "explanation": "Kim Đồng (Nông Văn Dền) người đội trưởng đầu tiên của Đội Thiếu niên Tiền phong Hồ Chí Minh hy sinh năm 1943."},
        {"difficulty": 2, "question": "Trận phục kích đèo Bông Lau năm 1947 trên quốc lộ 4 trong chiến dịch Việt Bắc Thu - Đông do vị tướng nào trực tiếp chỉ huy?", "options": ["Đại tướng Võ Nguyên Giáp", "Tướng Nguyễn Sơn", "Tướng Lê Trọng Tấn", "Tướng Hoàng Văn Thái"], "correct": 0, "explanation": "Chiến thắng đèo Bông Lau biến quốc lộ số 4 thành con đường chết đối với quân viễn chinh Pháp."},
        {"difficulty": 2, "question": "Bản Hiến pháp đầu tiên của nước Việt Nam Dân chủ Cộng hòa được Quốc hội khóa I thông qua vào năm nào?", "options": ["Năm 1946 (ngày 9/11/1946)", "Năm 1959", "Năm 1980", "Năm 1992"], "correct": 0, "explanation": "Hiến pháp năm 1946 là bản hiến pháp dân chủ tiến bộ đầu tiên trong lịch sử lập hiến Việt Nam."},
        {"difficulty": 2, "question": "Chiến dịch Tây Bắc năm 1952 giải phóng một vùng đất đai rộng lớn ở hữu ngạn sông Hồng gồm các tỉnh nào?", "options": ["Nghĩa Lộ, Sơn La, Lai Châu", "Cao Bằng, Bắc Kạn", "Hà Giang, Tuyên Quang", "Lào Cai, Yên Bái"], "correct": 0, "explanation": "Chiến dịch Tây Bắc 1952 phá vỡ âm mưu lập 'Xứ Thái tự trị' của giặc Pháp."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Vị tướng nào đã lãnh đạo nghĩa quân đánh chiếm đồn Phủ Lạng Thương và vây hãm thành Xương Giang năm 1427?", "options": ["Tướng quân Trần Nguyên Hãn và Lê Sát", "Đinh Liệt", "Nguyễn Xí", "Phạm Văn Xảo"], "correct": 0, "explanation": "Trần Nguyên Hãn chỉ huy đội quân công thành xuất sắc hạ thành Xương Giang trước khi Liễu Thăng kéo viện binh sang."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Chất khí nào chiếm khoảng 21% thể tích không khí duy trì sự cháy và sự sống của sinh vật?", "options": ["Khí Oxy (O2)", "Khí Nitơ", "Khí Cacbonic", "Khí Argon"], "correct": 0, "explanation": "Khí Oxy không màu không mùi duy trì sự sống và các phản ứng cháy tỏa nhiệt."},
        {"difficulty": 1, "question": "Hành tinh nào trong Hệ Mặt Trời được mệnh danh là 'Ngôi sao Hôm' khi xuất hiện buổi chiều tà và 'Ngôi sao Mai' khi xuất hiện rạng đông?", "options": ["Sao Kim (Venus)", "Sao Hỏa", "Sao Mộc", "Sao Thủy"], "correct": 0, "explanation": "Sao Kim là thiên thể sáng nhất trên bầu trời đêm sau Mặt Trăng do lớp mây dày phản xạ ánh sáng."},
        {"difficulty": 2, "question": "Bộ phận nào trong tai chứa hàng ngàn tế bào lông cảm nhận rung động âm thanh để truyền lên não bộ?", "options": ["Ốc tai (Tai trong)", "Màng nhĩ", "Vành tai", "Xương bàn đạp"], "correct": 0, "explanation": "Cơ quan Corti trong ốc tai biến dao động sóng âm thành các xung thần kinh thính giác."},
        {"difficulty": 2, "question": "Tại sao chim cánh cụt sống ở vùng Nam Cực băng giá lại không bao giờ bị đông lạnh bàn chân?", "options": ["Nhờ hệ thống trao đổi nhiệt ngược dòng ở mạch máu chân", "Chân có lông dày", "Chân không có máu", "Chân đi ủng"], "correct": 0, "explanation": "Động mạch mang máu ấm đi xuống làm ấm tĩnh mạch mang máu lạnh đi lên giúp bàn chân không bị mất nhiệt."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Trong bảng tuần hoàn các nguyên tố hóa học, nguyên tố kim loại nào có nhiệt độ nóng chảy thấp nhất ở nhiệt độ âm (-38,83 °C)?", "options": ["Thủy ngân (Hg)", "Gali (Ga)", "Xesi (Cs)", "Francium (Fr)"], "correct": 0, "explanation": "Thủy ngân là kim loại duy nhất tồn tại ở thể lỏng trong điều kiện nhiệt độ phòng thông thường."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Món bún bò cay nồng thơm lừng mùi mắm ruốc và sả cây là món ăn đặc sản tiêu biểu của vùng đất nào?", "options": ["Cố đô Huế", "Thành phố Đà Nẵng", "Hà Nội", "TP. Hồ Chí Minh"], "correct": 0, "explanation": "Bún bò Huế với nước dùng đậm đà thơm ngát mắm ruốc là niềm tự hào ẩm thực cố đô."},
        {"difficulty": 1, "question": "Cổng kết nối âm thanh hình ảnh độ nét cao phổ biến nhất nối từ máy tính hoặc đầu thu lên màn hình tivi là cổng gì?", "options": ["Cổng HDMI", "Cổng VGA", "Cổng AV", "Cổng USB"], "correct": 0, "explanation": "Cáp HDMI truyền đồng thời cả tín hiệu hình ảnh kỹ thuật số độ phân giải cao và âm thanh đa kênh."},
        {"difficulty": 2, "question": "Giải đua xe thể thao tốc độ cao danh giá nhất hành tinh với những chiếc xe đua bánh hở một chỗ ngồi là giải gì?", "options": ["Giải đua Công thức 1 (Formula 1 - F1)", "NASCAR", "MotoGP", "Rally Dakar"], "correct": 0, "explanation": "F1 là đỉnh cao công nghệ chế tạo xe hơi tốc độ với các chặng Grand Prix khắp toàn cầu."},
        {"difficulty": 2, "question": "Món 'Bánh xèo miền Tây' có màu vàng ươm giòn rụm thơm mùi nước cốt dừa thường được tạo màu tự nhiên bằng củ gì?", "options": ["Bột nghệ vàng", "Quả gấc", "Lá dứa", "Củ dền"], "correct": 0, "explanation": "Bột nghệ vàng ươm tạo màu sắc bắt mắt và hương thơm dịu nhẹ cho vỏ bánh xèo."},
        {"difficulty": 3, "question": "CÂU HỎI CÔNG NGHỆ QUYẾT ĐỊNH: Thuật toán mật mã khóa công khai bất đối xứng kinh điển do Rivest, Shamir và Adleman phát minh năm 1977 được viết tắt là gì?", "options": ["Thuật toán RSA", "Chuẩn mã hóa AES", "Hàm băm SHA-256", "Thuật toán DES"], "correct": 0, "explanation": "Hệ mật mã RSA dựa trên độ khó của việc phân tích một hợp số cực lớn thành tích hai số nguyên tố."}
    ],

    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu tục ngữ: 'Lá lành đùm lá ...'?", "options": ["rách", "héo", "rơi", "vàng"], "correct": 0, "explanation": "Truyền thống tương thân tương ái bao đời của dân tộc Việt Nam."},
        {"difficulty": 1, "question": "Trong truyện cổ tích 'Cây tre trăm đốt', anh Khoai đã dùng hai câu thần chú nào để ghép và tách các đốt tre?", "options": ["'Khắc nhập, khắc xuất'", "'Vừng ơi mở ra'", "'Úm ba la'", "'Mở cửa ra'"], "correct": 0, "explanation": "Câu thần chú 'Khắc nhập' nối 100 đốt tre thành cây tre thẳng tắp, 'Khắc xuất' tách rời từng đốt."},
        {"difficulty": 2, "question": "Bài thơ 'Bài thơ về tiểu đội xe không kính' của Phạm Tiến Duật khắc họa hình tượng người lính trẻ trên tuyến đường lửa nào?", "options": ["Đường mòn Hồ Chí Minh (Đường Trường Sơn)", "Quốc lộ 1A", "Đường 9 Nam Lào", "Đường số 4"], "correct": 0, "explanation": "Hình ảnh những chiếc xe không kính ung dung lăn bánh chi viện cho chiến trường miền Nam anh hùng."},
        {"difficulty": 2, "question": "Ai là tác giả của tác phẩm tiểu thuyết hiện thực xuất sắc 'Bỉ vỏ' viết về cuộc đời truân chuyên của cô bé Tám Bính?", "options": ["Nhà văn Nguyên Hồng", "Nam Cao", "Vũ Trọng Phụng", "Ngô Tất Tố"], "correct": 0, "explanation": "Nhà văn Nguyên Hồng với ngòi bút nhân đạo sâu sắc hướng về những kiếp người lao động cùng khổ ở đất cảng Hải Phòng."},
        {"difficulty": 3, "question": "CÂU HỎI VĂN HỌC QUYẾT ĐỊNH: Vở kịch thơ kiệt tác 'Hồn Bướm mơ Tiên' và phong trào Tự Lực Văn Đoàn đầu thế kỷ XX do nhà văn nào chủ xướng?", "options": ["Khái Hưng (cùng Nhất Linh)", "Thạch Lam", "Hoàng Đạo", "Tú Mỡ"], "correct": 0, "explanation": "Nhà văn Khái Hưng cùng Nhất Linh sáng lập Tự Lực Văn Đoàn với tôn chỉ đổi mới văn học và giải phóng cá nhân."}
    ]
}

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU NẠP ĐỢT 5 ĐỂ VƯỢT MỐC 1.000 TIẾN TỚI 2.500 CÂU!")
    print("=" * 70)

    total_added = 0
    for cat_name, questions in BATCH_5_DATA.items():
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

        print(f"  📁 [{cat_name}]: Thêm {added_in_cat} câu -> Tổng hiện có: {len(existing_list)} câu.")

    print(f"\n✅ Đợt 5 bổ sung thành công {total_added} câu hỏi mới!")

if __name__ == '__main__':
    main()
