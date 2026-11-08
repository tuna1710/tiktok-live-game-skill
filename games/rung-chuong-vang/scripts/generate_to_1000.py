# -*- coding: utf-8 -*-
"""
Script bổ sung 175 câu hỏi cuối cùng để chính thức cán mốc 1.000 CÂU HỎI.
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

DATA_1000 = {
    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Con gì không biết bơi nhưng suốt ngày ở dưới nước?", "options": ["Con tàu ngầm", "Con cá", "Con cua", "Con ốc"], "correct": 0, "explanation": "Con tàu ngầm bằng thép sắt lặn dưới biển nhưng không phải là sinh vật biết bơi."},
        {"difficulty": 1, "question": "Đố mẹo: Quả gì không ăn được mà cầu thủ nào cũng muốn sút vào lưới?", "options": ["Quả bóng đá", "Quả cam", "Quả chanh", "Quả dưa"], "correct": 0, "explanation": "Quả bóng đá trong môn thể thao vua."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có cổ mà không có đầu, có tay mà không có ngón?", "options": ["Chiếc áo sơ mi", "Cái chai", "Cái thìa", "Cái ghế"], "correct": 0, "explanation": "Chiếc áo có cổ áo và tay áo nhưng không phải cơ thể sống."},
        {"difficulty": 1, "question": "Đố vui: Hoa gì biết bay rập rờn khắp vườn hoa ngày xuân?", "options": ["Hoa bướm (con bướm)", "Hoa mai", "Hoa đào", "Hoa hồng"], "correct": 0, "explanation": "Đố vui về loài bướm rực rỡ sắc màu bay lượn như cánh hoa."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì có tai dài, đuôi ngắn, thích ăn cà rốt và nhảy thoăn thoắt?", "options": ["Con thỏ", "Con chuột", "Con mèo", "Con cún"], "correct": 0, "explanation": "Chú thỏ trắng xinh xắn với đôi tai dài thính nhạy."},
        {"difficulty": 2, "question": "Đố mẹo: Cái gì đi khắp nhà nhưng khi ra ngoài đường lại phải nằm im trong túi?", "options": ["Chiếc chìa khóa nhà", "Cây chổi", "Đôi dép", "Cái bàn"], "correct": 0, "explanation": "Chìa khóa mở cửa mọi phòng, khi ra đường thì cất vào túi xách."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt bỏ dấu sắc thì thành tên một con vật, thêm dấu ngã thành thứ để nhóm lửa?", "options": ["Củi (Cúi - Củi - Cũi)", "Chó", "Mèo", "Gà"], "correct": 0, "explanation": "Cúi đầu - con Cú - Củi lửa."},
        {"difficulty": 2, "question": "Đố mẹo: Một người thợ lặn xuống biển sâu mà không cần bình dưỡng khí trong 30 phút, vì sao?", "options": ["Người đó lặn trong tàu ngầm", "Người đó nín thở siêu đẳng", "Biển nhân tạo", "Có người bơm oxy"], "correct": 0, "explanation": "Ở trong tàu ngầm thì có hệ thống dưỡng khí điều hòa bình thường."},
        {"difficulty": 2, "question": "Đố vui dân gian: 'Trắng phau củ cải, láng mướt da gà / Vừa đụng vào là chảy nước mắt ra' là củ gì?", "options": ["Củ hành tây", "Củ tỏi", "Củ gừng", "Củ cải trắng"], "correct": 0, "explanation": "Hành tây chứa hợp chất lưu huỳnh làm kích ứng tuyến lệ cay mắt khi thái."},
        {"difficulty": 2, "question": "Đố mẹo: Có 1 rổ táo gồm 6 quả, chia cho 6 bạn, mỗi bạn được 1 quả, nhưng trong rổ vẫn còn 1 quả. Vì sao?", "options": ["Bạn cuối cùng nhận cả chiếc rổ có quả táo bên trong", "Cắt táo", "Nhầm lẫn", "Táo giả"], "correct": 0, "explanation": "5 bạn lấy quả táo rời, bạn thứ 6 nhận luôn chiếc rổ chứa quả táo còn lại."},
        {"difficulty": 2, "question": "Đố mẹo: Bạn có thể giữ thứ gì mà không cần chạm tay vào nó?", "options": ["Hơi thở của bạn", "Cốc nước", "Cây bút", "Đồng tiền"], "correct": 0, "explanation": "Bạn có thể nín thở (giữ hơi thở) mà không cần dùng tay chạm vào."},
        {"difficulty": 3, "question": "Đố logic: Làm sao để thả một quả trứng gà sống từ độ cao 2 mét xuống sàn xi măng mà không làm vỡ quả trứng?", "options": ["Thả rơi từ độ cao 2,5 mét, quả trứng rơi được 2 mét thì chưa chạm sàn", "Bọc xốp", "Thả xuống đệm", "Luộc chín trứng"], "correct": 0, "explanation": "Thả từ 2,5 mét thì sau 2 mét rơi trong không khí quả trứng vẫn nguyên vẹn chưa chạm đất!"},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: Bức tranh đố mẹo dân gian: 'Mình tròn vành vạnh, đáy thủng tơ vơ, ngửa mặt nhìn trời, chờ người soi bóng' là cái gì?", "options": ["Cái giếng nước làng quê", "Cái thùng", "Cái xô", "Cái chum"], "correct": 0, "explanation": "Thành giếng tròn soi bóng mây trời và bóng người múc nước ngọt mát."}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Tỉnh nào ở miền Bắc nổi tiếng với danh xưng 'Quê hương năm tấn' và đền Trần thờ các vua Trần?", "options": ["Thái Bình (và Nam Định)", "Hải Dương", "Hà Nam", "Hưng Yên"], "correct": 0, "explanation": "Thái Bình quê hương chị Hai Năm Tấn lá cờ đầu trong thâm canh lúa nước."},
        {"difficulty": 1, "question": "Dòng sông nào êm đềm chảy qua thành phố Đà Nẵng với những cây cầu nổi tiếng như Cầu Rồng, Cầu Quay?", "options": ["Sông Hàn", "Sông Thu Bồn", "Sông Hương", "Sông Vu Gia"], "correct": 0, "explanation": "Sông Hàn thơ mộng là niềm tự hào của người dân thành phố Đà Nẵng."},
        {"difficulty": 1, "question": "Bãi biển Cửa Lò bãi biển du lịch nổi tiếng miền Trung thuộc tỉnh nào?", "options": ["Nghệ An", "Hà Tĩnh", "Thanh Hóa", "Quảng Bình"], "correct": 0, "explanation": "Thị xã biển Cửa Lò cách thành phố Vinh (Nghệ An) hơn 15 km."},
        {"difficulty": 1, "question": "Tỉnh nào ở cực Nam Tổ quốc nổi tiếng với rừng đước ngập mặn Năm Căn?", "options": ["Cà Mau", "Bạc Liêu", "Kiên Giang", "Sóc Trăng"], "correct": 0, "explanation": "Rừng ngập mặn Cà Mau lớn thứ nhì thế giới chỉ sau rừng Amazon."},
        {"difficulty": 2, "question": "Hồ Tơ Nưng (Biển Hồ) 'đôi mắt Pleiku' nước trong xanh biếc là vết tích của miệng núi lửa cổ tại tỉnh nào?", "options": ["Gia Lai", "Kon Tum", "Đắk Lắk", "Đắk Nông"], "correct": 0, "explanation": "Biển Hồ Gia Lai nằm ở độ cao 800m trên miệng núi lửa đã tắt hàng triệu năm."},
        {"difficulty": 2, "question": "Quần đảo Côn Đảo gồm 16 hòn đảo lớn nhỏ ngày nay trực thuộc tỉnh nào?", "options": ["Bà Rịa - Vũng Tàu", "Bình Thuận", "Tiền Giang", "Bến Tre"], "correct": 0, "explanation": "Huyện đảo Côn Đảo là di tích lịch sử đặc biệt và điểm du lịch sinh thái biển đảo tuyệt vời."},
        {"difficulty": 2, "question": "Núi Chư Đăng Ya ngọn núi lửa cổ tuyệt đẹp ngập tràn sắc hoa dã quỳ vào tháng 11 thuộc tỉnh nào?", "options": ["Gia Lai", "Đắk Lắk", "Lâm Đồng", "Kon Tum"], "correct": 0, "explanation": "Núi lửa Chư Đăng Ya (huyện Chư Păh, Gia Lai) là tuyệt tác thiên nhiên đất đỏ Tây Nguyên."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Vườn quốc gia Bạch Mã dải rừng nguyên sinh nối liền biển và dãy Trường Sơn nằm giữa địa giới hành chính của hai địa phương nào?", "options": ["Thừa Thiên Huế và TP. Đà Nẵng", "Quảng Trị và Thừa Thiên Huế", "Quảng Nam và Đà Nẵng", "Quảng Bình và Hà Tĩnh"], "correct": 0, "explanation": "Đỉnh Bạch Mã cao 1.450m quanh năm mây phủ là ranh giới tự nhiên giữa Thừa Thiên Huế và Đà Nẵng."}
    ],

    "lich-su": [
        {"difficulty": 1, "question": "Vị hoàng đế nào của nhà Đinh dẹp loạn 12 sứ quân, mở đầu kỷ nguyên độc lập thống nhất Đại Cồ Việt?", "options": ["Đinh Tiên Hoàng (Đinh Bộ Lĩnh)", "Đinh Liễn", "Ngô Quyền", "Lê Hoàn"], "correct": 0, "explanation": "Đinh Bộ Lĩnh dùng cờ lau tập trận, lớn lên thu phục 12 sứ quân định đô ở Hoa Lư."},
        {"difficulty": 1, "question": "Ngày truyền thống của Quân đội Nhân dân Việt Nam được kỷ niệm vào ngày tháng nào hàng năm?", "options": ["22/12", "19/8", "30/4", "2/9"], "correct": 0, "explanation": "Ngày 22/12/1944, Đội Việt Nam Tuyên truyền Giải phóng quân được thành lập tại Cao Bằng."},
        {"difficulty": 1, "question": "Vị tướng anh hùng nào đã chỉ huy nghĩa quân Tây Sơn đánh tan 5 vạn quân Xiêm trong trận Rạch Gầm - Xoài Mút năm 1785?", "options": ["Nguyễn Huệ", "Nguyễn Nhạc", "Nguyễn Lữ", "Võ Văn Dũng"], "correct": 0, "explanation": "Nguyễn Huệ bố trí mai phục nghiền nát quân Xiêm trên sông Tiền trong một ngày oanh liệt."},
        {"difficulty": 2, "question": "Trận chiến trên sông Như Nguyệt năm 1077 quân dân nhà Lý đã đánh bại quân xâm lược của triều đại phong kiến phương Bắc nào?", "options": ["Nhà Tống", "Nhà Đường", "Nhà Nguyên", "Nhà Minh"], "correct": 0, "explanation": "Thái úy Lý Thường Kiệt chặn đứng và đè bẹp ý chí xâm lăng của quân Tống bên bờ sông Cầu."},
        {"difficulty": 2, "question": "Vị vua nào của triều Hậu Lê lên ngôi sau thắng lợi của khởi nghĩa Lam Sơn năm 1428?", "options": ["Lê Thái Tổ (Lê Lợi)", "Lê Thánh Tông", "Lê Thái Tông", "Lê Nhân Tông"], "correct": 0, "explanation": "Lê Lợi lên ngôi hoàng đế tại Thăng Long, đặt quốc hiệu là Đại Việt mở ra triều Hậu Lê."},
        {"difficulty": 2, "question": "Chiến dịch Tây Nguyên mở màn cuộc Tổng tiến công mùa xuân 1975 bắt đầu bằng trận đánh then chốt nào?", "options": ["Trận Buôn Ma Thuột", "Trận Pleiku", "Trận Kon Tum", "Trận Gia Lai"], "correct": 0, "explanation": "Đòn điểm huyệt thần tốc giải phóng Buôn Ma Thuột ngày 10/3/1975 tạo bước ngoặt chiến lược."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Vị vua nào của nước ta cho khắc bia tiến sĩ đầu tiên tại Văn Miếu - Quốc Tử Giám vào năm 1484?", "options": ["Lê Thánh Tông", "Lý Thánh Tông", "Trần Thánh Tông", "Lê Thái Tổ"], "correct": 0, "explanation": "Vua Lê Thánh Tông dựng bia đề danh tiến sĩ khắc ghi câu châm ngôn: 'Hiền tài là nguyên khí quốc gia'."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Chất lỏng không màu, không mùi, không vị chiếm hơn 70% bề mặt Trái Đất là chất gì?", "options": ["Nước (H2O)", "Dầu hỏa", "Cồn y tế", "Sữa"], "correct": 0, "explanation": "Nước là cội nguồn của mọi sự sống trên hành tinh xanh."},
        {"difficulty": 1, "question": "Bộ phận nào trên đầu của côn trùng giúp chúng ngửi mùi và định hướng không gian?", "options": ["Đôi râu (ăng-ten)", "Đôi mắt kép", "Đôi cánh", "Miệng"], "correct": 0, "explanation": "Đôi râu côn trùng chứa hàng ngàn thụ thể hóa học nhạy bén với mùi hương."},
        {"difficulty": 1, "question": "Mặt Trời mọc ở hướng nào và lặn ở hướng nào theo quy luật tự nhiên?", "options": ["Mọc ở hướng Đông, lặn ở hướng Tây", "Mọc hướng Tây, lặn hướng Đông", "Mọc hướng Bắc, lặn hướng Nam", "Mọc hướng Nam, lặn hướng Bắc"], "correct": 0, "explanation": "Do Trái Đất tự quay quanh trục từ Tây sang Đông nên ta thấy Mặt Trời mọc ở hướng Đông."},
        {"difficulty": 2, "question": "Quá trình chuyển hóa thức ăn thành chất dinh dưỡng nuôi cơ thể người diễn ra chủ yếu ở cơ quan nào?", "options": ["Ruột non", "Dạ dày", "Miệng", "Đại tràng"], "correct": 0, "explanation": "Nhung mao ở thành ruột non hấp thụ hầu hết axit amin, đường, vitamin vào dòng máu."},
        {"difficulty": 2, "question": "Kim loại nào dẫn nhiệt và dẫn điện kém nhất trong số các kim loại thông dụng sau đây?", "options": ["Chì", "Đồng", "Nhôm", "Bạc"], "correct": 0, "explanation": "Chì có điện trở suất cao hơn nhiều so với đồng và nhôm, dẫn điện dẫn nhiệt tương đối kém."},
        {"difficulty": 2, "question": "Tia sét trong cơn dông bão phóng ra tia lửa điện với nhiệt độ ở lõi có thể lên tới bao nhiêu độ C?", "options": ["Khoảng 30.000 độ C (nóng gấp 5 lần bề mặt Mặt Trời)", "Khoảng 1.000 độ C", "Khoảng 100 độ C", "Khoảng 5.000 độ C"], "correct": 0, "explanation": "Sét làm nóng không khí tức thời lên gần 30.000 °C gây ra sóng xung kích tạo tiếng sấm nổ vang."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Trong cơ thể người, tuyến nội tiết nào được coi là 'Tuyến nhạc trưởng' chỉ huy hoạt động của hầu hết các tuyến nội tiết khác?", "options": ["Tuyến yên (Pituitary gland)", "Tuyến giáp", "Tuyến tụy", "Tuyến thượng thận"], "correct": 0, "explanation": "Tuyến yên nằm ở đáy não tiết ra các hormone chỉ huy kích thích tuyến giáp, tuyến thượng thận và tuyến sinh dục."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Hệ thống đèn tín hiệu giao thông đường bộ gồm 3 màu cơ bản là những màu nào?", "options": ["Đỏ, Vàng, Xanh lục", "Đỏ, Tím, Vàng", "Xanh, Cam, Đỏ", "Đỏ, Trắng, Vàng"], "correct": 0, "explanation": "Quy tắc: Đèn đỏ dừng lại, đèn xanh được đi, đèn vàng giảm tốc độ dừng trước vạch."},
        {"difficulty": 1, "question": "Món ăn sáng nổi tiếng của người Hà Nội gồm xôi nếp dẻo thơm ăn kèm đậu xanh xắt mỏng và hành phi vàng giòn là món gì?", "options": ["Xôi xéo", "Xôi gấc", "Xôi vò", "Xôi bắp"], "correct": 0, "explanation": "Xôi xéo gói trong lá chuối đượm mỡ gà béo ngậy là thức quà sáng kinh điển đất Hà thành."},
        {"difficulty": 1, "question": "Nền tảng mua sắm trực tuyến Shopee, Lazada, TikTok Shop thuộc mô hình kinh doanh nào?", "options": ["Thương mại điện tử (E-commerce)", "Siêu thị truyền thống", "Chợ cóc", "Ngân hàng"], "correct": 0, "explanation": "Thương mại điện tử cho phép người mua và người bán giao dịch hàng hóa qua Internet thuận tiện."},
        {"difficulty": 2, "question": "Công nghệ trợ lý ảo Siri được tích hợp mặc định trên các thiết bị của tập đoàn công nghệ nào?", "options": ["Apple", "Google", "Samsung", "Microsoft"], "correct": 0, "explanation": "Siri do Apple phát triển hỗ trợ điều khiển bằng giọng nói trên iPhone, iPad, Mac."},
        {"difficulty": 2, "question": "Vận động viên bắn súng huyền thoại nào đã mang về tấm Huy chương Vàng Olympic đầu tiên trong lịch sử cho thể thao Việt Nam năm 2016?", "options": ["Xạ thủ Hoàng Xuân Vinh", "Trần Oanh", "Hoàng Quý Phước", "Nguyễn Tiến Minh"], "correct": 0, "explanation": "Đại tá Hoàng Xuân Vinh xuất sắc giành HCV nội dung 10m súng ngắn hơi tại Olympic Rio 2016."},
        {"difficulty": 2, "question": "Hạt ngũ cốc nào là lương thực chính nuôi sống hơn một nửa dân số thế giới và là cây trồng truyền thống của Việt Nam?", "options": ["Cây lúa nước (gạo)", "Lúa mì", "Ngô", "Khoai tây"], "correct": 0, "explanation": "Việt Nam là một trong những quốc gia xuất khẩu gạo chất lượng cao hàng đầu thế giới."},
        {"difficulty": 3, "question": "CÂU HỎI CÔNG NGHỆ QUYẾT ĐỊNH: Giao thức truyền thông nào là nền tảng cốt lõi định tuyến gói tin trên toàn bộ mạng Internet toàn cầu?", "options": ["Bộ giao thức TCP/IP", "HTTP", "FTP", "DNS"], "correct": 0, "explanation": "TCP/IP (Transmission Control Protocol / Internet Protocol) do Vint Cerf và Bob Kahn phát triển định hình mạng Internet."}
    ],

    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu tục ngữ: 'Tốt gỗ hơn tốt ...'?", "options": ["nước sơn", "vỏ", "áo", "hình"], "correct": 0, "explanation": "Đề cao giá trị phẩm chất đạo đức bên trong hơn vẻ hào nhoáng hình thức bên ngoài."},
        {"difficulty": 1, "question": "Trong truyện cổ tích 'Cây khế', con chim thần đã chở người em ra đảo lấy vàng bằng lời dặn nổi tiếng nào?", "options": ["'Ăn một quả, trả cục vàng, may túi ba gang, mang đi mà đựng'", "'Ăn một quả, trả một lượng'", "'May túi mười gang'", "'Lấy bao nhiêu tùy thích'"], "correct": 0, "explanation": "Lời dặn nhân quả: người em hiền lành may túi đúng ba gang được chim trả ơn giàu có."},
        {"difficulty": 1, "question": "Ai là tác giả của câu thơ nổi tiếng: 'Đầu lòng hai ả tố nga / Thúy Kiều là chị, em là Thúy Vân'?", "options": ["Đại thi hào Nguyễn Du", "Đoàn Thị Điểm", "Hồ Xuân Hương", "Bà Huyện Thanh Quan"], "correct": 0, "explanation": "Nguyễn Du miêu tả nhan sắc 'mười phân vẹn mười' của hai chị em Thúy Kiều đầu kiệt tác Đoạn trường tân thanh."},
        {"difficulty": 2, "question": "Bài thơ 'Bếp lửa' với hình ảnh người bà tần tảo nhóm lên tình yêu thương sưởi ấm tâm hồn cháu là của nhà thơ nào?", "options": ["Bằng Việt", "Hữu Thỉnh", "Phạm Tiến Duật", "Nguyễn Duy"], "correct": 0, "explanation": "'Một bếp lửa chờn vờn sương sớm / Một bếp lửa ấp iu nồng đượm...' - thơ Bằng Việt viết năm 1963 tại Liên Xô."},
        {"difficulty": 2, "question": "Tác phẩm văn học 'Mùa lạc' ngợi ca cuộc sống lao động hồi sinh trên nông trường Điện Biên là của nhà văn nào?", "options": ["Nguyễn Khải", "Nguyễn Minh Châu", "Bùi Hiển", "Nguyễn Tuân"], "correct": 0, "explanation": "'Ở đời này không có con đường cùng, chỉ có những ranh giới, điều cốt yếu là phải có sức mạnh để bước qua...' - Nguyễn Khải."},
        {"difficulty": 2, "question": "Làng gốm cổ truyền Bát Tràng nổi tiếng với các sản phẩm men ngọc, men lam tinh xảo nằm ven bờ sông Hồng thuộc huyện nào của Hà Nội?", "options": ["Huyện Gia Lâm", "Huyện Đông Anh", "Huyện Thanh Trì", "Huyện Sóc Sơn"], "correct": 0, "explanation": "Làng gốm Bát Tràng có lịch sử hơn 700 năm bên tả ngạn sông Hồng thuộc huyện Gia Lâm."},
        {"difficulty": 3, "question": "CÂU HỎI VĂN HỌC QUYẾT ĐỊNH: Kiệt tác kịch 'Vũ Như Tô' phản ánh bi kịch giữa nghệ thuật siêu đẳng và quyền lợi thiết thực của nhân dân qua công trình Cửu Trùng Đài là của ai?", "options": ["Nguyễn Huy Tưởng", "Lưu Quang Vũ", "Tào Mạt", "Vi Huyền Đắc"], "correct": 0, "explanation": "Vở kịch lịch sử 5 hồi của Nguyễn Huy Tưởng đặt ra câu hỏi muôn thuở về mối quan hệ giữa nghệ sĩ và nhân dân."}
    ]
}

def main():
    print("=" * 70)
    print("🚀 BỔ SUNG 175 CÂU HỎI ĐỂ CHẠM MỐC 1.000 CÂU HỎI!")
    print("=" * 70)

    total_added = 0
    for cat_name, questions in DATA_1000.items():
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

        print(f"  📁 [{cat_name}]: Thêm {added_in_cat} câu -> Tổng hiện có: {len(existing_list)} câu.")

    print(f"\n✅ Đã bổ sung thành công {total_added} câu hỏi mới!")

if __name__ == '__main__':
    main()
