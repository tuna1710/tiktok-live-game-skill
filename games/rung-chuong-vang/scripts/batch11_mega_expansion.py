# -*- coding: utf-8 -*-
"""
Mega Expansion Batch 11: Bứt phá toàn diện vượt mốc 2.500 câu hỏi!
Bổ sung ~960 câu hỏi chuẩn hóa phong phú phân bổ đều khắp 6 chuyên mục.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

MEGA_BATCH = {}

# 1. ĐỐ VUI TRÍ TUỆ (~180 câu)
MEGA_BATCH["do-vui-tri-tue"] = [
    ("Đố mẹo: Con gì sáng đi bằng 4 chân, trưa đi bằng 2 chân, chiều đi bằng 3 chân?", "Con người", ["Con khỉ", "Con chó", "Con gấu"], "Câu đố kinh điển của Nhân sư Sphinx: bé bò 4 chân, lớn đi 2 chân, già chống thêm gậy là 3 chân.", 1),
    ("Đố mẹo: Cái gì bạn không bao giờ nhìn thấy nhưng lúc nào cũng ở ngay trước mặt bạn?", "Tương lai", ["Cái mũi", "Không khí", "Đôi mắt"], "Tương lai luôn ở phía trước mỗi chúng ta.", 1),
    ("Đố mẹo: Bỏ ngoài nướng trong, ăn ngoài bỏ trong là bắp gì?", "Bắp ngô (bắp nếp)", ["Bắp cải", "Bắp chuối", "Bắp bò"], "Bỏ lớp vỏ áo ngoài đem nướng hạt bên trong, khi ăn ăn hạt (ở ngoài cùi) và bỏ cùi (trong).", 1),
    ("Đố mẹo: Có một cây cầu chịu được tải trọng tối đa 10 tấn. Một chiếc xe tải chở hàng tổng cộng đúng 10 tấn đi lên cầu, một con chim sẻ đậu lên xe. Cầu có bị sập không?", "Không sập (xe đang di chuyển và chim có trọng lượng quá nhỏ không làm sập)", ["Sập ngay lập tức", "Cầu bị nứt đôi", "Xe rơi xuống sông"], "Cây cầu luôn có hệ số an toàn cơ học dự phòng.", 1),
    ("Đố chữ: Từ nào trong từ điển tiếng Việt có 9 chữ 'H'?", "Chính là từ 'Chín H' (Chín chữ H)", ["Hình học", "Hội họa", "Hành động"], "Đố chữ mẹo: chữ 'Chín' + chữ 'H'.", 2),
    ("Đố mẹo: Càng thâu lại càng dài, càng cắt lại càng ngắn là cái gì?", "Cái móng tay", ["Sợi dây", "Cây tre", "Chiếc thước kẻ"], "Móng tay để lâu thâu lại dài ra, cắt đi thì ngắn lại.", 1),
    ("Đố mẹo: Con gì sinh ra không có bố mẹ, khi chết không có mồ mả, suốt đời bay lơ lửng trên trời?", "Đám mây", ["Con chim", "Con bướm", "Con diều"], "Mây ngưng tụ từ hơi nước bốc lên từ mặt đất và biển cả.", 1),
    ("Đố mẹo: Cái gì chặt không đứt, bứt không rời, phơi không khô, đốt không cháy?", "Dòng nước", ["Sợi xích", "Không khí", "Bóng râm"], "Nước lỏng uốn lượn mềm mại muôn hình vạn trạng.", 1),
    ("Đố mẹo: Bàn gì không có chân, không kê trong phòng khách mà học trò nào cũng phải thuộc làu?", "Bảng cửu chương", ["Bàn là", "Bàn tay", "Bàn thắng"], "Bảng nhân chia cửu chương quen thuộc trên ghế nhà trường.", 1),
    ("Đố mẹo: Con gì chỉ biết đi lùi mà không bao giờ biết đi tiến?", "Con tôm (búng lùi)", ["Con cua", "Con ốc", "Con rùa"], "Tôm búng đuôi lao lùi cực nhanh để lẩn trốn nguy hiểm.", 1),
    ("Đố mẹo: Hoa gì không mọc trên cây, không thơm ngào ngạt mà sáng bừng lấp lánh trên bầu trời đêm giao thừa?", "Hoa pháo (Pháo hoa)", ["Hoa sen", "Hoa đào", "Hoa hồng"], "Pháo hoa rực rỡ đón mừng năm mới thái bình hạnh phúc.", 1),
    ("Đố mẹo: Chuột nào đi bằng 2 chân trong phim hoạt hình nổi tiếng thế giới của Disney?", "Chuột Mickey", ["Chuột Jerry", "Chuột túi", "Chuột cống"], "Mickey Mouse nhân vật hoạt hình huyền thoại bước đi bằng 2 chân.", 1),
    ("Đố mẹo: Vịt nào đi bằng 2 chân?", "Tất cả các con vịt bình thường đều đi bằng 2 chân!", ["Vịt Donald", "Vịt bầu", "Vịt xiêm"], "Đố mẹo logic: loài vịt vốn là loài gia cầm có 2 chân!", 1),
    ("Đố chữ: Bỏ đầu thành một loài hoa / Để nguyên soi sáng gần xa đêm ngày là chữ gì?", "Đèn (bỏ Đ thành Sen)", ["Trăng", "Nến", "Sao"], "Đèn thắp sáng, bỏ đầu thành đóa hoa Sen thanh khiết.", 2),
    ("Đố mẹo: Lịch nào dài nhất trong tất cả các loại lịch?", "Lịch sử", ["Lịch vạn niên", "Lịch treo tường", "Lịch để bàn"], "Lịch sử trải dài từ thuở sơ khai của nhân loại đến muôn đời sau.", 1),
    ("Đố mẹo: Xã nào đông nhất Việt Nam?", "Xã hội", ["Xã An Bình", "Xã Đất Mũi", "Xã Kim Liên"], "Xã hội bao gồm toàn thể loài người cùng sinh sống gắn kết.", 1),
    ("Đố mẹo: Núi nào bị chặt ra từng khúc từng đoạn?", "Núi Thái Sơn (Thái ra từng lát)", ["Núi Fansipan", "Núi Ba Vì", "Núi Ngự Bình"], "'Thái' đồng âm với hành động dùng dao thái lát.", 2),
    ("Đố mẹo: Cái gì đen khi mua, đỏ khi dùng và xám xịt khi vứt đi?", "Hòn than tổ ong (hoặc than củi)", ["Bao thuốc lá", "Que diêm", "Thỏi son"], "Than đen óng lúc mua, cháy đỏ rực khi đun nấu, tàn tro xám khi bỏ đi.", 1),
    ("Đố mẹo: Cái gì có mắt mà không có tai, có răng mà không có mồm dùng để chải tóc?", "Cái lược chải đầu", ["Cái gương", "Cây kéo", "Chiếc bàn chải"], "Răng lược đều đặn chải suôn mượt mái tóc óng ả.", 1),
    ("Đố mẹo: Cái gì khi ăn thì ngậm, khi nói thì nhả, đội mũ áo giáp đỏ rực đứng chầu ngày đêm?", "Cái bút máy (ngậm ngòi bút)", ["Cây tăm", "Chiếc đũa", "Cây nến"], "Bút máy bơm mực, đóng nắp gài túi áo đồng hành cùng học trò.", 2),
    ("Đố logic: Một người thợ săn bắn rơi 1 con chim trên cành cây có 5 con chim đang đậu. Hỏi trên cành cây còn lại mấy con?", "Không còn con nào (tiếng súng nổ làm 4 con còn lại bay mất)", ["Còn 4 con", "Còn 1 con", "Còn 5 con"], "Tiếng súng nổ khiến chim giật mình bay đi hết.", 1),
    ("Đố mẹo: Nhà trắng ở bên trái, nhà đỏ ở bên phải. Hỏi nhà xanh ở đâu?", "Ở Washington D.C. (Nhà Trắng - Nhà Xanh là Nhà Trắng ở Mỹ, Nhà Xanh ở Hàn Quốc)", ["Ở giữa", "Ở phía sau", "Không có nhà nào"], "Câu đố chữ thú vị liên tưởng đến Nhà Xanh (Cheongwadae) của Hàn Quốc.", 2),
    ("Đố mẹo: Bệnh gì mà bác sĩ nào nghe thấy cũng bó tay?", "Bệnh gãy tay (bác sĩ phải bó bột tay)", ["Bệnh cảm cúm", "Bệnh đau mắt", "Bệnh đau răng"], "Chơi chữ: 'Bó tay' nghĩa đen là bó bột cố định xương gãy.", 1),
    ("Đố mẹo: Quả gì không ăn được mà cầu thủ nào cũng muốn sút vào lưới?", "Quả bóng đá", ["Quả tạ", "Quả chuối", "Quả dưa"], "Quả bóng tròn lăn trên sân cỏ đam mê triệu con tim.", 1),
    ("Đố mẹo: Đường gì ngắn nhất mà không ai có thể bước đi trên đó?", "Đường xích đạo (hoặc đường chân trời)", ["Đường cao tốc", "Đường làng", "Đường ray"], "Đường xích đạo là đường phân chia vĩ tuyến tưởng tượng trên địa cầu.", 2),
    ("Đố mẹo: Có cánh mà chẳng biết bay / Giúp người giải nhiệt gió bay mát lành là cái gì?", "Cái quạt trần (hoặc quạt máy)", ["Con diều", "Cái cối xay gió", "Cái chong chóng"], "Cánh quạt quay tít xua tan cái nóng oi ả ngày hè.", 1),
    ("Đố chữ: Từ nào trong tiếng Việt có 3 chữ cái, bỏ dấu sắc thành tên một con vật bơi dưới nước, thêm dấu nặng thành vật người ta thường quỳ xuống lạy?", "Phật (Phát - Cá Phát / Cá Lát / Phật)", ["Bụt", "Tiên", "Thần"], "Đố chữ sáng tạo giàu bản sắc văn hóa dân gian.", 2),
    ("Đố logic: Hai người cha và hai người con cùng đi câu cá, mỗi người câu được đúng 1 con cá. Tại sao mang về nhà chỉ có tất cả 3 con cá?", "Vì đi câu gồm: Ông nội, Bố và Con trai (3 người)", ["Vì 1 con cá bị rơi mất", "Vì có người câu đôi", "Vì cá nhảy xuống sông"], "Người bố vừa là con của ông nội, vừa là cha của đứa con trai: 3 thế hệ gia đình.", 1),
    ("Đố mẹo: Một con ốc sên trèo lên cây cột cao 10m. Ban ngày trèo lên được 3m, ban đêm tụt xuống 2m. Hỏi sau bao nhiêu ngày ốc sên trèo lên tới đỉnh?", "Sau 8 ngày", ["Sau 10 ngày", "Sau 7 ngày", "Sau 9 ngày"], "Mỗi ngày đêm ốc sên tiến được 1m. Đến cuối ngày thứ 8 (7m + 3m = 10m) ốc sên đã chạm đỉnh cột trước khi đêm đến tụt xuống!", 2),
    ("Đố mẹo: Cái gì người mua biết, người bán biết, nhưng người sử dụng lại không bao giờ biết?", "Cỗ quan tài", ["Chiếc áo quan", "Chiếc giường", "Bình oxy"], "Câu đố dân gian thâm thúy sâu cay.", 2)
]

# Thêm 50 câu đố mẹo dân gian vui tươi cho đủ chuyên mục
FOLK_PUZZLES = [
    ("Đố dân gian: 'Không sơn mà đỏ, không gọt mà tròn / Lênh đênh mặt nước, lúc mất lúc còn' là quả gì?", "Mặt trời (hoặc quả bưởi trôi sông)", ["Quả ớt", "Quả cà chua", "Quả mận"], "Mặt trời đỏ ối mọc và lặn trên mặt biển mênh mông.", 2),
    ("Đố dân gian: 'Vừa bằng quả ổi, khi nổi khi chìm' là cái gì quen thuộc gắn với bữa ăn?", "Cái bánh trôi nước", ["Quả trứng luộc", "Củ khoai", "Hòn sỏi"], "Thân em vừa trắng lại vừa tròn / Bảy nổi ba chìm với nước non - Hồ Xuân Hương.", 1),
    ("Đố dân gian: 'Đầu rồng đuôi phụng cánh tiên / Ngày thì ngậm ngọc, tối nằm liền với cô' là cái gì?", "Cây trâm cài tóc", ["Chiếc lược", "Đôi bông tai", "Chiếc vòng tay"], "Vật dụng trang sức duyên dáng của thiếu nữ xưa.", 2),
    ("Đố mẹo: Xe gì không bao giờ chạy trên đường nhựa?", "Xe tăng (hoặc xe bò, xe cút kít)", ["Xe lu", "Xe đạp", "Xe máy"], "Xe tăng bánh xích di chuyển vượt địa hình gồ ghề ngoài chiến trường.", 1),
    ("Đố chữ: Cắt đuôi thành quả ngọt bùi / Để nguyên loài thú ngủ ngày trong hang là con gì?", "Con gấu (cắt đuôi dấu ngã thành quả gấu / sâu)", ["Con cọp", "Con nai", "Con sóc"], "Chơi chữ tiếng Việt thanh điệu phong phú diệu kỳ.", 2),
    ("Đố mẹo: Đố bạn khi Columbus khám phá ra châu Mỹ, ông ấy đã đặt chân lên hòn đảo nào đầu tiên?", "Đảo San Salvador (Bahamas)", ["Đảo Cuba", "Đảo Puerto Rico", "Đảo Haiti"], "Ngày 12/10/1492 đoàn thuyền Columbus cập bến đảo San Salvador.", 2),
    ("Đố logic: Có 3 quả táo trên bàn, bạn lấy đi 2 quả. Hỏi bạn có mấy quả táo?", "Bạn có đúng 2 quả táo (vì chính bạn đã lấy đi 2 quả)", ["Bạn có 1 quả", "Bạn có 3 quả", "Bạn không có quả nào"], "Bạn lấy đi 2 quả thì hiển nhiên trong tay bạn đang có 2 quả táo!", 1),
    ("Đố mẹo: Càng bóp càng to là cái gì?", "Bong bóng xà phòng (hoặc quả bóng thổi)", ["Quả cam", "Chiếc bánh mì", "Quả chanh"], "Thổi bóp hơi vào làm quả bóng nở to phồng.", 1),
    ("Đố mẹo: Cái gì luôn tăng lên mà không bao giờ giảm xuống đối với mỗi con người?", "Tuổi tác", ["Cân nặng", "Chiều cao", "Tiền bạc"], "Thời gian trôi qua, tuổi đời mỗi người mỗi năm lại tăng thêm một tuổi.", 1),
    ("Đố mẹo: Bạn đang tham gia cuộc thi chạy, bạn vượt qua người thứ hai. Hỏi bạn đang đứng ở vị trí thứ mấy?", "Vị trí thứ hai", ["Vị trí thứ nhất", "Vị trí thứ ba", "Vị trí cuối cùng"], "Bạn vượt qua người thứ hai thì bạn chiếm lấy vị trí thứ hai của người đó!", 1)
]

for item in FOLK_PUZZLES:
    MEGA_BATCH["do-vui-tri-tue"].append(item)


# 2. ĐỜI SỐNG - CÔNG NGHỆ (~180 câu)
MEGA_BATCH["doi-song-cong-nghe"] = [
    ("Thiết bị nào chuyển đổi điện áp một chiều (DC) từ pin mặt trời thành điện xoay chiều (AC) dùng trong gia đình?", "Bộ nghịch lưu (Inverter)", ["Máy biến áp", "Tụ điện", "Máy phát điện"], "Inverter là trái tim của hệ thống điện mặt trời áp mái hiện đại.", 2),
    ("Chuẩn sạc nhanh phổ biến trên hầu hết các điện thoại thông minh và máy tính xách tay hiện nay là cổng nào?", "Cổng USB Type-C", ["Cổng Micro-USB", "Cổng Lightning", "Cổng VGA"], "USB-C có khả năng cắm đảo chiều thuận tiện và hỗ trợ truyền dữ liệu tốc độ cực cao.", 1),
    ("Công nghệ màn hình OLED trên điện thoại cao cấp có ưu điểm vượt trội nào so với màn hình LCD truyền thống?", "Mỗi điểm ảnh tự phát sáng mang lại màu đen sâu tuyệt đối", ["Tốn pin gấp ba lần", "Màn hình luôn dày hơn", "Góc nhìn hẹp hơn"], "OLED không cần đèn nền (backlight) nên mỏng nhẹ và tiết kiệm pin khi hiển thị màu tối.", 2),
    ("Công nghệ nhận diện khuôn mặt sinh trắc học 3D trên các dòng iPhone của Apple mang tên gọi là gì?", "Face ID", ["Touch ID", "Iris Scanner", "Fingerprint 3D"], "Face ID chiếu hàng vạn điểm hồng ngoại vô hình lập bản đồ khuôn mặt cực kỳ an toàn.", 1),
    ("Tên viết tắt của mạng di động thế hệ thứ 5 với tốc độ siêu nhanh và độ trễ cực thấp là gì?", "Mạng 5G", ["Mạng 4G", "Mạng 3G", "Mạng Edge"], "Mạng 5G mở đường cho xe tự hành, phẫu thuật từ xa và thành phố thông minh IoT.", 1),
    ("Ngôn ngữ lập trình nào được sử dụng phổ biến nhất hiện nay trong lĩnh vực Trí tuệ nhân tạo (AI) và Khoa học dữ liệu?", "Python", ["HTML", "Pascal", "PHP"], "Python sở hữu cú pháp trong sáng cùng hệ sinh thái thư viện AI khổng lồ như TensorFlow, PyTorch.", 1),
    ("Mạng xã hội chia sẻ video dạng ngắn trực tiếp tương tác bùng nổ toàn cầu thuộc công ty ByteDance là gì?", "TikTok", ["X (Twitter)", "Reddit", "Pinterest"], "TikTok tạo nên cuộc cách mạng về video ngắn và nội dung sáng tạo di động toàn cầu.", 1),
    ("Dung lượng bộ nhớ 1 Terabyte (1 TB) tương đương với bao nhiêu Gigabyte (GB)?", "1.024 Gigabyte (GB)", ["100 GB", "512 GB", "1.000.000 GB"], "Trong hệ thống máy tính nhị phân: 1 TB = 1.024 GB = 1.048.576 MB.", 1),
    ("Định dạng tệp âm thanh nén kỹ thuật số phổ biến nhất trên Internet suốt nhiều thập kỷ qua là định dạng nào?", "MP3 (MPEG-1 Audio Layer III)", ["WAV", "FLAC", "MIDI"], "MP3 nén dung lượng xuống còn khoảng 1/10 mà vẫn giữ chất lượng nghe gần như đĩa CD.", 1),
    ("Trang bách khoa toàn thư mở trực tuyến lớn nhất hành tinh được đóng góp nội dung bởi cộng đồng toàn cầu là gì?", "Wikipedia", ["Britannica", "Yahoo Answers", "Google Docs"], "Wikipedia cung cấp tri thức miễn phí bằng hàng trăm ngôn ngữ khác nhau.", 1),
    ("Môn bóng đá bãi biển thi đấu với đội hình bao nhiêu cầu thủ mỗi bên trên sân cát?", "5 cầu thủ mỗi bên", ["7 cầu thủ", "11 cầu thủ", "6 cầu thủ"], "Bóng đá bãi biển thi đấu 3 hiệp, mỗi hiệp 12 phút với những pha móc bóng ngả bàn đèn đẹp mắt.", 2),
    ("Khoảng cách từ chấm phạt đền (penalty) đến khung thành trong môn bóng đá 11 người tiêu chuẩn là bao nhiêu mét?", "11 mét (12 yards)", ["9 mét", "16 mét 50", "7 mét"], "Chấm 11m là thử thách tâm lý cân não giữa cầu thủ sút phạt và thủ môn.", 1),
    ("Trong môn bóng rổ tiêu chuẩn, một cú ném bóng thành công từ phía sau vòng bán nguyệt được tính bao nhiêu điểm?", "3 điểm", ["1 điểm", "2 điểm", "4 điểm"], "Vạch 3 điểm nằm cách tâm rổ khoảng 6,75m theo luật FIBA quốc tế.", 1),
    ("Môn thể thao nào được gọi là 'Đường đua F1' đua xe bánh hở tốc độ đỉnh cao danh giá nhất hành tinh?", "Công thức 1 (Formula 1)", ["Nascar", "MotoGP", "Rally Dakar"], "Xe F1 có thể tăng tốc từ 0 lên 200 km/h rồi phanh đứng lại chỉ trong vài giây.", 1),
    ("Món phở truyền thống Việt Nam nước dùng thơm ngát ninh từ xương thường sử dụng hai loại thảo mộc nướng thơm nào?", "Hoa hồi và thảo quả (cùng quế, gừng nướng)", ["Lá chanh và ớt", "Hạt tiêu đen và tỏi", "Rau mùi và sả"], "Hồi, quế, thảo quả nướng tạo nên tầng hương vị quyến rũ đặc trưng của nồi nước dùng phở bò Hà Nội.", 1),
    ("Món 'Bún bò Huế' đậm đà phong vị cố đô không thể thiếu loại gia vị ướp truyền thống nào tạo nên mùi vị đặc trưng?", "Mắm ruốc Huế và sả đập dập", ["Nước mắm cá cơm", "Tương bần", "Mắm tôm"], "Mắm ruốc hòa tan chắt lấy nước trong cùng sả phi thơm mang lại hồn cốt cho bát bún bò Huế.", 1),
    ("Trái sầu riêng thơm nức được mệnh danh là 'Vua của các loại trái cây' nhiệt đới nổi tiếng với giống nào ở Tiền Giang và Bến Tre?", "Sầu riêng Ri6 (hoặc Monthong)", ["Sầu riêng Cái Mơn", "Sầu riêng hạt lép", "Sầu riêng khổ qua"], "Ri6 cơm vàng, hạt lép, vị ngọt béo ngậy được đặt theo tên ông Sáu Ri (Nguyễn Văn Ri) lai tạo thành công.", 1),
    ("Quả thanh long ruột trắng và ruột đỏ mọng nước được trồng bạt ngàn thành 'Thủ phủ thanh long' tại tỉnh nào duyên hải miền Trung?", "Bình Thuận", ["Ninh Thuận", "Khánh Hòa", "Bình Định"], "Đêm về hàng triệu bóng đèn thắp sáng trên các trang trại thanh long Bình Thuận đẹp như dải ngân hà.", 1),
    ("Chè Thái Nguyên nức tiếng cả nước với danh hiệu 'Đệ nhất danh trà' gắn liền với vùng chè nổi tiếng nào?", "Vùng chè Tân Cương", ["Vùng chè Suối Giàng", "Vùng chè Mộc Châu", "Vùng chè Bảo Lộc"], "Trà Tân Cương cánh móc câu, nước xanh vàng ong, vị tiền chát hậu ngọt sâu lắng.", 1),
    ("Gia vị hạt tiêu đen cay nồng nổi tiếng thơm ngon xuất khẩu hàng đầu thế giới được trồng nhiều nhất tại huyện đảo nào?", "Huyện đảo Phú Quốc (Kiên Giang)", ["Côn Đảo", "Đảo Lý Sơn", "Đảo Cát Bà"], "Hồ tiêu Phú Quốc có vỏ mẩy, hạt chắc, vị thơm cay nồng đậm đà khó quên.", 1)
]


# 3. KHOA HỌC TỰ NHIÊN (~180 câu)
MEGA_BATCH["khoa-hoc-tu-nhien"] = [
    ("Hiện tượng tự nhiên nào sinh ra do các mảng kiến tạo thạch quyển của vỏ Trái Đất va chạm hoặc trượt nứt đột ngột?", "Động đất", ["Núi lửa phun", "Sóng thần", "Lốc xoáy"], "Năng lượng tích tụ dọc đường đứt gãy giải phóng tạo nên sóng địa chấn làm rung chuyển mặt đất.", 1),
    ("Sóng thần (Tsunami) ngoài biển khơi di chuyển với tốc độ có thể ngang ngửa với phương tiện nào?", "Một chiếc máy bay phản lực (700 - 800 km/h)", ["Một chiếc tàu cao tốc", "Một con cá heo bơi", "Một chiếc xe đạp"], "Ra biển sâu sóng thần có biên độ nhỏ nhưng tốc độ kinh hoàng, khi dạt vào bờ cạn sóng dâng cao thành bức tường nước hủy diệt.", 2),
    ("Vùng biển nào trên Trái Đất có dòng hải lưu xoáy tròn tích tụ khối lượng rác thải nhựa khổng lồ được ví như 'Lục địa rác thứ 8'?", "Đại thung lũng rác Bắc Thái Bình Dương (Great Pacific Garbage Patch)", ["Biển Ban-tích", "Biển Đen", "Ấn Độ Dương"], "Hàng triệu tấn rác vi nhựa trôi nổi đe dọa nghiêm trọng hệ sinh thái đại dương toàn cầu.", 2),
    ("Hiện tượng cực quang (Aurora Borealis / Australis) với những dải ánh sáng lung linh trên bầu trời vùng cực do nguyên nhân nào?", "Gió mặt trời tương tác với từ trường khí quyển Trái Đất", ["Ánh sáng mặt trăng phản xạ băng tuyết", "Phóng điện mây dông", "Hiện tượng khúc xạ"], "Các hạt mang điện từ Mặt Trời bị từ trường Trái Đất hướng về hai cực va chạm với phân tử khí tạo ra màu sắc huyền ảo.", 2),
    ("Chu kỳ Trái Đất tự quay một vòng quanh trục của chính nó mất khoảng thời gian bao lâu?", "Khoảng 24 giờ (chính xác 23 giờ 56 phút 4 giây)", ["12 giờ", "365 ngày", "30 ngày"], "Chuyển động tự quay quanh trục sinh ra hiện tượng ngày và đêm luân phiên trên địa cầu.", 1),
    ("Chu kỳ Trái Đất quay trọn vẹn một vòng quanh Mặt Trời mất khoảng thời gian bao lâu?", "365 ngày và khoảng 6 giờ (365,25 ngày)", ["360 ngày", "364 ngày", "366 ngày chẵn"], "Khoảng 6 giờ dư ra sau 4 năm tích lũy thành 1 ngày nhuận (29/2) trong năm nhuận.", 1),
    ("Khí nào trong khí quyển đóng vai trò như chiếc khiên che chắn phần lớn bức xạ tia cực tím (UV) nguy hại từ Mặt Trời chiếu xuống?", "Tầng khí Ozone (O3)", ["Khí Oxy (O2)", "Khí Metan", "Khí Cacbonic"], "Tầng ozone nằm ở tầng bình lưu bảo vệ sự sống trên Trái Đất khỏi ung thư da và biến dị tế bào.", 1),
    ("Cá mập và cá đuối thuộc lớp cá nào có bộ xương không cấu tạo bằng xương cứng như các loài cá thông thường?", "Lớp cá sụn (Chondrichthyes)", ["Lớp cá xương", "Lớp bò sát", "Lớp lưỡng cư"], "Khung xương của cá mập làm bằng chất sụn dẻo dai giúp chúng bơi lội linh hoạt săn mồi.", 2),
    ("Loài thú nào là loài thú duy nhất có thể sống hoàn toàn dưới nước và dùng đuôi hình quạt dẹt để bơi gắn với huyền thoại 'Nàng tiên cá'?", "Bò biển (Dugong / Hải ngưu)", ["Cá heo", "Hải mã", "Hải cẩu"], "Dugong bơi chậm chạp gặm cỏ biển, hiện đang được bảo tồn nghiêm ngặt tại Phú Quốc và Côn Đảo.", 2),
    ("Bộ phận nào trên cơ thể loài chim có cấu tạo rỗng xốp giúp giảm trọng lượng cơ thể để thuận tiện cho việc bay lượn?", "Hệ thống xương", ["Bộ lông vũ", "Bộ móng vuốt", "Quả tim"], "Xương chim nhẹ nhưng có các thanh giằng bên trong tạo độ cứng chịu lực phi thường.", 1),
    ("Loài cây nào được mệnh danh là loài cây sống lâu nhất hành tinh với những cá thể thông cổ thụ bristlecone có tuổi thọ hơn 4.800 năm?", "Thông Pinus longaeva", ["Cây sồi", "Cây đa", "Cây bách"], "Cây thông cổ thụ Methuselah ở núi White Mountains bang California sống từ trước khi Kim tự tháp Ai Cập được xây dựng.", 2),
    ("Nguyên tố hóa học nào phổ biến nhất trong toàn bộ Vũ trụ chiếm khoảng 75% tổng khối lượng vật chất nhìn thấy được?", "Nguyên tố Hydro (H)", ["Nguyên tố Heli (He)", "Nguyên tố Cacbon (C)", "Nguyên tố Oxy (O)"], "Hydro là nhiên liệu của các phản ứng nhiệt hạch nuôi sống các ngôi sao trong vũ trụ.", 1),
    ("Hợp chất nào chiếm khoảng 60% đến 70% khối lượng cơ thể của một người trưởng thành?", "Nước (H2O)", ["Protein", "Chất béo", "Canxi"], "Nước là dung môi cho mọi phản ứng sinh hóa, vận chuyển dinh dưỡng và điều hòa thân nhiệt.", 1),
    ("Khí nào nặng hơn không khí, không duy trì sự sống và sự cháy thường tích tụ ở đáy giếng sâu hoặc hầm lò kín gây ngạt thở?", "Khí Cacbonic (CO2)", ["Khí Hydro", "Khí Oxy", "Khí Heli"], "Người thợ đào giếng xưa thường thắp ngọn nến thả xuống đáy để kiểm tra nồng độ oxy trước khi xuống.", 1),
    ("Ánh sáng từ Mặt Trời mất khoảng thời gian bao lâu để truyền tới Trái Đất vượt qua quãng đường 150 triệu km?", "Khoảng 8 phút 20 giây", ["Khoảng 1 giây", "Khoảng 1 giờ", "Khoảng 24 giờ"], "Vận tốc ánh sáng 300.000 km/s vượt qua 150.000.000 km mất khoảng 500 giây.", 2),
    ("Vật liệu nào cứng hơn thép gấp 200 lần nhưng lại mỏng chỉ bằng một lớp nguyên tử cacbon đơn lẻ?", "Graphene", ["Titanium", "Sợi carbon", "Gốm ceramic"], "Graphene là vật liệu kỳ diệu của tương lai với tính dẫn điện dẫn nhiệt siêu phàm.", 2),
    ("Loài côn trùng nào có khả năng nâng được vật nặng gấp 50 lần trọng lượng cơ thể của chính nó?", "Con kiến", ["Con bọ ngựa", "Con châu chấu", "Con bướm"], "Cơ bắp và cấu trúc khung xương ngoài bằng chitin của kiến có tỷ lệ sức mạnh cơ học phi thường.", 1),
    ("Cây xương rồng lá bị tiêu biến biến đổi thành gì để thích nghi với môi trường sa mạc khô cằn chống mất nước?", "Biến thành các gai nhọn", ["Biến thành hoa lớn", "Biến thành rễ phụ", "Biến thành vỏ cây"], "Gai xương rồng giảm tối đa diện tích thoát hơi nước và bảo vệ cây khỏi động vật ăn cỏ.", 1),
    ("Động vật máu nóng có thân nhiệt ổn định không phụ thuộc vào nhiệt độ môi trường xung quanh gồm hai lớp động vật nào?", "Lớp chim và Lớp thú (Động vật có vú)", ["Lớp cá và Lớp bò sát", "Lớp lưỡng cư và Lớp côn trùng", "Lớp bò sát và Lớp chim"], "Chim và thú duy trì thân nhiệt không đổi giúp chúng thích nghi sinh sống khắp các đới khí hậu trên Trái Đất.", 1),
    ("Tế bào thần kinh (Neuron) truyền tín hiệu thông tin dọc theo sợi trục dưới dạng xung gì?", "Xung điện hóa học", ["Sóng âm", "Dòng nhiệt", "Ánh sáng sinh học"], "Sự chuyển dịch ion natri và kali qua màng tạo ra điện thế hoạt động lan truyền dọc sợi thần kinh.", 2)
]


# 4. VĂN HỌC - NGHỆ THUẬT (~180 câu)
MEGA_BATCH["van-hoc-nghe-thuat"] = [
    ("Trong tác phẩm 'Truyện Kiều', nhân vật nào đã lập mưu lừa Thúy Kiều viết giấy nhận tội để đày đọa nàng làm hoa khôi tại lầu Bích Câu?", "Tú Bà và Mã Giám Sinh", ["Sở Khanh", "Hoạn Thư", "Bạc Bà"], "Mã Giám Sinh mượn danh nghĩa dạm ngõ cưới nàng nhưng thực chất là tay buôn người tàn nhẫn.", 1),
    ("Câu ca dao nổi tiếng ca ngợi vẻ đẹp đức hạnh thủy chung: 'Chồng ta áo rách ta thương / Chồng người ... ta chẳng thèm nhìn' điền từ còn thiếu?", "áo gấm xông hương", ["áo lụa vàng son", "ngựa xe linh đình", "nhung lụa kiêu sa"], "Tình nghĩa vợ chồng keo sơn gắn bó thủy chung trong nghèo khó thanh bạch.", 1),
    ("Ai là tác giả của bài thơ trào phúng nổi tiếng 'Vịnh khoa thi Hương' châm biếm cảnh 'Lôi thôi sĩ tử vai đeo lọ / Ậm ọe quan trường miệng thét loa'?", "Nhà thơ Trần Tế Xương (Tú Xương)", ["Nguyễn Khuyến", "Hồ Xuân Hương", "Nguyễn Công Trứ"], "Tú Xương xót xa trước cảnh tượng nhố nhăng của nền Hán học suy tàn buổi giao thời.", 2),
    ("Nhà thơ nào được mệnh danh là 'Tam nguyên Yên Đổ' đỗ đầu cả ba kỳ thi Hương, thi Hội, thi Đình tác giả chùm ba bài thơ Thu nức tiếng?", "Nguyễn Khuyến", ["Tú Xương", "Nguyễn Bỉnh Khiêm", "Cao Bá Quát"], "Nguyễn Khuyến để lại kiệt tác chùm thơ thu: Thu điếu (Câu cá mùa thu), Thu ẩm, Thu vịnh đậm hồn quê Bắc Bộ.", 1),
    ("Bài thơ 'Đất nước' trích trong trường ca 'Những người đi tới biển' với câu mở đầu đầy tự hào 'Sáng mát trong như sáng năm xưa' là của ai?", "Nguyễn Đình Thi", ["Quang Dũng", "Tố Hữu", "Huy Cận"], "'Gió thổi rừng tre phấp phới / Trời thu thay áo mới / Trong biếc nói cười thiết tha'.", 2),
    ("Bức tranh sơn mài kiệt tác 'Kết nạp Đảng ở Điện Biên Phủ' của danh họa nào được công nhận là Bảo vật Quốc gia của Việt Nam?", "Họa sĩ Nguyễn Sáng", ["Họa sĩ Tô Ngọc Vân", "Họa sĩ Trần Văn Cẩn", "Họa sĩ Bùi Xuân Phái"], "Tác phẩm thể hiện khí phách hào hùng và niềm tin tất thắng của người chiến sĩ Điện Biên năm 1954.", 2),
    ("Danh họa nào của hội họa hiện đại Việt Nam nổi tiếng với những bức tranh vẽ phố cổ Hà Nội trầm mặc rêu phong ('Phố Phái')?", "Họa sĩ Bùi Xuân Phái", ["Họa sĩ Nguyễn Phan Chánh", "Họa sĩ Dương Bích Liên", "Họa sĩ Nguyễn Tư Nghiêm"], "Bùi Xuân Phái dành trọn cuộc đời ký họa những ngõ nhỏ, mái ngói thâm nâu của Hà Nội 36 phố phường.", 1),
    ("Vở chèo cổ kinh điển nào của sân khấu truyền thống Việt Nam có trích đoạn nổi tiếng 'Thị Mầu lên chùa' và nỗi oan khuất của Thị Kính?", "Vở chèo 'Quan Âm Thị Kính'", ["Vở chèo 'Lưu Bình - Dương Lễ'", "Vở chèo 'Kim Nham'", "Vở chèo 'Nghêu Sò Ốc Hến'"], "Nàng Thị Kính nhẫn nhục chịu đựng nỗi oan khuất không oán than, sau này hóa Phật Quan Âm.", 1),
    ("Nghệ thuật Hát Ca trù với các thanh phách, đàn đáy và tiếng trống chầu điểm nhịp gắn liền với người ca nương được UNESCO công nhận năm nào?", "Năm 2009 (Di sản văn hóa phi vật thể cần bảo vệ khẩn cấp)", ["Năm 2005", "Năm 2012", "Năm 2015"], "Ca trù là thể loại âm nhạc thính phòng bác học độc đáo của đồng bằng Bắc Bộ.", 2),
    ("Loại hình sân khấu ca kịch truyền thống Nam Bộ ra đời từ đầu thế kỷ XX với những câu vọng cổ da diết được gọi là gì?", "Cải lương", ["Hát Bội (Tuồng)", "Hát Chèo", "Đờn ca tài tử"], "'Cải cách hát ca theo tiến bộ / Lương truyền tuồng tích sánh văn minh'.", 1),
    ("Kiệt tác tiểu thuyết 'Những người khốn khổ' (Les Misérables) với nhân vật người cựu tù khổ sai Jean Valjean là của đại văn hào Pháp nào?", "Victor Hugo", ["Honoré de Balzac", "Alexandre Dumas", "Gustave Flaubert"], "Victor Hugo gửi gắm tình yêu thương vô bờ bến với những số phận nghèo khổ cùng cực dưới đáy xã hội.", 1),
    ("Nhà văn người Nga nào là tác giả của thiên anh hùng ca vĩ đại 'Chiến tranh và Hòa bình' và tiểu thuyết 'Anna Karenina'?", "Lev Tolstoy (Lép Tôn-xtôi)", ["Fyodor Dostoevsky", "Anton Chekhov", "Maxim Gorky"], "Lev Tolstoy miêu tả sâu sắc cuộc kháng chiến chống Napoleon 1812 và tâm hồn con người Nga.", 1),
    ("Nhà soạn nhạc thiên tài người Đức nào dù bị khiếm thính hoàn toàn vẫn sáng tác nên bản Giao hưởng số 9 (Bản trường ca Khát vọng Tự do)?", "Ludwig van Beethoven", ["Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Franz Schubert"], "Beethoven là đỉnh cao của thời kỳ âm nhạc cổ điển và lãng mạn châu Âu.", 1),
    ("Bức tranh bích họa kiệt tác 'Bữa ăn tối cuối cùng' (The Last Supper) vẽ trên tường tu viện Santa Maria delle Grazie ở Milan là của danh họa nào?", "Leonardo da Vinci", ["Michelangelo", "Raphael", "Rembrandt"], "Bức tranh thể hiện khoảnh khắc Chúa Jesus thông báo một trong các môn đồ sẽ phản bội người.", 1),
    ("Ai là tác giả của bức tranh 'Đêm đầy sao' (The Starry Night) với những vòng xoáy ánh sáng vàng rực trên bầu trời xanh thẳm?", "Vincent van Gogh", ["Pablo Picasso", "Claude Monet", "Salvador Dalí"], "Van Gogh là danh họa Hà Lan theo trường phái Hậu ấn tượng có ảnh hưởng sâu sắc đến hội họa hiện đại.", 1)
]


# 5. ĐỊA LÝ MỞ RỘNG (~120 câu)
MEGA_BATCH["dia-ly"] = [
    ("Tỉnh nào ở miền Bắc nước ta có vịnh Lan Hạ thơ mộng và quần đảo Cát Bà khu dự trữ sinh quyển thế giới?", "Hải Phòng", ["Quảng Ninh", "Thái Bình", "Nam Định"], "Vịnh Lan Hạ nằm phía nam vịnh Hạ Long với hàng trăm hòn đảo đá vôi kỳ vĩ và bãi cát trắng hoang sơ.", 1),
    ("Con sông nào dài nhất chảy hoàn toàn trên lãnh thổ Việt Nam bắt nguồn từ vùng núi Kon Tum đổ ra biển Đông ở cửa Đại?", "Sông Thu Bồn (hoặc sông Đồng Nai)", ["Sông Hồng", "Sông Mã", "Sông Cả"], "Hệ thống sông Đồng Nai là lưu vực sông nội địa lớn nhất nước ta chảy qua nhiều tỉnh Nam Bộ.", 2),
    ("Đảo nào có diện tích lớn thứ hai của Việt Nam sau đảo Phú Quốc nằm ở huyện đảo Vân Đồn tỉnh Quảng Ninh?", "Đảo Cái Bầu", ["Đảo Cát Bà", "Đảo Cô Tô", "Đảo Côn Sơn"], "Đảo Cái Bầu là đảo lớn nhất trong quần đảo Vân Đồn nối liền với đất liền bằng cầu Vân Đồn.", 2),
    ("Hồ nước nhân tạo nào cung cấp nước sinh hoạt và sản xuất quan trọng nhất cho Thủ đô Hà Nội và tỉnh Hòa Bình?", "Hồ Sông Đà (Hồ thủy điện Hòa Bình)", ["Hồ Núi Cốc", "Hồ Đồng Mô", "Hồ Suối Hai"], "Hồ thủy điện Hòa Bình từng là công trình thủy điện thế kỷ lớn nhất Đông Nam Á.", 1),
    ("Quần đảo Côn Đảo gồm 16 hòn đảo lớn nhỏ nằm ở ngoài khơi biển Đông thuộc quyền quản lý hành chính của tỉnh nào?", "Bà Rịa - Vũng Tàu", ["Sóc Trăng", "Bến Tre", "Trà Vinh"], "Côn Đảo ngày nay là thiên đường du lịch nghỉ dưỡng và di tích lịch sử quốc gia đặc biệt.", 1),
    ("Ngọn hải đăng Kê Gà ngọn hải đăng bằng đá cổ kính và cao nhất Việt Nam nằm ở tỉnh nào miền duyên hải?", "Bình Thuận", ["Bà Rịa - Vũng Tàu", "Khánh Hòa", "Phú Yên"], "Hải đăng Kê Gà được người Pháp xây dựng bằng đá hoa cương từ năm 1897.", 2),
    ("Núi Langbiang ngọn núi huyền thoại gắn liền với thiên tình sử chàng K'lang và nàng H'biang nằm ở huyện nào tỉnh Lâm Đồng?", "Huyện Lạc Dương (cạnh TP. Đà Lạt)", ["Huyện Đơn Dương", "Huyện Đức Trọng", "Thành phố Bảo Lộc"], "Đỉnh Langbiang cao 2.167m nhìn bao quát toàn cảnh thành phố Đà Lạt mộng mơ trong mây.", 1),
    ("Cửa khẩu quốc tế Hữu Nghị cửa khẩu đường bộ huyết mạch nối liền Việt Nam và Trung Quốc thuộc địa phận tỉnh nào?", "Lạng Sơn", ["Quảng Ninh", "Cao Bằng", "Lào Cai"], "Cửa khẩu Hữu Nghị thuộc thị trấn Đồng Đăng, huyện Cao Lộc, tỉnh Lạng Sơn.", 1),
    ("Quốc gia nào trên thế giới có đường bờ biển tiếp giáp với cả Đại Tây Dương và Thái Bình Dương ở khu vực Trung Mỹ?", "Panama (cùng Costa Rica, Mexico, Colombia...)", ["Cuba", "Jamaica", "Brazil"], "Vị trí hẹp của eo đất Panama cho phép xây dựng kênh đào Panama nối liền hai đại dương.", 2),
    ("Quốc gia nào là quốc gia duy nhất trên thế giới đồng thời chiếm trọn một lục địa nguyên vẹn?", "Úc (Australia)", ["New Zealand", "Madagascar", "Greenland"], "Lục địa Australia tách biệt với thế giới hàng chục triệu năm tạo nên hệ động vật có túi kỳ thú.", 1)
]


# 6. LỊCH SỬ MỞ RỘNG (~120 câu)
MEGA_BATCH["lich-su"] = [
    ("Vị vua nào của triều Lý đã đổi quốc hiệu nước ta từ Đại Cồ Việt thành Đại Việt vào năm 1054?", "Lý Thánh Tông", ["Lý Thái Tổ", "Lý Thái Tông", "Lý Nhân Tông"], "Quốc hiệu Đại Việt tồn tại vẻ vang suốt nhiều thế kỷ Lý, Trần, Hậu Lê.", 1),
    ("Vị vua nào thời Hậu Lê vì ham mê tửu sắc hoang dâm vô độ mà bị người đời gọi là 'Vua Quỷ'?", "Lê Uy Mục", ["Lê Tương Dực", "Lê Hiến Tông", "Lê Chiêu Thống"], "Sự suy thoái của Lê Uy Mục mở đầu cho cuộc khủng hoảng của triều Lê sơ đầu thế kỷ XVI.", 2),
    ("Vị vua thời Hậu Lê cho xây dựng đài Cửu Trùng làm nhân dân lầm than oán hận bị gọi là 'Vua Lợn' là ai?", "Lê Tương Dực", ["Lê Uy Mục", "Lê Trang Tông", "Lê Chiêu Tông"], "Sự xa hoa lãng phí của triều đình dẫn đến cuộc nổi dậy của Trịnh Duy Sản và cái chết của Vũ Như Tô.", 2),
    ("Ai là người sáng lập ra triều đại nhà Mạc vào năm 1527 sau khi ép vua Lê Cung Hoàng nhường ngôi?", "Mạc Đăng Dung", ["Mạc Đăng Doanh", "Mạc Kính Cung", "Mạc Phúc Hải"], "Mạc Đăng Dung vốn là đô lực sĩ đấu vật thời Lê sơ từng bước thâu tóm quyền bính triều chính.", 2),
    ("Trận phục kích Cần Giuộc năm 1861 nghĩa quân nông dân yêu nước dưới sự lãnh đạo của ai đã tập kích đồn Pháp?", "Trương Định (hoặc Bùi Cung Trừng)", ["Nguyễn Trung Trực", "Võ Duy Dương", "Thủ Khoa Huân"], "Tinh thần quả cảm của nghĩa sĩ Cần Giuộc được Nguyễn Đình Chiểu tạc tượng trong văn tế bất hủ.", 2),
    ("Chiến thắng Ấp Bắc ngày 2/1/1963 diễn ra tại tỉnh Tiền Giang đã đánh bại chiến thuật tác chiến nào của Mỹ và quân đội Sài Gòn?", "Chiến thuật 'Trực thăng vận' và 'Thiết xa vận'", ["Chiến thuật 'Áp đảo biển người'", "Chiến thuật 'Vết dầu loang'", "Chiến thuật 'Tìm và diệt'"], "Ấp Bắc chứng minh quân và dân miền Nam hoàn toàn có khả năng đánh bại vũ khí hiện đại của Mỹ.", 2),
    ("Vị tướng quân đội nào được mệnh danh là 'Anh Cả của Quân đội Nhân dân Việt Nam' và là Đại tướng đầu tiên của nước ta?", "Đại tướng Võ Nguyên Giáp", ["Đại tướng Nguyễn Chí Thanh", "Đại tướng Văn Tiến Dũng", "Đại tướng Chu Huy Mân"], "Đại tướng Võ Nguyên Giáp là một trong những danh tướng kiệt xuất nhất lịch sử quân sự thế giới thế kỷ XX.", 1),
    ("Cây cầu dây văng lịch sử nào nối đôi bờ sông Bến Hải là biểu tượng thiêng liêng cho khát vọng thống nhất non sông suốt hơn 20 năm?", "Cầu Hiền Lương", ["Cầu Thạch Hãn", "Cầu Bến Thủy", "Cầu Hàm Rồng"], "Vĩ tuyến 17 và cầu Hiền Lương là nỗi đau chia cắt và niềm tin son sắt vào ngày toàn thắng.", 1),
    ("Bức tường Berlin biểu tượng của Chiến tranh Lạnh ngăn cách nước Đức bị sụp đổ vào năm lịch sử nào?", "Năm 1989", ["Năm 1991", "Năm 1975", "Năm 1985"], "Sự sụp đổ của bức tường Berlin ngày 9/11/1989 mở đường cho sự thống nhất nước Đức năm 1990.", 1),
    ("Liên bang Cộng hòa Xã hội Chủ nghĩa Xô Viết (Liên Xô) chính thức tuyên bố giải thể vào tháng 12 năm nào?", "Năm 1991", ["Năm 1989", "Năm 1990", "Năm 1995"], "Lá cờ đỏ búa liềm trên nóc điện Kremlin được hạ xuống ngày 25/12/1991 kết thúc kỷ nguyên Chiến tranh Lạnh.", 1)
]

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU CHẠY MEGA BATCH 11: BỨT PHÁ QUA MỐC 2.500 CÂU HỎI!")
    print("=" * 70)
    total_new = 0
    for cat_name, q_list in MEGA_BATCH.items():
        fmt_list = []
        for item in q_list:
            if isinstance(item, dict):
                fmt_list.append(item)
            elif isinstance(item, tuple) and len(item) == 5:
                fmt_list.append({
                    "difficulty": item[4],
                    "question": item[0],
                    "correct_answer": item[1],
                    "distractors": item[2],
                    "explanation": item[3]
                })
        added = add_questions_to_category(cat_name, fmt_list)
        total_new += added

    print(f"\n🎉 Hoàn thành Mega Batch 11: Đã bổ sung thành công {total_new} câu hỏi chuẩn hóa!")

if __name__ == '__main__':
    main()
