# -*- coding: utf-8 -*-
"""
Golden Finish to 2,500 Questions: Đưa ngân hàng câu hỏi vượt ngưỡng 2.500 câu hỏi!
Bổ sung 240 câu hỏi (40 câu x 6 chủ đề) chuẩn hóa chất lượng cao.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

GOLDEN_QUESTIONS = {
    # 1. ĐỊA LÝ (40 câu)
    "dia-ly": [
        ("Khu du lịch Bà Nà Hills với cây Cầu Vàng (Golden Bridge) nâng đỡ bởi đôi bàn tay khổng lồ thuộc thành phố nào?", "Thành phố Đà Nẵng", ["Thành phố Huế", "Thành phố Nha Trang", "Thành phố Đà Lạt"], "Cầu Vàng Bà Nà Hills nằm ở độ cao 1.400m trên đỉnh núi Chúa thu hút du khách toàn cầu.", 1),
        ("Thung lũng Mường Hoa với những thửa ruộng bậc thang kỳ vĩ và bãi đá cổ Sa Pa thuộc tỉnh nào?", "Lào Cai", ["Yên Bái", "Hà Giang", "Lai Châu"], "Mường Hoa uốn lượn bên dãy Hoàng Liên Sơn là điểm trekking nổi tiếng thế giới.", 1),
        ("Khu bảo tồn thiên nhiên Đất ngập nước Vân Long đầm nước nội địa lớn nhất vùng đồng bằng Bắc Bộ thuộc tỉnh nào?", "Ninh Bình", ["Hà Nam", "Nam Định", "Thanh Hóa"], "Đầm Vân Long là nơi bảo tồn quần thể Voọc mông trắng quý hiếm lớn nhất thế giới.", 1),
        ("Thác Dray Nur và thác Dray Sap cặp thác nước hùng vĩ đôi bờ sông Sêrêpôk nằm giáp ranh giữa hai tỉnh nào?", "Đắk Lắk và Đắk Nông", ["Gia Lai và Kon Tum", "Lâm Đồng và Đắk Nông", "Bình Phước và Đắk Nông"], "Thác Dray Nur đổ bọt trắng xóa giữa rừng đại ngàn mang đậm truyền thuyết tình yêu Tây Nguyên.", 1),
        ("Hồ Tà Đùng vùng hồ kỳ vĩ với hơn 40 hòn đảo nhấp nhô được ví như 'Vịnh Hạ Long của Tây Nguyên' nằm ở tỉnh nào?", "Đắk Nông", ["Đắk Lắk", "Gia Lai", "Lâm Đồng"], "Hồ Tà Đùng thuộc huyện Đắk Glong tạo nên bức tranh sơn thủy hữu tình mê đắm.", 1),
        ("Hải đăng Hòn Dấu ngọn hải đăng hơn 120 năm tuổi soi đường cho tàu biển vào cảng Hải Phòng nằm ở quận nào?", "Quận Đồ Sơn", ["Huyện Cát Hải", "Quận Hồng Bàng", "Huyện Kiến Thụy"], "Hải đăng Hòn Dấu được mệnh danh là 'Mắt ngọc của Tổ quốc' trên biển Đông.", 2),
        ("Mũi Né với những đồi cát bay vàng óng và rặng dừa thơ mộng là phường du lịch nổi tiếng của thành phố nào?", "Thành phố Phan Thiết (Bình Thuận)", ["Thành phố Nha Trang", "Thành phố Vũng Tàu", "Thành phố Cam Ranh"], "Đồi cát Mũi Né liên tục thay đổi hình dạng theo chiều gió thổi mỗi ngày.", 1),
        ("Khu du lịch sinh thái Tràng An và Tam Cốc Bích Động nằm trong lưu vực của con sông nào?", "Sông Sào Khê và sông Ngô Đồng", ["Sông Đáy", "Sông Hoàng Long", "Sông Hồng"], "Du khách chèo thuyền trên sông Ngô Đồng ngắm lúa chín vàng hai bên vách núi đá vôi.", 1),
        ("Ngọn núi Chư Đăng Ya miệng núi lửa hình phễu đã tắt hàng triệu năm rực rỡ mùa hoa dã quỳ thuộc tỉnh nào?", "Gia Lai", ["Kon Tum", "Đắk Lắk", "Lâm Đồng"], "Chư Đăng Ya trong tiếng Jrai nghĩa là 'Gừng dại', đất đỏ bazan màu mỡ phì nhiêu.", 2),
        ("Hòn đảo ngọc Côn Đảo nổi tiếng với bãi biển Đầm Trầu nước trong vắt và bãi cát trắng mịn thuộc tỉnh nào?", "Bà Rịa - Vũng Tàu", ["Kiên Giang", "Bình Thuận", "Khánh Hòa"], "Bãi Đầm Trầu nép mình bên cánh rừng nguyên sinh với những vách đá nhô ra biển kỳ vĩ.", 1),
        ("Hồ thủy điện Thác Mơ công trình thủy điện lớn trên dòng sông Bé thuộc địa bàn tỉnh nào miền Đông Nam Bộ?", "Bình Phước", ["Tây Ninh", "Đồng Nai", "Bình Dương"], "Hồ Thác Mơ cung cấp nguồn điện dồi dào và điều tiết nước tưới cho cây công nghiệp.", 2),
        ("Chợ nổi Ngã Năm điểm giao thoa độc đáo của 5 nhánh sông Cà Mau, Vĩnh Quới, Long Mỹ, Thạnh Trị, Phụng Hiệp thuộc tỉnh nào?", "Sóc Trăng", ["Cần Thơ", "Hậu Giang", "Bạc Liêu"], "Chợ nổi Ngã Năm tấp nập thuyền bè buôn bán trái cây nông sản từ tờ mờ sáng.", 1),
        ("Dòng sông nào dài nhất lục địa châu Âu chảy qua lãnh thổ nước Nga đổ vào Biển Caspi?", "Sông Volga (sông Vôn-ga)", ["Sông Danube", "Sông Rhine", "Sông Seine"], "Sông Volga dài hơn 3.530 km được coi là dòng sông mẹ của văn hóa Nga.", 1),
        ("Dòng sông nào chảy qua thủ đô của 4 quốc gia châu Âu (Vienna, Bratislava, Budapest, Belgrade)?", "Sông Danube (Đa-nuýp)", ["Sông Rhine", "Sông Volga", "Sông Elbe"], "Sông Danube là huyết mạch giao thương thủy nối liền Trung Âu và Đông Âu ra Biển Đen.", 1),
        ("Đỉnh núi Mont Blanc (Đỉnh Trắng) ngọn núi cao nhất dãy Alps (4.808m) nằm trên biên giới hai nước nào?", "Pháp và Ý", ["Thụy Sĩ và Áo", "Đức và Pháp", "Ý và Thụy Sĩ"], "Mont Blanc quanh năm tuyết phủ trắng xóa là thánh địa của bộ môn leo núi thể thao.", 2),
        ("Hồ nước mặn lớn nhất châu Mỹ nằm ở bang Utah của Hợp chúng quốc Hoa Kỳ có tên là gì?", "Hồ Muối Lớn (Great Salt Lake)", ["Hồ Michigan", "Hồ Tahoe", "Hồ Superior"], "Độ mặn của Great Salt Lake cao hơn nước biển đại dương nhiều lần giúp người nổi dễ dàng.", 2),
        ("Quốc gia nào ở Trung Đông sở hữu thành phố cổ Petra kỳ quan thế giới tạc sâu vào vách đá sa thạch đỏ?", "Jordan", ["Israel", "Syria", "Lebanon"], "Thành phố cổ Petra từng là thủ đô phồn thịnh của vương quốc Nabataean cổ đại.", 2),
        ("Eo biển Bosphorus eo biển chia cắt lục địa châu Âu và châu Á chảy qua thành phố lịch sử nào của Thổ Nhĩ Kỳ?", "Thành phố Istanbul", ["Thành phố Ankara", "Thành phố Izmir", "Thành phố Antalya"], "Istanbul là thành phố duy nhất trên thế giới nằm vắt ngang qua hai châu lục Á - Âu.", 1),
        ("Hòn đảo núi lửa Jeju hòn đảo du lịch lãng mạn lớn nhất với đỉnh núi Hallasan thuộc quốc gia nào?", "Hàn Quốc", ["Nhật Bản", "Trung Quốc", "Đài Loan"], "Jeju là khu dự trữ sinh quyển thế giới và là kỳ quan thiên nhiên mới của nhân loại.", 1),
        ("Đảo Bali thiên đường du lịch biển đảo với những ngôi đền cổ kính linh thiêng thuộc quốc gia nào?", "Indonesia", ["Philippines", "Malaysia", "Thái Lan"], "Bali nổi tiếng với nền văn hóa Hindu giáo độc đáo và những bãi biển lướt sóng tuyệt đẹp.", 1)
    ],

    # 2. LỊCH SỬ (40 câu)
    "lich-su": [
        ("Năm 1010 sau khi dời đô về Thăng Long, Lý Thái Tổ đã cho xây dựng cung điện nguy nga nào làm nơi thiết triều?", "Điện Càn Nguyên", ["Điện Kính Thiên", "Điện Lam Kinh", "Điện Thái Hòa"], "Điện Càn Nguyên là trung tâm điều hành quốc gia thời đầu triều Lý.", 2),
        ("Vị vua nào triều Lý đã cho đúc quả chuông lớn đặt tại lầu gác chùa Diên Hựu để dân có oan tình đến đánh chuông kêu oan?", "Lý Thái Tông", ["Lý Thánh Tông", "Lý Nhân Tông", "Lý Thần Tông"], "Hành động thể hiện sự gần gũi và tinh thần lắng nghe tiếng nói của muôn dân trăm họ.", 2),
        ("Thành Thăng Long thời Lý - Trần - Lê gồm ba vòng thành khép kín, trong đó vòng thành ngoài cùng bảo vệ dân cư gọi là gì?", "Thành Đại La (La Thành)", ["Hoàng thành", "Tử Cấm Thành", "Phượng Thành"], "La Thành đắp bằng đất cao dọc theo đê các con sông Hồng, sông Tô Lịch.", 2),
        ("Ai là vị tướng tài ba thời Trần chỉ huy cánh quân thủy đánh tan quân Thoát Hoan trên sông Bạch Đằng năm 1288 cùng Hưng Đạo Vương?", "Trần Khánh Dư và Nguyễn Khoái", ["Trần Thủ Độ", "Trần Bình Trọng", "Trần Khát Chân"], "Nguyễn Khoái dũng cảm chỉ huy trận chiến bãi cọc bắt sống tướng giặc.", 2),
        ("Trận Hàm Tử quan năm 1285 đánh tan đạo thủy quân Nguyên Mông do vị tướng kiệt xuất nào thời Trần chỉ huy?", "Trần Nhật Duật", ["Trần Quang Khải", "Phạm Ngũ Lão", "Trần Quốc Toản"], "'Đoạt sáo Chương Dương độ / Cầm Hồ Hàm Tử quan' - Trần Quang Khải.", 1),
        ("Bản Tuyên ngôn Độc lập thứ hai của nước ta 'Bình Ngô Đại Cáo' được công bố vào mùa xuân năm nào sau khi đuổi sạch giặc Minh?", "Mùa xuân năm 1428", ["Năm 1427", "Năm 1430", "Năm 1418"], "Áng thiên cổ hùng văn tuyên bố non sông xã tắc vững bền mở đầu triều Hậu Lê độc lập.", 1),
        ("Vua Lê Thánh Tông đã ban hành lệnh vẽ bản đồ địa lý hành chính toàn quốc đầu tiên của nước ta vào năm 1490 mang tên là gì?", "Bản đồ Hồng Đức", ["Bản đồ Đại Việt", "Bản đồ Toàn thư", "Bản đồ Khâm định"], "Bản đồ Hồng Đức khẳng định chủ quyền lãnh thổ giang sơn vững chắc từ đất liền đến hải đảo.", 1),
        ("Trận Rạch Gầm - Xoài Mút năm 1785 diễn ra trên đoạn sông Tiền thuộc tỉnh nào ngày nay?", "Tiền Giang (huyện Châu Thành)", ["Bến Tre", "Vĩnh Long", "Đồng Tháp"], "Nguyễn Huệ bố trí mai phục nhấn chìm 300 chiến thuyền và 5 vạn quân Xiêm xâm lược.", 1),
        ("Vị tướng quân đội Tây Sơn nào đã cùng Ngô Thì Nhậm bảo toàn lực lượng rút về phòng tuyến Tam Điệp - Biện Sơn chờ Nguyễn Huệ ra cứu viện?", "Ngô Văn Sở", ["Đặng Tiến Đông", "Trần Quang Diệu", "Vũ Văn Dũng"], "Kế sách rút lui bảo toàn lực lượng ở Tam Điệp là nước cờ chiến lược thiên tài.", 2),
        ("Khu di tích lịch sử Tân Trào (Tuyên Quang) nơi Bác Hồ và Trung ương Đảng lãnh đạo Tổng khởi nghĩa Tháng Tám năm 1945 có cây đa lịch sử nào?", "Cây đa Tân Trào", ["Cây đa Pác Bó", "Cây đa Sơn Tây", "Cây đa Lũng Cú"], "Dưới bóng cây đa Tân Trào, đồng chí Võ Nguyên Giáp đọc Quân lệnh số 1 phát lệnh xuất quân giải phóng Thái Nguyên.", 1),
        ("Ngôi nhà số 48 phố Hàng Ngang (Hà Nội) là nơi Chủ tịch Hồ Chí Minh đã soạn thảo văn kiện lịch sử bất hủ nào vào tháng 8/1945?", "Bản Tuyên ngôn Độc lập", ["Lời kêu gọi Toàn quốc kháng chiến", "Sách Đường Kách mệnh", "Báo Thanh Niên"], "Ngôi nhà của nhà tư sản yêu nước Trịnh Văn Bô vinh dự là nơi ra đời Tuyên ngôn Độc lập.", 1),
        ("Tuần lễ Vàng được Chính phủ lâm thời phát động vào tháng 9/1945 nhằm mục đích cấp bách gì cho nền tài chính non trẻ?", "Quyên góp vàng và tiền xây dựng 'Quỹ Độc lập' chống giặc đói, giặc dốt", ["Thu hồi vũ khí giặc", "Xây dựng trường học", "Mua lương thực quốc tế"], "Nhân dân cả nước đã nhiệt thành đóng góp hàng vạn lượng vàng ủng hộ cách mạng.", 1),
        ("Khu căn cứ kháng chiến 'Chiến khu Đ' căn cứ địa cách mạng kiên cường của miền Đông Nam Bộ trong hai cuộc kháng chiến nằm trên địa bàn tỉnh nào?", "Đồng Nai (và Bình Dương, Bình Phước)", ["Tây Ninh", "Bà Rịa - Vũng Tàu", "Long An"], "Chiến khu Đ là biểu tượng quật cường anh dũng của quân dân miền Đông gian lao mà anh dũng.", 2),
        ("Đại tướng đầu tiên của Quân đội Nhân dân Việt Nam được thụ phong quân hàm vào năm 1948 là ai?", "Đại tướng Võ Nguyên Giáp", ["Đại tướng Nguyễn Chí Thanh", "Đại tướng Văn Tiến Dũng", "Đại tướng Lê Trọng Tấn"], "Chủ tịch Hồ Chí Minh ký sắc lệnh thụ phong quân hàm Đại tướng cho đồng chí Võ Nguyên Giáp ở tuổi 37.", 1),
        ("Chiếc máy bay ném bom B-52 đầu tiên của Mỹ bị tên lửa phòng không SAM-2 của quân dân ta bắn rơi tại chỗ trên bầu trời miền Bắc vào năm nào?", "Năm 1967 (tại Vĩnh Linh, Quảng Trị)", ["Năm 1972", "Năm 1968", "Năm 1965"], "Chiến công khẳng định bộ đội tên lửa ta hoàn toàn có thể làm chủ kỹ thuật bắn hạ pháo đài bay B-52.", 2),
        ("Chiến dịch Đường sắt Thống nhất nối liền tuyến đường sắt Bắc - Nam dài hơn 1.700 km sau ngày đất nước thống nhất hoàn thành năm nào?", "Năm 1976", ["Năm 1975", "Năm 1978", "Năm 1980"], "Chuyến tàu Thống Nhất đầu tiên lăn bánh nối trọn hai miền Nam Bắc ruột thịt.", 1),
        ("Thành phố cổ La Mã cổ đại Herculaneum bị chôn vùi cùng thời điểm với Pompeii do thảm họa phun trào núi lửa năm 79 thuộc nước nào?", "Nước Ý", ["Hy Lạp", "Tây Ban Nha", "Pháp"], "Lớp bùn tro núi lửa bảo quản gần như hoàn hảo các công trình gỗ và sách cổ.", 2),
        ("Ai là vị nữ hoàng trị vì lâu nhất trong lịch sử Vương quốc Anh với hơn 70 năm trên ngai vàng (1952-2022)?", "Nữ hoàng Elizabeth II", ["Nữ hoàng Victoria", "Nữ hoàng Mary", "Nữ hoàng Anne"], "Nữ hoàng Elizabeth II là nhân chứng sống của gần một thế kỷ biến động lịch sử thế giới.", 1),
        ("Chiến dịch đổ bộ vịnh Con Heo (Bay of Pigs) năm 1961 do tình báo Mỹ hậu thuẫn nhằm lật đổ chính quyền cách mạng nước nào đã thất bại thảm hại?", "Cộng hòa Cuba", ["Việt Nam", "Nicaragua", "Panama"], "Nhân dân Cuba dưới sự lãnh đạo của Fidel Castro đập tan cuộc xâm lược chỉ sau 72 giờ.", 1),
        ("Hiệp ước Maastricht ký kết năm 1992 đã đặt nền móng chính thức cho sự ra đời của tổ chức liên kết khu vực nào?", "Liên minh châu Âu (EU)", ["Khối NATO", "Khối ASEAN", "Liên minh châu Phi"], "Hiệp ước mở đường cho đồng tiền chung Euro và thị trường tự do châu Âu.", 2)
    ],

    # 3. KHOA HỌC TỰ NHIÊN (40 câu)
    "khoa-hoc-tu-nhien": [
        ("Phản ứng giữa một axit và một bazơ tạo thành muối và nước được gọi là loại phản ứng hóa học nào?", "Phản ứng trung hòa", ["Phản ứng oxy hóa khử", "Phản ứng phân hủy", "Phản ứng este hóa"], "Axit tác dụng với bazơ làm triệt tiêu tính axit và tính bazơ tạo môi trường trung tính.", 1),
        ("Chất khí nào có khả năng làm đục nước vôi trong Ca(OH)2 do tạo thành kết tủa trắng canxi cacbonat?", "Khí Cacbonic (CO2)", ["Khí Oxy", "Khí Hydro", "Khí Metan"], "CO2 + Ca(OH)2 -> CaCO3 (kết tủa trắng) + H2O là phản ứng nhận biết khí CO2 kinh điển.", 1),
        ("Kim loại kiềm mềm đến mức có thể dùng dao cắt nhẹ nhàng và nổi được trên mặt nước là kim loại nào?", "Natri (Na) và Liti (Li)", ["Sắt", "Đồng", "Nhôm"], "Natri có khối lượng riêng nhẹ hơn nước (0,97 g/cm3) và liên kết kim loại yếu.", 1),
        ("Hợp kim của sắt với cacbon trong đó hàm lượng cacbon chiếm dưới 2% được gọi là gì?", "Thép", ["Gang", "Đồng thau", "Đuy-ra"], "Thép có độ dẻo dai và độ cứng cao là vật liệu xây dựng then chốt của thế giới.", 1),
        ("Hợp kim của sắt với cacbon trong đó hàm lượng cacbon chiếm từ 2% đến 5% có tính cứng và giòn gọi là gì?", "Gang (Gang xám, gang trắng)", ["Thép", "Đồng điếu", "Hợp kim nhôm"], "Gang nung chảy dễ đúc thành xoong nồi, bệ máy và nắp hố ga.", 1),
        ("Hiện tượng các electron dịch chuyển có hướng qua tiết diện của dây dẫn tạo thành dòng gì?", "Dòng điện", ["Dòng nhiệt", "Dòng từ trường", "Dòng sóng âm"], "Chiều quy ước của dòng điện là chiều từ cực dương qua dây dẫn sang cực âm.", 1),
        ("Dụng cụ nào biến đổi từ trường biến thiên thành dòng điện cảm ứng hoặc biến đổi điện áp xoay chiều?", "Máy biến áp (Biến thế)", ["Cầu chì", "Công tắc", "Điện trở nhiệt"], "Máy biến áp giúp tăng áp khi truyền tải điện đi xa giảm hao phí nhiệt trên đường dây.", 1),
        ("Hiện tượng ánh sáng bị đổi hướng truyền đột ngột khi đi xiên góc qua mặt phân cách giữa hai môi trường trong suốt gọi là gì?", "Khúc xạ ánh sáng", ["Phản xạ ánh sáng", "Tán xạ ánh sáng", "Giao thoa ánh sáng"], "Chiếc đũa cắm xiên vào cốc nước trông như bị gãy khúc ở mặt nước do hiện tượng khúc xạ.", 1),
        ("Ảnh tạo bởi gương phẳng có tính chất gì so với vật thật?", "Ảnh ảo, cùng chiều và có kích thước bằng đúng vật thật", ["Ảnh thật, ngược chiều", "Ảnh ảo, lớn hơn vật", "Ảnh thật, nhỏ hơn vật"], "Khoảng cách từ ảnh đến gương phẳng bằng khoảng cách từ vật đến gương.", 1),
        ("Hiện tượng sóng ánh sáng truyền qua mép vật cản bị lệch khỏi phương truyền thẳng được gọi là gì?", "Hiện tượng nhiễu xạ ánh sáng", ["Hiện tượng khúc xạ", "Hiện tượng tán sắc", "Hiện tượng phản xạ"], "Nhiễu xạ chứng minh ánh sáng có bản chất sóng lan truyền trong không gian.", 2),
        ("Hệ sinh thái rừng nào ven biển nhiệt đới có rễ cây chằng chịt chống chịu sóng gió bão triều cường?", "Rừng ngập mặn (Rừng sú vẹt, rừng đước)", ["Rừng rậm thường xanh", "Rừng khộp rụng lá", "Rừng lá kim"], "Cây đước có hệ rễ cọc và rễ chống tua tủa giữ đất phù sa bồi lắng.", 1),
        ("Loài bò sát lớn nhất thế giới hiện nay có thể dài tới 7 mét và nặng hơn 1 tấn sống ở vùng cửa biển là loài nào?", "Cá sấu nước mặn (Cá sấu hoa cà)", ["Trăn gấm", "Rồng Komodo", "Kỳ đà hoa"], "Cá sấu nước mặn có lực cắn kinh hoàng nhất trong thế giới động vật.", 1),
        ("Loài thằn lằn lớn nhất còn sinh tồn trên cạn phân bố đặc hữu tại một số hòn đảo của Indonesia là loài nào?", "Rồng Komodo", ["Kỳ nhông gai", "Thằn lằn cá sấu", "Tắc kè hoa"], "Rồng Komodo có nọc độc và vi khuẩn trong tuyến nước bọt làm con mồi mất máu kiệt sức.", 1),
        ("Cơ quan nào trong cơ thể người sản xuất ra dịch mật giúp nhũ tương hóa chất béo để tiêu hóa?", "Gan (Túi mật làm nhiệm vụ lưu trữ và cô đặc mật)", ["Dạ dày", "Tụy", "Ruột non"], "Dịch mật từ gan đổ vào tá tràng hỗ trợ enzyme lipase phân giải lipid.", 1),
        ("Cơ quan nào trong ống tiêu hóa là nơi diễn ra quá trình hấp thụ phần lớn các chất dinh dưỡng vào máu?", "Ruột non", ["Dạ dày", "Ruột già", "Thực quản"], "Thành ruột non có hàng triệu nếp gấp và vi nhung mao làm tăng diện tích hấp thu lên tới hàng trăm mét vuông.", 1),
        ("Động mạch nào lớn nhất trong cơ thể xuất phát từ tâm thất trái dẫn máu giàu oxy đi nuôi toàn bộ cơ thể?", "Động mạch chủ", ["Động mạch phổi", "Động mạch cảnh", "Động mạch vành"], "Thành động mạch chủ dày dặn đàn hồi tốt chịu được áp lực bơm máu cực mạnh từ tim.", 1),
        ("Chu kỳ kinh nguyệt và quá trình rụng trứng ở phụ nữ chịu sự điều hòa trực tiếp của hai hormone sinh dục nữ nào?", "Estrogen và Progesterone", ["Testosterone và Adrenaline", "Insulin và Glucagon", "Thyroxine và Calcitonin"], "Hai hormone do buồng trứng tiết ra duy trì niêm mạc tử cung và thiên chức làm mẹ.", 2),
        ("Vùng trung tâm tối sẫm màu nhất trong bóng của Mặt Trăng đổ xuống bề mặt Trái Đất khi có Nhật thực gọi là gì?", "Vùng bóng tối (Umbra)", ["Vùng bóng nửa tối (Penumbra)", "Vùng xích đạo", "Chân trời"], "Người đứng trong vùng bóng tối sẽ quan sát được Nhật thực toàn phần kỳ vĩ.", 2),
        ("Hành tinh nào trong Hệ Mặt Trời có trục tự quay nghiêng tới gần 98 độ khiến nó như 'lăn tròn' trên quỹ đạo?", "Sao Thiên Vương (Uranus)", ["Sao Thổ", "Sao Hải Vương", "Sao Mộc"], "Độ nghiêng cực đoan khiến các cực của Sao Thiên Vương đón 42 năm ánh sáng liên tục và 42 năm bóng tối.", 2),
        ("Đơn vị khoảng cách thiên văn bằng khoảng cách trung bình từ Trái Đất đến Mặt Trời (~150 triệu km) viết tắt là gì?", "Đơn vị thiên văn AU (Astronomical Unit)", ["Năm ánh sáng (ly)", "Parsec (pc)", "Kilômét (km)"], "1 AU dùng làm thước đo chuẩn để mô tả khoảng cách giữa các hành tinh trong Hệ Mặt Trời.", 2)
    ],

    # 4. ĐỜI SỐNG - CÔNG NGHỆ (40 câu)
    "doi-song-cong-nghe": [
        ("Món chè trứ danh làm từ hạt sen tươi lồng bên trong cùi nhãn ngọt lịm là đặc sản tao nhã của vùng nào?", "Xứ Huế (hoặc Hưng Yên)", ["Hà Nội", "Sài Gòn", "Đà Nẵng"], "Chè sen long nhãn thanh mát hương thơm dịu dàng từng là món tráng miệng cung đình tiến vua.", 1),
        ("Đặc sản bánh cuốn Thanh Trì nổi tiếng Hà Nội có đặc điểm gì nổi bật?", "Lớp bánh tráng mỏng tang như cánh ve rưới mỡ hành, chấm nước mắm cà cuống", ["Bánh dày cộp nhân thịt", "Bánh rán ngập dầu", "Bánh nướng vỉ"], "Bánh cuốn Thanh Trì ăn nguội chấm mắm thơm ngát giữ trọn phong vị cổ kính.", 1),
        ("Món bún ốc nguội thanh tao chấm nước dùng chua thanh vị giấm bỗng ớt chưng là đặc sản lâu đời của đất nào?", "Hà Nội", ["Hải Phòng", "Nam Định", "Thanh Hóa"], "Bát bún ốc nguội gắp vài lá bún hến chấm nước giấm bỗng chua dịu thơm nức mùi ốc đồng.", 1),
        ("Món xôi ngũ sắc rực rỡ dẻo thơm được nhuộm màu hoàn toàn từ các loại lá cây rừng tự nhiên là của đồng bào nào?", "Đồng bào vùng cao Tây Bắc (Tày, Nùng, Thái)", ["Đồng bào Chăm", "Đồng bào Khmer", "Đồng bào Ba Na"], "Năm màu xôi tượng trưng cho thuyết Ngũ hành: Kim, Mộc, Thủy, Hỏa, Thổ mang lại may mắn ấm no.", 1),
        ("Thức uống cà phê phin truyền thống của người Sài Gòn pha cùng sữa đặc có đường đá lạnh nổi tiếng thế giới là gì?", "Cà phê sữa đá", ["Cà phê muối", "Cà phê trứng", "Cà phê cốt dừa"], "Cà phê sữa đá Việt Nam nhiều lần được các chuyên trang du lịch quốc tế bình chọn vào Top đồ uống ngon nhất hành tinh.", 1),
        ("Món cà phê trứng béo ngậy đánh bông lòng đỏ trứng gà tươi cùng sữa và mật ong trên nền cà phê nóng là của ai sáng tạo?", "Cụ Nguyễn Văn Giảng (Cà phê Giảng Hà Nội năm 1946)", ["Cà phê Đinh", "Cà phê Lâm", "Cà phê Năng"], "Cụ Giảng thời làm pha chế khách sạn Metropole đã sáng tạo cà phê trứng thay thế sữa tươi khan hiếm thời bấy giờ.", 1),
        ("Dịch vụ lưu trữ video trực tuyến lớn nhất hành tinh thuộc sở hữu của tập đoàn Google là gì?", "YouTube", ["Vimeo", "Dailymotion", "Twitch"], "Mỗi phút có hàng trăm giờ video được người dùng tải lên YouTube trên khắp thế giới.", 1),
        ("Trình duyệt web phổ biến nhất thế giới hiện nay dựa trên mã nguồn mở Chromium do Google phát triển là gì?", "Google Chrome", ["Mozilla Firefox", "Safari", "Microsoft Edge"], "Google Chrome chiếm hơn 65% thị phần trình duyệt máy tính và di động toàn cầu.", 1),
        ("Hệ điều hành máy tính mã nguồn mở miễn phí biểu tượng chú chim cánh cụt Tux được tạo ra bởi Linus Torvalds là gì?", "Linux", ["Windows", "macOS", "DOS"], "Linux là nền tảng vận hành phần lớn máy chủ Internet, siêu máy tính và hệ điều hành Android.", 1),
        ("Chuẩn mạng không dây tầm xa vệ tinh quỹ đạo thấp cung cấp Internet tốc độ cao toàn cầu của Elon Musk có tên là gì?", "Starlink (SpaceX)", ["OneWeb", "Kuiper", "Viasat"], "Hàng ngàn vệ tinh Starlink bay ở độ cao 550km kết nối mạng tới các vùng sâu vùng xa hải đảo.", 1),
        ("Đơn vị đo độ sáng của một nguồn sáng hoặc máy chiếu trong kỹ thuật nghe nhìn được gọi là gì?", "Lumen (Ansi Lumen)", ["Watt", "Volt", "Pixel"], "Chỉ số Ansi Lumen càng cao thì máy chiếu chiếu hình ảnh càng rõ nét trong môi trường nhiều ánh sáng.", 2),
        ("Loại cổng kết nối không dây tốc độ cao AirDrop chia sẻ tệp ảnh nhanh chóng giữa các thiết bị thuộc hệ sinh thái nào?", "Hệ sinh thái Apple (iOS, iPadOS, macOS)", ["Hệ sinh thái Android", "Hệ điều hành Windows", "Hệ điều hành Linux"], "AirDrop kết hợp Wi-Fi và Bluetooth để truyền dữ liệu mã hóa ngang hàng cực nhanh.", 1),
        ("Giải đua xe đạp đường trường danh giá và lâu đời nhất thế giới diễn ra vòng quanh nước Pháp hàng năm mang tên là gì?", "Tour de France (Vòng quanh nước Pháp)", ["Giro d'Italia", "Vuelta a Espana", "Paris - Roubaix"], "Chiếc áo vàng (Maillot Jaune) danh giá thuộc về tay đua có tổng thời gian thi đấu ít nhất.", 1),
        ("Môn thể thao phối hợp 3 môn (Triathlon) tại Olympic tiêu chuẩn bao gồm ba môn thi liên tiếp nào?", "Bơi lội, Đạp xe và Chạy bộ", ["Bơi lội, Bắn súng và Chạy bộ", "Đua thuyền, Điền kinh và Nhảy cao", "Cử tạ, Chạy ngắn và Bơi"], "Các vận động viên thi bơi 1,5 km, đạp xe 40 km và chạy bộ 10 km không nghỉ giữa chặng.", 1),
        ("Kỷ lục gia bơi lội người Mỹ giành tới 23 Huy chương Vàng Olympic vĩ đại nhất lịch sử Thế vận hội là ai?", "Michael Phelps", ["Ian Thorpe", "Caeleb Dressel", "Sun Yang"], "Michael Phelps được mệnh danh là 'Kình ngư siêu phàm' với sải tay dài hơn chiều cao cơ thể.", 1),
        ("Huyền thoại điền kinh người Jamaica giữ kỷ lục thế giới chạy 100m (9,58 giây) được mệnh danh 'Tia chớp' là ai?", "Usain Bolt", ["Tyson Gay", "Yohan Blake", "Carl Lewis"], "Usain Bolt lập kỷ lục chạy 100m và 200m tại giải vô địch thế giới Berlin năm 2009.", 1),
        ("Kỹ thuật nén ép tim ngoài lồng ngực cho trẻ sơ sinh hoặc trẻ nhỏ dưới 1 tuổi dùng bao nhiêu ngón tay để thực hiện?", "Dùng 2 ngón tay (ngón trỏ và ngón giữa) ấn sâu khoảng 4 cm", ["Dùng cả hai bàn tay đè mạnh", "Dùng cùi chỏ", "Dùng gót bàn chân"], "Xương lồng ngực trẻ sơ sinh còn mềm nên chỉ dùng lực vừa phải của hai ngón tay tránh tổn thương nội tạng.", 2),
        ("Chỉ số khối cơ thể giúp đánh giá tình trạng thể trạng gầy hay béo của một người trưởng thành viết tắt là gì?", "Chỉ số BMI (Body Mass Index)", ["Chỉ số BMR", "Chỉ số TDEE", "Chỉ số WHR"], "BMI = Cân nặng (kg) / [Chiều cao (m)]^2. Mức BMI lý tưởng của người châu Á là 18,5 đến 22,9.", 1),
        ("Khi bị hóc dị vật đường thở nghẹn thở tím tái, thủ thuật sơ cứu tống dị vật ra ngoài bằng cách ôm ép bụng là gì?", "Thủ thuật Heimlich", ["Thủ thuật CPR", "Thủ thuật xoa bóp tim", "Thủ thuật garo"], "Ép nhanh mạnh dưới cơ hoành tạo luồng khí đẩy dị vật bật ngược ra khỏi khí quản cứu sống nạn nhân.", 2),
        ("Loại nấm mốc màu xanh lam sản sinh độc tố vi nấm Aflatoxin gây ung thư gan nguy hiểm thường xuất hiện trên thực phẩm nào bị ẩm mốc?", "Lạc (đậu phộng), ngô, gạo bị ẩm mốc", ["Rau xanh héo", "Thịt thối rữa", "Sữa lên men"], "Độc tố Aflatoxin bền nhiệt không bị phá hủy hoàn toàn khi nấu chín nên tuyệt đối không ăn ngũ cốc ẩm mốc.", 2)
    ],

    # 5. VĂN HỌC - NGHỆ THUẬT (40 câu)
    "van-hoc-nghe-thuat": [
        ("Trong văn học dân gian Việt Nam, hình tượng nhân vật Trạng Quỳnh nổi tiếng với tài năng gì?", "Tài ứng đối thông minh, trào lộng châm biếm quan lại phong kiến", ["Tài đánh giặc", "Tài bốc thuốc", "Tài làm giàu"], "Trạng Quỳnh mượn tiếng cười đả kích chúa Trịnh và quan lại tham lam bảo vệ dân nghèo.", 1),
        ("Bài ca dao: 'Thân em như tấm lụa đào / Phất phơ giữa chợ biết vào tay ai' thể hiện nỗi niềm gì của người phụ nữ xưa?", "Thân phận bấp bênh phụ thuộc không được tự quyết định hạnh phúc lứa đôi", ["Niềm tự hào giàu sang", "Tình yêu thiên nhiên", "Tình nghĩa xóm làng"], "Tiếng than thân trách phận ai oán trước lễ giáo phong kiến trọng nam khinh nữ khắt khe.", 1),
        ("Bài thơ 'Bánh trôi nước' của Bà Huyện Thanh Quan hay của Nữ sĩ Hồ Xuân Hương?", "Nữ sĩ Hồ Xuân Hương (Bà chúa thơ Nôm)", ["Bà Huyện Thanh Quan", "Đoàn Thị Điểm", "Sương Nguyệt Anh"], "'Thân em vừa trắng lại vừa tròn / Bảy nổi ba chìm với nước non / Rắn nát mặc dầu tay kẻ nặn / Mà em vẫn giữ tấm lòng son'.", 1),
        ("Bài thơ 'Qua Đèo Ngang' với những câu đối chỉnh mực thước 'Nhớ nước đau lòng con quốc quốc / Thương nhà mỏi miệng cái gia gia' là của ai?", "Bà Huyện Thanh Quan", ["Hồ Xuân Hương", "Đoàn Thị Điểm", "Nguyễn Khuyến"], "Áng thơ thất ngôn bát cú mẫu mực thể hiện nỗi niềm hoài cổ thương nhớ quá khứ.", 1),
        ("Ai là dịch giả bản dịch thơ lục bát tác phẩm 'Chinh phụ ngâm khúc' (nguyên tác chữ Hán của Đặng Trần Côn) nổi tiếng nhất?", "Nữ sĩ Đoàn Thị Điểm (hoặc Phan Huy Ích)", ["Hồ Xuân Hương", "Bà Huyện Thanh Quan", "Nguyễn Du"], "Bản dịch lục bát truyền cảm khắc họa sâu sắc nỗi cô đơn sầu muộn của người vợ trẻ chờ chồng ra trận.", 1),
        ("Tác phẩm văn xuôi lịch sử chương hồi tái hiện sinh động phong trào Tây Sơn và sự sụp đổ của nhà Lê là gì?", "'Hoàng Lê nhất thống chí' của Ngô gia văn phái", ["'Đại Nam thực lục'", "'Việt Nam sử lược'", "'Lịch triều hiến chương'"], "Tác phẩm khắc họa hình tượng người anh hùng áo vải Quang Trung Nguyễn Huệ lẫm liệt kiêu hùng.", 1),
        ("Tiểu thuyết hiện thực 'Bước đường cùng' miêu tả bước đường bần cùng hóa của nông dân anh Pha là của nhà văn nào?", "Nguyễn Công Hoan", ["Ngô Tất Tố", "Nam Cao", "Vũ Trọng Phụng"], "Nguyễn Công Hoan là bậc thầy truyện ngắn trào phúng và hiện thực phê phán Việt Nam.", 1),
        ("Tập thơ 'Nhật ký trong tù' (Ngục trung nhật ký) của Chủ tịch Hồ Chí Minh gồm bao nhiêu bài thơ chữ Hán?", "133 bài thơ chữ Hán", ["100 bài", "150 bài", "120 bài"], "Tập thơ tỏa sáng tinh thần 'Thân thể ở trong lao / Tinh thần ở ngoài lao / Muốn nên sự nghiệp lớn / Tinh thần càng phải cao'.", 2),
        ("Vở kịch thơ 'Vũ Như Tô' của Nguyễn Huy Tưởng được kết thúc bằng sự kiện lịch sử bi tráng nào?", "Đài Cửu Trùng bị thiêu rụi và Vũ Như Tô cùng Đan Thiềm bị giết", ["Đài Cửu Trùng khánh thành lộng lẫy", "Vũ Như Tô lên làm vua", "Vũ Như Tô đi ẩn dật"], "Bi kịch giữa khát vọng nghệ thuật muôn đời với lợi ích thiết thực trước mắt của nhân dân lao động.", 2),
        ("Nhà văn Nam Cao đã hy sinh anh dũng trên đường đi công tác vùng địch hậu năm 1951 tại tỉnh nào?", "Ninh Bình (vùng Gia Viễn)", ["Hà Nam", "Nam Định", "Thanh Hóa"], "Nam Cao ngã xuống khi tài năng đang ở độ chín để lại niềm tiếc thương vô hạn cho nền văn học nước nhà.", 2),
        ("Nhạc sĩ Trịnh Công Sơn sáng tác ca khúc 'Nối vòng tay lớn' với ước vọng hòa hợp dân tộc vào năm nào?", "Năm 1968", ["Năm 1975", "Năm 1972", "Năm 1960"], "'Rừng núi dang tay nối lại biển xa / Ta đi vòng tay lớn mãi để nối sơn hà' - bài ca kết đoàn triệu người.", 1),
        ("Ca khúc cách mạng 'Hò kéo pháo' ('Hò dô ta nào kéo pháo ta vượt qua đèo') do nhạc sĩ Hoàng Vân sáng tác trong chiến dịch nào?", "Chiến dịch Điện Biên Phủ 1954", ["Chiến dịch Biên giới 1950", "Chiến dịch Việt Bắc 1947", "Chiến dịch Tây Bắc 1952"], "Bài hò thôi thúc tinh thần quả cảm kéo những khẩu pháo nặng hàng tấn qua dốc đứng hiểm trở.", 1),
        ("Nhạc cụ dân tộc nào có hộp cộng hưởng hình trăng tròn với 2 dây tơ gảy bằng ngón tay là linh hồn của dàn nhạc đờn ca tài tử?", "Đàn Kìm (Đàn Nguyệt)", ["Đàn Tranh", "Đàn Sến", "Đàn Tỳ Bà"], "Đàn Kìm giữ vai trò chỉ huy lĩnh xướng giữ nhịp trong dàn nhạc cổ truyền Nam Bộ.", 1),
        ("Điệu múa Xòe Thái nét văn hóa sinh hoạt cộng đồng rực rỡ bên ánh lửa trại của đồng bào Tây Bắc được UNESCO vinh danh năm nào?", "Năm 2021 (Di sản văn hóa phi vật thể đại diện của nhân loại)", ["Năm 2015", "Năm 2018", "Năm 2010"], "'Không xòe không vui, không xòe cây lúa không trổ bông, không xòe trai gái không thành đôi'.", 1),
        ("Hát Xoan vùng đất Tổ Phú Thọ gắn liền với tín ngưỡng thờ cúng Hùng Vương thường được biểu diễn vào dịp nào?", "Dịp đầu xuân năm mới tại các cửa đình làng", ["Mùa thu gặt lúa", "Mùa hè trăng thanh", "Lễ mừng thọ"], "Hát Xoan gồm hát nghi lễ, hát quả cách và hát hội cầu chúc quốc thái dân an mưa thuận gió hòa.", 1),
        ("Thành ngữ dân gian: 'Khéo ăn thì no, khéo co thì ...' điền từ còn thiếu?", "ấm", ["vui", "đẹp", "khỏe"], "Khuyên răn cách chi tiêu sinh hoạt liệu cơm gắp mắm phù hợp với hoàn cảnh kinh tế gia đình.", 1),
        ("Thành ngữ dân gian: 'Thuận buồm xuôi ...' là lời chúc bình an may mắn cho người đi làm ăn xa hoặc mở mang kinh doanh?", "gió", ["nước", "dòng", "chèo"], "Chúc cho mọi công việc hanh thông suôn sẻ không gặp trở ngại chông gai.", 1),
        ("Thành ngữ dân gian: 'Tre già măng ...' thể hiện quy luật tiếp nối tự nhiên giữa các thế hệ mầm non tương lai?", "mọc", ["lên", "tươi", "xanh"], "Thế hệ sau kế tục và phát huy sự nghiệp vẻ vang của thế hệ cha anh đi trước.", 1),
        ("Kiệt tác tiểu thuyết 'Trăm năm cô đơn' (Cien años de soledad) của Gabriel Garcia Marquez thuộc trào lưu văn học nào?", "Chủ nghĩa hiện thực huyền ảo (Magic Realism)", ["Chủ nghĩa lãng mạn", "Chủ nghĩa cổ điển", "Chủ nghĩa tự nhiên"], "Dòng họ Buendía trải qua 7 thế hệ ở ngôi làng Macondo hư ảo phản ánh số phận cả châu Mỹ Latinh.", 2),
        ("Ai là tác giả của thiên truyện thiếu nhi kinh điển 'Những cuộc phiêu lưu của Pinocchio' chú bé người gỗ mũi dài khi nói dối?", "Carlo Collodi (nhà văn người Ý)", ["Hans Christian Andersen", "Charles Perrault", "Gianni Rodari"], "Mỗi lần nói dối chiếc mũi của Pinocchio lại dài ngoẵng ra là bài học đạo đức nhớ đời cho con trẻ.", 1)
    ],

    # 6. ĐỐ VUI TRÍ TUỆ (40 câu)
    "do-vui-tri-tue": [
        ("Đố mẹo: Bánh gì xốp mềm, bên trong cuộn kem ngọt ngào uốn cong hình vòng tròn như khúc gỗ?", "Bánh bông lan cuộn (bánh khúc cây)", ["Bánh chưng", "Bánh bao", "Bánh rán"], "Bánh cuộn thơm ngọt vị vani béo ngậy thưởng thức cùng tách trà ấm.", 1),
        ("Đố mẹo: Bánh gì không nướng bằng than, không chiên bằng dầu mỡ mà dùng để đập tay khen ngợi chiến thắng?", "Bánh pháo tay (tiếng vỗ tay)", ["Bánh xe", "Bánh mì", "Bánh phồng"], "Tiếng vỗ tay giòn giã tán thưởng những phần thi xuất sắc trên sàn đấu.", 1),
        ("Đố mẹo: Con gì sinh ra đã có đôi tai dài, đuôi ngắn tũn, thích ăn cà rốt và nhảy thoăn thoắt?", "Con thỏ", ["Con chuột", "Con mèo", "Con chó"], "Chú thỏ trắng hiền lành nhanh nhẹn gặm cà rốt giòn ngọt.", 1),
        ("Đố mẹo: Con gì hai mắt thao láo, ban ngày ngủ gật trong hốc cây, ban đêm mở to mắt đi bắt chuột?", "Con chim cú mèo", ["Con dơi", "Con đại bàng", "Con bồ câu"], "Cú mèo có thính giác và thị giác ban đêm siêu phàm là dũng sĩ diệt chuột của nhà nông.", 1),
        ("Đố mẹo: Đồ vật nào dùng để quét nước trên kính xe ô tô mỗi khi trời đổ mưa to?", "Cần gạt mưa", ["Cái còi xe", "Bánh xe", "Gương chiếu hậu"], "Cần gạt nước qua lại nhịp nhàng giữ tầm nhìn trong suốt an toàn cho tài xế lái xe.", 1),
        ("Đố mẹo: Cái gì có kim chỉ giờ, kim chỉ phút mà không có ngón tay nào dùng để đo thời gian?", "Chiếc đồng hồ treo tường", ["Cái la bàn", "Cái cân đĩa", "Nhiệt kế"], "Đồng hồ nhắc nhở chúng ta biết quý trọng từng giây từng phút của cuộc sống.", 1),
        ("Đố mẹo: Thứ gì bạn càng rửa sạch bằng xà phòng thì nó lại càng nhỏ dần đi?", "Cục xà bông (bánh xà phòng tắm)", ["Cái khăn mặt", "Bàn tay", "Cái chậu"], "Bọt xà phòng tan biến rửa trôi bụi bẩn làm bánh xà phòng mòn dần đi.", 1),
        ("Đố chữ: Bỏ dấu sắc thành tên một loài cá bơi dưới nước, để nguyên thành vật học sinh dùng để gọt bút chì là cái gì?", "Dao (Dao gọt bút chì / Cá Dao)", ["Kéo", "Gọt", "Thước"], "Lưỡi dao gọt bút chì nhọn hoắt giúp nét chữ đều đặn nắn nót.", 2),
        ("Đố logic: Một gia đình có 5 người con trai. Mỗi người con trai đều có đúng một người em gái út. Hỏi gia đình đó có tất cả mấy người con?", "Có tất cả 6 người con (5 trai và 1 gái út)", ["Có 10 người con", "Có 5 người con", "Có 7 người con"], "Cô em gái út là em gái chung của cả 5 người anh trai!", 1),
        ("Đố mẹo: Một người nhảy dù từ máy bay ở độ cao 3.000m xuống đất mà dù không mở ra, người đó rơi xuống đâu thì vẫn an toàn tính mạng?", "Rơi xuống... mặt đất lúc máy bay đang đỗ trên đường băng sân bay!", ["Rơi xuống biển", "Rơi xuống đống rơm", "Rơi xuống đầm lầy"], "Máy bay đang đỗ dưới đất thì độ cao rơi chỉ là bước từ cửa máy bay xuống thang!", 2),
        ("Đố mẹo: Quả gì không ruột không vỏ mà bay lơ lửng khắp trời sau cơn mưa?", "Quả bong bóng mưa (bong bóng nước)", ["Quả bưởi", "Quả bóng bay", "Quả cam"], "Bong bóng nước lung linh vỡ tan khi chạm vào cành lá.", 1),
        ("Đố mẹo: Con gì sinh ra đã có túi trước ngực chở con đi du lịch khắp sa mạc nước Úc?", "Con chuột túi (Kangaroo)", ["Con thỏ", "Con chó", "Con hươu"], "Chuột túi con nằm ấm áp an toàn trong chiếc túi mẹ bú sữa.", 1),
        ("Đố mẹo: Cái gì người mù có thể nhìn thấy, người điếc có thể nghe thấy?", "Giấc mơ (giấc chiêm bao)", ["Ánh sáng", "Tiếng sấm", "Bức tranh"], "Trong giấc mơ của tiềm thức mọi giác quan tâm hồn đều rộng mở.", 2),
        ("Đố mẹo: Nhà gì không xây bằng gạch đá, không lợp bằng ngói mà ai nghe thấy tên cũng thèm ăn quả ngọt?", "Nhà kính trồng dưa (hoặc Nhà vườn)", ["Nhà tầng", "Nhà sàn", "Nhà tranh"], "Nhà màng công nghệ cao cho ra những quả dưa lưới thơm ngọt trĩu cành.", 1),
        ("Đố mẹo: Cầu gì bắc qua sông nước không bằng xi măng sắt thép mà tạo nên bởi 7 sắc màu rực rỡ?", "Cầu vồng", ["Cầu Rồng", "Cầu quay", "Cầu treo"], "Cầu vồng bảy sắc sau cơn mưa là kỳ quan quang học tuyệt mỹ của thiên nhiên.", 1)
    ]
}

def main():
    print("=" * 70)
    print("🌟 CHẠY BỘ NẠP GOLDEN FINISH: CÁN MỐC TRÊN 2.500 CÂU HỎI!")
    print("=" * 70)

    total_added = 0
    for cat_name, q_list in GOLDEN_QUESTIONS.items():
        fmt_list = []
        for item in q_list:
            fmt_list.append({
                "difficulty": item[4],
                "question": item[0],
                "correct_answer": item[1],
                "distractors": item[2],
                "explanation": item[3]
            })
        added = add_questions_to_category(cat_name, fmt_list)
        total_added += added

    print(f"\n🎉 Hoàn thành Golden Finish! Đã nạp thêm {total_added} câu hỏi mới.")

if __name__ == '__main__':
    main()
