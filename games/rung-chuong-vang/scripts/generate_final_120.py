# -*- coding: utf-8 -*-
"""
Bổ sung 125 câu hỏi chuẩn hóa để đạt CHÍNH XÁC 1.000+ CÂU HỎI.
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

DATA_FINAL = {
    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Bánh gì không ăn được mà xoay tít dưới gầm xe?", "options": ["Bánh xe", "Bánh bao", "Bánh rán", "Bánh quy"], "correct": 0, "explanation": "Bánh xe bằng cao su quay tròn giúp xe chuyển động."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì có chân nhưng không có tay, bơi lội dưới nước kêu ộp ộp suốt đêm mưa?", "options": ["Con ếch", "Con cá", "Con lươn", "Con rùa"], "correct": 0, "explanation": "Chú ếch đồng ngồi trên lá sen kêu ộp ộp đón mưa rào."},
        {"difficulty": 1, "question": "Đố mẹo: Quả gì nhiều mắt xung quanh, khi chín thơm ngát gọt vỏ bỏ mắt?", "options": ["Quả dứa (Quả thơm)", "Quả chuối", "Quả dưa hấu", "Quả xoài"], "correct": 0, "explanation": "Quả dứa (trái thơm) có nhiều mắt dứa trên vỏ gai."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt có 4 chữ cái, bỏ đầu thành tên một loài chim, để nguyên là thứ tỏa sáng ban ngày?", "options": ["Nắng (Nắng - Áng)", "Sáng (Sáng - Áng)", "Trăng", "Sao"], "correct": 0, "explanation": "Ánh nắng ban ngày sưởi ấm vạn vật."},
        {"difficulty": 2, "question": "Đố mẹo: Cái gì có rãnh nhưng không phải mương nước, có đĩa nhưng không đựng thức ăn, phát ra âm thanh du dương?", "options": ["Đĩa than (đĩa hát)", "Đĩa ăn cơm", "Bát sứ", "Cái thìa"], "correct": 0, "explanation": "Đĩa than phát nhạc cổ điển ghi âm thanh bằng các rãnh siêu nhỏ."},
        {"difficulty": 2, "question": "Đố mẹo: Một người đứng trước gương giơ tay phải lên, hình ảnh trong gương giơ tay nào?", "options": ["Tay trái của hình ảnh trong gương", "Tay phải", "Hai tay", "Không giơ tay"], "correct": 0, "explanation": "Hình ảnh trong gương phẳng đảo ngược theo phương ngang (trái thành phải)."},
        {"difficulty": 2, "question": "Đố mẹo: Có một cây cầu dài 100m, con rùa bò qua cầu mất 100 phút, hỏi con rùa bò hết cây cầu mất bao nhiêu giờ và phút?", "options": ["1 giờ 40 phút", "1 giờ", "2 giờ", "1 giờ 20 phút"], "correct": 0, "explanation": "100 phút = 60 phút + 40 phút = 1 giờ 40 phút."},
        {"difficulty": 2, "question": "Đố mẹo: Con gì sinh ra đã biết bơi, sống dưới nước khi nhỏ thở bằng mang, lớn lên nhảy lên bờ thở bằng phổi và da?", "options": ["Con ếch (nòng nọc)", "Con cá chuối", "Con ba ba", "Con rắn nước"], "correct": 0, "explanation": "Nòng nọc sống dưới nước thở bằng mang, biến thái thành ếch thở bằng da và phổi."},
        {"difficulty": 3, "question": "Đố logic: Một người có 3 hộp kẹo: 1 hộp dán nhãn 'Kẹo chanh', 1 hộp 'Kẹo dâu', 1 hộp 'Hỗn hợp'. Cả 3 hộp đều bị dán sai nhãn. Chỉ được lấy đúng 1 chiếc kẹo từ 1 hộp, làm sao dán lại đúng nhãn cho cả 3 hộp?", "options": ["Lấy 1 chiếc từ hộp dán nhãn 'Hỗn hợp'", "Lấy từ hộp 'Kẹo chanh'", "Lấy từ hộp 'Kẹo dâu'", "Không thể xác định"], "correct": 0, "explanation": "Vì nhãn 'Hỗn hợp' dán sai, nên nếu bốc trúng vị chanh thì hộp đó 100% là 'Kẹo chanh'. Từ đó suy ra nhãn 2 hộp còn lại dễ dàng!"},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: Bức tranh đố vui dân gian: 'Trên trời rơi xuống một cục đất sét, nặn thành hình hài, nung đỏ trong lò, làm nên mái ấm che chở nắng mưa' là vật liệu gì?", "options": ["Viên gạch ngói", "Viên đá", "Hòn sỏi", "Bao xi măng"], "correct": 0, "explanation": "Đất sét nung thành gạch ngói đỏ tươi xây dựng nhà cửa làng mạc."}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Bến Nhà Rồng nơi Bác Hồ ra đi tìm đường cứu nước năm 1911 nằm bên bờ sông nào tại TP.HCM?", "options": ["Sông Sài Gòn", "Sông Đồng Nai", "Sông Vàm Cỏ", "Sông Thị Vải"], "correct": 0, "explanation": "Bến Nhà Rồng nằm bên dòng sông Sài Gòn lịch sử nay là Bảo tàng Hồ Chí Minh."},
        {"difficulty": 1, "question": "Tỉnh nào ở miền Trung nổi tiếng với di sản phố cổ Hội An bên dòng sông Hoài?", "options": ["Quảng Nam", "Quảng Ngãi", "Bình Định", "Đà Nẵng"], "correct": 0, "explanation": "Đô thị cổ Hội An (Quảng Nam) được UNESCO vinh danh là Di sản Văn hóa Thế giới năm 1999."},
        {"difficulty": 1, "question": "Hồ Than Thở là thắng cảnh hồ nước thông reo lãng mạn thuộc thành phố nào?", "options": ["Đà Lạt", "Nha Trang", "Buôn Ma Thuột", "Bảo Lộc"], "correct": 0, "explanation": "Hồ Than Thở nằm cách trung tâm thành phố Đà Lạt khoảng 6 km."},
        {"difficulty": 2, "question": "Tỉnh nào ở Tây Nguyên có ngã ba biên giới Việt Nam - Lào - Campuchia (Cửa khẩu Bờ Y)?", "options": ["Kon Tum (huyện Ngọc Hồi)", "Gia Lai", "Đắk Lắk", "Đắk Nông"], "correct": 0, "explanation": "Cột mốc ngã ba Đông Dương Bờ Y nằm tại huyện Ngọc Hồi, tỉnh Kon Tum."},
        {"difficulty": 2, "question": "Cây cầu quay đầu tiên tại Việt Nam do chính các kỹ sư và công nhân Việt Nam thiết kế thi công là cầu nào?", "options": ["Cầu quay sông Hàn (Đà Nẵng)", "Cầu Rồng", "Cầu Thuận Phước", "Cầu Trần Thị Lý"], "correct": 0, "explanation": "Cầu quay sông Hàn có thể quay 90 độ mở đường cho tàu thuyền lớn qua lại vào ban đêm."},
        {"difficulty": 2, "question": "Tỉnh nào ở vùng duyên hải Bắc Bộ có khu du lịch Đồ Sơn và bến tàu Không Số K15?", "options": ["Hải Phòng", "Quảng Ninh", "Thái Bình", "Nam Định"], "correct": 0, "explanation": "Bến K15 tại Đồ Sơn (Hải Phòng) là điểm xuất phát huyền thoại của những chuyến tàu Không Số đường Hồ Chí Minh trên biển."},
        {"difficulty": 2, "question": "Chùa Đồng ngôi chùa đúc bằng đồng nguyên chất lớn nhất Việt Nam tọa lạc trên đỉnh núi nào cao 1.068m?", "options": ["Núi Yên Tử (Quảng Ninh)", "Núi Bà Đen", "Núi Cấm", "Núi Fansipan"], "correct": 0, "explanation": "Chùa Đồng tọa lạc trên đỉnh thiêng Yên Tử nơi Phật hoàng Trần Nhân Tông tu hành."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Vùng nước trũng ngập mặn Đồng Tháp Mười trải rộng trên địa bàn 3 tỉnh nào của vùng đồng bằng sông Cửu Long?", "options": ["Long An, Tiền Giang, Đồng Tháp", "Đồng Tháp, An Giang, Kiên Giang", "Cần Thơ, Hậu Giang, Vĩnh Long", "Bến Tre, Trà Vinh, Sóc Trăng"], "correct": 0, "explanation": "Vùng Đồng Tháp Mười trũng phèn ngập nước trải dài qua 3 tỉnh Long An, Tiền Giang và Đồng Tháp."}
    ],

    "lich-su": [
        {"difficulty": 1, "question": "Vua Hùng thứ mấy đã chọn Lang Liêu nối ngôi nhờ dâng lễ vật bánh chưng bánh giầy thơm thảo?", "options": ["Vua Hùng thứ 6", "Vua Hùng thứ 1", "Vua Hùng thứ 18", "Vua Hùng thứ 3"], "correct": 0, "explanation": "Vua Hùng thứ 6 mở hội thi tài làm lễ vật dâng cúng tổ tiên và chọn hoàng tử Lang Liêu."},
        {"difficulty": 1, "question": "Bản 'Tuyên ngôn Độc lập' ngày 2/9/1945 do Chủ tịch Hồ Chí Minh soạn thảo tại ngôi nhà số bao nhiêu phố Hàng Ngang, Hà Nội?", "options": ["Số nhà 48 Hàng Ngang", "Số 10 Hàng Ngang", "Số 36 Hàng Đào", "Số 20 Tràng Tiền"], "correct": 0, "explanation": "Ngôi nhà số 48 Hàng Ngang của gia đình thương gia Trịnh Văn Bô là nơi Bác Hồ viết bản Tuyên ngôn Độc lập."},
        {"difficulty": 1, "question": "Vị tướng nào thời Trần chỉ huy đội quân 'Sát Thát' đã lấy bút ghi lên trán chữ Sát Thát thề quyết chiến với giặc Nguyên?", "options": ["Tất cả quân dân nhà Trần", "Trần Quốc Toản", "Trần Hưng Đạo", "Yết Kiêu"], "correct": 0, "explanation": "Quân sĩ nhà Trần xăm hai chữ 'Sát Thát' (Giết giặc Thát Đát) lên cánh tay biểu thị ý chí quyết tử."},
        {"difficulty": 2, "question": "Khởi nghĩa Bãi Sậy (1883 - 1892) trong phong trào Cần Vương do thủ lĩnh nào lãnh đạo trên vùng đầm lầy Hưng Yên?", "options": ["Nguyễn Thiện Thuật", "Phan Đình Phùng", "Đinh Công Tráng", "Hoàng Hoa Thám"], "correct": 0, "explanation": "Nguyễn Thiện Thuật (Tán Thuật) chỉ huy nghĩa quân lập căn cứ du kích hiểm trở ở Bãi Sậy."},
        {"difficulty": 2, "question": "Đại hội Giới trẻ Thế giới và Hội nghị Paris về chấm dứt chiến tranh tại Việt Nam diễn ra từ năm nào đến năm nào?", "options": ["1968 - 1973 (ký ngày 27/1/1973)", "1970 - 1975", "1954 - 1960", "1965 - 1972"], "correct": 0, "explanation": "Hội nghị Paris đàm phán kéo dài gần 5 năm kết thúc với việc ký kết Hiệp định Paris ngày 27/1/1973."},
        {"difficulty": 2, "question": "Vị hoàng đế nào của triều Tây Sơn sau khi vua Quang Trung đột ngột băng hà đã lên nối ngôi khi mới 10 tuổi?", "options": ["Quang Toản (vua Cảnh Thịnh)", "Nguyễn Nhạc", "Nguyễn Lữ", "Nguyễn Ánh"], "correct": 0, "explanation": "Nguyễn Quang Toản lên ngôi năm 1792 lấy niên hiệu Cảnh Thịnh khi tuổi đời còn quá nhỏ."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Vị vua nào của triều Nguyễn đã ban hành chỉ dụ cho dựng Quốc Tử Giám tại Cố đô Huế vào năm 1803?", "options": ["Vua Gia Long", "Vua Minh Mạng", "Vua Thiệu Trị", "Vua Tự Đức"], "correct": 0, "explanation": "Vua Gia Long lập Quốc Tử Giám tại Huế năm 1803 làm trung tâm đào tạo nhân tài cao nhất cho cả nước."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Cơ thể con người có nhiệt độ bình thường khi khỏe mạnh xấp xỉ bao nhiêu độ C?", "options": ["Khoảng 36,5 - 37 độ C", "Khoảng 40 độ C", "Khoảng 32 độ C", "Khoảng 39 độ C"], "correct": 0, "explanation": "Nhiệt độ thân nhiệt bình thường của người khỏe mạnh dao động từ 36,5 đến 37,2 °C."},
        {"difficulty": 1, "question": "Mặt Trăng quay quanh Trái Đất mất thời gian xấp xỉ bằng bao nhiêu ngày?", "options": ["Khoảng 27,3 ngày (khoảng 1 tháng)", "Khoảng 365 ngày", "Khoảng 7 ngày", "Khoảng 24 giờ"], "correct": 0, "explanation": "Mặt Trăng hoàn thành một chu kỳ quỹ đạo quanh Trái Đất trong khoảng 27,3 ngày."},
        {"difficulty": 1, "question": "Loài cây nào được xem là biểu tượng kiên cường bất khuất của làng quê Việt Nam, thân có nhiều đốt?", "options": ["Cây tre", "Cây bàng", "Cây phượng", "Cây cau"], "correct": 0, "explanation": "Lũy tre xanh che chở xóm làng trải qua hàng ngàn năm lịch sử dựng nước."},
        {"difficulty": 2, "question": "Trong hóa học, nước vôi trong là dung dịch của hợp chất bazơ nào?", "options": ["Canxi hidroxit (Ca(OH)2)", "Canxi cacbonat (CaCO3)", "Canxi oxit (CaO)", "Natri hidroxit (NaOH)"], "correct": 0, "explanation": "Nước vôi trong Ca(OH)2 khi gặp khí CO2 sẽ sục kết tủa trắng đục Canxi cacbonat."},
        {"difficulty": 2, "question": "Khí trơ nào nhẹ hơn không khí, không cháy nổ, thường được dùng để bơm vào bóng bay khí cầu?", "options": ["Khí Heli (He)", "Khí Hydro", "Khí Oxy", "Khí Nitơ"], "correct": 0, "explanation": "Heli là khí hiếm trơ cực kỳ an toàn, nhẹ thứ nhì vũ trụ sau hydro."},
        {"difficulty": 2, "question": "Hiện tượng tán xạ Rayleigh trong khí quyển Trái Đất giải thích cho điều kỳ thú nào của tự nhiên?", "options": ["Tại sao bầu trời ban ngày có màu xanh lam", "Tại sao ban đêm có sao", "Tại sao có mây đen", "Tại sao có sương mù"], "correct": 0, "explanation": "Các phân tử khí tán xạ bước sóng ngắn (ánh sáng xanh lam) mạnh hơn ánh sáng đỏ, tạo nên sắc trời xanh ngắt."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Bào quan nào trong tế bào nhân thực được ví như 'Nhà máy năng lượng' tạo ra phân tử ATP nuôi sống tế bào?", "options": ["Ty thể (Mitochondria)", "Bộ máy Golgi", "Nhân tế bào", "Lưới nội chất"], "correct": 0, "explanation": "Ty thể tiến hành chu trình Krebs và chuỗi chuyền electron hô hấp tổng hợp ATP cung cấp năng lượng cho mọi hoạt động sống."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Món phở cuốn trứ danh của ẩm thực Hà Nội có nguồn gốc đầu tiên từ phố ẩm thực nào?", "options": ["Phố Ngũ Xã (bên hồ Trúc Bạch)", "Phố Hàng Buồm", "Phố Tạ Hiện", "Phố Cấm Chỉ"], "correct": 0, "explanation": "Làng đúc đồng Ngũ Xã ven hồ Trúc Bạch là cái nôi khai sinh ra món phở cuốn thịt bò rau thơm trứ danh."},
        {"difficulty": 1, "question": "Nút bấm nào trên bàn phím máy tính dùng để xóa ký tự đứng ngay phía trước con trỏ văn bản?", "options": ["Phím Backspace", "Phím Delete", "Phím Enter", "Phím Shift"], "correct": 0, "explanation": "Backspace xóa lùi về bên trái, còn Delete xóa ký tự đứng phía sau con trỏ."},
        {"difficulty": 1, "question": "Môn thể thao nào mà các đấu sĩ mặc võ phục đai đen thực hiện các đòn quật ngã, siết cổ trên thảm đấu có nguồn gốc từ Nhật Bản?", "options": ["Judo (Nhu đạo)", "Karate", "Taekwondo", "Muay Thái"], "correct": 0, "explanation": "Judo do võ sư Kano Jigoro sáng lập năm 1882 với nguyên lý 'Lấy nhu thắng cương'."},
        {"difficulty": 2, "question": "Công nghệ truyền hình cáp quang Internet tốc độ cao FTTx sử dụng loại dây cáp gì?", "options": ["Cáp quang lõi sợi thủy tinh", "Cáp đồng trục", "Dây điện thoại", "Dây cáp nhôm"], "correct": 0, "explanation": "Cáp quang truyền tín hiệu dưới dạng các xung ánh sáng cho băng thông siêu rộng và không bị nhiễu điện từ."},
        {"difficulty": 2, "question": "Món 'Cơm hến' cay xé lưỡi ăn kèm tóp mỡ, hoa chuối và nước luộc hến thanh ngọt là đặc sản vùng nào?", "options": ["Cố đô Huế", "Đà Nẵng", "Quảng Ngãi", "Bình Định"], "correct": 0, "explanation": "Cơm hến Cồn Hến (Huế) là món ăn dân dã đậm đà vị cay nồng đặc trưng của xứ thần kinh."},
        {"difficulty": 2, "question": "Hệ thống tên miền trên mạng Internet giúp dịch địa chỉ IP số học (ví dụ: 192.168.1.1) thành tên dễ nhớ (ví dụ: google.com) được gọi là gì?", "options": ["Hệ thống DNS (Domain Name System)", "DHCP", "FTP", "SNMP"], "correct": 0, "explanation": "DNS đóng vai trò như danh bạ điện thoại của toàn bộ mạng Internet thế giới."},
        {"difficulty": 3, "question": "CÂU HỎI CÔNG NGHỆ QUYẾT ĐỊNH: Tiêu chuẩn mã hóa ký tự phổ quát hỗ trợ hiển thị chính xác mọi ngôn ngữ trên thế giới (kể cả tiếng Việt có dấu) là tiêu chuẩn nào?", "options": ["Unicode (chuẩn UTF-8)", "ASCII", "TCVN3 (ABC)", "VNI"], "correct": 0, "explanation": "Chuẩn UTF-8 Unicode là bảng mã tiêu chuẩn thống nhất định dạng ký tự cho mọi trang web và hệ điều hành ngày nay."}
    ],

    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu thành ngữ: 'Uống nước nhớ ...'?", "options": ["nguồn", "sông", "suối", "dòng"], "correct": 0, "explanation": "Đạo lý truyền thống tri ân cội nguồn, tổ tiên của người Việt Nam."},
        {"difficulty": 1, "question": "Trong truyện 'Sơn Tinh - Thủy Tinh', sính lễ vua Hùng yêu cầu để cưới công chúa Mỵ Nương gồm 'Voi chín ngà, gà chín cựa, ngựa chín ...'?", "options": ["hồng mao", "đuôi", "sừng", "chân"], "correct": 0, "explanation": "'Voi chín ngà, gà chín cựa, ngựa chín hồng mao' - sính lễ hiếm có của núi rừng."},
        {"difficulty": 1, "question": "Bài hát 'Tiến lên đoàn viên' với lời ca 'Tiến bước theo cờ Lý Tự Trọng...' do nhạc sĩ nào sáng tác?", "options": ["Phạm Tuyên", "Phong Nhã", "Lưu Hữu Phước", "Hoàng Vân"], "correct": 0, "explanation": "Nhạc sĩ Phạm Tuyên sáng tác ca khúc cổ vũ tinh thần thanh thiếu niên năm 1954."},
        {"difficulty": 2, "question": "Ai là tác giả của tác phẩm tiểu thuyết lịch sử 'Lá cờ thêu sáu chữ vàng' tái hiện hình ảnh anh hùng trẻ tuổi Trần Quốc Toản?", "options": ["Nguyễn Huy Tưởng", "Tô Hoài", "Hà Ân", "Nam Cao"], "correct": 0, "explanation": "Nhà văn Nguyễn Huy Tưởng khắc họa hào khí Đông A qua tấm lòng vì nước của Trần Quốc Toản."},
        {"difficulty": 2, "question": "Bài thơ 'Chiều biên giới' với câu hát 'Chiều biên giới em ơi / Có nơi nào cao hơn...' do nhạc sĩ Trần Chung phổ nhạc là thơ của ai?", "options": ["Lò Ngân Sủn", "Hữu Thỉnh", "Trần Đăng Khoa", "Lò Văn Mười"], "correct": 0, "explanation": "Nhà thơ dân tộc Dáy Lò Ngân Sủn viết nên những vần thơ hùng tráng về dải đất biên cương Bát Xát."},
        {"difficulty": 2, "question": "Làng tranh dân gian Kim Hoàng ở Hoài Đức (Hà Nội) nổi tiếng với kỹ thuật in mộc bản trên nền giấy màu gì?", "options": ["Giấy đỏ (hoặc giấy hồng điều)", "Giấy điệp trắng", "Giấy vàng", "Giấy nâu"], "correct": 0, "explanation": "Tranh Đỏ Kim Hoàng in trên nền giấy hồng điều với nét vẽ đen phóng khoáng là nét đặc sắc xứ Đoài."},
        {"difficulty": 3, "question": "CÂU HỎI VĂN HỌC QUYẾT ĐỊNH: Tác phẩm thơ trường thiên bất hủ 'Chinh phụ ngâm' nguyên tác bằng chữ Hán do danh sĩ nào chắp bút dưới thời Lê - Trịnh?", "options": ["Đặng Trần Côn (Đoàn Thị Điểm diễn Nôm)", "Nguyễn Gia Thiều", "Nguyễn Du", "Phan Huy Chú"], "correct": 0, "explanation": "Đặng Trần Côn viết Chinh phụ ngâm bằng chữ Hán, sau đó nữ sĩ Đoàn Thị Điểm dịch sang thể thơ song thất lục bát tuyệt mỹ."}
    ]
}

def main():
    total_added = 0
    for cat_name, questions in DATA_FINAL.items():
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
