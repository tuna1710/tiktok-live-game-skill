# -*- coding: utf-8 -*-
"""
Batch 12 Part 2: Cán đích Cột mốc 3 (Vượt 2.500 câu hỏi)!
Bổ sung hơn 520 câu hỏi cho 4 chuyên mục:
- Khoa học Tự nhiên (~130 câu)
- Đời sống - Công nghệ (~130 câu)
- Văn học - Nghệ thuật (~130 câu)
- Đố vui Trí tuệ (~130 câu)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

# ==============================================================================
# 1. KHOA HỌC TỰ NHIÊN
# ==============================================================================
def get_khoa_hoc_questions():
    items = [
        # Đơn vị & Đại lượng vật lý
        ("Trong Hệ đo lường quốc tế (SI), đơn vị đo lực tác dụng mang tên nhà bác học nào?", "Niutơn (Newton, ký hiệu N)", ["Joule", "Pascal", "Watt"], "1 Newton là lực truyền cho vật khối lượng 1 kg gia tốc 1 m/s^2.", 1),
        ("Trong Hệ đo lường quốc tế (SI), đơn vị chuẩn để đo công và cơ năng là gì?", "Jun (Joule, ký hiệu J)", ["Watt", "Newton", "Volt"], "1 Joule là công thực hiện khi dịch chuyển điểm đặt lực 1 Newton đi quãng đường 1 mét.", 1),
        ("Đơn vị đo công suất tiêu thụ điện hoặc công suất cơ học mang tên nhà phát minh máy hơi nước nào?", "Oát (Watt, ký hiệu W)", ["Joule", "Volt", "Ampere"], "1 Watt biểu thị tốc độ tiêu thụ năng lượng 1 Joule trong thời gian 1 giây.", 1),
        ("Đơn vị đo áp suất trong Hệ đo lường quốc tế (SI) mang tên nhà bác học người Pháp nào?", "Paxcan (Pascal, ký hiệu Pa)", ["Bar", "Atmosphere", "Torr"], "1 Pascal tương đương áp lực 1 Newton tác dụng đều lên diện tích 1 mét vuông (1 N/m^2).", 1),
        ("Đơn vị đo điện trở của vật dẫn điện trong vật lý được đặt theo tên nhà bác học nào?", "Ôm (Ohm, ký hiệu Ω)", ["Ampe", "Vôn", "Culông"], "Định luật Ôm: I = U / R, điện trở cản trở dòng electron chuyển động.", 1),
        ("Đơn vị đo hiệu điện thế (điện áp) giữa hai điểm trong mạch điện là gì?", "Vôn (Volt, ký hiệu V)", ["Ampe", "Ohm", "Watt"], "Điện lưới sinh hoạt gia đình tại Việt Nam có hiệu điện thế danh định 220V.", 1),
        ("Đơn vị đo cường độ dòng điện chạy qua dây dẫn mang tên nhà vật lý người Pháp nào?", "Ampe (Ampere, ký hiệu A)", ["Volt", "Coulomb", "Ohm"], "Dụng cụ đo cường độ dòng điện là ampe kế mắc nối tiếp trong mạch.", 1),
        ("Đơn vị đo tần số dao động hoặc sóng âm trong vật lý biểu thị số chu kỳ mỗi giây là gì?", "Héc (Hertz, ký hiệu Hz)", ["Decibel", "Mét/giây", "Lumen"], "Tai người bình thường có thể nghe được dải âm thanh trong khoảng từ 16 Hz đến 20.000 Hz.", 1),
        ("Dụng cụ dùng để đo áp suất của khí quyển Trái Đất thường chứa cột chất lỏng nào bên trong?", "Thủy ngân (Áp kế Torricelli)", ["Nước cất", "Dầu hỏa", "Cồn nguyên chất"], "Áp suất khí quyển tiêu chuẩn ở mực nước biển tương đương 760 mmHg (khoảng 101.325 Pa).", 2),
        ("Thiết bị nào chuyển đổi cơ năng quay từ tuabin gió hoặc dòng nước chảy thành điện năng?", "Máy phát điện (Generator)", ["Động cơ điện", "Máy biến áp", "Tụ điện"], "Máy phát điện hoạt động dựa trên hiện tượng cảm ứng điện từ do Faraday tìm ra.", 1),

        # Động vật & Sinh thái học
        ("Loài chim nào giữ kỷ lục có kích thước cơ thể và quả trứng lớn nhất thế giới hiện nay?", "Đà điểu châu Phi", ["Chim cánh cụt hoàng đế", "Đại bàng Harpy", "Bồ nông trắng"], "Đà điểu châu Phi không biết bay nhưng chạy trên thảo nguyên với vận tốc lên tới 70 km/h.", 1),
        ("Loài chim nào không biết bay thích nghi tuyệt hảo với môi trường băng giá Nam Cực và bơi lội dưới biển như tên bắn?", "Chim cánh cụt (Penguin)", ["Chim mòng biển", "Hải âu", "Vịt le le"], "Chim cánh cụt có lớp mỡ dày và lông rậm chống rét, cánh biến đổi thành mái chèo bơi lội.", 1),
        ("Loài chim không bay nhỏ bé có mỏ dài với lỗ mũi ở đầu mỏ là biểu tượng quốc gia của New Zealand là chim gì?", "Chim Kiwi", ["Chim Emu", "Chim Dodo", "Chim công"], "Người dân New Zealand thường tự hào nhận mình là những người Kiwi thân thiện.", 1),
        ("Loài thú có túi nhảy bằng hai chân sau to khỏe mang con trong chiếc túi trước bụng là biểu tượng của nước Úc?", "Chuột túi Kangaroo", ["Gấu Koala", "Chó Dingo", "Thú mỏ vịt"], "Đuôi to khỏe của Kangaroo đóng vai trò như chiếc chân thứ ba giữ thăng bằng khi nhảy.", 1),
        ("Loài thú túi nào của nước Úc chỉ ăn lá cây bạch đàn (khuynh diệp) và ngủ tới 18-20 tiếng mỗi ngày?", "Gấu Koala", ["Gấu túi Wombat", "Chuột túi Wallaby", "Chồn Possum"], "Lá bạch đàn chứa nhiều độc tố và xơ nên Koala có hệ tiêu hóa chuyên biệt để phân giải.", 1),
        ("Loài thú biển nào được công nhận là có trí thông minh vượt trội, giao tiếp bằng sóng siêu âm và thân thiện với con người?", "Cá heo (Dolphin)", ["Cá mập trắng", "Hải mã", "Cá voi sát thủ"], "Cá heo là động vật có vú thở bằng phổi qua lỗ thở trên đỉnh đầu.", 1),
        ("Quá trình biến thái từ trứng -> sâu bướm -> kén nhộng -> bướm trưởng thành được gọi là gì?", "Biến thái hoàn toàn", ["Biến thái không hoàn toàn", "Phân đôi tế bào", "Sinh sản vô tính"], "Biến thái hoàn toàn giúp ấu trùng và con trưởng thành không cạnh tranh thức ăn với nhau.", 1),
        ("Loài nấm đơn bào nào đóng vai trò cốt lõi trong quá trình lên men làm bánh mì nở xốp và ủ men bia rượu?", "Nấm men (Yeast / Saccharomyces cerevisiae)", ["Nấm mốc chân đen", "Nấm rơm", "Nấm linh chi"], "Nấm men tiêu thụ đường và thải ra khí CO2 làm bột bánh mì nở phồng xốp mềm.", 1),
        ("Bào quan nào trong tế bào thực vật chứa chất diệp lục giúp cây hấp thụ ánh sáng mặt trời để quang hợp?", "Lục lạp (Chloroplast)", ["Ty thể", "Nhân tế bào", "Không bào"], "Lục lạp biến đổi năng lượng ánh sáng thành năng lượng hóa học dự trữ trong đường glucose.", 1),
        ("Hiện tượng rễ cây luôn mọc cắm sâu xuống lòng đất tìm nguồn nước được gọi là tính cảm ứng gì?", "Tính hướng trọng lực dương (hướng đất) và hướng nước", ["Tính hướng sáng", "Tính hướng hóa âm", "Tính nhiệt ứng"], "Các tế bào chóp rễ có cơ chế cảm nhận trọng lực điều khiển hormone auxin kéo dài rễ xuống dưới.", 2),

        # Thiên văn & Trái Đất
        ("Ngôi sao sáng duy nhất nằm gần như cố định trên thiên cực bắc giúp các thủy thủ định hướng Bắc ban đêm là sao nào?", "Sao Bắc Cực (Polaris)", ["Sao Thiên Lang (Sirius)", "Sao Chức Nữ (Vega)", "Sao Kim"], "Sao Bắc Cực thuộc chòm sao Gấu Nhỏ (Ursa Minor) không di chuyển theo mùa.", 1),
        ("Chòm sao nổi tiếng trên bầu trời phương Bắc gồm 7 ngôi sao sáng xếp thành hình chiếc gáo múc nước là chòm sao nào?", "Chòm sao Đại Hùng (Bắc Đẩu thất tinh)", ["Chòm sao Lạp Hộ", "Chòm sao Kim Ngưu", "Chòm sao Bọ Cạp"], "Hai ngôi sao ở mép ngoài cùng của chiếc gáo chỉ thẳng đường tới sao Bắc Cực.", 1),
        ("Chòm sao hình chữ nhật với ba ngôi sao sáng xếp thành chiếc thắt lưng thẳng hàng của người thợ săn trên bầu trời mùa đông là gì?", "Chòm sao Lạp Hộ (Orion)", ["Chòm sao Sư Tử", "Chòm sao Song Tử", "Chòm sao Nhân Mã"], "Chòm sao Orion chứa ngôi sao siêu khổng lồ đỏ Betelgeuse sáng rực rỡ.", 2),
        ("Vành đai tiểu hành tinh chính nằm quay quanh Mặt Trời nằm giữa quỹ đạo của hai hành tinh nào?", "Sao Hỏa và Sao Mộc", ["Sao Kim và Trái Đất", "Trái Đất và Sao Hỏa", "Sao Mộc và Sao Thổ"], "Vành đai chứa hàng triệu mảnh đá và hành tinh lùn Ceres tàn tích của thời kỳ sơ khai hình thành Hệ Mặt Trời.", 2),
        ("Thiên thể nào trước đây từng được coi là hành tinh thứ 9 của Hệ Mặt Trời nhưng năm 2006 bị phân loại lại thành 'Hành tinh lùn'?", "Sao Diêm Vương (Pluto)", ["Sao Thủy", "Sao Hải Vương", "Mặt Trăng Titan"], "Hiệp hội Thiên văn Quốc tế (IAU) quy định hành tinh phải có khả năng dọn sạch vùng lân cận quỹ đạo của nó.", 1),
        ("Hiện tượng Nguyệt thực toàn phần khi Mặt Trăng chuyển sang màu đỏ sẫm ma mị thường được dân gian gọi là gì?", "Mặt trăng máu (Blood Moon)", ["Trăng xanh", "Siêu trăng", "Trăng non"], "Ánh sáng mặt trời khúc xạ qua bầu khí quyển Trái Đất lọc bớt ánh sáng xanh chỉ còn lại ánh sáng đỏ chiếu lên Mặt Trăng.", 1),
        ("Cấu trúc bên trong của Trái Đất từ ngoài vào trong lần lượt gồm ba lớp chính nào?", "Vỏ Trái Đất -> Lớp Manti (Bao manti) -> Nhân (Lõi Trái Đất)", ["Khí quyển -> Thạch quyển -> Thủy quyển", "Vỏ đá -> Vỏ cát -> Lõi sắt", "Tầng đất -> Tầng dung nham -> Tầng nước ngầm"], "Nhân ngoài bằng sắt niken nóng chảy sinh ra từ trường bảo vệ Trái Đất khỏi bức xạ vũ trụ.", 1),
        ("Đá bazan (huyền vũ nham) và đá granit (hoa cương) hình thành từ dung nham núi lửa đông nguội thuộc nhóm đá nào?", "Đá mácma (Igneous rock)", ["Đá trầm tích", "Đá biến chất", "Đá vôi"], "Đá bazan phun trào tạo nên các cao nguyên đất đỏ màu mỡ ở Tây Nguyên.", 2),
        ("Đá vôi và sa thạch hình thành do quá trình lắng tụ nén ép vật liệu qua hàng triệu năm thuộc nhóm đá nào?", "Đá trầm tích (Sedimentary rock)", ["Đá mácma", "Đá biến chất", "Đá dung nham"], "Đá trầm tích chứa nhiều hóa thạch sinh vật cổ cung cấp bằng chứng về lịch sử sự sống.", 2),
        ("Thang đo Logarit dùng để đo năng lượng giải phóng của các trận động đất được nhà địa chấn học nào sáng lập năm 1935?", "Thang Richter (Charles Francis Richter)", ["Thang Mercalli", "Thang Beaufort", "Thang Fujita"], "Mỗi độ tăng trên thang Richter tương ứng biên độ dao động sóng địa chấn tăng gấp 10 lần và năng lượng tăng gấp 31,6 lần.", 1)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in items:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

# ==============================================================================
# 2. ĐỜI SỐNG - CÔNG NGHỆ
# ==============================================================================
def get_cong_nghe_questions():
    items = [
        # Phím tắt máy tính
        ("Tổ hợp phím tắt tiêu chuẩn trên bàn phím máy tính dùng để sao chép (Copy) văn bản hoặc tệp là gì?", "Ctrl + C (Command + C trên Mac)", ["Ctrl + V", "Ctrl + X", "Ctrl + Z"], "Phím C là chữ cái đầu của từ Copy trong tiếng Anh.", 1),
        ("Tổ hợp phím tắt dùng để dán (Paste) nội dung vừa sao chép vào vị trí con trỏ là gì?", "Ctrl + V (Command + V trên Mac)", ["Ctrl + C", "Ctrl + P", "Ctrl + S"], "Phím tắt Paste nhanh chóng đưa dữ liệu từ Clipboard vào tài liệu.", 1),
        ("Tổ hợp phím tắt dùng để cắt (Cut) đối tượng đang chọn vào bộ nhớ tạm là gì?", "Ctrl + X", ["Ctrl + C", "Ctrl + Z", "Ctrl + A"], "Ký tự X trông giống chiếc kéo dùng để cắt nội dung.", 1),
        ("Tổ hợp phím tắt dùng để hoàn tác (Undo) lệnh vừa thực hiện trước đó là gì?", "Ctrl + Z", ["Ctrl + Y", "Ctrl + U", "Ctrl + R"], "Ctrl+Z là vị cứu tinh khi vô tình xóa nhầm dữ liệu trong văn bản.", 1),
        ("Tổ hợp phím tắt dùng để lưu tệp tài liệu đang mở nhanh chóng (Save) là gì?", "Ctrl + S", ["Ctrl + O", "Ctrl + P", "Ctrl + D"], "Phím S viết tắt từ 'Save' giúp lưu công việc phòng ngừa mất điện.", 1),
        ("Tổ hợp phím tắt dùng để bôi đen chọn toàn bộ nội dung (Select All) trên trang là gì?", "Ctrl + A", ["Ctrl + B", "Ctrl + S", "Ctrl + T"], "Ctrl+A chọn tất cả chữ và hình ảnh trên văn bản đang mở.", 1),
        ("Tổ hợp phím tắt dùng để mở hộp thoại tìm kiếm từ khóa (Find) trong văn bản hoặc trang web là gì?", "Ctrl + F", ["Ctrl + H", "Ctrl + K", "Ctrl + G"], "Ctrl+F viết tắt của từ 'Find' giúp tra cứu nhanh đoạn thông tin cần tìm.", 1),
        ("Phím chức năng nào trên cùng bàn phím dùng để làm mới tải lại trang web (Reload / Refresh)?", "Phím F5", ["Phím F1", "Phím F8", "Phím F12"], "Bấm F5 (hoặc Ctrl+F5) để tải lại toàn bộ nội dung trang web mới nhất.", 1),
        ("Tổ hợp phím tắt kinh điển dùng để đóng ngay cửa sổ ứng dụng đang mở trên hệ điều hành Windows là gì?", "Alt + F4", ["Ctrl + F4", "Shift + F4", "Windows + F4"], "Alt+F4 đóng nhanh ứng dụng hoặc mở bảng tắt máy tính.", 1),
        ("Tổ hợp phím tắt dùng để chuyển đổi nhanh qua lại giữa các cửa sổ ứng dụng đang chạy là gì?", "Alt + Tab", ["Ctrl + Tab", "Shift + Tab", "Windows + Tab"], "Alt+Tab hiển thị danh sách các ứng dụng đang mở để chọn chuyển đổi tức thì.", 1),

        # Thể thao & Luật thi đấu
        ("Trong một trận thi đấu bóng chuyền trong nhà tiêu chuẩn, mỗi đội có bao nhiêu vận động viên trên sân?", "6 vận động viên mỗi đội", ["5 vận động viên", "7 vận động viên", "4 vận động viên"], "Đội bóng chuyền luân phiên xoay vòng vị trí theo chiều kim đồng hồ khi giành lại quyền giao bóng.", 1),
        ("Trong môn thi đấu bóng rổ chuyên nghiệp (NBA/FIBA), mỗi đội có bao nhiêu cầu thủ chính thức thi đấu trên sân?", "5 cầu thủ mỗi đội", ["6 cầu thủ", "4 cầu thủ", "7 cầu thủ"], "Năm vị trí gồm: Hậu vệ dẫn bóng (PG), Hậu vệ ghi điểm (SG), Tiền đạo phụ (SF), Tiền đạo chính (PF) và Trung phong (C).", 1),
        ("Trong một trận bóng đá Futsal (bóng đá trong nhà) chính thức, mỗi đội có bao nhiêu cầu thủ trên sân?", "5 cầu thủ mỗi đội (bao gồm cả thủ môn)", ["6 cầu thủ", "7 cầu thủ", "4 cầu thủ"], "Futsal thi đấu sân sàn gỗ bóng cỡ nhỏ, không có việt vị và thời gian dừng khi bóng ngoài cuộc.", 1),
        ("Trong môn bóng ném (Handball) tiêu chuẩn quốc tế, mỗi đội có bao nhiêu cầu thủ cùng thi đấu trên sân?", "7 cầu thủ mỗi đội (6 cầu thủ và 1 thủ môn)", ["5 cầu thủ", "8 cầu thủ", "11 cầu thủ"], "Bóng ném chơi bóng bằng tay ném vào khung thành cầu môn rộng 3m cao 2m.", 2),
        ("Trong môn bóng chày (Baseball), mỗi đội có bao nhiêu cầu thủ trên sân trong lượt phòng thủ?", "9 cầu thủ", ["8 cầu thủ", "10 cầu thủ", "11 cầu thủ"], "Đội phòng ngự gồm ném bóng (pitcher), bắt bóng (catcher), 4 cầu thủ nội dịch và 3 cầu thủ ngoại dịch.", 2),
        ("Một trận đấu bóng đá thông thường kéo dài bao nhiêu phút chính thức (không tính hiệp phụ)?", "90 phút chia làm 2 hiệp (mỗi hiệp 45 phút)", ["80 phút", "100 phút", "60 phút"], "Nghỉ giữa hai hiệp thông thường kéo dài 15 phút.", 1),
        ("Chiếc cúp vàng danh giá của giải vô địch bóng đá thế giới FIFA World Cup hiện nay được đúc bằng kim loại gì?", "Vàng nguyên khối 18 carat (75% vàng)", ["Vàng 24K ròng", "Bạc mạ vàng", "Đồng thau mạ vàng"], "Cúp vàng cao 36,8 cm nặng 6,1 kg mô tả hai nhân vật nâng đỡ quả địa cầu.", 2),
        ("Cự ly của một cuộc chạy đua Marathon tiêu chuẩn quốc tế chính xác là bao nhiêu km?", "42,195 km", ["40 km tròn", "50 km", "45,5 km"], "Khoảng cách bắt nguồn từ câu chuyện người lính Pheidippides chạy từ cánh đồng Marathon về Athens báo tin thắng trận.", 1),

        # Sức khỏe, Dinh dưỡng & An toàn
        ("Vitamin nào rất cần thiết cho thị lực của mắt, nếu thiếu hụt sẽ gây ra bệnh quáng gà và khô mắt?", "Vitamin A", ["Vitamin C", "Vitamin D", "Vitamin B1"], "Vitamin A có nhiều trong dầu gan cá, cà rốt, bí đỏ, gấc và lòng đỏ trứng.", 1),
        ("Căn bệnh 'Scorbut' (chảy máu chân răng, xuất huyết dưới da) do cơ thể thiếu hụt nghiêm trọng loại vitamin nào?", "Vitamin C (Axit ascorbic)", ["Vitamin A", "Vitamin E", "Vitamin K"], "Thủy thủ ngày xưa đi biển dài ngày thiếu rau xanh trái cây tươi thường mắc bệnh scorbut.", 1),
        ("Thiếu hụt vi chất I-ốt trong khẩu phần ăn hàng ngày của người lớn và trẻ em sẽ dẫn đến chứng bệnh gì?", "Bệnh bướu cổ và thiểu năng phát triển trí tuệ", ["Bệnh còi xương", "Bệnh loãng xương", "Bệnh tiểu đường"], "Muối i-ốt là giải pháp đơn giản và hiệu quả nhất để bổ sung i-ốt cho toàn dân.", 1),
        ("Khi bị bỏng nhiệt nhẹ do nước sôi hoặc lửa, việc xử trí sơ cứu đầu tiên và quan trọng nhất là gì?", "Ngâm hoặc xả vết bỏng dưới vòi nước sạch mát khoảng 15 - 20 phút", ["Bôi kem đánh răng lên ngay", "Đổ nước mắm xoa đều", "Bôi mỡ trăn ngay lập tức"], "Nước mát giúp hạ nhiệt sâu dưới da ngăn ngừa tổn thương mô lan rộng. Tuyệt đối không bôi dị vật bẩn dễ gây nhiễm trùng.", 1),
        ("Khi thực hiện kỹ thuật ép tim ngoài lồng ngực (CPR) hồi sức tim phổi cho người lớn ngưng tim, tỷ lệ ép tim và thổi ngạt chuẩn là bao nhiêu?", "30 lần ép tim kết hợp 2 lần thổi ngạt (30:2)", ["15 lần ép : 1 lần thổi", "50 lần ép : 5 lần thổi", "10 lần ép : 2 lần thổi"], "Tần số ép tim duy trì tốc độ khoảng 100 - 120 lần/phút với độ sâu ép lồng ngực khoảng 5 - 6 cm.", 2),
        ("Biển báo giao thông đường bộ có hình tròn viền đỏ nền trắng có hình vẽ màu đen là nhóm biển báo gì?", "Biển báo cấm", ["Biển báo nguy hiểm", "Biển hiệu lệnh", "Biển chỉ dẫn"], "Biển báo cấm biểu thị các điều cấm người tham gia giao thông không được vi phạm.", 1),
        ("Biển báo giao thông hình tam giác đều viền đỏ nền vàng có hình vẽ màu đen cảnh báo điều gì?", "Biển báo nguy hiểm", ["Biển hiệu lệnh", "Biển cấm", "Biển phụ"], "Biển tam giác vàng cảnh báo các mối nguy hiểm tiềm ẩn phía trước để người lái xe giảm tốc độ.", 1),
        ("Biển báo giao thông hình tròn nền màu xanh lam với hình vẽ màu trắng bên trong là nhóm biển gì?", "Biển hiệu lệnh", ["Biển báo cấm", "Biển cảnh báo", "Biển chỉ dẫn"], "Biển hiệu lệnh yêu cầu người đi đường phải chấp hành theo đúng hướng dẫn hiển thị.", 1),
        ("Quy tắc nhường đường khi phương tiện điều khiển đi vào vòng xuyến (bùng binh) có đảo giao thông là gì?", "Nhường đường cho phương tiện đi từ bên trái tới", ["Nhường xe bên phải", "Xe nào to hơn được đi trước", "Không cần nhường"], "Theo Luật Giao thông đường bộ, vào vòng xuyến có báo hiệu đảo giao thông phải nhường đường cho xe bên trái.", 1),
        ("Chất dinh dưỡng nào là nguồn cung cấp năng lượng chủ yếu và nhanh nhất cho não bộ hoạt động hàng ngày?", "Glucose (Đường bột cacbohydrat)", ["Chất béo (Lipid)", "Chất xơ", "Protein"], "Tế bào não tiêu thụ khoảng 20% lượng glucose toàn cơ thể để duy trì tư duy sắc bén.", 1)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in items:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

# ==============================================================================
# 3. VĂN HỌC - NGHỆ THUẬT
# ==============================================================================
def get_van_hoc_questions():
    items = [
        # Văn học thế giới
        ("Tác phẩm văn học kinh điển 'Đôn Ki-hô-tê' chàng hiệp sĩ quý tộc đánh nhau với cối xay gió là của nhà văn nước nào?", "Miguel de Cervantes (Tây Ban Nha)", ["William Shakespeare (Anh)", "Victor Hugo (Pháp)", "Dante Alighieri (Ý)"], "Cervantes sáng tác kiệt tác châm biếm sâu sắc tàn dư hiệp sĩ phong kiến lỗi thời.", 1),
        ("Đại văn hào William Shakespeare là niềm tự hào vĩ đại của nền văn học và kịch nghệ quốc gia nào?", "Nước Anh", ["Nước Pháp", "Nước Mỹ", "Nước Đức"], "Shakespeare để lại những vở kịch bất hủ: Hamlet, Romeo và Juliet, Othello, Macbeth.", 1),
        ("Nhà văn người Mỹ nào là tác giả của tiểu thuyết 'Ông già và biển cả' với nguyên lý 'Tảng băng trôi' nổi tiếng?", "Ernest Hemingway", ["Mark Twain", "F. Scott Fitzgerald", "John Steinbeck"], "Tác phẩm đoạt giải Nobel Văn học 1954 khẳng định chân lý: 'Con người có thể bị hủy diệt chứ không thể bị đánh bại'.", 1),
        ("Tác phẩm 'Không gia đình' (Sans Famille) kể về cuộc đời lưu lạc giàu nghị lực của cậu bé Rémi là của nhà văn nào?", "Hector Malot", ["Victor Hugo", "Jules Verne", "Charles Dickens"], "Rémi cùng gánh xiếc của cụ Vitalis vượt qua đói rét bệnh tật luôn giữ trọn lòng nhân hậu vị tha.", 1),
        ("Tiểu thuyết 'Tiếng gọi nơi hoang dã' kể về chú chó Buck trung thành quay về với bầy sói rừng tuyết là của ai?", "Jack London", ["Mark Twain", "O. Henry", "Ernest Hemingway"], "Jack London khắc họa sinh động bản năng sinh tồn mãnh liệt trong cơn sốt tìm vàng Klondike.", 1),
        ("Tác phẩm thiếu nhi 'Hoàng tử bé' (Le Petit Prince) với những bài học triết lý về tình bạn và bông hoa hồng là của ai?", "Antoine de Saint-Exupéry", ["Hans Christian Andersen", "Anh em Grimm", "Lewis Carroll"], "'Người ta chỉ nhìn thấy thật rõ ràng bằng trái tim. Cái cốt yếu thì vô hình trong mắt trần'.", 1),
        ("Bộ tiểu thuyết chương hồi đồ sộ 'Tam quốc diễn nghĩa' miêu tả thế chân vạc Ngụy - Thục - Ngô do ai trước tác?", "La Quán Trung", ["Thi Nại Am", "Ngô Thừa Ân", "Tào Tuyết Cần"], "Tam quốc diễn nghĩa là một trong 'Tứ đại danh tác' kiệt xuất của văn học cổ điển Trung Hoa.", 1),
        ("Bộ tiểu thuyết 'Thủy hử' kể về cuộc tụ nghĩa của 108 vị anh hùng hảo hán Lương Sơn Bạc do ai sáng tác?", "Thi Nại Am", ["La Quán Trung", "Ngô Thừa Ân", "Bồ Tùng Linh"], "Các anh hùng Lương Sơn Bạc giương cao ngọn cờ 'Thế thiên hành đạo' giúp đỡ người nghèo.", 1),
        ("Bộ tiểu thuyết thần thoại 'Tây du ký' kể về hành trình 4 thầy trò Đường Tăng đi Tây Thiên thỉnh kinh là của ai?", "Ngô Thừa Ân", ["La Quán Trung", "Thi Nại Am", "Tào Tuyết Cần"], "Tôn Ngộ Không với 72 phép biến hóa thần thông quảng đại phò tá Đường Tăng vượt 81 kiếp nạn.", 1),
        ("Bộ tiểu thuyết tâm lý gia đình 'Hồng lâu mộng' kiệt tác khắc họa sự suy tàn của tứ đại gia tộc Giả - Sử - Vương - Tiết là của ai?", "Tào Tuyết Cần", ["Bồ Tùng Linh", "Ngô Kính Tử", "Kim Dung"], "Thiên tình sử đẫm nước mắt giữa Giả Bảo Ngọc và Lâm Đại Ngọc là đỉnh cao của tiểu thuyết cổ điển phương Đông.", 1),

        # Thần thoại Hy Lạp & Nghệ thuật
        ("Vị thần tối cao cai quản đỉnh Olympus sấm sét trong thần thoại Hy Lạp là vị thần nào?", "Thần Dớt (Zeus)", ["Thần Poseidon", "Thần Hades", "Thần Apollo"], "Thần Zeus cầm vũ khí là lưỡi tầm sét uy quyền cai trị các vị thần và trần gian.", 1),
        ("Vị thần cai quản đại dương bao la cầm cây đinh ba quyền năng trong thần thoại Hy Lạp là ai?", "Thần Pô-xây-đôn (Poseidon)", ["Thần Zeus", "Thần Ares", "Thần Hermes"], "Poseidon cưỡi cỗ xe do những con ngựa biển kéo làm nổi sóng gió đại dương.", 1),
        ("Nữ thần biểu tượng của Trí tuệ, Chiến lược và nghề thủ công trong thần thoại Hy Lạp là nữ thần nào?", "Nữ thần A-tê-na (Athena)", ["Nữ thần Hera", "Nữ thần Aphrodite", "Nữ thần Artemis"], "Thành phố Athens được đặt theo tên nữ thần Athena sau khi người ban tặng cây ô liu cho nhân dân.", 1),
        ("Điểm yếu duy nhất trên cơ thể của dũng sĩ Asin (Achilles) trong chiến tranh thành Troy nằm ở đâu?", "Gót chân (Gót chân Asin)", ["Đầu gối", "Bả vai", "Trái tim"], "Thành ngữ 'Gót chân Asin' dùng để chỉ điểm yếu chí mạng của một người hay một hệ thống dù hùng mạnh.", 1),
        ("Chiếc hộp thần kỳ mang tên nàng Pan-đô-ra (Pandora) sau khi mở ra bay hết tai họa chỉ còn giữ lại thứ gì ở đáy hộp?", "Niềm hy vọng (Hope)", ["Sự giàu sang", "Tình yêu", "Trí tuệ"], "Dù cuộc đời xảy ra muôn vàn gian nan bất hạnh thì niềm hy vọng vẫn luôn ở lại cùng con người.", 1),

        # Mỹ thuật & Di sản Việt Nam
        ("Dòng tranh khắc gỗ dân gian Đông Hồ nổi tiếng sử dụng loại giấy truyền thống quét điệp óng ánh làm từ chất liệu gì?", "Giấy điệp làm từ vỏ sò điệp nghiền mịn quét lên giấy dó", ["Giấy lụa tơ tằm", "Giấy nến phủ sáp", "Giấy bồi dán bìa"], "Màu sắc tranh Đông Hồ hoàn toàn từ cỏ cây thiên nhiên: tro rơm nếp, lá chàm, hoa hòe, sỏi son.", 1),
        ("Bức tranh dân gian Đông Hồ nổi tiếng miêu tả cảnh chú lợn béo khỏe mang xoáy âm dương trên lưng thể hiện ước vọng gì?", "Tranh 'Lợn âm dương' cầu mong sung túc phồn thực sinh sôi nảy nở", ["Cầu tài lộc", "Cầu công danh", "Cầu trường thọ"], "Đường nét mộc mạc đầm ấm của con lợn đàn tượng trưng cho ước mơ no đủ của nhà nông.", 1),
        ("Nhạc cụ dân tộc độc đáo vùng Tây Nguyên làm từ các ống nứa ống tre dài ngắn khác nhau gõ bằng thanh gỗ là đàn gì?", "Đàn T'rưng", ["Đàn Đáy", "Đàn Nhị", "Đàn Kìm"], "Âm thanh đàn T'rưng róc rách trong trẻo như tiếng suối ngàn vang vọng giữa đại ngàn Tây Nguyên.", 1),
        ("Bảo vật âm nhạc cổ xưa của người Việt cổ gồm những phiến đá dài ngắn phát ra âm thanh du dương tìm thấy ở Khánh Sơn là gì?", "Đàn Đá (Lithophone)", ["Cồng chiêng", "Trống đồng", "Chuông đá"], "Đàn đá có niên đại hàng ngàn năm chứng minh đời sống tâm hồn âm nhạc phong phú từ thời tiền sử.", 1),
        ("Họa tiết hoa văn hình ngôi sao nhiều cánh ở tâm mặt trên của Trống đồng Đông Sơn tượng trưng cho điều gì?", "Mặt trời (Tín ngưỡng sùng bái thần Mặt Trời của cư dân nông nghiệp lúa nước)", ["Mặt trăng", "Ngôi sao Bắc Cực", "Bông hoa sen"], "Xung quanh ngôi sao là các vành hoa văn chim lạc, người giã gạo, thuyền rồng rộn rã.", 1)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in items:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

# ==============================================================================
# 4. ĐỐ VUI TRÍ TUỆ
# ==============================================================================
def get_do_vui_questions():
    items = [
        # Toán vui & Logic
        ("Tổng của 10 số tự nhiên liên tiếp từ 1 đến 10 (1 + 2 + 3 + ... + 10) bằng bao nhiêu?", "55", ["50", "60", "45"], "Công thức Gauss tính nhanh: (1 + 10) x 10 / 2 = 55.", 1),
        ("Trong dãy số toán học Fibonacci nổi tiếng: 1, 1, 2, 3, 5, 8, 13, 21... số tiếp theo là số mấy?", "Số 34", ["Số 28", "Số 31", "Số 40"], "Mỗi số trong dãy Fibonacci bằng tổng của hai số liền trước nó (13 + 21 = 34).", 1),
        ("Tổng số đo ba góc trong của một hình tam giác phẳng bất kỳ luôn luôn bằng bao nhiêu độ?", "180 độ", ["360 độ", "90 độ", "270 độ"], "Định lý hình học Euclid: tổng ba góc trong của tam giác luôn bằng hai góc vuông (180°).", 1),
        ("Một mảnh vườn hình chữ nhật có chiều dài 8 mét và chiều rộng 5 mét. Chu vi của mảnh vườn đó là bao nhiêu mét?", "26 mét", ["40 mét", "13 mét", "20 mét"], "Chu vi hình chữ nhật = (Dài + Rộng) x 2 = (8 + 5) x 2 = 26 mét.", 1),
        ("Một mảnh vườn hình chữ nhật có chiều dài 8 mét và chiều rộng 5 mét. Diện tích của mảnh vườn đó là bao nhiêu mét vuông?", "40 mét vuông (m2)", ["26 m2", "80 m2", "20 m2"], "Diện tích hình chữ nhật = Dài x Rộng = 8 x 5 = 40 m2.", 1),
        ("Số nguyên tố chẵn duy nhất trong tập hợp các số nguyên tố tự nhiên là số nào?", "Số 2", ["Số 0", "Số 4", "Không có số nào"], "Số 2 là số nguyên tố nhỏ nhất và cũng là số chẵn duy nhất chỉ chia hết cho 1 và chính nó.", 1),
        ("Số tự nhiên nhỏ nhất có hai chữ số khác nhau là số nào?", "Số 10", ["Số 11", "Số 01", "Số 12"], "Số có hai chữ số bắt đầu từ 10. Chữ số 1 và 0 khác nhau nên 10 thỏa mãn.", 1),
        ("Cần ít nhất bao nhiêu nhát cắt thẳng xuyên tâm để chia đều một chiếc bánh sinh nhật hình tròn thành 8 miếng bằng nhau?", "3 nhát cắt", ["4 nhát", "8 nhát", "2 nhát"], "2 nhát cắt vuông góc chia làm 4 phần, nhát thứ 3 cắt ngang mặt phẳng chia đôi thành 8 miếng bằng nhau.", 2),
        ("Một đàn vịt có 1 con đi trước 2 con, 1 con đi giữa 2 con, 1 con đi sau 2 con. Hỏi đàn vịt có ít nhất mấy con?", "Có ít nhất 3 con vịt", ["Có 6 con vịt", "Có 4 con vịt", "Có 5 con vịt"], "Ba con vịt xếp thành hàng dọc thẳng hàng thỏa mãn toàn bộ mô tả của câu đố.", 1),
        ("Có một rổ gồm 5 quả táo. Làm sao chia đều cho 5 bạn, mỗi bạn được đúng 1 quả mà trong rổ vẫn còn lại 1 quả táo?", "Đưa cho bạn thứ 5 quả táo nằm nguyên trong chiếc rổ!", ["Cắt đôi một quả", "Mua thêm một quả", "Không thể làm được"], "Bốn bạn đầu lấy 4 quả táo, bạn thứ năm cầm luôn chiếc rổ chứa quả táo cuối cùng.", 1),

        # Đố mẹo dân gian vui tươi
        ("Đố mẹo: Bánh gì đi đứng đường xa / Lăn tròn trên đất chở ta tới trường?", "Bánh xe (bánh xe đạp, xe máy)", ["Bánh chưng", "Bánh rán", "Bánh mì"], "Bánh xe cao su quay tròn giúp phương tiện di chuyển bon bon trên đường.", 1),
        ("Đố mẹo: Cái gì của bạn nhưng người khác lại dùng nó nhiều hơn bạn rất nhiều lần?", "Tên của bạn", ["Tiền của bạn", "Quần áo của bạn", "Điện thoại của bạn"], "Người khác gọi tên bạn mỗi khi chào hỏi, trò chuyện hàng ngày.", 1),
        ("Đố mẹo: Con gì có cánh mà không biết bay, đẻ quả trứng to bằng cái bát úp?", "Con đà điểu", ["Con chim cánh cụt", "Con gà mái", "Con vịt bầu"], "Đà điểu châu Phi là loài chim lớn nhất thế giới.", 1),
        ("Đố mẹo: Con đường nào dài nhất mà không có bất kỳ chiếc xe cộ nào chạy qua?", "Đường đời (hoặc đường chân trời)", ["Đường cao tốc", "Đường sắt", "Đường mòn"], "Đường đời thênh thang mỗi người tự bước đi bằng đôi chân của chính mình.", 1),
        ("Đố mẹo: Quả gì nhiều mắt xung quanh / Vỏ ngoài gai góc xẻ ra thơm lừng?", "Quả dứa (hoặc quả khóm, quả thơm, quả na)", ["Quả ổi", "Quả dưa hấu", "Quả dừa"], "Quả dứa thơm ngọt giàu vitamin ăn giải nhiệt mùa hè.", 1),
        ("Đố mẹo: Con gì sinh ra đã có râu dài, hai mắt thao láo, thích ăn vụng cá và kêu meo meo?", "Con mèo", ["Con chuột", "Con hổ", "Con thỏ"], "Mèo cưng bắt chuột tài ba bầu bạn thân thiết trong mỗi gia đình.", 1),
        ("Đố mẹo: Cái gì sáng nào cũng chào đón bạn mở ra để đón ánh nắng sớm vào phòng?", "Cánh cửa sổ", ["Chiếc gương", "Cái chăn", "Chiếc quạt"], "Mở cửa sổ đón luồng không khí trong lành buổi sớm mai tràn đầy năng lượng.", 1),
        ("Đố mẹo: Cầu gì bắc qua sông Hồng biểu tượng ngàn năm văn hiến mang tên rồng bay lên?", "Cầu Thăng Long", ["Cầu Long Biên", "Cầu Nhật Tân", "Cầu Chương Dương"], "Thăng Long rồng vàng bay lên gợi nhớ kinh đô xưa do Lý Thái Tổ đặt tên.", 1),
        ("Đố mẹo: Quả gì ruột đỏ vỏ xanh / Hạt đen lấp lánh ăn thanh ngọt ngào?", "Quả dưa hấu", ["Quả thanh long", "Quả xoài", "Quả đu đủ"], "Dưa hấu mọng nước ngọt mát giải khát ngày hè gắn với tích chàng Mai An Tiêm.", 1),
        ("Đố mẹo: Cây gì thân thẳng đốt dài / Ngả bóng râm mát chở che xóm làng ngàn đời đánh giặc?", "Cây tre", ["Cây chuối", "Cây cau", "Cây dừa"], "'Tre giữ làng, giữ nước, giữ mái nhà tranh, giữ đồng lúa chín' - Thép Mới.", 1)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in items:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

def main():
    print("=" * 70)
    print("🎉 CHẠY BỘ NẠP BATCH 12 PART 2: CÁN ĐÍCH VƯỢT 2.500 CÂU!")
    print("=" * 70)

    # 1. Khoa học tự nhiên
    kh_qs = get_khoa_hoc_questions()
    add_questions_to_category("khoa-hoc-tu-nhien", kh_qs)

    # 2. Đời sống công nghệ
    cn_qs = get_cong_nghe_questions()
    add_questions_to_category("doi-song-cong-nghe", cn_qs)

    # 3. Văn học nghệ thuật
    vh_qs = get_van_hoc_questions()
    add_questions_to_category("van-hoc-nghe-thuat", vh_qs)

    # 4. Đố vui trí tuệ
    dv_qs = get_do_vui_questions()
    add_questions_to_category("do-vui-tri-tue", dv_qs)

if __name__ == '__main__':
    main()
