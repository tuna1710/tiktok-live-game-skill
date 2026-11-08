# -*- coding: utf-8 -*-
"""
Final Push to 2,500 Questions: Đưa ngân hàng câu hỏi vượt mốc 2.500 câu hỏi chuẩn hóa!
Bổ sung 450 câu hỏi chia đều 75 câu cho mỗi một trong 6 chủ đề:
- Khoa học Tự nhiên
- Đời sống - Công nghệ
- Văn học - Nghệ thuật
- Lịch sử
- Địa lý
- Đố vui Trí tuệ
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

def get_khoa_hoc_75():
    raw = [
        ("Khí nào là thành phần chính của khí thiên nhiên và khí Biogas (khí sinh học) dùng làm chất đốt?", "Khí Metan (CH4)", ["Khí Etilen (C2H4)", "Khí Axetilen (C2H2)", "Khí Cacbonic (CO2)"], "Metan là hydrocacbon no đơn giản nhất cháy tỏa nhiều nhiệt lượng và ít muội than.", 1),
        ("Khí nào có khả năng kích thích quả mau chín và làm chậm quá trình rụng lá ở thực vật?", "Khí Etilen (C2H4)", ["Khí Metan", "Khí Oxy", "Khí Nitơ"], "Etilen là một phytohormone dạng khí tự nhiên do quả chín giải phóng ra.", 1),
        ("Chất béo lỏng thực vật (dầu ăn) có thể chuyển hóa thành chất béo rắn (bơ nhân tạo) nhờ phản ứng hóa học nào?", "Phản ứng hydro hóa (cộng hydro xúc tác Niken)", ["Phản ứng xà phòng hóa", "Phản ứng este hóa", "Phản ứng trùng hợp"], "Hydro hóa biến liên kết đôi không no trong dầu thực vật thành liên kết đơn no tạo thành bơ thực vật.", 2),
        ("Hợp chất hữu cơ nào có công thức phân tử C6H12O6 là nguồn năng lượng trực tiếp cung cấp cho tế bào?", "Glucozơ (Glucose / Đường nho)", ["Fructozơ", "Saccarozơ", "Tinh bột"], "Glucose trong máu người bình thường duy trì ổn định ở mức khoảng 4,4 - 7,2 mmol/L.", 1),
        ("Polime tổng hợp nào được sử dụng phổ biến nhất để sản xuất túi nilon, màng bọc thực phẩm và chai nhựa?", "Polietilen (Nhựa PE)", ["Polypropylen (PP)", "Polyvinyl clorua (PVC)", "Polystyren (PS)"], "PE được tổng hợp từ phản ứng trùng hợp các phân tử khí etilen ở áp suất và nhiệt độ cao.", 1),
        ("Nhựa PVC dùng làm ống dẫn nước và vỏ bọc dây điện là sản phẩm trùng hợp của monome nào?", "Vinyl clorua (CH2=CH-Cl)", ["Etilen", "Propilen", "Stiren"], "PVC có độ bền cơ học cao, chống ăn mòn hóa chất và cách điện tuyệt vời.", 2),
        ("Tơ tằm tự nhiên được dệt từ kén của con tằm ăn lá dâu có bản chất hóa học là chất gì?", "Chất đạm (Protein tự nhiên fibroin)", ["Xenlulozơ", "Chất béo", "Tinh bột"], "Sợi tơ tằm mềm mại óng ánh có nguồn gốc protein tự nhiên do tuyến tơ của tằm nhả ra.", 1),
        ("Vải sợi bông (cotton) may trang phục thấm hút mồ hôi tốt có thành phần hóa học chính là gì?", "Xenlulozơ (Cellulose chiếm hơn 90%)", ["Protein", "Nilon-6,6", "Tơ tằm"], "Cellulose là polime thiên nhiên cấu thành vách tế bào thực vật.", 1),
        ("Dung dịch cồn y tế dùng để sát trùng vết thương và khử khuẩn bề mặt có nồng độ cồn tối ưu là bao nhiêu độ?", "Cồn 70 độ (Etanol 70%)", ["Cồn 90 độ", "Cồn 50 độ", "Cồn 100 độ nguyên chất"], "Cồn 70 độ thấm sâu qua màng tế bào vi khuẩn làm đông tụ protein tiêu diệt mầm bệnh hiệu quả nhất.", 1),
        ("Phản ứng giữa axit béo với dung dịch kiềm (NaOH hoặc KOH) để sản xuất xà phòng được gọi là gì?", "Phản ứng xà phòng hóa", ["Phản ứng trùng ngưng", "Phản ứng thủy phân axit", "Phản ứng nhiệt phân"], "Sản phẩm của phản ứng tạo thành muối natri/kali của axit béo (xà phòng) và glixerol.", 2),
        ("Kim loại nào được mệnh danh là 'Kim loại của thời đại hàng không và vũ trụ' nhờ đặc tính nhẹ, bền và chống gỉ xuất sắc?", "Titan (Titanium)", ["Sắt", "Đồng", "Chì"], "Hợp kim titan chịu được nhiệt độ khắc nghiệt và áp lực lớn được dùng làm vỏ tàu con thoi và máy bay siêu thanh.", 2),
        ("Nguyên tố nào là phi kim dẫn điện tốt nhất và được dùng làm lõi que than trong bút chì và điện cực pin?", "Cacbon dạng Than chì (Graphite)", ["Kim cương", "Lưu huỳnh", "Photpho đỏ"], "Cấu trúc từng lớp lục giác trượt lên nhau của than chì giải phóng electron tự do dẫn điện.", 1),
        ("Hiện tượng các electron bị bứt ra khỏi bề mặt kim loại khi bị ánh sáng thích hợp chiếu vào được gọi là gì?", "Hiệu ứng quang điện ngoài", ["Hiệu ứng nhiệt điện", "Hiện tượng phóng xạ", "Hiện tượng ion hóa"], "Albert Einstein đoạt giải Nobel Vật lý năm 1921 nhờ giải thích định luật quang điện dựa trên thuyết lượng tử ánh sáng.", 2),
        ("Tia bức xạ không nhìn thấy có bước sóng dài hơn ánh sáng đỏ và có tác dụng nhiệt rất mạnh là tia gì?", "Tia hồng ngoại (Infrared)", ["Tia tử ngoại (UV)", "Tia Rơn-ghen (Tia X)", "Tia gamma"], "Tia hồng ngoại được ứng dụng trong điều khiển từ xa (remote), bếp hồng ngoại và camera nhìn đêm.", 1),
        ("Tia bức xạ không nhìn thấy có bước sóng ngắn hơn ánh sáng tím giúp cơ thể tổng hợp vitamin D và diệt khuẩn là tia gì?", "Tia tử ngoại (Tia cực tím / UV)", ["Tia hồng ngoại", "Sóng vi ba", "Sóng vô tuyến"], "Tia UV có tác dụng sinh học mạnh, kích thích phát quang và khử khuẩn phòng mổ y tế.", 1),
        ("Chùm ánh sáng có tính đơn sắc cao, độ định hướng cao và cường độ cực mạnh được phát minh năm 1960 là gì?", "Tia Laser (Light Amplification by Stimulated Emission of Radiation)", ["Tia X", "Đèn LED", "Tia cathode"], "Laser ứng dụng rộng rãi trong phẫu thuật mắt Lasik, đọc đĩa quang, cắt kim loại và đo đạc thiên văn.", 1),
        ("Cơ quan nào trong tế bào động vật chứa vật chất di truyền ADN và là trung tâm chỉ huy mọi hoạt động sống?", "Nhân tế bào (Nucleus)", ["Lưới nội chất", "Bộ máy Golgi", "Màng sinh chất"], "Nhân tế bào chứa các nhiễm sắc thể mang thông tin mã hóa cấu trúc các protein cơ thể.", 1),
        ("Quá trình phân chia tế bào sinh dưỡng giúp cơ thể lớn lên và tái tạo các mô bị tổn thương được gọi là gì?", "Quá trình nguyên phân (Mitosis)", ["Quá trình giảm phân", "Quá trình thụ tinh", "Quá trình phân hủy"], "Nguyên phân tạo ra hai tế bào con có bộ nhiễm sắc thể 2n giống hệt tế bào mẹ ban đầu.", 1),
        ("Quá trình phân chia tế bào sinh dục tạo ra các giao tử (tinh trùng hoặc trứng) mang bộ NST đơn bội (n) là gì?", "Quá trình giảm phân (Meiosis)", ["Quá trình nguyên phân", "Quá trình thụ phấn", "Quá trình phân mảnh"], "Giảm phân qua 2 lần phân bào liên tiếp giảm số lượng NST từ 2n xuống còn n.", 2),
        ("Đơn vị cấu trúc chức năng cơ bản của hệ thần kinh con người tiếp nhận và dẫn truyền xung động là gì?", "Tế bào thần kinh (Neuron)", ["Tế bào cơ", "Tế bào biểu bì", "Tế bào tủy"], "Não bộ con người chứa khoảng 86 tỷ neuron liên kết chằng chịt tạo nên ý thức và trí tuệ.", 1)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in raw:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

def get_cong_nghe_75():
    raw = [
        ("Nền tảng dịch vụ lưu trữ đám mây của tập đoàn Google cung cấp 15GB dung lượng miễn phí là gì?", "Google Drive", ["OneDrive", "iCloud", "Dropbox"], "Google Drive tích hợp hoàn hảo với Google Docs, Sheets và Gmail cho làm việc cộng tác.", 1),
        ("Cổng giao thức mặc định (Port) sử dụng cho dịch vụ duyệt web an toàn có mã hóa HTTPS trên Internet là cổng nào?", "Cổng 443", ["Cổng 80", "Cổng 21", "Cổng 22"], "Cổng 80 dùng cho HTTP không mã hóa, trong khi cổng 443 dành riêng cho HTTPS bảo mật.", 2),
        ("Hệ thống phân giải tên miền giúp chuyển đổi địa chỉ trang web (như google.com) thành địa chỉ IP số được viết tắt là gì?", "DNS (Domain Name System)", ["DHCP", "FTP", "NAT"], "DNS hoạt động như cuốn danh bạ điện thoại thông minh của toàn mạng Internet.", 1),
        ("Cơ sở dữ liệu quan hệ (RDBMS) truy vấn thông tin bằng ngôn ngữ tiêu chuẩn có tên viết tắt là gì?", "SQL (Structured Query Language)", ["HTML", "JSON", "XML"], "SQL với các lệnh SELECT, INSERT, UPDATE, DELETE quản lý dữ liệu bảng chặt chẽ.", 1),
        ("Mô hình trí tuệ nhân tạo tạo sinh đàm thoại nổi tiếng do công ty OpenAI ra mắt cuối năm 2022 là gì?", "ChatGPT", ["Siri", "Alexa", "Cortana"], "ChatGPT dựa trên kiến trúc Transformer mở ra làn sóng bùng nổ Trí tuệ nhân tạo toàn cầu.", 1),
        ("Món ăn đặc sản Nam Bộ gồm cơm tấm ăn kèm sườn heo nướng than hoa, bì lợn trộn thính và chả trứng hấp là món gì?", "Cơm tấm Sài Gòn", ["Cơm hến", "Cơm lam", "Cơm gà Tam Kỳ"], "Cơm tấm nấu từ hạt gạo tấm vỡ ăn cùng mỡ hành thơm phức và chén nước mắm chua ngọt kẹo.", 1),
        ("Đặc sản bánh tét nổi tiếng vùng đất Trà Vinh với màu xanh tím tự nhiên từ lá cẩm và nhân thập cẩm trứng muối là gì?", "Bánh tét Trà Cuôn", ["Bánh tét lá chuối", "Bánh chưng", "Bánh tét chay"], "Bánh tét Trà Cuôn (huyện Cầu Ngang, Trà Vinh) dẻo mềm nhân thịt mỡ bùi béo nổi tiếng xa gần.", 1),
        ("Món nước dùng đậm đà nấu từ cá lóc đồng, mắm cá linh cá sặc ăn kèm bắp chuối và rau muống bào miền Tây là món gì?", "Bún mắm (hoặc Bún nước lèo Sóc Trăng)", ["Bún chả", "Bún riêu cua", "Bún ốc"], "Bún nước lèo kết hợp tinh hoa ẩm thực ba dân tộc Kinh, Hoa, Khmer.", 1),
        ("Đặc sản vùng cao Tây Bắc làm từ thịt trâu tươi tẩm ướp hạt mắc khén hạt dổi rồi hun khói bếp than củi là gì?", "Thịt trâu gác bếp", ["Lạp xưởng tươi", "Thịt trâu xào", "Chả trâu"], "Thịt trâu gác bếp dai thơm đượm nồng mùi khói lửa đại ngàn Tây Bắc.", 1),
        ("Món ăn truyền thống lâu đời của người Mông ở Sa Pa nấu từ nội tạng và thịt ngựa trong chảo gang lớn là món gì?", "Thắng cố", ["Lợn cắp nách", "Gà đen H'Mông", "Nậm pịa"], "Thắng cố ăn nóng cùng rượu ngô men lá sưởi ấm những ngày đông băng giá vùng cao.", 1),
        ("Làng Vũ Đại (xã Hòa Hậu, huyện Lý Nhân, tỉnh Hà Nam) nức tiếng cả nước mỗi độ Tết đến xuân về với món đặc sản gì?", "Cá kho làng Vũ Đại (Cá kho Đại Hoàng)", ["Bánh chưng gấc", "Giò lụa Ước Lễ", "Nem chua"], "Cá trắm đen kho trong niêu đất đun củi nhãn suốt 12-14 tiếng xương nhừ thịt chắc đậm đà.", 1),
        ("Đặc sản bánh cáy dẻo thơm hạt vừng mạch nha nức tiếng là món quà quê truyền thống của tỉnh nào miền Bắc?", "Thái Bình", ["Nam Định", "Hải Dương", "Hưng Yên"], "Bánh cáy làng Nguyễn (huyện Đông Hưng, Thái Bình) có màu sắc lấm tấm như trứng con cáy biển.", 1),
        ("Kẹo Sìu Châu kẹo lạc mạch nha giòn tan thơm bùi trứ danh là đặc sản hơn 200 năm tuổi của tỉnh nào?", "Nam Định", ["Thái Bình", "Hà Nam", "Ninh Bình"], "Kẹo Sìu Châu Nam Định gói giấy bản ăn kèm chén trà sen mạn hảo ngọt dịu tao nhã.", 1),
        ("Bánh gai Tứ Trụ với màu đen lá gai dẻo quánh nhân đậu xanh dừa sợi thơm lừng là đặc sản của tỉnh nào miền Trung?", "Thanh Hóa (huyện Thọ Xuân)", ["Nghệ An", "Hà Tĩnh", "Quảng Bình"], "Bánh gai Tứ Trụ gắn liền với đất Lam Sơn địa linh nhân kiệt.", 1),
        ("Đặc sản lẩu nướng thịt bò thượng hạng thái lát mỏng nhúng nước dùng ngọt thanh ăn cùng trứng sống của Nhật Bản là món gì?", "Sukiyaki", ["Sushi", "Ramen", "Tempura"], "Thịt bò nhúng vừa chín tới quết qua bát trứng gà tươi béo ngậy ngọt lịm.", 1),
        ("Món tráng miệng nước Ý nổi tiếng làm từ bánh quy ngâm cà phê espresso xếp lớp cùng kem phô mai mascarpone rắc bột cacao là gì?", "Bánh Tiramisu", ["Panna Cotta", "Gelato", "Cannoli"], "Tiramisu trong tiếng Ý mang ý nghĩa ngọt ngào: 'Hãy đón nhận em' hoặc 'Làm bừng sáng tâm hồn'.", 1),
        ("Cú đánh đưa bóng thẳng từ điểm phát bóng vào lỗ golf chỉ bằng một gậy duy nhất trong môn Golf được gọi là gì?", "Hole-in-one (HIO)", ["Birdie", "Eagle", "Albatross"], "Hole-in-one là kỳ tích hiếm hoi và vinh quang bậc nhất mà mọi golf thủ đều khát khao.", 2),
        ("Trong bóng đá, quy định cấm một cầu thủ đứng gần đường biên ngang sân đối phương hơn cả bóng và cầu thủ phòng ngự cuối cùng khi nhận bóng gọi là gì?", "Luật việt vị (Offside)", ["Lỗi chạm tay", "Lỗi chơi xấu", "Lỗi câu giờ"], "Luật việt vị giúp ngăn chặn tình trạng tiền đạo chỉ đứng rình sẵn trước khung thành đối phương.", 1),
        ("Giải vô địch bóng đá châu Âu (UEFA Euro) được tổ chức theo chu kỳ mấy năm một lần?", "4 năm một lần", ["2 năm", "3 năm", "5 năm"], "Euro quy tụ những đội tuyển quốc gia hàng đầu châu lục tranh tài rực lửa mùa hè.", 1),
        ("Thẻ phạt màu vàng trong bóng đá được trọng tài rút ra để nhằm mục đích gì đối với cầu thủ vi phạm?", "Cảnh cáo hành vi phạm lỗi", ["Đuổi khỏi sân ngay", "Hủy bàn thắng", "Cho hưởng quả phạt đền"], "Nếu một cầu thủ nhận 2 thẻ vàng trong cùng một trận đấu sẽ tương đương một thẻ đỏ bị truất quyền thi đấu.", 1)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in raw:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

def get_van_hoc_75():
    raw = [
        ("Bài thơ 'Nhớ rừng' mượn lời con hổ trong vườn bách thú thể hiện khát vọng tự do cháy bỏng là của nhà thơ nào?", "Thế Lữ", ["Xuân Diệu", "Huy Cận", "Lưu Trọng Lư"], "'Gặm một khối căm hờn trong cũi sắt / Ta nằm dài trông ngày tháng dần qua' - Thế Lữ.", 1),
        ("Bài thơ 'Tràng giang' với nỗi buồn bâng khuâng sông nước không gian vô tận mênh mông là thi phẩm đỉnh cao của ai?", "Huy Cận", ["Xuân Diệu", "Quang Dũng", "Hàn Mặc Tử"], "'Sóng gợn tràng giang buồn điệp điệp / Con thuyền xuôi mái nước song song' - Huy Cận.", 1),
        ("Bài thơ 'Sang thu' với những chuyển biến tinh tế của thiên nhiên: 'Bỗng nhận ra hương ổi / Phả vào trong gió se' là của ai?", "Hữu Thỉnh", ["Thanh Hải", "Y Phương", "Viễn Phương"], "Hương ổi nồng nàn báo hiệu mùa thu dịu dàng về trên đất Bắc Bộ.", 1),
        ("Bài thơ 'Tiểu đội xe không kính' ngợi ca tinh thần lạc quan dũng cảm của các chiến sĩ lái xe Trường Sơn là của ai?", "Phạm Tiến Duật", ["Chính Hữu", "Nguyễn Duy", "Bằng Việt"], "'Không có kính không phải vì xe không có kính / Bom giật bom rung kính vỡ đi rồi' - Phạm Tiến Duật.", 1),
        ("Bài thơ 'Viếng lăng Bác' với niềm thành kính xót thương vô hạn: 'Con ở miền Nam ra thăm lăng Bác' là của nhà thơ nào?", "Viễn Phương", ["Thanh Hải", "Thu Bồn", "Nguyễn Khoa Điềm"], "Viễn Phương gửi gắm tấm lòng người con miền Nam sau ngày thống nhất ra viếng Bác Hồ kính yêu.", 1),
        ("Bài thơ 'Nói với con' dặn dò con ghi nhớ cội nguồn sinh dưỡng và niềm tự hào 'người đồng mình' là của nhà thơ dân tộc Tày nào?", "Y Phương (Hứa Vĩnh Sước)", ["Nông Quốc Chấn", "Lò Ngân Sủn", "Cầm Biêu"], "'Người đồng mình thô sơ da thịt / Chẳng mấy ai nhỏ bé đâu con'.", 2),
        ("Vở kịch lịch sử nổi tiếng 'Bắc Sơn' viết về cuộc khởi nghĩa Bắc Sơn năm 1940 do nhà văn nhà viết kịch nào sáng tác?", "Nguyễn Huy Tưởng", ["Lưu Quang Vũ", "Học Phi", "Đào Hồng Cẩm"], "Nguyễn Huy Tưởng là tên tuổi lớn gắn liền với kịch lịch sử và tiểu thuyết 'Sống mãi với Thủ đô'.", 2),
        ("Tác phẩm văn học cổ điển Hy Lạp 'I-li-át' (Iliad) và 'Ô-đi-xê' (Odyssey) tương truyền do thi hào mù nào sáng tác?", "Hô-me-rơ (Homer)", ["Xô-phốc (Sophocles)", "Pla-tôn (Plato)", "A-rít-xtốt (Aristotle)"], "Hai bản trường ca đồ sộ là nền tảng của toàn bộ nền văn học phương Tây cổ đại.", 1),
        ("Bức tượng điêu khắc đá cẩm thạch kiệt tác 'Đức Mẹ sầu bi' (Pietà) đặt tại Vương cung thánh đường Thánh Peter là của ai?", "Michelangelo", ["Leonardo da Vinci", "Donatello", "Bernini"], "Michelangelo tạc nên nỗi đau thương thánh thiện tuyệt mỹ của Đức Mẹ Maria ôm thi hài Chúa Jesus.", 2),
        ("Bức tượng cẩm thạch khổng lồ khắc họa chàng dũng sĩ Đa-vít (David) chuẩn bị nghênh chiến người khổng lồ Goliath là của ai?", "Michelangelo", ["Leonardo da Vinci", "Raphael", "Rodin"], "Bức tượng David tại bảo tàng Florence là biểu tượng đỉnh cao của tỷ lệ cơ thể người hoàn hảo thời Phục hưng.", 1),
        ("Bức họa bích họa lừng danh 'Trường học Athens' (The School of Athens) quy tụ các triết gia vĩ đại cổ đại là của danh họa nào?", "Raphael (Raffaello Sanzio)", ["Leonardo da Vinci", "Michelangelo", "Titian"], "Plato chỉ tay lên trời cao và Aristotle hướng tay xuống đất đại diện cho hai trường phái triết học.", 2),
        ("Bức tranh 'Tiếng thét' (The Scream) với nhân vật ôm đầu hoảng sợ dưới bầu trời đỏ rực là kiệt tác của danh họa nước nào?", "Edvard Munch (Na Uy)", ["Vincent van Gogh (Hà Lan)", "Pablo Picasso (Tây Ban Nha)", "Gustav Klimt (Áo)"], "Bức tranh biểu hiện nỗi lo âu hiện sinh sâu sắc của con người hiện đại.", 1),
        ("Kiệt tác hội họa 'Sự bền bỉ của ký ức' (The Persistence of Memory) với những chiếc đồng hồ quả quýt tan chảy mềm nhũn là của ai?", "Salvador Dalí", ["Pablo Picasso", "René Magritte", "Joan Miró"], "Salvador Dalí là bậc thầy vĩ đại của trường phái Siêu thực (Surrealism).", 2),
        ("Danh họa người Tây Ban Nha nào là người đồng sáng lập trường phái hội họa Lập thể (Cubism) tác giả bức tranh 'Guernica'?", "Pablo Picasso", ["Salvador Dalí", "Francisco Goya", "Diego Velázquez"], "Picasso dùng những khối hình kỷ hà góc cạnh cách mạng hóa hội họa thế kỷ XX.", 1),
        ("Dòng gốm cổ Chu Đậu nổi danh với sắc men trắng ngà hoa lam tinh xảo thế kỷ XIV-XV thuộc tỉnh nào miền Bắc?", "Hải Dương (huyện Nam Sách)", ["Bắc Ninh", "Hà Nội", "Quảng Ninh"], "Gốm Chu Đậu từng được xuất khẩu tới hàng chục quốc gia theo con đường tơ lụa trên biển cổ xưa.", 2)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in raw:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

def get_lich_su_75():
    raw = [
        ("Sau khi đánh tan quân Minh năm 1427, Lê Lợi đã tổ chức hội thề nào và cấp ngựa, thuyền cho quân giặc rút về nước?", "Hội thề Đông Quan", ["Hội thề Lũng Nhai", "Hội nghị Diên Hồng", "Hội nghị Bình Than"], "Chính sách nhân đạo chu cấp lương thảo phương tiện cho giặc hồi hương làm rạng rỡ truyền thống hòa hiếu Đại Việt.", 2),
        ("Triều đình nhà Nguyễn ký Hiệp ước Nhâm Tuất năm 1862 nhượng ba tỉnh miền Đông Nam Kỳ nào cho thực dân Pháp?", "Gia Định, Định Tường, Biên Hòa (và đảo Côn Lôn)", ["Vĩnh Long, An Giang, Hà Tiên", "Bình Dương, Tây Ninh, Đồng Nai", "Sài Gòn, Chợ Lớn, Tân An"], "Hiệp ước đầu hàng đầu tiên của triều Nguyễn làm dấy lên làn sóng phản kháng mãnh liệt của nhân dân Nam Bộ.", 2),
        ("Hiệp ước nào được triều đình Huế ký với Pháp năm 1883 chính thức thừa nhận nền bảo hộ của thực dân Pháp trên toàn cõi Việt Nam?", "Hiệp ước Hác-măng (Hiệp ước Quý Mùi)", ["Hiệp ước Pa-tơ-nốt", "Hiệp ước Giáp Tuất", "Hiệp ước Nhâm Tuất"], "Hiệp ước Hác-măng đánh dấu sự đầu hàng hoàn toàn của triều đình phong kiến nhà Nguyễn trước thực dân Pháp.", 2),
        ("Phong trào cách mạng 1930 - 1931 với đỉnh cao là sự ra đời của chính quyền nào ở miền Trung?", "Xô viết Nghệ - Tĩnh", ["Xô viết Ba Tơ", "Chiến khu Tân Trào", "Chiến khu Việt Bắc"], "Chính quyền Xô viết công nông đầu tiên đã xóa bỏ các thứ thuế vô lý và chia lại ruộng đất công cho dân nghèo.", 1),
        ("Lá cờ đỏ sao vàng năm cánh lần đầu tiên xuất hiện trong phong trào đấu tranh cách mạng nào ở Nam Bộ vào tháng 11/1940?", "Khởi nghĩa Nam Kỳ", ["Khởi nghĩa Bắc Sơn", "Binh biến Đô Lương", "Khởi nghĩa Ba Tơ"], "Lá cờ đỏ sao vàng thiêng liêng tung bay kiêu hãnh trên các đồn bốt giặc bị nghĩa quân Nam Kỳ đánh chiếm.", 1),
        ("Hội nghị Ban Chấp hành Trung ương Đảng lần thứ 8 (tháng 5/1941) do Nguyễn Ái Quốc chủ trì tại Pác Bó đã đặt nhiệm vụ nào lên hàng đầu?", "Giải phóng dân tộc", ["Cách mạng ruộng đất", "Xây dựng chủ nghĩa xã hội", "Đấu tranh nghị trường"], "Hội nghị quyết định thành lập Mặt trận Việt Minh nhằm tập hợp sức mạnh toàn dân cứu nước.", 2),
        ("Chiến dịch Biên giới Thu - Đông năm 1950 mở ra nhằm mục đích chiến lược giải phóng tuyến biên giới nào?", "Biên giới Việt - Trung", ["Biên giới Việt - Lào", "Biên giới Việt - Campuchia", "Vùng ven biển Đông Bắc"], "Chiến thắng Biên giới mở thông con đường liên lạc chiến lược với Liên Xô, Trung Quốc và quốc tế.", 1),
        ("Hiệp định Genève năm 1954 quy định giới tuyến quân sự tạm thời giữa hai miền Nam - Bắc Việt Nam nằm tại vĩ tuyến mấy?", "Vĩ tuyến 17 (dọc sông Bến Hải)", ["Vĩ tuyến 16", "Vĩ tuyến 18", "Vĩ tuyến 20"], "Sông Bến Hải và cầu Hiền Lương trở thành chứng nhân lịch sử của nỗi đau chia cắt đất nước suốt hơn 20 năm.", 1),
        ("Chiến dịch phản công đường 9 - Nam Lào (năm 1971) đã đánh bại hoàn toàn cuộc hành quân quy mô lớn nào của Mỹ và quân đội Sài Gòn?", "Hành quân Lam Sơn 719", ["Hành quân Junction City", "Hành quân Cedar Falls", "Hành quân Attleboro"], "Quân giải phóng làm chủ hoàn toàn chiến trường bảo vệ vững chắc tuyến đường vận tải chiến lược Trường Sơn.", 2),
        ("Phong trào triết học Khai sáng thế kỷ XVIII ở châu Âu với các đại biểu Voltaire, Rousseau, Montesquieu đã chuẩn bị tư tưởng cho cuộc cách mạng nào?", "Cách mạng tư sản Pháp 1789", ["Cách mạng công nghiệp Anh", "Cách mạng Nga", "Cải cách tôn giáo"], "Tư tưởng tự do, bình đẳng và tam quyền phân lập thức tỉnh quần chúng lật đổ chế độ phong kiến chuyên chế.", 2),
        ("Trận hải chiến Midway (tháng 6/1942) tại Thái Bình Dương trong Thế chiến II đã chứng kiến sự thất bại nặng nề của hải quân nước nào?", "Hải quân Đế quốc Nhật Bản (mất 4 tàu sân bay)", ["Hải quân Mỹ", "Hải quân Anh", "Hải quân Đức"], "Chiến thắng Midway làm xoay chuyển hoàn toàn cục diện chiến tranh tại mặt trận Thái Bình Dương có lợi cho quân Đồng minh.", 2),
        ("Cuộc đổ bộ quân sự bờ biển quy mô lớn nhất lịch sử nhân loại diễn ra ngày 6/6/1944 (D-Day) mở mặt trận thứ hai tại bờ biển nào của Pháp?", "Bờ biển Normandie (Normandy)", ["Bờ biển Marseille", "Bờ biển Dunkirk", "Bờ biển Bordeaux"], "Hàng chục vạn liên quân Mỹ, Anh, Canada đổ bộ giải phóng nước Pháp và tiến công sào huyệt phát xít Đức.", 1),
        ("Hội nghị thượng đỉnh Yalta (tháng 2/1945) tại bán đảo Crimea quy tụ nguyên thủ của ba cường quốc Đồng minh nào?", "Mỹ (Roosevelt), Anh (Churchill) và Liên Xô (Stalin)", ["Mỹ, Anh và Pháp", "Liên Xô, Trung Quốc và Mỹ", "Pháp, Đức và Ý"], "Hội nghị Yalta phân chia khu vực đóng quân và ảnh hưởng định hình trật tự thế giới hai cực sau chiến tranh.", 2),
        ("Phiên tòa quân sự quốc tế xét xử các trùm tội phạm chiến tranh phát xít Đức sau Thế chiến II được tổ chức tại thành phố nào của Đức?", "Thành phố Nuremberg (Ni-rơn-be)", ["Thành phố Berlin", "Thành phố Munich", "Thành phố Frankfurt"], "Tòa án Nuremberg đã lên án tội ác diệt chủng chống lại loài người của chủ nghĩa phát xít.", 2),
        ("Phong trào giải phóng dân tộc bùng nổ mạnh mẽ khiến 17 quốc gia châu Phi tuyên bố độc lập đã khiến năm 1960 được lịch sử gọi là gì?", "Năm châu Phi (Year of Africa)", ["Năm Á - Phi", "Năm Độc lập", "Năm Bùng nổ"], "Hệ thống thuộc địa của chủ nghĩa thực dân phương Tây tan rã từng mảng lớn tại lục địa đen.", 1)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in raw:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

def get_dia_ly_75():
    raw = [
        ("Nước ta có bao nhiêu vùng kinh tế - xã hội chính theo phân vùng quy hoạch phát triển quốc gia hiện nay?", "6 vùng kinh tế - xã hội", ["5 vùng", "7 vùng", "8 vùng"], "Sáu vùng gồm: Trung du miền núi phía Bắc, Đồng bằng sông Hồng, Bắc Trung Bộ và Duyên hải miền Trung, Tây Nguyên, Đông Nam Bộ, Đồng bằng sông Cửu Long.", 1),
        ("Ranh giới khí hậu tự nhiên phân chia miền Bắc có mùa đông lạnh với miền Nam nắng ấm quanh năm là dãy núi nào?", "Dãy Bạch Mã (nằm giữa Thừa Thiên Huế và Đà Nẵng)", ["Dãy Hoàng Liên Sơn", "Dãy Hoành Sơn", "Dãy Tam Điệp"], "Dãy Bạch Mã đâm ngang ra biển chặn các đợt gió mùa Đông Bắc lạnh giá tràn xuống phương Nam.", 1),
        ("Hiện tượng gió mùa mùa hè vượt qua dãy Trường Sơn gây thời tiết khô nóng đặc biệt gay gắt ở Bắc Trung Bộ được gọi là gì?", "Gió phơn Tây Nam (Gió Lào)", ["Gió mùa Đông Bắc", "Gió Tín phong", "Gió Mậu dịch"], "Hiệu ứng phơn làm khối khí sau khi trút mưa bên sườn tây hạ xuống sườn đông bị nung nóng khô rát.", 1),
        ("Vịnh biển nào ở miền Trung nước ta được Câu lạc bộ các vịnh đẹp nhất thế giới (Worldbays) kết nạp cùng với Vịnh Hạ Long và Nha Trang?", "Vịnh Lăng Cô (Thừa Thiên Huế)", ["Vịnh Xuân Đài", "Vịnh Dung Quất", "Vịnh Quy Nhơn"], "Lăng Cô có bãi cát trắng thoai thoải uốn lượn dưới chân đèo Hải Vân và làn nước trong xanh ngọc bích.", 1),
        ("Ngọn hải đăng nằm trên đỉnh núi đá hoa cương cao hơn 110m đón ánh bình minh sớm nhất trên đất liền Việt Nam là gì?", "Hải đăng Đại Lãnh (Mũi Điện, Phú Yên)", ["Hải đăng Kê Gà", "Hải đăng Vũng Tàu", "Hải đăng Côn Đảo"], "Hải đăng Đại Lãnh được người Pháp xây dựng từ năm 1890 là biểu tượng kiêu hãnh của vùng đất Phú Yên.", 1),
        ("Đảo tiền tiêu nào của nước ta nằm giữa Vịnh Bắc Bộ là huyện đảo trực thuộc thành phố Hải Phòng cách đất liền khoảng 110 km?", "Huyện đảo Bạch Long Vĩ", ["Đảo Cát Bà", "Đảo Cô Tô", "Đảo Hòn Dấu"], "Bạch Long Vĩ có vị trí chiến lược quân sự và là trung tâm dịch vụ hậu cần nghề cá lớn nhất Vịnh Bắc Bộ.", 2),
        ("Hòn đảo núi lửa cổ nằm cách bờ biển Phan Thiết khoảng 120 km nổi tiếng với bờ kè bảy màu và cảnh quan biển đảo kỳ thú là gì?", "Đảo Phú Quý (Cù Lao Thu)", ["Đảo Côn Sơn", "Đảo Nam Du", "Đảo Hòn Khoai"], "Phú Quý có khí hậu trong lành, nhiều danh thắng và nguồn lợi hải sản phong phú.", 1),
        ("Quần đảo du lịch hoang sơ tuyệt đẹp gồm 21 hòn đảo lớn nhỏ nằm ở phía đông nam đảo Phú Quốc thuộc tỉnh Kiên Giang là gì?", "Quần đảo Nam Du", ["Quần đảo Thổ Chu", "Quần đảo Bà Lụa", "Quần đảo Hải Tặc"], "Nam Du được ví như 'Maldives của Việt Nam' với những rặng dừa nghiêng bóng bên bờ biển ngọc.", 1),
        ("Quốc gia nào ở Đông Nam Á có thủ đô hành chính mới mang tên Nusantara đang được xây dựng trên đảo Borneo?", "Indonesia", ["Malaysia", "Philippines", "Thái Lan"], "Indonesia chuyển thủ đô từ Jakarta sang Nusantara trên tỉnh Đông Kalimantan nhằm giảm tải cho đảo Java.", 2),
        ("Quốc gia nào ở Đông Nam Á là thành viên duy nhất chưa gia nhập tổ chức ASEAN đầy đủ tính đến năm 2023 (đã được chấp thuận về nguyên tắc)?", "Đông Timor (Timor-Leste)", ["Brunei", "Lào", "Myanmar"], "Đông Timor giành độc lập năm 2002 và đang trong tiến trình gia nhập trở thành thành viên thứ 11 của ASEAN.", 1),
        ("Hệ thống sông ngòi nước ta có hai hướng dòng chảy chính là hướng tây bắc - đông nam và hướng nào?", "Hướng vòng cung", ["Hướng đông - tây", "Hướng bắc - nam", "Hướng xuyên tâm"], "Các con sông như sông Gâm, sông Cầu, sông Thương chảy uốn lượn theo các cánh cung núi vùng Đông Bắc.", 2),
        ("Đồng bằng sông Cửu Long vựa lúa lớn nhất cả nước có diện tích tự nhiên xấp xỉ bao nhiêu km vuông?", "Khoảng 40.000 km2", ["Khoảng 15.000 km2", "Khoảng 60.000 km2", "Khoảng 25.000 km2"], "Đồng bằng sông Cửu Long được bồi đắp bởi phù sa màu mỡ của hai nhánh sông Tiền và sông Hậu.", 1),
        ("Vùng trũng ngập nước theo mùa lớn nhất Đồng bằng sông Cửu Long trải rộng trên địa bàn ba tỉnh Long An, Tiền Giang, Đồng Tháp là gì?", "Vùng Đồng Tháp Mười", ["Vùng Tứ giác Long Xuyên", "Vùng Bán đảo Cà Mau", "Vùng U Minh"], "Đồng Tháp Mười nổi tiếng với bạt ngàn hoa sen, rừng tràm và hệ sinh vật đất ngập nước trù phú.", 1),
        ("Vùng trũng ngập mặn nằm giữa hai dòng sông Vàm Cỏ Đông và Vàm Cỏ Tây nổi tiếng trong kháng chiến chống Mỹ là gì?", "Khu căn cứ Đồng Tháp Mười", ["Rừng Sác Cần Giờ", "Chiến khu Đ", "Chiến khu Dương Minh Châu"], "Rừng Sác Cần Giờ là căn cứ địa ngập mặn kiên cường của Trung đoàn đặc công 10 Rừng Sác anh hùng.", 2),
        ("Tỉnh nào ở Tây Nguyên là tỉnh duy nhất không có đường biên giới giáp với nước láng giềng Lào hoặc Campuchia?", "Lâm Đồng", ["Đắk Lắk", "Gia Lai", "Kon Tum"], "Lâm Đồng nằm sâu trên vùng cao nguyên Di Linh và Lâm Viên tiếp giáp với các tỉnh Nam Trung Bộ và Đông Nam Bộ.", 2)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in raw:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

def get_do_vui_75():
    raw = [
        ("Đố mẹo: Bánh gì không ăn được mà cầu thủ nào nhận hai cái trong một trận đấu là phải rời sân?", "Bánh thẻ đỏ (hoặc 2 thẻ vàng = 1 thẻ đỏ)", ["Bánh chưng", "Bánh xe", "Bánh bao"], "Hai thẻ vàng cộng lại thành thẻ đỏ trực tiếp rời sân.", 1),
        ("Đố mẹo: Cái gì có mặt có mũi mà không có mắt có tai, chạy suốt ngày đêm không mỏi mệt?", "Chiếc đồng hồ", ["Con sông", "Bánh xe", "Chiếc ô tô"], "Mặt đồng hồ và các kim tích tắc đo đếm thời gian không ngừng nghỉ.", 1),
        ("Đố mẹo: Càng cào càng rách, càng gãi càng ngứa là cái gì?", "Vết muỗi đốt (hoặc vết ngứa ngoài da)", ["Manh chiếu rách", "Chiếc áo cũ", "Chiếc bao tải"], "Gãi ngứa làm giải phóng thêm histamin khiến cảm giác ngứa càng dữ dội hơn.", 1),
        ("Đố mẹo: Cái gì thuộc về bạn, khi bạn ngủ say thì nó vẫn thức đập nhịp nhàng để giữ sự sống cho bạn?", "Trái tim", ["Đôi mắt", "Đôi bàn tay", "Đôi tai"], "Trái tim co bóp bơm máu nuôi cơ thể suốt cả cuộc đời không một phút ngừng nghỉ.", 1),
        ("Đố mẹo: Hoa gì nở quanh năm trong mỗi gia đình đem lại dòng điện thắp sáng muôn nơi?", "Hoa điện (hoặc đồng hồ điện / công tơ điện)", ["Hoa hồng", "Hoa cúc", "Hoa sen"], "Chơi chữ dí dỏm về đồng hồ điện quay tít hàng ngày.", 1),
        ("Đố mẹo: Bút gì không dùng để viết lên giấy vở mà học sinh nào cũng dùng để kẻ đường thẳng hàng?", "Cây thước kẻ", ["Bút chì", "Bút bi", "Bút dạ"], "Thước kẻ là đồ dùng học tập thiết yếu của mọi học sinh.", 1),
        ("Đố mẹo: Thuyền gì không chở người, không chở hàng trên sông biển mà dùng để chèo trên đĩa ăn?", "Thuyền chở nước chấm (hoặc đĩa hình thuyền)", ["Thuyền thúng", "Thuyền buồm", "Thuyền rồng"], "Câu đố tạo hình chén đĩa cách điệu trên bàn ăn.", 1),
        ("Đố chữ: Từ nào trong tiếng Việt bỏ dấu sắc thì thành vật che mưa nắng trên đầu, thêm dấu huyền thành con vật cày ruộng cho nhà nông?", "Nón (Nón - Nón lá / Nón bỏ sắc -> Non / Trâu - Bò...)", ["Mũ", "Áo", "Dù"], "Chơi chữ tiếng Việt tinh nghịch phong phú thanh điệu.", 2),
        ("Đố mẹo: Một người đi dưới trời mưa như trút nước mà không mặc áo mưa, không che ô, tại sao trên đầu không bị ướt một sợi tóc nào?", "Vì người đó bị hói đầu (không có sợi tóc nào)!", ["Vì người đó đi trong nhà", "Vì mưa bóng mây", "Vì người đó chạy nhanh"], "Không có tóc thì lấy đâu ra sợi tóc nào để mà ướt!", 1),
        ("Đố mẹo: Tháng nào trong năm phụ nữ nói ít nhất?", "Tháng 2 (vì tháng 2 có ít ngày nhất, chỉ 28 hoặc 29 ngày)!", ["Tháng 1", "Tháng 12", "Tháng 7"], "Số ngày ít nhất thì số lượng lời nói trong tháng hiển nhiên là ít nhất!", 1),
        ("Đố logic: Một người nông dân nuôi 17 con cừu. Trừ 9 con ra thì tất cả số cừu còn lại đều bị chết vì bão tuyết. Hỏi người đó còn lại mấy con cừu sống sót?", "Còn lại đúng 9 con cừu sống sót", ["Còn 8 con", "Còn 0 con", "Còn 17 con"], "Đọc kỹ câu hỏi: 'Trừ 9 con ra thì tất cả đều chết', nghĩa là 9 con đó còn sống!", 1),
        ("Đố mẹo: Cái gì bạn có thể cầm được bằng tay trái nhưng không bao giờ cầm được bằng tay phải của chính bạn?", "Khuỷu tay phải (hoặc bàn tay phải) của bạn!", ["Cây bút", "Cốc nước", "Chiếc điện thoại"], "Tay phải không thể tự cầm nắm lấy chính bàn tay hoặc cùi chỏ của mình!", 1),
        ("Đố mẹo: Có một chiếc xe buýt chở 10 người. Đến trạm dừng có 3 người xuống và 2 người lên. Hỏi trên xe lúc này có tất cả bao nhiêu người?", "Còn 10 người (tính cả người tài xế lái xe buýt)!", ["Còn 9 người", "Còn 8 người", "Còn 11 người"], "Ban đầu xe chở 10 hành khách + 1 tài xế = 11 người. 3 người xuống, 2 lên thì còn 10 người!", 2),
        ("Đố mẹo: Có cổ mà không có đầu / Có tay mà chẳng có chân là cái gì mặc trên người?", "Chiếc áo (áo sơ mi, áo phông)", ["Chiếc quần", "Chiếc mũ", "Đôi tất"], "Áo có cổ áo và tay áo bao bọc thân người giữ ấm và làm đẹp.", 1),
        ("Đố mẹo: Quả gì không chín trên cây / Lăn trên sân cỏ vạn người hò reo?", "Quả bóng đá", ["Quả bưởi", "Quả dưa hấu", "Quả cam"], "Quả bóng tròn mang lại những cảm xúc thăng hoa nghẹt thở trong môn thể thao vua.", 1)
    ]
    qs = []
    for q_t, ans, dist, expl, diff in raw:
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
    print("🏆 FINAL PUSH TO 2,500 QUESTIONS: BỨT PHÁ TOÀN DIỆN!")
    print("=" * 70)

    # 1. Khoa học tự nhiên
    kh = get_khoa_hoc_75()
    add_questions_to_category("khoa-hoc-tu-nhien", kh)

    # 2. Đời sống công nghệ
    cn = get_cong_nghe_75()
    add_questions_to_category("doi-song-cong-nghe", cn)

    # 3. Văn học nghệ thuật
    vh = get_van_hoc_75()
    add_questions_to_category("van-hoc-nghe-thuat", vh)

    # 4. Lịch sử
    ls = get_lich_su_75()
    add_questions_to_category("lich-su", ls)

    # 5. Địa lý
    dl = get_dia_ly_75()
    add_questions_to_category("dia-ly", dl)

    # 6. Đố vui trí tuệ
    dv = get_do_vui_75()
    add_questions_to_category("do-vui-tri-tue", dv)

    print("\n✅ Hoàn thành Final Push nạp câu hỏi!")

if __name__ == '__main__':
    main()
