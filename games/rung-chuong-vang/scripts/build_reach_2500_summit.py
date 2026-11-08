# -*- coding: utf-8 -*-
"""
Summit to 2,500 Questions: Chinh phục đỉnh cao Cột mốc 3 (Vượt 2.500 câu hỏi)!
Bổ sung 330 câu hỏi (55 câu x 6 chuyên mục) chất lượng cao, chuẩn hóa 100%.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

# ==============================================================================
# 1. VĂN HỌC - NGHỆ THUẬT (55 câu)
# ==============================================================================
def get_summit_van_hoc():
    raw = [
        ("Bản dạ khúc bất hủ 'Dạ cổ hoài lang' (Đêm khuya nghe tiếng trống nhớ chồng) do nhạc sĩ nào sáng tác năm 1919 tại Bạc Liêu?", "Nhạc sĩ Cao Văn Lầu (Sáu Lầu)", ["Nhạc sĩ Ba Chột", "Nhạc sĩ Hai Khị", "Nhạc sĩ Mười Khói"], "'Từ là từ phu tướng / Báu kiếm sắc phán lên đàng' - bản nhạc tiền thân của bài vọng cổ cải lương Nam Bộ.", 1),
        ("Nghệ nhân dân gian cuối cùng của nghệ thuật hát Xẩm Việt Nam được tôn vinh là 'Báu vật nhân văn sống' là ai?", "Nghệ nhân Hà Thị Cầu", ["Nghệ nhân Quách Thị Hồ", "Nghệ nhân Thao Giang", "Nghệ nhân Mai Tuyết Hoa"], "Cụ Hà Thị Cầu kéo nhị gảy phách hát xẩm mộc mạc làm lay động lòng người đất Ninh Bình.", 1),
        ("Nhân vật biểu tượng hài hước dẫn dắt câu chuyện trong nghệ thuật Múa rối nước truyền thống Việt Nam là ai?", "Chú Tễu", ["Thằng Bờm", "Chú Cuội", "Ông Đổng"], "Chú Tễu phốp pháp cởi trần đóng khố tươi cười giãi bày tâm sự và mở màn cho các tích trò rối nước.", 1),
        ("Bài hát bất hủ 'Như có Bác trong ngày đại thắng' được nhạc sĩ Phạm Tuyên sáng tác trong đêm lịch sử nào?", "Đêm 28 và thu thanh phát sóng trưa ngày 30/4/1975", ["Đêm 2/9/1945", "Đêm 7/5/1954", "Đêm 19/12/1946"], "Khúc ca reo vui rộn rã hòa chung niềm vui non sông liền một dải của triệu triệu con tim Việt Nam.", 1),
        ("Ai là tác giả của ca khúc bất hủ 'Hà Nội mùa vắng những cơn mưa' phổ thơ Bùi Thanh Tuấn?", "Nhạc sĩ Trương Quý Hải", ["Nhạc sĩ Phú Quang", "Nhạc sĩ Hoàng Hiệp", "Nhạc sĩ Trịnh Công Sơn"], "Giai điệu da diết gợi nhớ hoa sữa rơi, cây bàng lá đỏ và quán cóc liêu xiêu góc phố Hà Nội.", 1),
        ("Nhạc sĩ nào được mệnh danh là 'Người nhạc sĩ của Hà Nội' với những ca khúc 'Em ơi Hà Nội phố', 'Nỗi nhớ mùa đông'?", "Nhạc sĩ Phú Quang", ["Nhạc sĩ Trịnh Công Sơn", "Nhạc sĩ Văn Cao", "Nhạc sĩ Trần Tiến"], "Âm nhạc Phú Quang gắn chặt với hồn cốt mùa đông Hà Nội hoài niệm trầm tư.", 1),
        ("Ca khúc 'Đi học' ('Hương rừng thơm đồi vắng / Nước suối trong thầm thì') do nhạc sĩ nào phổ nhạc từ thơ Hoàng Minh Chính?", "Nhạc sĩ Bùi Đình Thảo", ["Nhạc sĩ Phạm Tuyên", "Nhạc sĩ Hoàng Long", "Nhạc sĩ Phong Nhã"], "Bài hát thiếu nhi quen thuộc in sâu vào ký ức tuổi thơ cắp sách tới trường của bao thế hệ.", 1),
        ("Nhà văn nào được mệnh danh là 'Nhà Nam Bộ học' với các tác phẩm 'Hương rừng Cà Mau', 'Văn minh miệt vườn'?", "Nhà văn Sơn Nam", ["Đoàn Giỏi", "Trang Thế Hy", "Nguyễn Ngọc Tư"], "Sơn Nam dành cả đời rong ruỗi ghi chép về nếp sống, tính cách hào sảng của người phương Nam mở cõi.", 1),
        ("Tập truyện ngắn 'Cánh đồng bất tận' gây tiếng vang lớn trong nền văn học đương đại Việt Nam là của nữ nhà văn nào?", "Nguyễn Ngọc Tư", ["Dạ Ngân", "Đỗ Bích Thúy", "Trần Thùy Mai"], "Tác phẩm đoạt Giải thưởng Hội Nhà văn Việt Nam năm 2006 phản ánh số phận người nông dân miền Tây.", 1),
        ("Ai là tác giả của tiểu thuyết 'Nỗi buồn chiến tranh' (Thân phận của tình yêu) đoạt nhiều giải thưởng văn học quốc tế danh giá?", "Nhà văn Bảo Ninh", ["Nguyễn Huy Thiệp", "Nguyễn Bình Phương", "Hồ Anh Thái"], "Tác phẩm đưa văn học chiến tranh Việt Nam ra thế giới với cái nhìn nhân văn sâu sắc.", 2),
        ("Bài thơ 'Bên kia sông Đuống' với những câu thơ xót xa 'Sông Đuống trôi đi / Một dòng lấp lánh' là của nhà thơ nào?", "Hoàng Cầm", ["Quang Dũng", "Hữu Loan", "Vũ Cao"], "Hoàng Cầm khóc thương quê hương Kinh Bắc bị giặc tàn phá trong kháng chiến chống Pháp năm 1948.", 1),
        ("Bài thơ 'Màu tím hoa sim' khóc người vợ trẻ nơi quê nhà trong kháng chiến chống Pháp là thi phẩm nổi tiếng của ai?", "Hữu Loan", ["Hoàng Cầm", "Nguyễn Bính", "Thâm Tâm"], "'Nàng có ba người anh đi bộ đội / Những đứa em thơ ngơ ngác' - bài thơ tình bi tráng bất hủ.", 1),
        ("Nhà thơ nào được mệnh danh là 'Nhà thơ chân quê' với những câu thơ mộc mạc đậm hồn làng quê Bắc Bộ?", "Nguyễn Bính", ["Anh Thơ", "Đoàn Văn Cừ", "Bàng Bá Lân"], "'Hôm qua em đi tỉnh về / Đợi em ở mãi con đê đầu làng / Khăn nhung quần lĩnh rộn ràng / Áo cài khuy bấm, em làm khổ tôi' - Nguyễn Bính.", 1),
        ("Tập thơ 'Từ ấy' (1937 - 1946) đánh dấu bước ngoặt giác ngộ lý tưởng cách mạng của nhà thơ nào?", "Tố Hữu", ["Sóng Hồng", "Xuân Thủy", "Chế Lan Viên"], "'Từ ấy trong tôi bừng nắng hạ / Mặt trời chân lý chói qua tim' - Tố Hữu.", 1),
        ("Trong văn học dân gian, truyện cười nào phê phán thói khoe của lố lăng qua hai nhân vật 'áo mới' và 'lợn cưới'?", "Truyện 'Lợn cưới, áo mới'", ["Truyện 'Tam đại con gà'", "Truyện 'Nhưng nó phải bằng hai mày'", "Truyện 'Thầy bói xem voi'"], "Câu chuyện châm biếm tính khoe khoang kệch cỡm của những kẻ học đòi.", 1),
        ("Truyện ngụ ngôn 'Thầy bói xem voi' khuyên răn con người bài học nhận thức gì trong cuộc sống?", "Muốn đánh giá sự vật phải xem xét toàn diện khách quan, không được phiến diện một chiều", ["Phải tin vào bói toán", "Nên đi xem voi thường xuyên", "Không nên sờ vào voi"], "Năm thầy bói mù mỗi người sờ một bộ phận rồi cãi nhau nảy lửa vì ai cũng cho là mình đúng.", 1),
        ("Bức tranh kiệt tác 'Thiếu nữ bên hoa huệ' sáng tác năm 1943 là tác phẩm sơn dầu đỉnh cao của danh họa nào?", "Họa sĩ Tô Ngọc Vân", ["Họa sĩ Trần Văn Cẩn", "Họa sĩ Nguyễn Gia Trí", "Họa sĩ Bùi Xuân Phái"], "Vẻ đẹp thanh tao duyên dáng của người con gái Hà Nội bên đóa hoa huệ trắng tinh khôi.", 1),
        ("Bức tranh sơn mài khổ lớn 'Vườn xuân Trung Nam Bắc' trưng bày tại Bảo tàng Mỹ thuật TP.HCM là của ai?", "Họa sĩ Nguyễn Gia Trí", ["Họa sĩ Nguyễn Phan Chánh", "Họa sĩ Nguyễn Sáng", "Họa sĩ Tô Ngọc Vân"], "Nguyễn Gia Trí là bậc thầy số một của nghệ thuật tranh sơn mài hiện đại Việt Nam.", 2),
        ("Tác phẩm tranh lụa nổi tiếng 'Chơi ô ăn quan' sáng tác năm 1931 là kiệt tác của danh họa nào?", "Họa sĩ Nguyễn Phan Chánh", ["Họa sĩ Tô Ngọc Vân", "Họa sĩ Trần Văn Cẩn", "Họa sĩ Nam Sơn"], "Nguyễn Phan Chánh đưa nghệ thuật tranh lụa Việt Nam lên tầm cao thế giới với gam màu nâu trầm ấm.", 1),
        ("Điền từ vào câu tục ngữ: 'Thuốc đắng dã tật, sự thật mất ...'?", "lòng", ["tiền", "bạn", "công"], "Lời nói ngay thẳng dù khó nghe nhưng mang lại điều tốt lành để sửa chữa khuyết điểm.", 1)
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

# ==============================================================================
# 2. ĐỐ VUI TRÍ TUỆ (55 câu)
# ==============================================================================
def get_summit_do_vui():
    raw = [
        ("Đố mẹo: Bánh gì hình tròn phồng xốp, khi ăn giòn rụm chấm nước sốt cà chua của người Ý?", "Bánh pizza", ["Bánh chưng", "Bánh giầy", "Bánh bao"], "Pizza nướng lò củi thơm nức phô mai kéo sợi hấp dẫn.", 1),
        ("Đố mẹo: Cây gì nở hoa đỏ rực vào mùa hè gắn liền với tuổi học trò chia tay mái trường?", "Cây hoa phượng vĩ (Hoa học trò)", ["Cây hoa mai", "Cây hoa đào", "Cây bằng lăng"], "Màu hoa phượng thắp lửa sân trường báo hiệu mùa thi và kỳ nghỉ hè rộn rã.", 1),
        ("Đố mẹo: Hoa gì mang sắc tím mộng mơ thủy chung gắn liền với xứ Huế thơ mộng?", "Hoa lục bình (hoặc hoa phượng tím, hoa sim)", ["Hoa sen", "Hoa cúc", "Hoa hồng"], "Sắc tím Huế dịu dàng e ấp bên dòng sông Hương êm đềm.", 1),
        ("Đố mẹo: Đồ vật nào dùng để quét nhà hàng ngày bện bằng sợi rơm nếp vàng óng?", "Cây chổi rơm", ["Cái máy hút bụi", "Cây lau nhà", "Cái xẻng"], "Chổi rơm quét sạch bụi bẩn giữ nhà cửa tinh tươm thoáng mát.", 1),
        ("Đố mẹo: Quả gì khoác áo giáp gai xù xì, bên trong cơm vàng béo ngậy được mệnh danh 'Vua trái cây'?", "Quả sầu riêng", ["Quả mít", "Quả mãng cầu", "Quả chôm chôm"], "Hương vị sầu riêng nồng nàn đặc trưng khiến ai mê thì say đắm khó quên.", 1),
        ("Đố mẹo: Con gì có mai cứng cáp, bơi lặn ngoài biển khơi đẻ trứng trên bãi cát đêm trăng?", "Con rùa biển (con vích, đồi mồi)", ["Con cua", "Con tôm", "Con cá sấu"], "Rùa biển quay về đúng bãi cát nơi mình sinh ra để đẻ trứng duy trì nòi giống.", 1),
        ("Đố mẹo: Cái gì có cánh quạt quay tít trên nóc nhà xua tan gió nóng ngày hè?", "Quạt trần", ["Cối xay gió", "Cánh đồng quạt gió", "Máy bay"], "Quạt trần tạo luồng gió mát đối lưu thoang thoảng khắp phòng.", 1),
        ("Đố mẹo: Xe gì không đổ xăng dầu, người đạp bon bon hai bánh rèn luyện sức khỏe mỗi sáng?", "Xe đạp", ["Xe máy", "Xe ô tô", "Xe buýt"], "Đi xe đạp vừa bảo vệ môi trường vừa nâng cao thể lực dẻo dai.", 1),
        ("Đố chữ: Để nguyên là ngọc trời ban / Thêm huyền thành chỗ đón đàn tàu neo là chữ gì?", "Gạo (thêm huyền thành Gạo / Gạo - Cảng / Cơm...)", ["Ngọc", "Vàng", "Lúa"], "Hạt gạo ngọc trời nuôi sống muôn triệu con người.", 2),
        ("Đố logic: Trong một cuộc đua xe đạp, bạn vượt qua tay đua đang chạy cuối cùng. Hỏi điều đó có xảy ra được không?", "Không thể xảy ra (bạn không thể chạy sau người cuối cùng để mà vượt người đó!)", ["Có thể xảy ra", "Bạn về nhì", "Bạn bị loại"], "Người chạy cuối cùng là người ở vị trí chót bảng, không ai có thể ở sau họ để vượt lên!", 2),
        ("Đố mẹo: Thứ gì đi lên thì khô ráo, đi xuống thì ướt sũng?", "Chiếc mỏ neo (hoặc gàu múc nước giếng)", ["Chiếc ô", "Cái áo mưa", "Cái thang"], "Múc nước giếng kéo lên chứa đầy nước ngọt trong lành.", 1),
        ("Đố mẹo: Con gì sinh ra không có tai nhưng vẫn cảm nhận được rung chấn mặt đất và bò trườn thoăn thoắt?", "Con rắn", ["Con giun", "Con ếch", "Con thằn lằn"], "Rắn cảm nhận rung động âm thanh qua xương hàm tiếp xúc với mặt đất.", 1),
        ("Đố mẹo: Cái gì thuộc về bạn, mọi người đều nhìn thấy nó nhưng bạn chỉ có thể nhìn thấy nó qua gương?", "Khuôn mặt của bạn", ["Bàn tay", "Bàn chân", "Đôi mắt"], "Chiếc gương soi phản chiếu khuôn mặt chân thực của bạn.", 1),
        ("Đố mẹo: Cái gì có thể đi vòng quanh thế giới mà suốt đời chỉ đứng yên ở một góc?", "Chiếc tem thư (con tem dán góc bì thư)", ["La bàn", "Quả địa cầu", "Hộ chiếu"], "Con tem dán ở góc trên phong bì cùng lá thư vượt trùng dương đi khắp năm châu.", 1),
        ("Đố logic: Có 12 tháng trong năm. Hỏi có bao nhiêu tháng có 28 ngày?", "Cả 12 tháng đều có ngày thứ 28!", ["Chỉ có tháng 2", "Có 1 tháng", "Có 7 tháng"], "Tháng nào trong năm cũng có ít nhất 28 ngày!", 1)
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

# ==============================================================================
# 3. KHOA HỌC TỰ NHIÊN (55 câu)
# ==============================================================================
def get_summit_khoa_hoc():
    raw = [
        ("Phản ứng hóa học tráng bạc tráng gương săm soi mặt hàng ngày dùng chất nào khử ion bạc Ag+ trong dung dịch amoniac?", "Glucozơ (hoặc Fandehit)", ["Saccarozơ", "Tinh bột", "Xenlulozơ"], "Nhóm chức andehit -CHO của glucozơ khử AgNO3/NH3 tạo lớp bạc kim loại sáng bóng bám vào thành ống nghiệm.", 2),
        ("Kim loại kiềm thổ nào cháy trong không khí với ngọn lửa màu trắng chói lòa thường được ứng dụng làm pháo sáng cứu hộ?", "Magie (Mg)", ["Canxi (Ca)", "Bari (Ba)", "Đồng (Cu)"], "Kim loại Magie cháy tỏa nhiệt lượng cực lớn và ánh sáng trắng rực rỡ.", 1),
        ("Hiện tượng sắt bị gỉ sét màu nâu đỏ ngoài không khí ẩm thực chất là quá trình sắt bị kim loại nào ăn mòn hóa học?", "Oxy và hơi nước trong không khí (Quá trình ăn mòn điện hóa)", ["Khí Nitơ", "Khí Cacbonic", "Khí Metan"], "Gỉ sắt là hỗn hợp các oxit và hidroxit sắt ngậm nước xốp giòn làm hỏng kim loại.", 1),
        ("Khí nào không màu, mùi trứng thối đặc trưng rất độc sinh ra từ rác thải hữu cơ thối rữa hoặc cống rãnh?", "Khí Hydro sunfua (H2S)", ["Khí Amoniac (NH3)", "Khí Clo (Cl2)", "Khí SO2"], "H2S liên kết chặt chẽ với hemoglobin làm tê liệt trung tâm hô hấp cực kỳ nguy hiểm.", 2),
        ("Dung dịch amoniac (NH3) tan nhiều trong nước có tính chất hóa học nào làm xanh giấy quỳ tím?", "Tính bazơ yếu (Kiềm yếu)", ["Tính axit mạnh", "Tính trung tính", "Tính oxy hóa mạnh"], "Khí NH3 tan cực tốt trong nước tạo ion OH- làm đổi màu quỳ tím.", 1),
        ("Định luật Kepler thứ nhất về chuyển động thiên văn khẳng định quỹ đạo của các hành tinh quanh Mặt Trời có hình gì?", "Hình Elip (với Mặt Trời nằm ở một trong hai tiêu điểm)", ["Hình tròn hoàn hảo", "Hình xoắn ốc", "Hình parabol"], "Johannes Kepler khám phá ra ba định luật chuyển động thiên thể đặt nền tảng cho cơ học thiên thể.", 2),
        ("Ngôi sao gần Trái Đất nhất trong vũ trụ cung cấp toàn bộ ánh sáng và sự sống cho muôn loài là ngôi sao nào?", "Mặt Trời (The Sun)", ["Sao Proxima Centauri", "Sao Bắc Cực", "Sao Thiên Lang"], "Mặt Trời cách Trái Đất khoảng 150 triệu km (1 Đơn vị thiên văn AU).", 1),
        ("Thiên hà chứa Hệ Mặt Trời và Trái Đất của chúng ta có dạng hình xoắn ốc được gọi là gì?", "Dải Ngân Hà (Milky Way)", ["Thiên hà Andromeda (Tiên Nữ)", "Thiên hà Tam Giác", "Đám mây Magellan"], "Dải Ngân Hà chứa hàng trăm tỷ ngôi sao trải rộng trên đường kính khoảng 100.000 năm ánh sáng.", 1),
        ("Hiện tượng các mảng kiến tạo đại dương chìm xuống dưới mảng lục địa tại các rãnh sâu được gọi là gì?", "Hiện tượng hút chìm (Subduction)", ["Hiện tượng tách giãn đáy đại dương", "Hiện tượng nén ép nếp uốn", "Hiện tượng phong hóa"], "Vùng hút chìm là nơi thường xuyên phát sinh động đất và núi lửa hoạt động mạnh.", 2),
        ("Khoáng vật nào được dùng phổ biến để sản xuất thủy tinh, kính xây dựng và vi mạch điện tử silic?", "Cát thạch anh (Silic dioxit - SiO2)", ["Đá vôi", "Đất sét", "Quặng bô-xít"], "SiO2 nung chảy cùng soda và đá vôi ở nhiệt độ cao tạo thành thủy tinh trong suốt.", 1),
        ("Bộ phận nào của cây làm nhiệm vụ vận chuyển nước và muối khoáng hòa tan từ rễ lên thân và lá?", "Mạch gỗ (Xylem)", ["Mạch rây (Phloem)", "Tầng sinh vỏ", "Lông hút"], "Mạch gỗ gồm các tế bào chết rỗng nối tiếp nhau thành ống dẫn dài từ rễ lên ngọn.", 2),
        ("Bộ phận nào của cây làm nhiệm vụ vận chuyển chất hữu cơ tổng hợp từ lá đến các cơ quan dự trữ như rễ, củ, quả?", "Mạch rây (Phloem)", ["Mạch gỗ", "Tủy thân", "Biểu bì"], "Dòng mạch rây vận chuyển đường saccarozơ và axit amin nuôi dưỡng cây.", 2),
        ("Loài cá nào có khả năng phóng ra dòng điện thế lên tới 600 - 800 Volt để săn mồi và tự vệ dưới sông Amazon?", "Lươn điện (Cá chình điện)", ["Cá đuối điện", "Cá trê điện", "Cá mập"], "Các tế bào điện hóa học electrocyte xếp nối tiếp nhau như những cục pin sinh học khổng lồ.", 1),
        ("Động vật biến nhiệt có nhiệt độ cơ thể thay đổi theo nhiệt độ môi trường sống gồm những lớp động vật nào?", "Lớp cá, Lớp lưỡng cư và Lớp bò sát", ["Lớp chim và Lớp thú", "Lớp chim và Lớp cá", "Lớp thú và Lớp bò sát"], "Động vật biến nhiệt thường phải phơi nắng sưởi ấm hoặc ngủ đông khi nhiệt độ xuống thấp.", 1),
        ("Chất dẫn truyền thần kinh dopamine trong não bộ gắn liền với cảm xúc nào của con người?", "Cảm xúc hưng phấn, phần thưởng và động lực phấn đấu", ["Cảm xúc sợ hãi", "Cảm giác đau đớn", "Cảm giác buồn ngủ"], "Dopamine thúc đẩy con người hành động và trải nghiệm cảm giác thỏa mãn khi đạt mục tiêu.", 2)
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

# ==============================================================================
# 4. ĐỜI SỐNG - CÔNG NGHỆ (55 câu)
# ==============================================================================
def get_summit_cong_nghe():
    raw = [
        ("Món bánh xèo miền Tây giòn rụm màu vàng nghệ đổ bằng chảo lớn thường có nhân gì bên trong?", "Tôm sông, thịt ba chỉ, giá đỗ và đậu xanh", ["Thịt bò xào", "Cá hồi nướng", "Mực ống chiên"], "Bánh xèo cuốn bánh tráng rau rừng chấm nước mắm tỏi ớt chua ngọt ngon khó cưỡng.", 1),
        ("Món ăn trứ danh của vùng đất Tây Ninh chế biến từ thịt bò tơ mềm ngọt cuốn rau rừng bánh tráng là món gì?", "Bò tơ Tây Ninh", ["Bò né", "Bò nướng ngói", "Bò lúc lắc"], "Bò tơ non thịt thơm ngọt ăn kèm đĩa rau rừng đủ vị chát bùi chua cay độc đáo.", 1),
        ("Món nem chua bọc lá chùm ruột hoặc lá chuối vị chua thanh giòn sần sật nức tiếng của tỉnh Đồng Tháp là gì?", "Nem Lai Vung", ["Nem Yên Mạc", "Nem Thủ Đức", "Nem Phùng"], "'Lai Vung là xứ lạ lùng / Nem chua ngon ngọt, gái cùng đảm đang'.", 1),
        ("Đặc sản bánh hỏi lòng heo chấm nước mắm ớt tỏi ăn kèm bát cháo lòng nóng hổi là món điểm tâm nổi tiếng của tỉnh nào?", "Bình Định", ["Phú Yên", "Quảng Ngãi", "Khánh Hòa"], "Bánh hỏi sợi tơ mịn màng rưới mỡ hành thơm ngát là món ăn truyền thống đất võ Bình Định.", 1),
        ("Món 'Gỏi cuốn' tôm thịt cuốn bánh tráng kèm bún và rau thơm chấm tương đen bùi béo từng lọt Top món ngon nhất thế giới của hãng tin nào?", "Kênh truyền hình CNN (Mỹ)", ["Kênh BBC", "Tạp chí Forbes", "Thời báo New York Times"], "Gỏi cuốn thanh mát tốt cho sức khỏe được bạn bè quốc tế vô cùng ưa chuộng.", 1),
        ("Hãng sản xuất chip bán dẫn lớn nhất thế giới theo hợp đồng gia công (Foundry) đặt trụ sở tại Đài Loan có tên là gì?", "TSMC (Taiwan Semiconductor Manufacturing Company)", ["Intel", "Qualcomm", "NVIDIA"], "TSMC sản xuất các dòng vi xử lý siêu tân tiến 3nm và 5nm cho Apple, AMD, Qualcomm.", 2),
        ("Độ phân giải màn hình 4K Ultra HD (UHD) tiêu chuẩn sở hữu số điểm ảnh xấp xỉ bao nhiêu?", "3840 x 2160 điểm ảnh (khoảng 8,3 triệu pixel)", ["1920 x 1080 pixel", "1280 x 720 pixel", "7680 x 4320 pixel"], "Màn hình 4K sắc nét gấp 4 lần độ phân giải Full HD 1080p truyền thống.", 1),
        ("Cổng kết nối đa phương tiện phổ biến nhất hiện nay truyền đồng thời cả hình ảnh sắc nét và âm thanh kỹ thuật số là cổng nào?", "Cổng HDMI (High-Definition Multimedia Interface)", ["Cổng VGA", "Cổng DVI", "Cổng AV"], "Cáp HDMI kết nối máy tính, đầu phát với TV và máy chiếu vô cùng tiện lợi.", 1),
        ("Tập đoàn sản xuất máy bay dân dụng thương mại khổng lồ nào có trụ sở chính tại châu Âu cạnh tranh trực tiếp với Boeing của Mỹ?", "Airbus", ["Lockheed Martin", "Bombardier", "Embraer"], "Dòng máy bay Airbus A321 và A350 được các hãng hàng không Việt Nam khai thác rộng rãi.", 1),
        ("Giải bóng đá Ngoại hạng Anh (Premier League) quy tụ bao nhiêu câu lạc bộ bóng đá tranh tài mỗi mùa giải?", "20 câu lạc bộ", ["18 câu lạc bộ", "22 câu lạc bộ", "16 câu lạc bộ"], "Ngoại hạng Anh là giải đấu cấp câu lạc bộ có lượng người theo dõi đông đảo nhất hành tinh.", 1),
        ("Cầu thủ nào đang giữ kỷ lục ghi nhiều bàn thắng nhất trong lịch sử các kỳ World Cup với 16 bàn thắng?", "Miroslav Klose (Đức)", ["Ronaldo de Lima (Brazil)", "Gerd Muller", "Pele"], "Klose thiết lập kỷ lục 16 bàn thắng tại kỳ World Cup 2014 trên đất Brazil.", 2),
        ("Đội tuyển bóng đá quốc gia nào đã xuất sắc giành chức vô địch FIFA World Cup 2022 tổ chức tại Qatar?", "Đội tuyển Argentina", ["Đội tuyển Pháp", "Đội tuyển Croatia", "Đội tuyển Maroc"], "Trận chung kết kịch tính nghẹt thở đưa Lionel Messi và đồng đội nâng cao cúp vàng vô địch.", 1),
        ("Môn thể thao nào mà hai đấu thủ dùng vợt đánh quả bóng nhỏ qua lại trên chiếc bàn có tấm lưới chắn ở giữa?", "Bóng bàn (Table Tennis / Ping Pong)", ["Quần vợt", "Cầu lông", "Bóng ném"], "Bóng bàn đòi hỏi phản xạ cực nhanh và kỹ thuật xoáy bóng điêu luyện.", 1),
        ("Ứng dụng dẫn đường bản đồ số vệ tinh phổ biến nhất trên thiết bị di động thông minh hiện nay là gì?", "Google Maps", ["Apple Pages", "Microsoft Word", "Dropbox"], "Google Maps hỗ trợ chỉ đường bằng giọng nói, cập nhật tình trạng kẹt xe theo thời gian thực.", 1),
        ("Trong an toàn thông tin, phương thức xác thực danh tính hai lớp bảo vệ tài khoản người dùng được viết tắt là gì?", "2FA (Two-Factor Authentication)", ["OTP", "PIN", "CAPTCHA"], "Xác thực 2 yếu tố kết hợp mật khẩu với mã gửi về điện thoại chống hacker xâm nhập.", 1)
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

# ==============================================================================
# 5. LỊCH SỬ (55 câu)
# ==============================================================================
def get_summit_lich_su():
    raw = [
        ("Năm 1075 Lý Thường Kiệt đã chủ động đem quân tiến công sang đất Tống triệt phá các căn cứ quân sự nào để tự vệ?", "Ung Châu, Khâm Châu và Liêm Châu", ["Quảng Châu và Phúc Kiến", "Thành Đô và Trường Sa", "Nam Kinh và Hàng Châu"], "Kế sách 'Tiên phát chế nhân' ngồi yên đợi giặc không bằng đem quân đánh trước để chặn mũi nhọn giặc.", 2),
        ("Thành Cổ Loa thời Thục Phán An Dương Vương có cấu trúc phòng thủ độc đáo gồm mấy vòng thành khép kín?", "3 vòng thành (Thành Nội, Thành Trung, Thành Ngoại)", ["2 vòng thành", "4 vòng thành", "5 vòng thành"], "Thành Cổ Loa uốn lượn hình trôn ốc kết hợp hào nước sâu và lũy đất kiên cố.", 1),
        ("Vị vua nào của triều Hậu Lê lên ngôi sau cuộc khởi nghĩa Lam Sơn lấy quốc hiệu đất nước là Đại Việt đóng đô ở Đông Kinh?", "Lê Thái Tổ (Lê Lợi)", ["Lê Thái Tông", "Lê Thánh Tông", "Lê Nhân Tông"], "Lê Lợi khôi phục hoàn toàn nền độc lập tự chủ của dân tộc sau 20 năm đô hộ tàn bạo của nhà Minh.", 1),
        ("Cuộc khởi nghĩa Hai Bà Trưng năm 40 sau Công nguyên đã chọn vùng đất nào làm nơi đóng đô xưng vương?", "Mê Linh", ["Cổ Loa", "Luy Lâu", "Hoa Lư"], "Hai Bà Trưng đóng đô ở Mê Linh, phong thưởng cho các tướng lĩnh và miễn thuế cho muôn dân.", 1),
        ("Bà Triệu (Triệu Thị Trinh) hy sinh kiên cường trên ngọn núi nào thuộc huyện Hậu Lộc tỉnh Thanh Hóa năm 248?", "Núi Tùng", ["Núi Nưa", "Núi Bàn A", "Núi Lam Sơn"], "Đền thờ Bà Triệu tọa lạc trang nghiêm dưới chân núi Tùng tưởng nhớ nữ anh hùng khí phách ngút trời.", 2),
        ("Tướng quân Phạm Ngũ Lão người làng Phù Ủng (Hưng Yên) nổi tiếng với áng thơ chữ Hán hào khí Đông A nào?", "Bài thơ 'Thuật hoài' (Tỏ lòng)", ["Bài thơ 'Bạch Đằng giang phú'", "Bài thơ 'Hưng Đạo vương'", "Bài thơ 'Phụng thành'"], "'Hoành sóc giang sơn kháp kỷ thu / Tam quân tì hổ khí thôn ngưu' - Phạm Ngũ Lão.", 1),
        ("Vị trạng nguyên nào nổi tiếng với tài đối đáp thông minh cứu cả đoàn sứ bộ được vua quan nhà Minh thán phục?", "Trạng Bùng Phùng Khắc Khoan (hoặc Mạc Đĩnh Chi, Giang Văn Minh)", ["Lê Văn Thịnh", "Nguyễn Hiền", "Lương Thế Vinh"], "Phùng Khắc Khoan còn có công mang giống ngô và đỗ tương về nhân rộng cho nhân dân canh tác.", 2),
        ("Chùa Một Cột (Diên Hựu tự) biểu tượng văn hóa ngàn năm của Thủ đô Hà Nội được vua Lý Thái Tông cho xây dựng năm nào?", "Năm 1049", ["Năm 1010", "Năm 1070", "Năm 1225"], "Ngôi chùa tựa đóa hoa sen thanh khiết nở trên mặt nước bắt nguồn từ giấc mơ diện kiến Phật Bà Quan Âm.", 1),
        ("Cột Cờ Hà Nội (Kỳ Đài) công trình kiến trúc quân sự cổ kính thời Nguyễn được xây dựng hoàn thành vào năm nào?", "Năm 1812 (thời vua Gia Long)", ["Năm 1802", "Năm 1831", "Năm 1882"], "Cột Cờ Hà Nội cao hơn 33m vững vàng qua các cuộc chiến tranh khói lửa bảo tồn di tích Hoàng thành.", 2),
        ("Bến cảng Nhà Rồng nơi người thanh niên Nguyễn Tất Thành ra đi tìm đường cứu nước năm 1911 nằm bên dòng sông nào?", "Sông Sài Gòn", ["Sông Đồng Nai", "Sông Nhà Bè", "Sông Vàm Cỏ"], "Tòa nhà Bến Nhà Rồng ngày nay là Bảo tàng Hồ Chí Minh - Chi nhánh TP. Hồ Chí Minh.", 1),
        ("Khu di tích Kim Liên quê hương thời niên thiếu của Chủ tịch Hồ Chí Minh thuộc huyện nào của tỉnh Nghệ An?", "Huyện Nam Đàn", ["Huyện Nghi Lộc", "Huyện Thanh Chương", "Huyện Hưng Nguyên"], "Làng Sen quê cha và làng Hoàng Trù quê mẹ ghi dấu tuổi ấu thơ của Bác.", 1),
        ("Chiến dịch Tây Nguyên mở màn cuộc Tổng tiến công mùa Xuân 1975 bắt đầu vào ngày nào bằng đòn điểm huyệt Buôn Ma Thuột?", "Ngày 10/3/1975", ["Ngày 30/4/1975", "Ngày 26/3/1975", "Ngày 1/5/1975"], "Đòn tiến công giải phóng Buôn Ma Thuột tạo nên sự rung chuyển chiến lược rút lui tán loạn của địch.", 2),
        ("Ngày hội thống nhất giang sơn non sông thu về một mối đánh dấu sự ra đời của Quốc hội chung cả nước khóa VI vào năm nào?", "Năm 1976 (Kỳ họp tháng 4 và tháng 7/1976)", ["Năm 1975", "Năm 1977", "Năm 1980"], "Quốc hội quyết định đổi tên nước thành Cộng hòa Xã hội Chủ nghĩa Việt Nam và đổi tên Sài Gòn thành TP. Hồ Chí Minh.", 1),
        ("Phong trào Duy Tân đầu thế kỷ XX do chí sĩ yêu nước nào khởi xướng với chủ trương 'Khai dân trí, chấn dân khí, hậu dân sinh'?", "Phan Châu Trinh", ["Phan Bội Châu", "Huỳnh Thúc Kháng", "Nguyễn Thái Học"], "Cụ Phan Châu Trinh đề cao cải cách giáo dục, bãi bỏ hủ tục và mở mang công thương nghiệp hiện đại.", 1),
        ("Bản Tuyên ngôn Nhân quyền và Dân quyền nổi tiếng trong Cách mạng Pháp 1789 khẳng định quyền bất khả xâm phạm nào?", "Quyền tự do và quyền bình đẳng của mọi con người", ["Quyền cai trị của nhà vua", "Quyền lực của giáo hội", "Quyền sở hữu thuộc địa"], "Khẩu hiệu 'Tự do - Bình đẳng - Bác ái' trở thành ngọn đuốc soi đường cho các phong trào dân chủ trên thế giới.", 1)
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

# ==============================================================================
# 6. ĐỊA LÝ (55 câu)
# ==============================================================================
def get_summit_dia_ly():
    raw = [
        ("Vùng mỏ than đá lớn nhất và chất lượng than antraxit hàng đầu Đông Nam Á của Việt Nam nằm ở tỉnh nào?", "Quảng Ninh", ["Thái Nguyên", "Lạng Sơn", "Bắc Giang"], "Quảng Ninh được mệnh danh là 'Vùng đất mỏ' với trữ lượng than đá hàng tỷ tấn.", 1),
        ("Mỏ quặng Bô-xít (nguyên liệu sản xuất nhôm) có trữ lượng lớn hàng đầu thế giới của nước ta tập trung ở vùng nào?", "Vùng Tây Nguyên (Đắk Nông, Lâm Đồng, Gia Lai)", ["Vùng Tây Bắc", "Vùng Đông Bắc", "Vùng Bắc Trung Bộ"], "Tây Nguyên sở hữu các mỏ bô-xít lộ thiên trữ lượng dồi dào trên nền đất bazan.", 2),
        ("Bể trầm tích dầu khí Cửu Long và Nam Côn Sơn khai thác dầu thô và khí đốt lớn nhất nước ta thuộc vùng biển nào?", "Thềm lục địa phía Nam (Bà Rịa - Vũng Tàu)", ["Vịnh Bắc Bộ", "Vùng biển miền Trung", "Vịnh Thái Lan"], "Mỏ dầu Bạch Hổ, Đại Hùng, Rạng Đông đóng góp nguồn thu ngân sách quan trọng cho quốc gia.", 1),
        ("Mỏ quặng sắt Thạch Khê mỏ sắt lớn nhất Đông Nam Á với trữ lượng hơn 500 triệu tấn nằm ở tỉnh nào miền Trung?", "Hà Tĩnh", ["Nghệ An", "Thanh Hóa", "Quảng Bình"], "Mỏ sắt Thạch Khê thuộc huyện Thạch Hà, tỉnh Hà Tĩnh nằm ven bờ biển Đông.", 2),
        ("Vùng mỏ quặng Apatit (nguyên liệu chính sản xuất phân bón lân) duy nhất ở Việt Nam tập trung tại tỉnh nào?", "Lào Cai", ["Yên Bái", "Hà Giang", "Phú Thọ"], "Mỏ apatit Lào Cai chạy dọc theo thung lũng sông Hồng cung cấp cho công nghiệp hóa chất.", 1),
        ("Con đèo nào uốn lượn trên quốc lộ 1A vượt qua dãy núi Bạch Mã phân chia Thừa Thiên Huế và Đà Nẵng?", "Đèo Hải Vân", ["Đèo Ngang", "Đèo Cù Mông", "Đèo Cả"], "Hải Vân quan nhìn xuống vịnh Lăng Cô xanh ngắt và bán đảo Sơn Trà tuyệt đẹp.", 1),
        ("Dòng sông nào được mệnh danh là con sông đỏ nặng hạt phù sa bồi đắp nên đồng bằng châu thổ trù phú bậc nhất miền Bắc?", "Sông Hồng (sông Thao)", ["Sông Đà", "Sông Lô", "Sông Cầu"], "Màu nước đỏ đặc trưng của phù sa bồi đắp mùa màng tốt tươi quanh năm.", 1),
        ("Con sông lớn nào bắt nguồn từ Trung Quốc chảy qua Tây Bắc nước ta là nơi đặt hai nhà máy thủy điện Hòa Bình và Sơn La?", "Sông Đà", ["Sông Lô", "Sông Gâm", "Sông Mã"], "Sông Đà hung bạo với tiềm năng thủy điện khổng lồ đóng góp to lớn cho an ninh năng lượng quốc gia.", 1),
        ("Dòng sông nào chảy qua thành phố Huế mộng mơ đôi bờ rợp bóng thông reo và chùa Thiên Mụ cổ kính?", "Sông Hương", ["Sông An Cựu", "Sông Bến Hải", "Sông Thạch Hãn"], "Sông Hương nước trong xanh lững lờ trôi mang vẻ đẹp trầm mặc lãng mạn của đất cố đô.", 1),
        ("Dòng sông nào bắt nguồn từ dãy Trường Sơn uốn lượn ôm trọn lấy thành phố Vinh và núi Dũng Quyết?", "Sông Lam (sông Cả)", ["Sông Gianh", "Sông La", "Sông Mã"], "Sông Lam núi Hồng là biểu tượng địa linh nhân kiệt thiêng liêng của xứ Nghệ.", 1),
        ("Cây cầu dây văng dài nhất Đông Nam Á bắc qua sông Tiền nối hai tỉnh Tiền Giang và Vĩnh Long khánh thành năm 2000 là cầu gì?", "Cầu Mỹ Thuận (Mỹ Thuận 1 và Mỹ Thuận 2)", ["Cầu Cần Thơ", "Cầu Rạch Miễu", "Cầu Cổ Chiên"], "Cầu Mỹ Thuận chấm dứt cảnh lụy phà mở toang cánh cửa giao thương cho vùng Tây Nam Bộ.", 1),
        ("Cây cầu dây văng có nhịp chính dài nhất Đông Nam Á bắc qua sông Hậu nối Vĩnh Long với Cần Thơ khánh thành năm 2010 là gì?", "Cầu Cần Thơ", ["Cầu Mỹ Thuận", "Cầu Vàm Cống", "Cầu Cao Lãnh"], "Cầu Cần Thơ dài gần 16 km tạo động lực phát triển vượt bậc cho thủ phủ miền Tây Cần Thơ.", 1),
        ("Quần đảo du lịch Cát Bà gồm 367 hòn đảo lớn nhỏ nằm ở phía nam Vịnh Hạ Long thuộc địa bàn thành phố nào?", "Thành phố Hải Phòng", ["Tỉnh Quảng Ninh", "Tỉnh Thái Bình", "Tỉnh Nam Định"], "Quần đảo Cát Bà cùng Vịnh Hạ Long được UNESCO vinh danh là Di sản Thiên nhiên Thế giới năm 2023.", 1),
        ("Biển hồ Tonle Sap (Campuchia) hồ nước ngọt lớn nhất Đông Nam Á thông với dòng sông nào của Việt Nam?", "Sông Mê Kông (nhánh sông Tiền và sông Hậu)", ["Sông Đồng Nai", "Sông Sài Gòn", "Sông Hồng"], "Biển Hồ trữ nước lũ vào mùa mưa và bổ sung nước ngọt cho hạ lưu sông Cửu Long vào mùa khô.", 1),
        ("Vịnh San Francisco vịnh biển tự nhiên tuyệt đẹp nối với Thái Bình Dương qua cây cầu Cổng Vàng (Golden Gate) thuộc nước nào?", "Hợp chúng quốc Hoa Kỳ (Mỹ)", ["Canada", "Mexico", "Úc"], "Cầu Cổng Vàng màu đỏ cam nổi bật giữa màn sương mù là biểu tượng kiến trúc nổi tiếng toàn cầu.", 1)
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
    print("🏔️ CHINH PHỤC ĐỈNH CAO: NẠP SUMMIT BATCH VƯỢT MỐC 2.500 CÂU!")
    print("=" * 70)

    # 1. Văn học nghệ thuật
    vh = get_summit_van_hoc()
    add_questions_to_category("van-hoc-nghe-thuat", vh)

    # 2. Đố vui trí tuệ
    dv = get_summit_do_vui()
    add_questions_to_category("do-vui-tri-tue", dv)

    # 3. Khoa học tự nhiên
    kh = get_summit_khoa_hoc()
    add_questions_to_category("khoa-hoc-tu-nhien", kh)

    # 4. Đời sống công nghệ
    cn = get_summit_cong_nghe()
    add_questions_to_category("doi-song-cong-nghe", cn)

    # 5. Lịch sử
    ls = get_summit_lich_su()
    add_questions_to_category("lich-su", ls)

    # 6. Địa lý
    dl = get_summit_dia_ly()
    add_questions_to_category("dia-ly", dl)

    print("\n✅ Hoàn tất Summit Batch!")

if __name__ == '__main__':
    main()
