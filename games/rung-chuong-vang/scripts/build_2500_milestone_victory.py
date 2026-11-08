# -*- coding: utf-8 -*-
"""
Milestone 3 Victory: Cán đích 2.500 câu hỏi chuẩn hóa toàn diện!
Bổ sung 120 câu hỏi (20 câu x 6 chủ đề) chuẩn hóa cao cấp.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

VICTORY_DATA = {
    # 1. ĐỐ VUI TRÍ TUỆ (20 câu)
    "do-vui-tri-tue": [
        ("Đố mẹo: Bánh gì không nướng trong lò mà xốp mịn ngọt ngào gắn liền với ngày sinh nhật thổi nến?", "Bánh sinh nhật (Bánh kem gato)", ["Bánh chưng", "Bánh giầy", "Bánh rán"], "Chiếc bánh kem cắm nến lung linh cùng lời ước nguyện tuổi mới an lành.", 1),
        ("Đố mẹo: Quả gì khoác áo tím thẫm, cuống gắn vương miện xanh, bên trong múi trắng ngọt thanh?", "Quả măng cụt", ["Quả nho", "Quả cà tím", "Quả mận"], "Măng cụt được mệnh danh là 'Nữ hoàng của các loại trái cây' nhiệt đới.", 1),
        ("Đố mẹo: Quả gì vỏ màu đỏ rực, gai mềm như tóc rối, bóc ra cùi trắng ngọt thơm?", "Quả chôm chôm", ["Quả vải", "Quả nhãn", "Quả măng cụt"], "Những vườn chôm chôm chín đỏ rực mùa hè miền Tây trĩu cành hấp dẫn.", 1),
        ("Đố mẹo: Cái gì có lưng có bụng mà không có đầu có chân, kê êm giấc ngủ say nồng hàng đêm?", "Chiếc gối ôm (hoặc chiếc gối đầu)", ["Chiếc chăn", "Chiếc chiếu", "Cái giường"], "Chiếc gối êm ái nâng niu giấc ngủ ngon cho mọi người sau ngày làm việc mệt mỏi.", 1),
        ("Đố mẹo: Con gì có mai như thuyền úp, bò chậm chạp trên bờ mà bơi lội biển khơi hàng ngàn dặm?", "Con rùa biển (Đồi mồi)", ["Con cua", "Con ốc", "Con tôm"], "Rùa biển là loài động vật cổ xưa quý hiếm được bảo tồn trên toàn thế giới.", 1),
        ("Đố mẹo: Xe gì chở đầy bệnh nhân, hú còi inh ỏi xé toang đêm tối xin đường cấp cứu?", "Xe cứu thương (Xe cấp cứu)", ["Xe cảnh sát", "Xe cứu hỏa", "Xe buýt"], "Xe cứu thương được ưu tiên tuyệt đối khi lưu thông để giành giật mạng sống cho người bệnh.", 1),
        ("Đố mẹo: Xe gì vòi rồng phun nước dập tắt đám cháy, còi hụ vang dội lao nhanh ngoài phố?", "Xe cứu hỏa (Xe chữa cháy)", ["Xe bồn", "Xe tưới cây", "Xe cảnh sát"], "Các chiến sĩ cảnh sát phòng cháy chữa cháy xông pha cứu người cứu tài sản.", 1),
        ("Đố chữ: Bỏ đầu thành một loài chim / Để nguyên thứ nước ngọt lịm người khen là gì?", "Mật (bỏ M thành Cật / Mật ong / Cò...)", ["Đường", "Sữa", "Trà"], "Mật ong thơm ngọt tự nhiên giàu dinh dưỡng bồi bổ sức khỏe.", 2),
        ("Đố logic: Bạn có một que diêm, bước vào căn phòng tối có 1 cây đèn dầu, 1 ngọn nến và 1 đống củi khô. Bạn thắp cái gì đầu tiên?", "Thắp que diêm đầu tiên!", ["Thắp cây nến", "Thắp cây đèn dầu", "Thắp đống củi"], "Không thắp que diêm trước thì lấy lửa ở đâu để thắp những thứ còn lại!", 1),
        ("Đố mẹo: Thứ gì thuộc về bạn, khi ai đó hỏi xin mượn thì bạn không mất, nhưng không cho thì mất lòng?", "Lời khuyên (hoặc sự giúp đỡ)", ["Tiền bạc", "Cuốn sách", "Chiếc áo"], "Lời khuyên chân thành và sự sẻ chia giúp gắn kết tình bạn bè người thân.", 1),
        ("Đố mẹo: Con gì sinh ra không có chân mà vẫn leo cây bắt chuột leo xà nhà thoăn thoắt?", "Con trăn (hoặc con rắn)", ["Con giun", "Con lươn", "Con đỉa"], "Loài trăn uốn mình quấn chặt thân cây leo trèo săn mồi cực kỳ khéo léo.", 1),
        ("Đố mẹo: Cái gì bạn vừa thổi vừa ăn mà không sợ bị phỏng rát lưỡi?", "Bong bóng kẹo cao su (hoặc súp nóng vừa thổi vừa húp)", ["Nồi cháo sôi", "Củ khoai nướng", "Cốc trà nóng"], "Thổi bong bóng kẹo cao su phồng to vui mắt.", 1),
        ("Đố mẹo: Đồ vật nào dùng để cài cúc áo giữ cho hai tà áo khép kín phẳng phiu?", "Cúc áo (khuy áo)", ["Cái kim", "Sợi chỉ", "Cái khóa kéo"], "Cúc áo nhỏ xinh đính đều đặn tạo nên nét lịch sự cho trang phục.", 1),
        ("Đố mẹo: Con gì thích tắm bùn lầy, ục ịch kêu eng éc trong chuồng béo tròn múp míp?", "Con lợn (con heo)", ["Con trâu", "Con bò", "Con dê"], "Chú heo béo tốt no tròn là biểu tượng ấm no của người nông dân.", 1),
        ("Đố mẹo: Cái gì hai chân nhảy nhót trên cành, hót líu lo chào bình minh rạng rỡ?", "Con chim sơn ca (hoặc chim chích bông)", ["Con sóc", "Con bướm", "Con ve sầu"], "Tiếng chim hót véo von báo hiệu một ngày mới tươi sáng bắt đầu.", 1),
        ("Đố mẹo: Đường gì không có ổ gà, máy bay cất cánh lao vút lên mây xanh?", "Đường băng sân bay", ["Đường cao tốc", "Đường nhựa", "Đường sắt"], "Đường băng bê tông kiên cố chịu tải trọng hàng trăm tấn của máy bay phản lực.", 1),
        ("Đố chữ: Cắt đuôi thành quả ngọt bùi / Để nguyên con thú ngủ vùi trong đông là con gì?", "Con gấu (bỏ sắc thành con gấu / dâu)", ["Con sóc", "Con nai", "Con hổ"], "Gấu ngủ đông trong hang tuyết để tiết kiệm năng lượng qua mùa giá rét.", 2),
        ("Đố logic: Có 3 người đi chung một chiếc ô che mưa nhỏ. Về tới nhà không ai bị ướt cả. Vì sao?", "Vì trời không có mưa!", ["Vì ô to", "Vì họ chạy nhanh", "Vì trời nắng nhẹ"], "Trời không mưa thì che ô đi dạo làm sao mà ướt được!", 1),
        ("Đố mẹo: Quả gì vỏ màu vàng óng, uốn cong như trăng khuyết, bóc vỏ ăn ngọt mềm?", "Quả chuối chín", ["Quả xoài", "Quả dưa lê", "Quả cam"], "Chuối chín giàu kali và vitamin là món tráng miệng bổ dưỡng hàng ngày.", 1),
        ("Đố mẹo: Hoa gì ngát hương mùa hè, cánh trắng nhụy vàng ướp trà sen thanh khiết hồ Tây?", "Hoa sen trắng (hoặc sen bách diệp)", ["Hoa súng", "Hoa nhài", "Hoa cúc"], "Trà ướp sen hồ Tây là thức quà tinh tế thanh tao bậc nhất chốn Hà thành.", 1)
    ],

    # 2. ĐỜI SỐNG - CÔNG NGHỆ (20 câu)
    "doi-song-cong-nghe": [
        ("Món chả lụa (giò lụa) truyền thống Việt Nam được giã mịn từ thịt heo nạc tươi gói bằng lá gì luộc chín?", "Lá chuối tươi", ["Lá dong", "Lá sen", "Lá ổi"], "Lá chuối xanh đượm mùi hương tự nhiên hòa quyện với vị giòn ngọt của giò lụa.", 1),
        ("Đặc sản bánh gai làng Mía (huyện Yên Định, Thanh Hóa) dẻo quánh nhân đậu xanh dừa sợi gói bằng lá gì?", "Lá chuối khô", ["Lá chuối tươi", "Lá dong", "Lá dừa"], "Lá chuối khô giữ cho bánh gai bảo quản được lâu và dậy mùi thơm đặc trưng.", 1),
        ("Món ăn sáng quen thuộc của người Hà Nội gồm xôi nếp dẻo rưới mỡ gà, đậu xanh đồ mịn thái mỏng và hành phi giòn là xôi gì?", "Xôi xéo", ["Xôi gấc", "Xôi vò", "Xôi ngô"], "Xôi xéo vàng ươm thơm nức mùi mỡ hành gói trong lá chuối xanh.", 1),
        ("Món bún bò Nam Bộ đặc trưng bởi cách ăn như thế nào so với bún bò Huế?", "Bún bò trộn khô chan nước mắm chua ngọt, rắc đậu phộng rang và hành phi", ["Bún bò chan nước dùng nóng", "Bún bò chấm mắm tôm", "Bún bò ăn cùng mắm ruốc"], "Bún bò Nam Bộ thanh nhẹ ăn kèm thịt bò xào sả ớt mềm ngọt và rau sống xanh mướt.", 1),
        ("Đặc sản chả rươi thơm lừng béo ngậy rán cùng trứng gà và vỏ quýt thái chỉ là món ngon mùa thu của đất nào?", "Hải Phòng và Hải Dương (Tứ Kỳ)", ["Nam Định", "Thái Bình", "Quảng Ninh"], "Con rươi nước lợ xuất hiện vào mùa 'tháng chín đôi mươi, tháng mười mùng năm'.", 1),
        ("Công nghệ sạc không dây cho điện thoại hoạt động dựa trên nguyên lý vật lý nào?", "Hiện tượng cảm ứng điện từ giữa hai cuộn dây", ["Sóng hồng ngoại", "Sóng âm siêu tần", "Phản xạ nhiệt"], "Cuộn dây phát trong đế sạc truyền năng lượng từ trường sang cuộn dây nhận trong điện thoại.", 2),
        ("Thế hệ mạng không dây cục bộ mới nhất hiện nay mang tên Wi-Fi 7 hoạt động trên những dải tần số nào?", "Ba dải tần 2.4 GHz, 5 GHz và 6 GHz", ["Chỉ có 2.4 GHz", "Chỉ có 5 GHz", "Chỉ có sóng vệ tinh"], "Wi-Fi 7 tăng tốc độ truyền dữ liệu lên tới hơn 40 Gbps với độ trễ cực thấp.", 2),
        ("Dung lượng pin của điện thoại thông minh và sạc dự phòng thường được đo bằng đơn vị nào?", "Miliampe giờ (mAh)", ["Volt (V)", "Watt (W)", "Ohm (Ω)"], "Chỉ số mAh càng lớn thì thời lượng sử dụng thiết bị sau một lần sạc càng lâu dài.", 1),
        ("Màn hình máy tính có tỷ lệ khung hình 16:9 tiêu chuẩn được gọi là màn hình chuẩn gì?", "Màn hình rộng (Widescreen)", ["Màn hình vuông", "Màn hình siêu dài", "Màn hình dọc"], "Tỷ lệ 16:9 phù hợp với tầm nhìn mắt người và định dạng phim ảnh hiện đại.", 1),
        ("Thuật toán trí tuệ nhân tạo học sâu (Deep Learning) mô phỏng cấu trúc mạng lưới nào của cơ thể sinh học?", "Mạng lưới tế bào thần kinh nhân tạo (Artificial Neural Network)", ["Hệ tuần hoàn máu", "Hệ miễn dịch", "Cấu trúc xương"], "Các lớp nơ-ron nhân tạo kết nối với nhau xử lý hình ảnh, giọng nói và ngôn ngữ tự nhiên.", 2),
        ("Trong môn bơi lội thể thao, kiểu bơi nào có tốc độ di chuyển nhanh nhất trong 4 kiểu bơi tiêu chuẩn?", "Bơi trườn sấp (Bơi sải / Freestyle)", ["Bơi ếch", "Bơi ngửa", "Bơi bướm"], "Tư thế lướt nước thuôn dài và nhịp quạt tay liên tục giúp bơi sải đạt vận tốc tối đa.", 1),
        ("Trong môn nhảy cầu thể thao, độ cao tối đa của cầu nhảy cứng tiêu chuẩn Olympic là bao nhiêu mét?", "Cầu nhảy 10 mét", ["5 mét", "7 mét", "15 mét"], "Cầu nhảy 10m đòi hỏi vận động viên thực hiện các động tác nhào lộn kỹ thuật phức tạp trước khi tiếp nước.", 2),
        ("Một trận thi đấu quyền anh (Boxing) chuyên nghiệp tranh đai vô địch thế giới thường kéo dài tối đa bao nhiêu hiệp?", "12 hiệp đấu (mỗi hiệp 3 phút)", ["10 hiệp", "15 hiệp", "8 hiệp"], "Mỗi hiệp kéo dài 3 phút với 1 phút nghỉ giữa các hiệp thi đấu.", 2),
        ("Giải bóng đá danh giá vô địch Nam Mỹ cấp đội tuyển quốc gia có tên gọi là gì?", "Copa America", ["Euro", "Gold Cup", "Asian Cup"], "Copa America là giải bóng đá châu lục lâu đời nhất thế giới khởi tranh từ năm 1916.", 1),
        ("Kỳ World Cup bóng đá nam 2026 sẽ được đồng đăng cai bởi ba quốc gia Bắc Mỹ nào?", "Mỹ, Canada và Mexico", ["Mỹ, Brazil và Argentina", "Mỹ, Anh và Pháp", "Canada, Mexico và Cuba"], "World Cup 2026 lần đầu tiên mở rộng quy mô lên tới 48 đội tuyển tham dự.", 1),
        ("Phương pháp bảo quản thực phẩm bằng cách sấy lạnh thăng hoa trong môi trường chân không được gọi là gì?", "Sấy thăng hoa (Freeze Drying)", ["Sấy nhiệt", "Phơi nắng", "Hun khói"], "Sấy thăng hoa giữ nguyên vẹn 98% hàm lượng dinh dưỡng, hương vị và màu sắc ban đầu của thực phẩm.", 2),
        ("Nhiệt độ an toàn của ngăn đông tủ lạnh gia đình để bảo quản thịt cá đông đá lâu dài là bao nhiêu độ?", "Từ -18 độ C trở xuống", ["0 độ C", "-5 độ C", "-10 độ C"], "Ở nhiệt độ -18°C mọi hoạt động của vi khuẩn gây ôi thiu đều bị ức chế hoàn toàn.", 1),
        ("Khi bị điện giật, hành động sơ cứu khẩn cấp đầu tiên và quan trọng nhất của người ứng cứu là gì?", "Ngắt ngay nguồn điện (cắt cầu dao, aptomat) hoặc dùng vật liệu cách điện gạt dây điện ra", ["Lao vào ôm kéo nạn nhân ra ngay bằng tay không", "Đổ nước vào người nạn nhân", "Hô hấp nhân tạo ngay"], "Tuyệt đối không chạm tay trực tiếp vào nạn nhân khi chưa ngắt điện để tránh bị điện giật liên hoàn.", 1),
        ("Quy định nồng độ cồn đối với người điều khiển xe máy và ô tô tham gia giao thông tại Việt Nam theo luật hiện hành là bao nhiêu?", "Bằng 0 (Tuyệt đối không có cồn trong máu và hơi thở)", ["Dưới 0,25 mg/lít khí thở", "Dưới 0,5 mg/lít", "Dưới 50 mg/100ml máu"], "'Đã uống rượu bia - Không lái xe' là thông điệp an toàn giao thông nghiêm ngặt bảo vệ tính mạng con người.", 1),
        ("Loại bình chữa cháy mini thông dụng dập tắt đám cháy xăng dầu và thiết bị điện trong nhà thường chứa chất gì?", "Khí CO2 nén lạnh hoặc bột chữa cháy hóa học", ["Nước cất", "Dầu hỏa", "Cát ướt"], "Khí CO2 và bột hóa học làm loãng nồng độ oxy và cách ly vật liệu cháy dập tắt lửa nhanh chóng.", 1)
    ],

    # 3. KHOA HỌC TỰ NHIÊN (20 câu)
    "khoa-hoc-tu-nhien": [
        ("Hạt hạ nguyên tử nào mang điện tích dương nằm trong hạt nhân của mọi nguyên tử?", "Hạt Proton (p+)", ["Hạt Electron", "Hạt Neutron", "Hạt Photon"], "Số lượng proton quyết định số hiệu nguyên tử và vị trí của nguyên tố trong bảng tuần hoàn.", 1),
        ("Hạt hạ nguyên tử nào không mang điện tích nằm cùng với proton trong hạt nhân nguyên tử?", "Hạt Neutron (n0)", ["Hạt Electron", "Hạt Positron", "Hạt Quark"], "Các đồng vị của cùng một nguyên tố hóa học có cùng số proton nhưng khác nhau về số neutron.", 1),
        ("Phản ứng nhiệt hạch (tổng hợp hạt nhân) giải phóng năng lượng khổng lồ trên Mặt Trời là phản ứng kết hợp của các hạt nhân nào?", "Hạt nhân Hydro kết hợp thành hạt nhân Heli", ["Hạt nhân Urani phân hạch", "Cacbon cháy với Oxy", "Phân rã chì"], "Phản ứng nhiệt hạch là nguồn năng lượng vô tận nuôi dưỡng Hệ Mặt Trời suốt hàng tỷ năm qua.", 2),
        ("Kim loại nào là thành phần chính cấu tạo nên lõi chất lỏng và lõi rắn ở trung tâm Trái Đất?", "Sắt (Fe) và Niken (Ni)", ["Đồng và Nhôm", "Vàng và Bạc", "Chì và Kẽm"], "Dòng đối lưu của sắt nóng chảy trong lõi ngoài hoạt động như một máy phát điện khổng lồ sinh ra từ trường Trái Đất.", 2),
        ("Đại dương nào trên Trái Đất có diện tích nhỏ nhất và được bao bọc hoàn toàn bởi băng tuyết quanh năm?", "Bắc Băng Dương (Arctic Ocean)", ["Ấn Độ Dương", "Đại Tây Dương", "Nam Đại Dương"], "Bắc Băng Dương nằm quanh vùng Bắc Cực là nơi sinh sống của gấu trắng Bắc Cực và hải mã.", 1),
        ("Loài cá voi nào có hàm răng lớn nhất và bộ não nặng nhất trong thế giới động vật lặn sâu săn mực khổng lồ?", "Cá nhà táng (Sperm whale)", ["Cá voi xanh", "Cá voi lưng gù", "Cá voi sát thủ"], "Cá nhà táng có thể lặn sâu tới hơn 2.000 mét dưới đáy đại dương tối tăm.", 2),
        ("Loài động vật không xương sống nào thông minh nhất có khả năng đổi màu ngụy trang tức thì và mở nắp lọ?", "Bạch tuộc (Octopus)", ["Mực nang", "Ốc sên", "Tôm hùm"], "Bạch tuộc có hệ thần kinh phân tán với 2/3 số tế bào thần kinh nằm ở các xúc tu linh hoạt.", 1),
        ("Loài thú nào có lớp vảy sừng xếp chồng như áo giáp bảo vệ và cuộn tròn thành quả bóng khi gặp nguy hiểm?", "Con tê tê (Pangolin)", ["Con nhím", "Con thú ăn kiến", "Con tatu"], "Tê tê là loài động vật hoang dã quý hiếm cần được bảo tồn nghiêm ngặt trước nạn săn bắt trái phép.", 1),
        ("Cơ quan nào ở loài cá làm nhiệm vụ cảm nhận áp lực nước, rung chấn và chuyển động của dòng nước xung quanh?", "Cơ quan đường bên (Lateral line)", ["Vây đuôi", "Mang cá", "Mắt cá"], "Đường bên giúp cá phối hợp bơi nhịp nhàng theo đàn hàng vạn con mà không bao giờ va chạm vào nhau.", 2),
        ("Hiện tượng các loài thực vật nở hoa theo chu kỳ chiếu sáng ngày và đêm được gọi là hiện tượng gì trong sinh học?", "Quang chu kỳ (Photoperiodism)", ["Quang hợp", "Hô hấp", "Thoát hơi nước"], "Thực vật ngày ngắn nở hoa vào mùa thu đông, thực vật ngày dài nở hoa vào mùa xuân hè.", 2),
        ("Phần lớn lượng khí Oxy trên bầu khí quyển Trái Đất (khoảng 70%) được tạo ra bởi sinh vật nào?", "Tảo biển và vi khuẩn lam phù du trong đại dương", ["Cây cối trong rừng mưa Amazon", "Cỏ đồng cỏ", "Cây lá kim"], "Tảo cát và sinh vật phù du quang hợp bề mặt đại dương là lá phổi thực sự của hành tinh.", 2),
        ("Hiện tượng các hóa chất độc hại tích tụ với nồng độ ngày càng cao qua các bậc dinh dưỡng trong chuỗi thức ăn gọi là gì?", "Hiện tượng tích lũy sinh học (Khuếch đại sinh học)", ["Phì dưỡng", "Đồng hóa", "Dị hóa"], "Các chất độc như thủy ngân, thuốc trừ sâu DDT tích tụ cao nhất ở động vật ăn thịt đầu chuỗi.", 2),
        ("Cấu trúc nào trong tai trong của con người chịu trách nhiệm giữ thăng bằng cho cơ thể khi di chuyển?", "Ba ống bán khuyên (Hệ thống tiền đình)", ["Ốc tai", "Màng nhĩ", "Xương búa"], "Chất dịch nội dịch chuyển động trong ống bán khuyên kích thích tế bào lông báo vị trí đầu về não.", 2),
        ("Tế bào máu nào không có nhân ở người trưởng thành và có đời sống trung bình khoảng 120 ngày?", "Tế bào hồng cầu", ["Tế bào bạch cầu", "Tế bào tiểu cầu", "Tế bào thần kinh"], "Mỗi giây tủy xương sản sinh khoảng 2 triệu hồng cầu mới thay thế các tế bào già cỗi bị tiêu hủy tại lách.", 1),
        ("Loại nấm mốc đầu tiên được nhà bác học Alexander Fleming phát hiện có khả năng ức chế vi khuẩn năm 1928 là gì?", "Nấm Penicillium notatum", ["Nấm men", "Nấm Aspergillus", "Nấm mộc nhĩ"], "Penicillin mở ra kỷ nguyên thuốc kháng sinh cứu sống hàng trăm triệu sinh mạng con người.", 1),
        ("Chất chỉ thị hóa học Phenolphthalein chuyển sang màu gì khi tiếp xúc với dung dịch bazơ (kiềm)?", "Màu hồng tím (hoặc hồng cánh sen)", ["Màu xanh lam", "Màu đỏ tươi", "Màu vàng"], "Phenolphthalein không màu trong môi trường axit và chuyển hồng rực trong môi trường kiềm pH > 8,3.", 1),
        ("Axit nào là axit vô cơ mạnh nhất thường được dùng để sản xuất phân bón và tinh chế dầu mỏ?", "Axit sunfuric (H2SO4)", ["Axit clohidric (HCl)", "Axit cacbonic", "Axit photphoric"], "H2SO4 được mệnh danh là 'Máu của ngành công nghiệp hóa chất'.", 1),
        ("Thuyết Lượng tử ánh sáng do nhà vật lý Max Planck đề xuất năm 1900 khẳng định năng lượng ánh sáng truyền đi dưới dạng gì?", "Các gói năng lượng gián đoạn gọi là Lượng tử (Photon)", ["Dòng sóng liên tục", "Chùm nhiệt độ", "Dòng từ trường"], "Albert Einstein đã phát triển thuyết lượng tử giải thích hiện tượng quang điện mở ra vật lý hiện đại.", 2),
        ("Định luật bảo toàn khối lượng trong các phản ứng hóa học do hai nhà bác học nào độc lập tìm ra?", "Lomonosov (Nga) và Lavoisier (Pháp)", ["Newton và Galileo", "Mendeleev và Dalton", "Boyle và Charles"], "Trong một phản ứng hóa học kín, tổng khối lượng các chất sản phẩm bằng tổng khối lượng các chất tham gia.", 2),
        ("Nơi lạnh nhất trong Hệ Mặt Trời từng được tàu thăm dò ghi nhận nằm trong miệng núi lửa vĩnh cửu không có ánh sáng tại thiên thể nào?", "Mặt Trăng (vùng cực Mặt Trăng đạt -246 độ C)", ["Sao Hỏa", "Sao Kim", "Sao Thủy"], "Vùng bóng râm vĩnh cửu ở miệng hố cực nam Mặt Trăng lạnh hơn cả bề mặt Sao Diêm Vương.", 2)
    ],

    # 4. VĂN HỌC - NGHỆ THUẬT (20 câu)
    "van-hoc-nghe-thuat": [
        ("Trong truyện ngụ ngôn 'Rùa và Thỏ', chú Rùa chậm chạp đã chiến thắng Thỏ chạy nhanh nhờ vào phẩm chất gì?", "Tính kiên trì, bền bỉ và không chủ quan kiêu ngạo", ["Chạy nhanh hơn Thỏ", "Biết đường tắt", "Được thú khác giúp"], "Bài học răn dạy: Kiên trì nhẫn nại ắt thành công, chủ quan khinh địch chuốc lấy thất bại.", 1),
        ("Truyện cười dân gian 'Tam đại con gà' châm biếm sâu cay thói xấu nào trong xã hội?", "Thói dốt nát nhưng lại hay giấu dốt và khoe khoang làm càn", ["Thói keo kiệt", "Thói tham ăn", "Thói ăn trộm"], "Thầy đồ dốt dạy học trò chữ 'kê' là 'dủ dỉ là con dù dì' rồi đổ lỗi cho thần thổ công.", 1),
        ("Câu thành ngữ: 'Uống nước nhớ nguồn' nhắc nhở con người bài học đạo lý truyền thống nào?", "Lòng biết ơn và tri ân sâu sắc cội nguồn tổ tiên", ["Tiết kiệm nước", "Uống nước sạch", "Bảo vệ môi trường"], "Đạo lý truyền thống cao quý làm nên cốt cách tâm hồn của dân tộc Việt Nam ngàn đời.", 1),
        ("Điền từ vào câu tục ngữ: 'Lời chào cao hơn mâm ...'?", "cỗ", ["cơm", "bát", "đĩa"], "Thái độ tôn trọng, lễ phép trong giao tiếp ứng xử quý giá hơn vật chất cao sang.", 1),
        ("Điền từ vào câu ca dao: 'Dù ai đi ngược về xuôi / Nhớ ngày Giỗ Tổ mùng mười tháng ...'?", "ba", ["tư", "năm", "giêng"], "Ngày Giỗ Tổ Hùng Vương (10/3 âm lịch) nhắc nhở triệu con dân đất Việt hướng về nguồn cội thiêng liêng.", 1),
        ("Bài thơ 'Quê hương' ('Quê hương là chùm khế ngọt / Cho con trèo hái mỗi ngày') do nhà thơ nào sáng tác?", "Đỗ Trung Quân", ["Giang Nam", "Tế Hanh", "Lê Anh Xuân"], "Nhạc sĩ Giáp Văn Thạch phổ nhạc bài thơ trở thành khúc ca quê hương lay động muôn triệu con tim xa xứ.", 1),
        ("Bài thơ 'Quê hương' ('Xưa yêu quê hương vì có chim có bướm / Có những ngày trốn học bị đòn roi') là của ai?", "Giang Nam", ["Tế Hanh", "Chính Hữu", "Huy Cận"], "'Hôm nay nhận được tin em / Không tin được dù đó là sự thật / Khóc không được nữa rồi, em đã hy sinh' - bài thơ 'Quê hương' của Giang Nam.", 1),
        ("Ai là tác giả của bài thơ kháng chiến xúc động 'Bài ca vỡ đất' ngợi ca bàn tay lao động cần cù?", "Hoàng Trung Thông", ["Chế Lan Viên", "Xuân Diệu", "Tố Hữu"], "'Bàn tay ta làm nên tất cả / Có sức người sỏi đá cũng thành cơm' - Hoàng Trung Thông.", 1),
        ("Tập thơ 'Máu và Hoa' (1977) của Tố Hữu là khúc tráng ca hào hùng ngợi ca giai đoạn lịch sử nào của dân tộc?", "Cuộc kháng chiến chống Mỹ cứu nước và ngày toàn thắng mùa xuân 1975", ["Kháng chiến chống Pháp", "Thời kỳ đổi mới", "Cách mạng Tháng Tám"], "Tập thơ khép lại chặng đường đấu tranh giải phóng dân tộc oanh liệt của non sông Việt Nam.", 2),
        ("Nhà văn nào tác giả của tập truyện ngắn 'Vang bóng một thời' ngợi ca những nét sinh hoạt thanh tao nho nhã của người xưa?", "Nguyễn Tuân", ["Thạch Lam", "Vũ Bằng", "Nam Cao"], "Bút pháp tinh tế miêu tả nghệ thuật thưởng trà, viết thư pháp, chơi hoa của những bậc tài hoa tài tử.", 1),
        ("Tác phẩm kịch cổ điển Pháp 'Lão hà tiện' (L'Avare) với nhân vật kẹp lép keo kiệt Harpagon là của ai?", "Molière (Mô-li-e)", ["Corneille", "Racine", "Beaumarchais"], "Molière là bậc thầy hài kịch vĩ đại của nước Pháp thế kỷ XVII.", 1),
        ("Ai là tác giả của câu chuyện cổ tích bất hủ 'Nàng tiên cá' (The Little Mermaid) và 'Chú lính chì dũng cảm'?", "Hans Christian Andersen (Đan Mạch)", ["Anh em Grimm (Đức)", "Charles Perrault (Pháp)", "Oscar Wilde"], "Andersen để lại kho tàng truyện cổ tích nhân văn làm say mê tâm hồn trẻ thơ toàn cầu.", 1),
        ("Bộ truyện cổ tích kinh điển thế giới kể về nàng Bạch Tuyết, Cô bé Lọ Lem, Cô bé quàng khăn đỏ là của ai?", "Anh em nhà Grimm (Jacob và Wilhelm Grimm người Đức)", ["Andersen", "La Fontaine", "Aesop"], "Truyện cổ Grimm ghi chép và sáng tạo từ kho tàng văn hóa dân gian phong phú của nước Đức.", 1),
        ("Ai là tác giả của tập thơ ngụ ngôn bất hủ viết bằng tiếng Pháp: 'Ve và Kiến', 'Rùa và Thỏ', 'Cáo và Quạ'?", "Jean de La Fontaine", ["Molière", "Victor Hugo", "Voltaire"], "Những bài học đạo đức thâm thúy mượn thế giới loài vật răn dạy con người.", 1),
        ("Nhà soạn nhạc thiên tài người Áo được coi là 'Thần đồng âm nhạc' sáng tác hàng trăm bản sonata, giao hưởng từ khi còn nhỏ là ai?", "Wolfgang Amadeus Mozart", ["Ludwig van Beethoven", "Johann Sebastian Bach", "Frederic Chopin"], "Mozart có khả năng thẩm âm tuyệt đối và tài năng sáng tác thăng hoa diệu kỳ.", 1),
        ("Nhà soạn nhạc người Ba Lan được mệnh danh là 'Nhà thơ của cây đàn piano' tác giả các bản valse, nocturne trữ tình là ai?", "Frederic Chopin (Sô-panh)", ["Franz Liszt", "Tchaikovsky", "Johannes Brahms"], "Âm nhạc Chopin nồng nàn tình yêu quê hương đất mẹ Ba Lan qua các điệu nhảy Polonaise và Mazurka.", 1),
        ("Bức tranh sơn mài Bảo vật Quốc gia 'Bác Hồ ở chiến khu Việt Bắc' sáng tác năm 1980 là tác phẩm của họa sĩ nào?", "Họa sĩ Dương Bích Liên", ["Họa sĩ Tô Ngọc Vân", "Họa sĩ Nguyễn Sáng", "Họa sĩ Bùi Xuân Phái"], "Tác phẩm khắc họa phong thái ung dung tự tại của Bác Hồ cưỡi ngựa giữa núi rừng chiến khu.", 2),
        ("Làng gốm Bát Tràng (Gia Lâm, Hà Nội) nằm bên bờ tả ngạn của con sông lớn nào?", "Sông Hồng", ["Sông Đuống", "Sông Cầu", "Sông Đáy"], "Bát Tràng là cái nôi làng nghề gốm sứ truyền thống có lịch sử hơn 700 năm thịnh vượng.", 1),
        ("Nghệ thuật Hát Bội (Tuồng) truyền thống nổi bật với cách trang điểm khuôn mặt như thế nào để thể hiện tính cách nhân vật?", "Vẽ mặt nạ tuồng cách điệu với các gam màu đỏ (trung thần), trắng (gian thần), đen (cương trực)", ["Đeo mặt nạ gỗ", "Để mặt mộc", "Trang điểm nhẹ"], "Màu sắc nét vẽ ước lệ trên khuôn mặt giúp khán giả nhận diện tính cách nhân vật ngay khi bước ra sân khấu.", 1),
        ("Cây cầu Hiền Lương lịch sử bắc qua sông Bến Hải sơn hai màu sơn khác nhau ở hai đầu cầu thể hiện điều gì?", "Sự chia cắt tạm thời hai miền Nam - Bắc trong thời kỳ kháng chiến chống Mỹ", ["Phân chia ranh giới tỉnh", "Màu cờ thể thao", "Chống gỉ sét"], "Cầu Hiền Lương là biểu tượng thiêng liêng về ý chí và khát vọng thống nhất non sông của dân tộc Việt Nam.", 1)
    ],

    # 5. LỊCH SỬ (20 câu)
    "lich-su": [
        ("Kinh đô đầu tiên của nhà nước Âu Lạc dưới thời Thục Phán An Dương Vương đóng tại tòa thành nào?", "Thành Cổ Loa (Đông Anh, Hà Nội)", ["Thành Hoa Lư", "Thành Bạch Hạc", "Thành Tây Đô"], "Thành Cổ Loa hình xoáy ốc là kỳ quan kiến trúc quân sự cổ xưa của người Việt.", 1),
        ("Nữ tướng kiệt xuất nào của cuộc khởi nghĩa Hai Bà Trưng là người lập trang An Biên khai sinh vùng đất Hải Phòng ngày nay?", "Nữ tướng Lê Chân", ["Nữ tướng Bát Nàn", "Nữ tướng Thiều Hoa", "Nữ tướng Thánh Thiên"], "Tượng đài Nữ tướng Lê Chân uy nghiêm tọa lạc tại trung tâm thành phố hoa phượng đỏ Hải Phòng.", 1),
        ("Vị hoàng đế nào đã lập ra nhà nước Vạn Xuân năm 544 đóng đô ở vùng cửa sông Tô Lịch?", "Lý Nam Đế (Lý Bí)", ["Triệu Quang Phục", "Lý Phật Tử", "Phùng Hưng"], "Lý Nam Đế mong muốn giang sơn xã tắc sẽ mãi trường tồn cùng vạn mùa xuân thái bình.", 1),
        ("Ai là người kế tục sự nghiệp của Lý Nam Đế lãnh đạo nghĩa quân đóng căn cứ tại đầm Dạ Trạch đánh tan quân Lương?", "Triệu Quang Phục (Dạ Trạch Vương)", ["Lý Thiên Bảo", "Lý Phật Tử", "Phùng Hưng"], "Dạ Trạch Vương dùng chiến thuật du kích ban ngày ẩn náu trong đầm lau sậy, ban đêm bất ngờ tập kích giặc.", 2),
        ("Vị anh hùng dân tộc nào được nhân dân tôn kính gọi là 'Bố Cái Đại Vương' sau cuộc khởi nghĩa Đường Lâm lật đổ quân Đường?", "Phùng Hưng", ["Mai Thúc Loan", "Khúc Thừa Dụ", "Ngô Quyền"], "Đường Lâm (Sơn Tây, Hà Nội) là mảnh đất địa linh nhân kiệt 'một ấp sinh hai vua' Phùng Hưng và Ngô Quyền.", 1),
        ("Khúc Thừa Dụ đã tận dụng cơ hội nhà Đường suy yếu tự xưng là chức vị gì vào năm 905 giành quyền tự chủ bước đầu cho dân tộc?", "Tiết độ sứ", ["Hoàng đế", "Vương", "Thái thú"], "Khúc Thừa Dụ mở đầu thời kỳ khôi phục nền độc lập tự chủ sau đêm dài nghìn năm Bắc thuộc.", 2),
        ("Trận đánh lịch sử năm 981 của vua Lê Hoàn đã đánh tan đạo thủy quân nhà Tống trên con sông huyền thoại nào?", "Sông Bạch Đằng", ["Sông Như Nguyệt", "Sông Lô", "Sông Cầu"], "Sông Bạch Đằng ba lần ghi dấu chiến công hiển hách đánh tan quân Nam Hán (938), quân Tống (981) và quân Nguyên Mông (1288).", 1),
        ("Năm 1070 vua Lý Thánh Tông cho khởi lập công trình nào để thờ Khổng Tử và các bậc hiền triết Nho học?", "Văn Miếu Thăng Long", ["Quốc Tử Giám", "Chùa Diên Hựu", "Đền Ngọc Sơn"], "Văn Miếu - Quốc Tử Giám là biểu tượng rực rỡ nghìn năm của truyền thống hiếu học tôn sư trọng đạo.", 1),
        ("Ai là vị vua khai sáng triều đại nhà Trần lên ngôi năm 1225 sau khi được Lý Chiêu Hoàng nhường ngôi?", "Trần Thái Tông (Trần Cảnh)", ["Trần Thánh Tông", "Trần Nhân Tông", "Trần Thủ Độ"], "Triều Trần tồn tại vẻ vang 175 năm lập nên hào khí Đông A ba lần đại thắng Mông - Nguyên.", 1),
        ("Hội thề Lũng Nhai lịch sử năm 1416 do Lê Lợi cùng 18 tướng lĩnh tổ chức nhằm mục đích gì?", "Kết nghĩa anh em, thề đồng tâm hiệp lực đánh đuổi giặc Minh cứu nước", ["Chia ruộng đất", "Lập triều đình", "Ký hòa ước"], "Hội thề Lũng Nhai tại Thường Xuân (Thanh Hóa) nhen nhóm ngọn lửa bùng cháy của khởi nghĩa Lam Sơn.", 1),
        ("Vị danh tướng khai quốc triều Hậu Lê nào đã liều mình đóng giả Lê Lợi phá vòng vây cứu chúa tại núi Chí Linh?", "Lê Lai", ["Nguyễn Xí", "Trần Nguyên Hãn", "Đinh Lễ"], "Hành động dũng cảm phi thường của Lê Lai cứu sống chủ tướng đưa phong trào Lam Sơn tới ngày toàn thắng.", 1),
        ("Vị vua nào thời Lê sơ được xem là nhà cải cách hành chính vĩ đại chia cả nước thành 13 đạo thừa tuyên và lập bản đồ quốc gia?", "Lê Thánh Tông", ["Lê Thái Tổ", "Lê Thái Tông", "Lê Nhân Tông"], "Dưới thời vua Lê Thánh Tông Đại Việt trở thành quốc gia hùng mạnh và văn minh bậc nhất Đông Nam Á.", 1),
        ("Trận quyết chiến chiến lược Ngọc Hồi - Đống Đa đại phá 29 vạn quân Mãn Thanh diễn ra vào mùa xuân năm nào?", "Mùa xuân Kỷ Dậu 1789", ["Năm 1788", "Năm 1785", "Năm 1792"], "Đêm mùng 4 rạng sáng mùng 5 Tết Kỷ Dậu, đại quân Quang Trung tiến vào Thăng Long trong tiếng reo hò dậy đất.", 1),
        ("Thành phố Sài Gòn chính thức được đổi tên mang tên Chủ tịch Hồ Chí Minh (Thành phố Hồ Chí Minh) vào năm nào?", "Năm 1976 (tại kỳ họp Quốc hội khóa VI)", ["Năm 1975", "Năm 1977", "Năm 1986"], "Vinh dự lớn lao cho thành phố mang tên Bác Hồ - 'Thành đồng Tổ quốc'.", 1),
        ("Chủ tịch Hồ Chí Minh ra Lời kêu gọi Thi đua ái quốc vào ngày tháng năm nào động viên toàn dân kháng chiến kiến quốc?", "Ngày 11/6/1948", ["Ngày 2/9/1945", "Ngày 19/12/1946", "Ngày 3/2/1950"], "'Thi đua là yêu nước, yêu nước thì phải thi đua, những người thi đua là những người yêu nước nhất'.", 1),
        ("Trận đánh phục kích nổi tiếng nào của quân dân Nam Bộ năm 1965 đã bẻ gãy cuộc hành quân 'Tìm và diệt' đầu tiên của lính thủy đánh bộ Mỹ?", "Chiến thắng Vạn Tường (Quảng Ngãi)", ["Chiến thắng Ấp Bắc", "Chiến thắng Bình Giã", "Chiến thắng Ba Gia"], "Vạn Tường chứng minh quân và dân ta hoàn toàn có khả năng đánh thắng trực diện quân đội viễn chinh Mỹ.", 2),
        ("Nền văn minh cổ đại nào ở châu Á đã phát minh ra giấy viết, la bàn, thuốc súng và kỹ thuật in ấn?", "Văn minh Trung Hoa cổ đại", ["Văn minh Ấn Độ", "Văn minh Lưỡng Hà", "Văn minh Ai Cập"], "Bốn phát minh vĩ đại (Tứ đại phát minh) đóng góp to lớn cho sự phát triển của văn minh nhân loại.", 1),
        ("Trận Waterloo năm 1815 tại Bỉ đã đánh dấu sự thất bại hoàn toàn và chấm dứt quyền lực của hoàng đế nào?", "Hoàng đế Napoleon Bonaparte (Pháp)", ["Vua Louis XIV", "Vua George III", "Sa hoàng Alexander I"], "Napoleon bị bắt lưu đày đến hòn đảo Saint Helena cô quạnh giữa Đại Tây Dương cho đến cuối đời.", 1),
        ("Kênh đào Panama chính thức được trao trả lại toàn bộ quyền quản lý và khai thác cho chính phủ nước Panama vào năm nào?", "Năm 1999 (ngày 31/12/1999)", ["Năm 1977", "Năm 1914", "Năm 1990"], "Panama hoàn toàn làm chủ con đường thủy huyết mạch quốc tế kết nối Thái Bình Dương và Đại Tây Dương.", 2),
        ("Bản Tuyên ngôn Quốc tế Nhân quyền đầu tiên của Đại hội đồng Liên Hợp Quốc được thông qua vào năm nào?", "Năm 1948 (ngày 10/12/1948)", ["Năm 1945", "Năm 1950", "Năm 1954"], "Ngày 10/12 hàng năm được chọn làm Ngày Nhân quyền Quốc tế tôn vinh phẩm giá và tự do của con người.", 1)
    ],

    # 6. ĐỊA LÝ (20 câu)
    "dia-ly": [
        ("Vịnh Hạ Long di sản thiên nhiên thế giới UNESCO với hàng ngàn hòn đảo đá vôi kỳ vĩ thuộc tỉnh nào?", "Quảng Ninh", ["Hải Phòng", "Thái Bình", "Nam Định"], "Vịnh Hạ Long hai lần được UNESCO công nhận về giá trị thẩm mỹ và giá trị địa chất địa mạo.", 1),
        ("Đảo Phú Quốc hòn đảo lớn nhất Việt Nam được mệnh danh là Đảo Ngọc thuộc tỉnh nào miền Tây Nam Bộ?", "Kiên Giang", ["Cà Mau", "An Giang", "Bạc Liêu"], "Phú Quốc nổi tiếng với bãi Sao, bãi Dài, làng chài Hàm Ninh và nước mắm truyền thống.", 1),
        ("Núi Hàm Rồng điểm ngắm toàn cảnh thị xã Sa Pa bồng bềnh mây trắng thơ mộng thuộc tỉnh nào?", "Lào Cai", ["Yên Bái", "Hà Giang", "Lai Châu"], "Núi Hàm Rồng có vườn lan rực rỡ và sân mây nhìn thẳng lên đỉnh Fansipan kiêu hãnh.", 1),
        ("Đèo Khau Phạ con đèo hiểm trở quanh co bậc nhất Tây Bắc uốn lượn nhìn xuống thung lũng Mù Cang Chải thuộc tỉnh nào?", "Yên Bái", ["Lào Cai", "Sơn La", "Hòa Bình"], "Khau Phạ là điểm xuất phát của lễ hội dù lượn 'Bay trên mùa vàng' rực rỡ lúa chín.", 1),
        ("Đèo Thung Khe (Đèo Đá Trắng) quanh năm sương mù bao phủ trắng xóa như tuyết nằm trên quốc lộ 6 thuộc tỉnh nào?", "Hòa Bình", ["Sơn La", "Phú Thọ", "Yên Bái"], "Đèo Thung Khe nối liền huyện Tân Lạc và thung lũng Mai Châu thơ mộng.", 1),
        ("Khu du lịch sinh thái Tràng An quần thể hang động karst kỳ ảo được mệnh danh là 'Hạ Long trên cạn' thuộc tỉnh nào?", "Ninh Bình", ["Thanh Hóa", "Quảng Ninh", "Hà Nam"], "Tràng An là di sản hỗn hợp Văn hóa và Thiên nhiên thế giới đầu tiên của Việt Nam.", 1),
        ("Động Phong Nha hang động nước tuyệt mỹ với dòng sông ngầm dài nhất nằm trong vườn quốc gia nào?", "Vườn quốc gia Phong Nha - Kẻ Bàng (Quảng Bình)", ["Vườn quốc gia Cúc Phương", "Vườn quốc gia Bạch Mã", "Vườn quốc gia Cát Tiên"], "Phong Nha sở hữu 7 cái nhất thế giới về hang động karst kỳ vĩ.", 1),
        ("Bán đảo Sơn Trà được mệnh danh là 'Lá phổi xanh của Đà Nẵng' là vương quốc sinh sống của loài linh trưởng quý hiếm nào?", "Voọc chà vá chân nâu", ["Vượn đen má trắng", "Khỉ vàng", "Cu li nhỏ"], "Voọc chà vá chân nâu với bộ lông năm màu rực rỡ được coi là 'Nữ hoàng linh trưởng'.", 1),
        ("Thánh địa Mỹ Sơn quần thể đền tháp Chămpa cổ kính linh thiêng giữa thung lũng thuộc tỉnh nào?", "Quảng Nam (huyện Duy Xuyên)", ["Đà Nẵng", "Quảng Ngãi", "Bình Định"], "Mỹ Sơn là di sản văn hóa thế giới UNESCO lưu giữ nghệ thuật kiến trúc điêu khắc gạch Chăm độc đáo.", 1),
        ("Cù Lao Chàm khu dự trữ sinh quyển thế giới nổi tiếng với hệ sinh thái rạn san hô hoang sơ thuộc địa bàn nào?", "Thành phố Hội An (Quảng Nam)", ["Thành phố Đà Nẵng", "Tỉnh Quảng Ngãi", "Tỉnh Bình Định"], "Cù Lao Chàm nghiêm cấm sử dụng túi nilon bảo vệ môi trường biển bền vững.", 1),
        ("Vịnh Vĩnh Hy một trong những vịnh biển nguyên sơ đẹp nhất Việt Nam với rạn san hô nhiều màu thuộc tỉnh nào?", "Ninh Thuận", ["Bình Thuận", "Khánh Hòa", "Phú Yên"], "Vịnh Vĩnh Hy nằm nép mình bên Vườn quốc gia Núi Chúa khí hậu nắng ấm quanh năm.", 1),
        ("Quần đảo Côn Đảo gồm 16 hòn đảo nổi tiếng giữa biển Đông thuộc quyền quản lý hành chính của tỉnh nào?", "Bà Rịa - Vũng Tàu", ["Kiên Giang", "Sóc Trăng", "Bến Tre"], "Côn Đảo có bãi biển tuyệt đẹp và vườn quốc gia bảo tồn rùa biển đẻ trứng.", 1),
        ("Vườn quốc gia Mũi Cà Mau khu rừng ngập mặn lớn thứ hai thế giới nằm ở điểm cực nam Tổ quốc thuộc huyện nào?", "Huyện Ngọc Hiển (Cà Mau)", ["Huyện Năm Căn", "Huyện Đầm Dơi", "Huyện Thới Bình"], "Cột mốc tọa độ quốc gia GPS 0001 tại Đất Mũi Cà Mau là điểm đến thiêng liêng của mọi người Việt.", 1),
        ("Rừng U Minh rừng tràm ngập nước đặc trưng đất than bùn phương Nam được chia cắt thành hai vùng U Minh Thượng và U Minh Hạ thuộc hai tỉnh nào?", "Kiên Giang và Cà Mau", ["Cà Mau và Bạc Liêu", "Kiên Giang và An Giang", "Bạc Liêu và Sóc Trăng"], "U Minh Thượng thuộc Kiên Giang và U Minh Hạ thuộc Cà Mau là xứ sở tràm bát ngát.", 1),
        ("Chợ nổi Cái Bè chợ nổi giao thương nông sản nổi tiếng trên sông Tiền nằm ở tỉnh nào miền Tây?", "Tiền Giang", ["Bến Tre", "Vĩnh Long", "Đồng Tháp"], "Chợ nổi Cái Bè nằm tại nơi tiếp giáp giữa ba tỉnh Tiền Giang, Bến Tre và Vĩnh Long.", 1),
        ("Hồ Tơ Nưng miệng núi lửa đã tắt hàng triệu năm phẳng lặng xanh biếc giữa đại ngàn Tây Nguyên thuộc tỉnh nào?", "Gia Lai", ["Kon Tum", "Đắk Lắk", "Đắk Nông"], "Biển Hồ Tơ Nưng được mệnh danh là 'Hạt ngọc Pleiku' cung cấp nước ngọt cho thành phố.", 1),
        ("Hồ Thác Bà một trong những hồ nhân tạo lớn nhất nước ta hình thành khi xây dựng thủy điện Thác Bà trên sông Chảy thuộc tỉnh nào?", "Yên Bái", ["Tuyên Quang", "Lào Cai", "Phú Thọ"], "Hồ Thác Bà có hơn 1.300 đảo lớn nhỏ nhấp nhô được ví như Vịnh Hạ Long trên núi.", 1),
        ("Quốc gia nào trên thế giới có diện tích lãnh thổ lớn nhất hành tinh chiếm 1/8 diện tích đất nổi Trái Đất?", "Liên bang Nga (hơn 17 triệu km2)", ["Canada", "Trung Quốc", "Mỹ"], "Nước Nga trải dài qua 11 múi giờ từ biển Baltic ở châu Âu đến Thái Bình Dương ở châu Á.", 1),
        ("Quốc gia nào ở châu Á có số dân đông nhất thế giới tính đến năm 2023 vượt qua Trung Quốc?", "Cộng hòa Ấn Độ (hơn 1,43 tỷ người)", ["Trung Quốc", "Indonesia", "Pakistan"], "Ấn Độ vươn lên thành quốc gia đông dân nhất hành tinh với cơ cấu dân số trẻ năng động.", 1),
        ("Thủ đô Tokyo trung tâm đô thị đông dân và phát triển kinh tế công nghệ hàng đầu thế giới là thủ đô của nước nào?", "Nhật Bản", ["Hàn Quốc", "Trung Quốc", "Singapore"], "Tokyo là siêu đô thị hiện đại bậc nhất hành tinh kết hợp hài hòa nét văn hóa truyền thống Á Đông.", 1)
    ]
}

def main():
    print("=" * 70)
    print("🏆 CHẠY BỘ NẠP MILESTONE 3 VICTORY: CÁN MỐC TRÊN 2.500 CÂU HỎI!")
    print("=" * 70)

    total_added = 0
    for cat_name, q_list in VICTORY_DATA.items():
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

    print(f"\n🎉 Hoàn thành Milestone 3 Victory! Đã nạp thêm {total_added} câu hỏi mới.")

if __name__ == '__main__':
    main()
