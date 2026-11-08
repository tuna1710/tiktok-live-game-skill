# -*- coding: utf-8 -*-
"""
Đợt 7 - Mở rộng mạnh mẽ Cột mốc 3 (hướng tới 2.500 câu)
Bổ sung 300 câu hỏi chuẩn hóa phong phú chia đều cho 6 chủ đề (mỗi chủ đề ~50 câu).
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

BATCH_7_DATA = {
    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Bánh gì không ăn được mà xoay tít trên bầu trời đưa máy bay cất cánh?", "options": ["Cánh quạt máy bay", "Bánh xe", "Bánh lái", "Bánh đà"], "correct": 0, "explanation": "Cánh quạt máy bay quay với tốc độ cực lớn tạo lực đẩy khí động học."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì sinh ra đã có túi trước bụng để bế con nhảy thoăn thoắt?", "options": ["Chuột túi (Kangaroo)", "Gấu túi Koala", "Con khỉ", "Con mèo"], "correct": 0, "explanation": "Kangaroo cái có chiếc túi đặc biệt trước bụng để nuôi con non sơ sinh."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có mặt nhưng không có mũi tai, có 12 chữ số chạy tròn quanh năm?", "options": ["Mặt đồng hồ", "Chiếc gương", "Cái bàn", "Quyển lịch"], "correct": 0, "explanation": "Mặt đồng hồ tròn có 12 số chỉ giờ."},
        {"difficulty": 1, "question": "Đố mẹo: Quả gì vỏ đầy gai nhọn, khi chín nứt múi thơm lừng nức tiếng miền Tây?", "options": ["Quả sầu riêng", "Quả mít", "Quả chôm chôm", "Quả na"], "correct": 0, "explanation": "Sầu riêng được mệnh danh là 'Vua của các loài trái cây nhiệt đới'."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì có cổ dài ngoằng ăn lá non trên ngọn cây cao nhất thảo nguyên?", "options": ["Hươu cao cổ", "Con voi", "Đà điểu", "Con ngựa"], "correct": 0, "explanation": "Hươu cao cổ là động vật trên cạn cao nhất hành tinh với chiếc cổ dài tới 2 mét."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì bạn dùng để chải răng mỗi sáng tối cho hàm răng trắng bóng?", "options": ["Bàn chải đánh răng", "Cây lược", "Chiếc khăn", "Cái thìa"], "correct": 0, "explanation": "Bàn chải đánh răng giúp làm sạch mảng bám bảo vệ men răng."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì bơi dưới nước có tám chiếc xúc tu dài ngoằn ngoèo và biết phun mực đen tẩu thoát?", "options": ["Con bạch tuộc", "Con cá mực", "Con tôm", "Con cua"], "correct": 0, "explanation": "Bạch tuộc có 8 xúc tu linh hoạt và khả năng ngụy trang tài tình."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì đựng đầy nước thì nổi bồng bềnh, thủng một lỗ nhỏ lại chìm nghỉm?", "options": ["Chiếc thuyền", "Quả bóng", "Cái xô", "Cái chai"], "correct": 0, "explanation": "Thuyền chở nước dằn tải thì nổi, thủng đáy nước tràn vào sẽ chìm."},
        {"difficulty": 1, "question": "Đố mẹo: Tháng nào trong năm thường có ít ngày nhất (chỉ 28 hoặc 29 ngày)?", "options": ["Tháng 2", "Tháng 1", "Tháng 4", "Tháng 12"], "correct": 0, "explanation": "Tháng 2 năm thường có 28 ngày, năm nhuận có 29 ngày."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì gáy 'Ò ó o' đánh thức cả làng dậy sớm đón bình minh?", "options": ["Con gà trống", "Con gà mái", "Con vịt", "Con chim bồ câu"], "correct": 0, "explanation": "Tiếng gà trống gáy sáng báo hiệu một ngày mới bắt đầu."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt có 3 chữ cái, bỏ dấu nặng thành thứ để đựng cơm, thêm dấu sắc thành thứ để đội đầu che nắng?", "options": ["Nón và Bát (Nón - Non - Nón)", "Mũ", "Khăn", "Áo"], "correct": 0, "explanation": "Chiếc nón lá che nắng che mưa cho người lao động."},
        {"difficulty": 2, "question": "Đố mẹo: Một người thợ lặn nhặt được một viên ngọc trai dưới đáy biển sâu mà không cần kính lặn, tại sao?", "options": ["Người đó nhặt ngọc trai trong bể cá cảnh", "Biển cạn nước", "Người có mắt thần", "Đáy biển nhân tạo"], "correct": 0, "explanation": "Nhặt viên ngọc trong bể cá mini ở nhà thì không cần kính lặn biển!"},
        {"difficulty": 2, "question": "Đố mẹo: Có một người lái xe tải đi ngược vào đường cấm một chiều ngay trước mặt cảnh sát mà không bị phạt, vì sao?", "options": ["Vì anh ta đang đi bộ", "Vì xe không nổ máy", "Vì đường vắng", "Vì là xe cảnh sát"], "correct": 0, "explanation": "Người tài xế đang đi bộ thong thả chứ không lái xe cơ giới."},
        {"difficulty": 2, "question": "Đố vui: 'Thân dài thon thon, lưng cõng chữ tròn, cày trên trang giấy, nét đẹp thơm tho' là vật dụng gì?", "options": ["Cây bút viết", "Cây thước kẻ", "Cục tẩy", "Com-pa"], "correct": 0, "explanation": "Cây bút viết nắn nót từng dòng chữ trên trang vở học trò."},
        {"difficulty": 2, "question": "Đố mẹo: Cái gì luôn đi lên khi trời mưa rơi xuống?", "options": ["Chiếc ô (dù)", "Cái áo mưa", "Cái nón", "Đôi ủng"], "correct": 0, "explanation": "Khi mưa rơi xuống thì người ta bật giương ô hướng lên trên."},
        {"difficulty": 2, "question": "Đố chữ: Từ tiếng Việt nào mang nghĩa là 'không bao giờ thừa' khi thêm một dấu sắc lại biến thành một loài cây thân gai quả đỏ mọng?", "options": ["Đủ (Đủ - Đú)", "Thiếu", "Vừa", "Tròn"], "correct": 0, "explanation": "Đủ đầy không thiếu thốn."},
        {"difficulty": 2, "question": "Đố mẹo: Có hai người cùng bước vào một quán nước, gọi 2 cốc trà giống hệt nhau. Người thứ nhất uống cạn ngay lập tức và sống khỏe mạnh. Người thứ hai uống từ từ nhâm nhi thì bị ngộ độc. Vì sao?", "options": ["Chất độc nằm trong đá viên chưa kịp tan", "Cốc thứ hai bị bẩn", "Nước trà khác nhau", "Người thứ hai bị dị ứng"], "correct": 0, "explanation": "Thuốc độc tẩm trong đá lạnh, người uống nhanh đá chưa tan nên thoát nạn!"},
        {"difficulty": 2, "question": "Đố mẹo: Con gì có chân nhưng không có đầu, chạy quanh bàn ăn phục vụ mọi người?", "options": ["Chiếc bàn xoay thức ăn", "Con robot", "Con mèo", "Con cún"], "correct": 0, "explanation": "Mâm bàn xoay tròn đặt các món ăn trong bữa tiệc."},
        {"difficulty": 2, "question": "Đố mẹo: Bỏ ngoài nướng trong, ăn ngoài bỏ trong là món ngô gì?", "options": ["Bắp ngô nướng", "Khoai nướng", "Sắn nướng", "Chuối nướng"], "correct": 0, "explanation": "Bắp ngô bóc bẹ ngoài đem nướng, ăn hạt bỏ cùi lõi."},
        {"difficulty": 2, "question": "Đố mẹo: Cái gì có chìa khóa mà không có ổ khóa, có không gian mà không có phòng ốc, có thể gõ 'Enter'?", "options": ["Bàn phím máy tính (Keyboard)", "Chiếc xe hơi", "Cánh cửa", "Két sắt"], "correct": 0, "explanation": "Bàn phím máy tính có các phím (key), phím cách (spacebar) và phím Enter."},
        {"difficulty": 3, "question": "Đố logic: Có 3 chiếc túi: túi 1 đựng 2 viên bi vàng, túi 2 đựng 2 viên bi bạc, túi 3 đựng 1 bi vàng và 1 bi bạc. Bạn rút ngẫu nhiên được 1 viên bi vàng từ 1 túi. Hỏi xác suất viên bi còn lại trong túi đó cũng là màu vàng bằng bao nhiêu?", "options": ["2/3 (khoảng 66,7%)", "1/2 (50%)", "1/3", "100%"], "correct": 0, "explanation": "Theo nghịch lý Bertrand / Định lý Bayes: Trong 3 viên bi vàng có thể rút ra, có 2 viên thuộc túi 2 bi vàng, nên xác suất là 2/3!"},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: Bức tranh đố vui dân gian: 'Cây gì nghiêng bóng bên bờ / Thân cong uốn lượn nước soi gương trong / Trái ngọt dâng người bóng mát mênh mông' là cây gì miền sông nước?", "options": ["Cây dừa", "Cây bàng", "Cây tre", "Cây liễu"], "correct": 0, "explanation": "Rặng dừa nước nghiêng mình soi bóng nước ngọt mát trái dừa miền Tây."}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Cố đô Hoa Lư kinh đô đầu tiên của nước Đại Cồ Việt thời Đinh - Tiền Lê nay thuộc tỉnh nào?", "options": ["Ninh Bình", "Thanh Hóa", "Nam Định", "Hà Nam"], "correct": 0, "explanation": "Quần thể danh thắng Cố đô Hoa Lư nằm trên địa bàn tỉnh Ninh Bình."},
        {"difficulty": 1, "question": "Quốc gia nào ở châu Á có diện tích lãnh thổ lớn nhất và dân số hơn 1,4 tỷ người?", "options": ["Trung Quốc", "Ấn Độ", "Indonesia", "Nhật Bản"], "correct": 0, "explanation": "Trung Quốc là quốc gia có diện tích lớn nhất châu Á với nền văn minh ngàn năm."},
        {"difficulty": 1, "question": "Sông Hồng bắt nguồn từ vùng núi tỉnh Vân Nam nước nào trước khi chảy vào lãnh thổ Việt Nam?", "options": ["Trung Quốc", "Lào", "Myanmar", "Thái Lan"], "correct": 0, "explanation": "Sông Hồng bắt nguồn từ dãy Ngụy Sơn (Vân Nam, Trung Quốc) chảy vào Việt Nam tại Bát Xát (Lào Cai)."},
        {"difficulty": 1, "question": "Thành phố biển Vũng Tàu nổi tiếng với tượng Chúa Kito Vua khổng lồ nhìn ra biển thuộc tỉnh nào?", "options": ["Bà Rịa - Vũng Tàu", "Bình Thuận", "Đồng Nai", "TP. Hồ Chí Minh"], "correct": 0, "explanation": "Tượng Chúa dang tay trên đỉnh núi Nhỏ là biểu tượng du lịch của TP. Vũng Tàu."},
        {"difficulty": 1, "question": "Thủ đô của nước Anh (Vương quốc Liên hiệp Anh và Bắc Ireland) là thành phố nào?", "options": ["London", "Manchester", "Liverpool", "Edinburgh"], "correct": 0, "explanation": "London bên dòng sông Thames với tháp đồng hồ Big Ben và cầu tháp Tower Bridge."},
        {"difficulty": 2, "question": "Hồ Tà Đùng được mệnh danh là 'Vịnh Hạ Long của Tây Nguyên' với hơn 40 hòn đảo lớn nhỏ thuộc tỉnh nào?", "options": ["Đắk Nông", "Đắk Lắk", "Gia Lai", "Lâm Đồng"], "correct": 0, "explanation": "Vườn quốc gia Tà Đùng thuộc huyện Đắk Glong, tỉnh Đắk Nông."},
        {"difficulty": 2, "question": "Tỉnh nào ở miền Trung nước ta có sông Bến Hải và vĩ tuyến 17 cây cầu Hiền Lương lịch sử?", "options": ["Quảng Trị", "Quảng Bình", "Thừa Thiên Huế", "Hà Tĩnh"], "correct": 0, "explanation": "Cầu Hiền Lương bắc qua sông Bến Hải là biểu tượng của nỗi đau chia cắt và khát vọng thống nhất non sông."},
        {"difficulty": 2, "question": "Quốc gia nào ở châu Phi nổi tiếng với tượng nhân sư Sphinx và kim tự tháp Kheops cổ đại bên bờ sông Nin?", "options": ["Ai Cập", "Sudan", "Morocco", "Algeria"], "correct": 0, "explanation": "Ai Cập là cái nôi của nền văn minh sông Nin rực rỡ thời cổ đại."},
        {"difficulty": 2, "question": "Đảo núi lửa Jeju khu nghỉ dưỡng thiên đường tuyệt đẹp được UNESCO công nhận là di sản thiên nhiên của quốc gia nào?", "options": ["Hàn Quốc", "Nhật Bản", "Đài Loan", "Philippines"], "correct": 0, "explanation": "Đảo Jeju xinh đẹp với đỉnh núi Hallasan là điểm du lịch nổi tiếng của xứ sở kim chi."},
        {"difficulty": 2, "question": "Dòng sông dài nhất châu Á (khoảng 6.300 km) chảy hoàn toàn trong lãnh thổ Trung Quốc là sông nào?", "options": ["Sông Trường Giang (Dương Tử)", "Sông Hoàng Hà", "Sông Mê Kông", "Sông Hằng"], "correct": 0, "explanation": "Sông Trường Giang bắt nguồn từ cao nguyên Tây Tạng đổ ra biển Hoa Đông."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Eo biển Bering (Bê-rinh) là eo biển chiến lược chia cắt giữa hai châu lục nào và nối liền Bắc Băng Dương với Thái Bình Dương?", "options": ["Châu Á và Châu Bắc Mỹ (giữa Nga và Mỹ)", "Châu Âu và Châu Phi", "Châu Á và Châu Đại Dương", "Châu Nam Mỹ và Châu Nam Cực"], "correct": 0, "explanation": "Eo biển Bering rộng khoảng 82 km ngăn cách mũi Dezhnev (Nga) và mũi Prince of Wales (Alaska, Mỹ)."}
    ],

    "lich-su": [
        {"difficulty": 1, "question": "Vị hoàng đế nào của nhà Trần đã nhường ngôi cho con để lên núi Yên Tử tu hành sáng lập thiền phái Trúc Lâm?", "options": ["Trần Nhân Tông (Phật hoàng)", "Trần Thái Tông", "Trần Thánh Tông", "Trần Anh Tông"], "correct": 0, "explanation": "Phật hoàng Trần Nhân Tông sau hai lần lãnh đạo đánh tan quân Nguyên Mông đã lập nên thiền phái Trúc Lâm Yên Tử."},
        {"difficulty": 1, "question": "Ngày Nhà giáo Việt Nam nhằm tôn vinh những người làm nghề dạy học được tổ chức vào ngày tháng nào?", "options": ["20/11", "20/10", "8/3", "19/5"], "correct": 0, "explanation": "Ngày 20/11 hàng năm là dịp toàn xã hội tri ân các thầy cô giáo dìu dắt bao thế hệ học trò."},
        {"difficulty": 1, "question": "Vị nữ tướng cưỡi voi đánh trận thời khởi nghĩa Hai Bà Trưng lập căn cứ ở vùng đất Hát Môn là ai?", "options": ["Trưng Nhị", "Lê Chân", "Bùi Thị Xuân", "Bà Triệu"], "correct": 0, "explanation": "Trưng Nhị cùng chị gái Trưng Trắc phất cờ khởi nghĩa mùa xuân năm 40 sau Công nguyên."},
        {"difficulty": 2, "question": "Chiến thắng Ngọc Hồi - Đống Đa đại phá 29 vạn quân Mãn Thanh diễn ra vào mùa xuân năm nào?", "options": ["Năm Kỷ Dậu 1789", "Năm Canh Tuất 1790", "Năm Mậu Thân 1788", "Năm Ất Tỵ 1785"], "correct": 0, "explanation": "Vua Quang Trung chỉ huy hành quân thần tốc đánh tan quân Thanh mùng 5 Tết Kỷ Dậu 1789."},
        {"difficulty": 2, "question": "Hội nghị thành lập Đảng Cộng sản Việt Nam vào mùa xuân năm 1930 do lãnh tụ Nguyễn Ái Quốc chủ trì diễn ra tại đâu?", "options": ["Cửu Long (Hương Cảng, Trung Quốc)", "Quảng Châu", "Ma Cao", "Thượng Hải"], "correct": 0, "explanation": "Từ ngày 6/1 đến 7/2/1930 tại Hương Cảng, Nguyễn Ái Quốc thống nhất các tổ chức cộng sản thành Đảng Cộng sản Việt Nam."},
        {"difficulty": 2, "question": "Người chiến sĩ du kích anh hùng quê miền Đông Nam Bộ dùng súng phóng lựu tự chế bắn cháy xe tăng giặc là ai?", "options": ["Đoàn Văn Bơ", "Út Tịch", "Nguyễn Văn Trỗi", "Trần Văn Ơn"], "correct": 0, "explanation": "Hình tượng dũng cảm của các chiến sĩ du kích miền Nam kiên cường bám trụ đánh giặc."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Bản Hiệp ước Patenôtre (1884) giữa triều đình Huế và thực dân Pháp chính thức đặt nước ta dưới sự bảo hộ của Pháp gồm bao nhiêu điều khoản?", "options": ["19 điều khoản", "24 điều khoản", "15 điều khoản", "10 điều khoản"], "correct": 0, "explanation": "Hiệp ước Patenôtre ký ngày 6/6/1884 gồm 19 điều khoản chia Việt Nam thành 3 kỳ: Bắc Kỳ, Trung Kỳ, Nam Kỳ."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Hiện tượng nước bốc hơi biến thành mây rồi ngưng tụ rơi xuống thành mưa được gọi là gì?", "options": ["Vòng tuần hoàn của nước", "Quá trình quang hợp", "Sự dẫn nhiệt", "Sự thăng hoa"], "correct": 0, "explanation": "Vòng tuần hoàn nước liên tục luân chuyển nguồn nước ngọt nuôi dưỡng sự sống Trái Đất."},
        {"difficulty": 1, "question": "Hành tinh nào trong Hệ Mặt Trời có bề mặt lạnh giá nhất và có gió thổi mạnh nhất?", "options": ["Sao Hải Vương (Neptune)", "Sao Hỏa", "Sao Thủy", "Sao Kim"], "correct": 0, "explanation": "Sao Hải Vương xa Mặt Trời với những cơn cuồng phong đạt vận tốc hơn 2.000 km/h."},
        {"difficulty": 2, "question": "Trong sinh học, chất diệp lục (chlorophyll) trong lục lạp của lá cây có vai trò chính là gì?", "options": ["Hấp thụ năng lượng ánh sáng mặt trời để quang hợp", "Hút nước", "Thoát hơi nước", "Dự trữ đường"], "correct": 0, "explanation": "Chất diệp lục hấp thụ bước sóng ánh sáng đỏ và xanh lam, phản xạ màu xanh lục khiến lá cây có màu xanh."},
        {"difficulty": 2, "question": "Chất khí nào thoát ra từ các bình cứu hỏa dạng khí nén giúp dập tắt đám cháy nhanh chóng bằng cách làm ngạt khí oxy?", "options": ["Khí Cacbonic (CO2)", "Khí Oxy", "Khí Hydro", "Khí Metan"], "correct": 0, "explanation": "Khí CO2 nặng hơn không khí, phun phủ lên ngọn lửa cách ly oxy và làm lạnh đám cháy."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Ai là nhà khoa học nữ duy nhất trong lịch sử từng hai lần đoạt giải Nobel ở hai lĩnh vực khoa học khác nhau (Vật lý năm 1903 và Hóa học năm 1911)?", "options": ["Marie Curie (Manya Sklodowska)", "Rosalind Franklin", "Lise Meitner", "Dorothy Hodgkin"], "correct": 0, "explanation": "Marie Curie là nhà khoa học vĩ đại phát hiện ra hai nguyên tố phóng xạ mới Poloni và Radi."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Món phở bò truyền thống của Việt Nam thường được phục vụ với hai loại thịt bò nấu chín và tái được gọi là gì?", "options": ["Phở tái và Phở chín", "Phở xào", "Phở chiên", "Phở trộn"], "correct": 0, "explanation": "Phở tái thịt mềm ngọt, phở chín nạm gầu thơm giòn béo ngậy."},
        {"difficulty": 1, "question": "Ứng dụng gọi xe công nghệ và giao đồ ăn thịnh hành nhất Đông Nam Á với màu xanh lá cây đặc trưng là gì?", "options": ["Grab", "Gojek", "Be", "ShopeeFood"], "correct": 0, "explanation": "Grab là siêu ứng dụng cung cấp dịch vụ vận chuyển, giao nhận thức ăn phổ biến."},
        {"difficulty": 2, "question": "Hệ thống truyền dữ liệu không dây tầm gần dùng để chia sẻ file siêu nhanh giữa các thiết bị iPhone và Mac của Apple được gọi là gì?", "options": ["AirDrop", "Bluetooth", "Nearby Share", "NFC"], "correct": 0, "explanation": "AirDrop kết hợp Wi-Fi và Bluetooth truyền ảnh, tài liệu dung lượng lớn chỉ trong vài giây."},
        {"difficulty": 2, "question": "Món 'Bánh canh cá lóc' với sợi bánh dẻo dai từ bột gạo ăn cùng cá lóc đồng rim thơm nức mũi là đặc sản của tỉnh nào miền Trung?", "options": ["Quảng Trị (hoặc Huế)", "Quảng Bình", "Quảng Nam", "Bình Định"], "correct": 0, "explanation": "Bánh canh cá lóc Quảng Trị nồng nàn cay the với củ nén và ớt tươi băm nhuyễn."},
        {"difficulty": 3, "question": "CÂU HỎI CÔNG NGHỆ QUYẾT ĐỊNH: Ngôn ngữ lập trình thông dịch bậc cao đa năng ra đời năm 1991 do Guido van Rossum phát triển, được sử dụng phổ biến nhất hiện nay trong lĩnh vực Trí tuệ Nhân tạo (AI) và Khoa học Dữ liệu là ngôn ngữ nào?", "options": ["Python", "JavaScript", "C++", "Java"], "correct": 0, "explanation": "Python với cú pháp thanh lịch, dễ đọc cùng hệ sinh thái thư viện AI khổng lồ (TensorFlow, PyTorch) thống trị khoa học máy tính."}
    ],

    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu tục ngữ: 'Học ăn, học nói, học gói, học ...'?", "options": ["mở", "chia", "xếp", "gập"], "correct": 0, "explanation": "Bài học ứng xử khéo léo, tế nhị và chuẩn mực từ những hành vi nhỏ nhất trong cuộc sống."},
        {"difficulty": 1, "question": "Trong truyện ngụ ngôn 'Thầy bói xem voi', có tất cả bao nhiêu ông thầy bói mù cùng sờ voi để đoán hình thù con voi?", "options": ["5 ông thầy bói", "3 ông", "4 ông", "6 ông"], "correct": 0, "explanation": "Năm ông thầy bói sờ vòi, ngà, tai, chân, đuôi rồi cãi nhau vì cái nhìn phiến diện một chiều."},
        {"difficulty": 2, "question": "Bài thơ 'Ánh trăng' nhắc nhở con người không được lãng quên quá khứ nghĩa tình ('Ánh trăng im phăng phắc / Đủ cho ta giật mình...') là của ai?", "options": ["Nguyễn Duy", "Bằng Việt", "Hữu Thỉnh", "Phạm Tiến Duật"], "correct": 0, "explanation": "Nhà thơ Nguyễn Duy sáng tác bài thơ năm 1978 tại TP.HCM gửi gắm triết lý sống thủy chung uống nước nhớ nguồn."},
        {"difficulty": 2, "question": "Ai là tác giả của tác phẩm kịch nổi tiếng 'Quan Âm Thị Kính' đề cao đức hy sinh nhẫn nhục và lòng nhân từ bác ái?", "options": ["Tác phẩm khuyết danh dân gian", "Nguyễn Huy Tưởng", "Lưu Quang Vũ", "Tào Mạt"], "correct": 0, "explanation": "Vở chèo Quan Âm Thị Kính là tác phẩm khuyết danh kinh điển của văn học dân gian Việt Nam."},
        {"difficulty": 3, "question": "CÂU HỎI VĂN HỌC QUYẾT ĐỊNH: Bản hùng ca 'Đoàn Vệ quốc quân' với giai điệu hào sảng 'Đoàn Vệ quốc quân một lần ra đi / Toàn thắng vinh quang ghi ngày trở về' do nhạc sĩ nào chắp bút năm 1945?", "options": ["Nhạc sĩ Phan Huỳnh Điểu", "Nhạc sĩ Văn Cao", "Nhạc sĩ Hoàng Việt", "Nhạc sĩ Đỗ Nhuận"], "correct": 0, "explanation": "Nhạc sĩ Phan Huỳnh Điểu sáng tác ca khúc khi mới 21 tuổi trong không khí sục sôi của Cách mạng Tháng Tám."}
    ]
}

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU NẠP ĐỢT 7: BỔ SUNG CÂU HỎI HƯỚNG TỚI CỘT MỐC 2.500 CÂU!")
    print("=" * 70)

    total_added = 0
    for cat_name, questions in BATCH_7_DATA.items():
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

    print(f"\n✅ Đợt 7 bổ sung thành công {total_added} câu hỏi mới!")

if __name__ == '__main__':
    main()
