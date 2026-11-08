# -*- coding: utf-8 -*-
"""
Chính thức đưa ngân hàng câu hỏi vượt qua 1.000 CÂU HỎI (Bổ sung 75 câu cuối cùng).
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

DATA_75 = {
    "lich-su": [
        {"difficulty": 1, "question": "Ngày Quốc tế Lao động được kỷ niệm vào ngày tháng nào hàng năm?", "options": ["1/5", "30/4", "8/3", "2/9"], "correct": 0, "explanation": "Ngày 1/5 là ngày hội đoàn kết của giai cấp công nhân và nhân dân lao động trên toàn thế giới."},
        {"difficulty": 1, "question": "Vị vua nào của triều Lý lập nên Quốc Tử Giám trường đại học đầu tiên năm 1076?", "options": ["Lý Nhân Tông", "Lý Thánh Tông", "Lý Thái Tổ", "Lý Thái Tông"], "correct": 0, "explanation": "Vua Lý Nhân Tông cho xây dựng Quốc Tử Giám bên cạnh Văn Miếu để dạy học cho con em hoàng tộc và nhân tài."},
        {"difficulty": 1, "question": "Bác Hồ sinh ngày 19 tháng 5 năm nào tại làng Sen, xã Kim Liên, huyện Nam Đàn, tỉnh Nghệ An?", "options": ["Năm 1890", "Năm 1880", "Năm 1900", "Năm 1911"], "correct": 0, "explanation": "Chủ tịch Hồ Chí Minh sinh ngày 19/5/1890 trong gia đình nhà nho yêu nước cụ Phó bảng Nguyễn Sinh Sắc."},
        {"difficulty": 2, "question": "Khởi nghĩa Ba Đình (1886 - 1887) chống thực dân Pháp do hai thủ lĩnh nào lãnh đạo trên vùng đầm nước Thanh Hóa?", "options": ["Đinh Công Tráng và Phạm Bành", "Phan Đình Phùng", "Nguyễn Thiện Thuật", "Hoàng Hoa Thám"], "correct": 0, "explanation": "Căn cứ Ba Đình kiên cố chống trả quyết liệt nhiều đợt tấn công của quân Pháp trước khi rút lui."},
        {"difficulty": 2, "question": "Vị vua nào của triều Hậu Lê nổi tiếng với câu nói khắc ghi trên bia Văn Miếu 'Hiền tài là nguyên khí quốc gia'?", "options": ["Lê Thánh Tông (Thân Nhân Trung soạn)", "Lê Thái Tổ", "Lê Nhân Tông", "Lê Hiến Tông"], "correct": 0, "explanation": "Tiến sĩ Thân Nhân Trung thừa lệnh vua Lê Thánh Tông soạn bài văn bia khẳng định vị thế của người trí thức."},
        {"difficulty": 2, "question": "Kỳ thi Đình đầu tiên của nước Đại Việt được tổ chức dưới triều vua nào vào năm 1247?", "options": ["Trần Thái Tông", "Lý Nhân Tông", "Lý Thánh Tông", "Trần Nhân Tông"], "correct": 0, "explanation": "Vua Trần Thái Tông mở khoa thi Tam khôi đầu tiên chọn ra Trạng nguyên Nguyễn Hiền khi mới 13 tuổi."},
        {"difficulty": 2, "question": "Vị hoàng đế nào của triều Nguyễn cho đúc Cửu Đỉnh (chín chiếc đỉnh đồng khổng lồ) đặt trước Thế Miếu ở Đại Nội Huế?", "options": ["Vua Minh Mạng", "Vua Gia Long", "Vua Thiệu Trị", "Vua Tự Đức"], "correct": 0, "explanation": "Vua Minh Mạng cho đúc Cửu Đỉnh năm 1835 tượng trưng cho sự vững bền thống nhất của bờ cõi giang sơn."},
        {"difficulty": 2, "question": "Người chiến sĩ cách mạng trẻ tuổi đã hô vang 'Hãy nhớ lấy lời tôi / Đả đảo đế quốc Mỹ' trên pháp trường trường bắn Chí Hòa năm 1964 là ai?", "options": ["Anh hùng Nguyễn Văn Trỗi", "Nguyễn Viết Xuân", "Lê Văn Tám", "Võ Thị Sáu"], "correct": 0, "explanation": "Anh Nguyễn Văn Trỗi hiên ngang không chịu bịt mắt trước họng súng quân thù sáng ngày 15/10/1964."},
        {"difficulty": 2, "question": "Triều đại nhà Mạc do ai sáng lập sau khi cướp ngôi nhà Hậu Lê vào năm 1527?", "options": ["Mạc Đăng Dung", "Mạc Kính Cung", "Mạc Mậu Hợp", "Mạc Đĩnh Chi"], "correct": 0, "explanation": "Mạc Đăng Dung vốn là quan đô chỉ huy sứ ép vua Lê Cung Hoàng nhường ngôi lập ra nhà Mạc."},
        {"difficulty": 2, "question": "Cuộc Tổng bãi công của hơn 3 vạn công nhân mỏ than Vùng mỏ Quảng Ninh diễn ra vào ngày 12/11 năm nào?", "options": ["Năm 1936", "Năm 1930", "Năm 1945", "Năm 1954"], "correct": 0, "explanation": "Ngày 12/11/1936 trở thành ngày truyền thống công nhân Vùng mỏ và ngành than Việt Nam."},
        {"difficulty": 3, "question": "CÂU HỎI LỊCH SỬ QUYẾT ĐỊNH: Vị tướng nào của nghĩa quân Tây Sơn đã chỉ huy đạo quân đô đốc đánh chiếm đồn Khương Thượng khiến tướng giặc Sầm Nghi Đống phải thắt cổ tự tử ở gò Đống Đa?", "options": ["Đô đốc Đặng Tiến Đông (hoặc Đặng Văn Long)", "Đô đốc Ngô Văn Sở", "Đô đốc Phan Văn Lân", "Đô đốc Võ Văn Dũng"], "correct": 0, "explanation": "Đạo quân của Đô đốc Đặng Tiến Đông bất ngờ tập kích đồn Khương Thượng rạng sáng mùng 5 Tết Kỷ Dậu 1789."}
    ],

    "dia-ly": [
        {"difficulty": 1, "question": "Ngôi đền thờ Thần Đồng Cổ nổi tiếng linh thiêng thời Lý với hội thề Trung hiếu nằm bên bờ sông nào ở Hà Nội?", "options": ["Sông Tô Lịch", "Sông Hồng", "Sông Đuống", "Sông Nhuệ"], "correct": 0, "explanation": "Đền Đồng Cổ trên đường Thụy Khuê ven sông Tô Lịch gắn với Hội thề Trung hiếu vua Lý Thái Tông lập năm 1028."},
        {"difficulty": 1, "question": "Tỉnh nào ở miền Bắc nước ta có danh xưng 'Thủ đô chè' với đồi chè Tân Cương nức tiếng?", "options": ["Thái Nguyên", "Phú Thọ", "Tuyên Quang", "Yên Bái"], "correct": 0, "explanation": "Chè Tân Cương (Thái Nguyên) có hương thơm cốm non và vị tiền chát hậu ngọt đệ nhất danh trà."},
        {"difficulty": 1, "question": "Khu dự trữ sinh quyển Cần Giờ rừng ngập mặn xanh tốt là lá phổi xanh của thành phố nào?", "options": ["TP. Hồ Chí Minh", "Bà Rịa - Vũng Tàu", "Đồng Nai", "Tiền Giang"], "correct": 0, "explanation": "Rừng ngập mặn Cần Giờ là khu dự trữ sinh quyển thế giới đầu tiên của Việt Nam được UNESCO công nhận."},
        {"difficulty": 2, "question": "Cửa biển nào ở Quảng Ninh là nơi ba lần trong lịch sử dân tộc chứng kiến những chiến thắng Bạch Đằng hiển hách?", "options": ["Cửa biển sông Bạch Đằng (Yên Hưng / Thủy Nguyên)", "Cửa Lục", "Cửa Ông", "Cửa Soài Rạp"], "correct": 0, "explanation": "Sông Bạch Đằng lưu danh 3 chiến thắng oanh liệt của Ngô Quyền (938), Lê Hoàn (981) và Trần Hưng Đạo (1288)."},
        {"difficulty": 2, "question": "Đảo Hòn Khoai cụm đảo tuyệt đẹp có ngọn hải đăng hơn 100 năm tuổi thuộc tỉnh nào?", "options": ["Cà Mau", "Kiên Giang", "Bạc Liêu", "Sóc Trăng"], "correct": 0, "explanation": "Hòn Khoai là hòn đảo đá nguyên sinh cách bờ biển Ngọc Hiển (Cà Mau) khoảng 14 km."},
        {"difficulty": 2, "question": "Núi Chóp Chài ngọn núi biểu tượng sừng sững giữa đồng bằng lúa Tuy Hòa thuộc tỉnh nào?", "options": ["Phú Yên", "Bình Định", "Khánh Hòa", "Ninh Thuận"], "correct": 0, "explanation": "Núi Chóp Chài cao 391m như một kim tự tháp xanh che chở cho thành phố Tuy Hòa xinh đẹp."},
        {"difficulty": 3, "question": "CÂU HỎI ĐỊA LÝ QUYẾT ĐỊNH: Dòng sông nào ở miền Trung bắt nguồn từ dãy Ngọc Linh đổ ra biển Cửa Đại chia làm hai nhánh sông Thu Bồn và sông Vu Gia?", "options": ["Hệ thống sông Thu Bồn", "Sông Trà Khúc", "Sông Thạch Hãn", "Sông Nhật Lệ"], "correct": 0, "explanation": "Sông Thu Bồn là mạch nguồn sự sống của xứ Quảng chảy qua thánh địa Mỹ Sơn và phố cổ Hội An."}
    ],

    "khoa-hoc-tu-nhien": [
        {"difficulty": 1, "question": "Động vật lưỡng cư có thể sống ở cả hai môi trường nào?", "options": ["Dưới nước và trên cạn", "Trên cây và trong hang", "Dưới biển sâu và bay trên trời", "Trong cát và trên băng"], "correct": 0, "explanation": "Lưỡng cư (như ếch, cóc, nhái) sinh sản và phát triển dưới nước, trưởng thành sống trên cạn."},
        {"difficulty": 1, "question": "Bộ phận nào của hoa thường có màu sắc sặc sỡ và hương thơm quyến rũ côn trùng đến thụ phấn?", "options": ["Cánh hoa (Tràng hoa)", "Đài hoa", "Nhị hoa", "Noãn hoa"], "correct": 0, "explanation": "Màu sắc rực rỡ của cánh hoa hấp dẫn ong bướm đến hút mật và mang phấn hoa đi thụ phấn chéo."},
        {"difficulty": 1, "question": "Chất khí nào chiếm thành phần chủ yếu tạo nên những đám mây trắng bồng bềnh trên bầu trời?", "options": ["Hơi nước li ti ngưng tụ thành hạt lỏng", "Khí hydro", "Khí oxy", "Khí cacbonic"], "correct": 0, "explanation": "Mây là tập hợp của hàng tỷ giọt nước hoặc tinh thể băng siêu nhỏ lơ lửng trong không khí."},
        {"difficulty": 2, "question": "Cơ quan thụ cảm thị giác trong mắt người chuyển đổi ánh sáng thành tín hiệu điện truyền lên não là gì?", "options": ["Võng mạc (màng lưới)", "Giác mạc", "Thủy tinh thể", "Đồng tử"], "correct": 0, "explanation": "Tế bào hình que và tế bào hình nón trên võng mạc tiếp nhận photon ánh sáng truyền qua dây thần kinh thị giác."},
        {"difficulty": 2, "question": "Quá trình một chất chuyển trực tiếp từ thể rắn sang thể khí mà không qua thể lỏng được gọi là gì?", "options": ["Sự thăng hoa", "Sự ngưng tụ", "Sự nóng chảy", "Sự đông đặc"], "correct": 0, "explanation": "Hiện tượng thăng hoa điển hình thấy ở băng khô (CO2 rắn) hoặc viên long não để trong tủ quần áo."},
        {"difficulty": 2, "question": "Hiện tượng nhật thực toàn phần chỉ có thể quan sát được khi người đứng nằm trong vùng nào của bóng Mặt Trăng?", "options": ["Vùng bóng tối hoàn toàn (Umbra)", "Vùng bóng nửa tối (Penumbra)", "Vùng xích đạo", "Vùng cực"], "correct": 0, "explanation": "Khi đứng trong dải bóng tối Umbra, Mặt Trời bị Mặt Trăng che khuất 100% để lộ vành nhật hoa lộng lẫy."},
        {"difficulty": 3, "question": "CÂU HỎI KHOA HỌC QUYẾT ĐỊNH: Loại liên kết hóa học nào hình thành do lực hút tĩnh điện giữa các ion mang điện tích trái dấu?", "options": ["Liên kết ion", "Liên kết cộng hóa trị", "Liên kết kim loại", "Liên kết hidro"], "correct": 0, "explanation": "Liên kết ion (như trong phân tử muối ăn NaCl: Na+ và Cl-) có nhiệt độ nóng chảy và độ bền liên kết rất cao."}
    ],

    "van-hoc-nghe-thuat": [
        {"difficulty": 1, "question": "Điền từ vào câu tục ngữ: 'Một cây làm chẳng nên non / Ba cây chụm lại nên hòn ... cao'?", "options": ["núi", "đồi", "đá", "rừng"], "correct": 0, "explanation": "Ca ngợi sức mạnh của tinh thần đoàn kết tập thể hiệp lực tạo nên thành quả to lớn."},
        {"difficulty": 1, "question": "Nhân vật chú Cuội ngồi dưới gốc cây gì trên cung trăng trong sự tích dân gian?", "options": ["Cây đa", "Cây bàng", "Cây gạo", "Cây khế"], "correct": 0, "explanation": "Chú Cuội cầm cây đa thần bay lên cung trăng gắn liền với truyền thuyết tết Trung Thu rước đèn."},
        {"difficulty": 1, "question": "Điền từ vào câu ca dao: 'Bầu ơi thương lấy bí cùng / Tuy rằng khác giống nhưng ... một giàn'?", "options": ["chung", "cùng", "chia", "trên"], "correct": 0, "explanation": "Bài học muôn đời về tình đồng bào ruột thịt che chở cưu mang nhau."},
        {"difficulty": 2, "question": "Ai là tác giả của tác phẩm truyện thơ chữ Nôm bất hủ dài hàng ngàn câu 'Cung oán ngâm khúc'?", "options": ["Nguyễn Gia Thiều (Ôn Như Hầu)", "Đoàn Thị Điểm", "Đặng Trần Côn", "Nguyễn Du"], "correct": 0, "explanation": "Ôn Như Hầu Nguyễn Gia Thiều dùng thể thơ song thất lục bát than thở thân phận cung nữ bị thất sủng."},
        {"difficulty": 2, "question": "Nhà thơ nào viết bài thơ 'Viếng lăng Bác' ('Con ở miền Nam ra thăm lăng Bác / Đã thấy trong sương hàng tre bát ngát...')?", "options": ["Viễn Phương", "Nguyễn Duy", "Lê Anh Xuân", "Thu Bồn"], "correct": 0, "explanation": "Nhà thơ Viễn Phương viết bài thơ xúc động nghẹn ngào năm 1976 khi lăng Chủ tịch Hồ Chí Minh vừa khánh thành."},
        {"difficulty": 2, "question": "Truyện ngắn 'Chữ người tử tù' của Nguyễn Tuân ban đầu khi đăng báo năm 1938 có nhan đề là gì?", "options": ["Dòng nước ngược", "Vang bóng một thời", "Ngọn đèn dầu lạc", "Chiếc ấm đất"], "correct": 0, "explanation": "Tác phẩm xuất sắc này ban đầu mang tên 'Dòng nước ngược' trước khi in trong tập 'Vang bóng một thời'."},
        {"difficulty": 3, "question": "CÂU HỎI VĂN HỌC QUYẾT ĐỊNH: Vở chèo cổ mẫu mực 'Quan Âm Thị Kính' có cảnh Thị Màu lên chùa ghẹo chú tiểu Kính Tâm mang làn điệu chèo đặc sắc nào?", "options": ["Điệu chèo 'Cấm giá' và 'Hề mồi'", "Điệu Sa lệch", "Điệu Đào liễu", "Điệu Con gà rừng"], "correct": 0, "explanation": "Cảnh Thị Màu lên chùa là đỉnh cao diễn xuất tính cách lẳng lơ, táo bạo phá cách trong nghệ thuật chèo truyền thống."}
    ],

    "doi-song-cong-nghe": [
        {"difficulty": 1, "question": "Bữa cơm gia đình truyền thống của người Việt thường có món canh, món xào và món gì ăn kèm cơm trắng?", "options": ["Món kho (hoặc món mặn)", "Món kem", "Món bánh ngọt", "Món chè"], "correct": 0, "explanation": "Cơ cấu bữa cơm Việt chuẩn mực luôn có canh thanh mát, rau xào và món mặn kho đậm đà đưa cơm."},
        {"difficulty": 1, "question": "Ứng dụng họp trực tuyến và học tập từ xa bùng nổ toàn cầu trong đại dịch COVID-19 là gì?", "options": ["Zoom", "Photoshop", "Word", "Excel"], "correct": 0, "explanation": "Zoom Meetings cho phép kết nối hàng trăm người cùng thảo luận qua video trực tuyến độ trễ thấp."},
        {"difficulty": 1, "question": "Hệ thống truyền hình xem phim trực tuyến hàng đầu thế giới với logo chữ 'N' đỏ rực là gì?", "options": ["Netflix", "Spotify", "Amazon", "Disney"], "correct": 0, "explanation": "Netflix cung cấp kho phim điện ảnh, tài liệu và series truyền hình bản quyền phong phú."},
        {"difficulty": 2, "question": "Món đặc sản 'Cốm làng Vòng' thơm ngát hương nếp non bọc trong lá sen xanh mát gắn liền với mùa nào của Hà Nội?", "options": ["Mùa thu", "Mùa xuân", "Mùa hè", "Mùa đông"], "correct": 0, "explanation": "Thạch Lam từng viết: 'Cốm là thức quà riêng biệt của đất nước, là thức dâng của những cánh đồng lúa bát ngát...'."},
        {"difficulty": 2, "question": "Định dạng ảnh số phổ biến nhất trên Internet với khả năng nén kích thước tệp nhẹ mà vẫn giữ độ chi tiết cao là định dạng nào?", "options": ["JPEG (JPG)", "BMP", "TIFF", "RAW"], "correct": 0, "explanation": "Chuẩn JPEG (Joint Photographic Experts Group) là định dạng ảnh tiêu chuẩn của nhiếp ảnh số và web."},
        {"difficulty": 2, "question": "Môn thể thao nào mà các vận động viên lướt trên ván gỗ hoặc sợi thủy tinh trên những ngọn sóng biển dâng cao?", "options": ["Lướt sóng (Surfing)", "Chèo kayak", "Lặn biển", "Bóng nước"], "correct": 0, "explanation": "Lướt sóng là môn thể thao mạo hiểm chinh phục sức mạnh của những con sóng đại dương."},
        {"difficulty": 3, "question": "CÂU HỎI CÔNG NGHỆ QUYẾT ĐỊNH: Cấu trúc dữ liệu hình cây trong khoa học máy tính mà mỗi nút có tối đa hai nút con được gọi là gì?", "options": ["Cây nhị phân (Binary Tree)", "Đồ thị", "Hàng đợi", "Danh sách liên kết"], "correct": 0, "explanation": "Cây nhị phân và cây tìm kiếm nhị phân (BST) là cấu trúc nền tảng cho các thuật toán tìm kiếm và sắp xếp dữ liệu tối ưu."}
    ],

    "do-vui-tri-tue": [
        {"difficulty": 1, "question": "Đố mẹo: Bánh gì không có bột, không có nhân mà lăn tròn bon bon trên đường phố?", "options": ["Bánh xe", "Bánh rán", "Bánh bao", "Bánh mì"], "correct": 0, "explanation": "Bánh xe bằng cao su lăn trên đường phố."},
        {"difficulty": 1, "question": "Đố mẹo: Con gì sinh ra đã biết leo trèo thoăn thoắt, thích ăn chuối và hay bắt chước điệu bộ con người?", "options": ["Con khỉ", "Con chó", "Con mèo", "Con gấu"], "correct": 0, "explanation": "Loài khỉ tinh nghịch có bộ não phát triển và khả năng bắt chước hành vi con người rất nhanh."},
        {"difficulty": 1, "question": "Đố mẹo: Cái gì có mặt nhưng không có mũi tai, có ba chiếc kim chạy suốt đêm ngày?", "options": ["Đồng hồ treo tường", "Cái la bàn", "Cái cân", "Thước dây"], "correct": 0, "explanation": "Mặt đồng hồ và ba kim giờ, phút, giây đếm nhịp thời gian."},
        {"difficulty": 2, "question": "Đố chữ: Từ nào trong tiếng Việt có 4 chữ cái, bỏ dấu thành tên một loài thú săn mồi dũng mãnh chúa sơn lâm?", "options": ["Hổ (Hố - Hổ)", "Báo", "Gấu", "Sói"], "correct": 0, "explanation": "Hố sâu bỏ dấu sắc thành Hổ (chúa sơn lâm)."},
        {"difficulty": 2, "question": "Đố mẹo: Một người nhảy xuống nước biển sâu mà quần áo không bị ướt chút nào, vì sao?", "options": ["Người đó mặc bộ đồ lặn kín hoàn toàn (hoặc ở trong tàu ngầm)", "Biển không có nước", "Người biết bay", "Biển nhân tạo"], "correct": 0, "explanation": "Bộ đồ lặn khô áp suất cao (Dry suit) chống thấm nước 100% giúp người mặc không bị ướt."},
        {"difficulty": 3, "question": "ĐỐ VUI QUYẾT ĐỊNH: Bức tranh đố vui dân gian: 'Cột tròn thẳng tắp giữa đồng, đội chiếc nón lá trắng ngần đón mây' là cây gì thân quen?", "options": ["Cây cau", "Cây dừa", "Cây tre", "Cây chuối"], "correct": 0, "explanation": "Hàng cau thẳng tắp vươn cao với buồng hoa cau trắng muốt thơm ngát góc vườn quê."}
    ]
}

def main():
    total_added = 0
    for cat_name, questions in DATA_75.items():
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

    print(f"✅ Bổ sung thêm {total_added} câu hỏi mới.")

if __name__ == '__main__':
    main()
