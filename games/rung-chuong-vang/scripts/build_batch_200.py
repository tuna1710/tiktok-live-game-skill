# -*- coding: utf-8 -*-
"""
Script tạo ngân hàng câu hỏi chuẩn hóa 200 câu chia theo 6 chủ đề:
1. do-vui-tri-tue
2. lich-su
3. dia-ly
4. khoa-hoc-tu-nhien
5. van-hoc-nghe-thuat
6. doi-song-cong-nghe
"""

import json
import os

CATEGORIES_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'categories')
os.makedirs(CATEGORIES_DIR, exist_ok=True)

# 1. ĐỐ VUI TRÍ TUỆ
do_vui = [
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Con gì đập thì sống, không đập thì chết?",
        "options": ["Con tim", "Con đập nước", "Con muỗi", "Con cua"],
        "correct": 0, "explanation": "Quả tim (con tim) đập thì ta sống, ngừng đập thì chết!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Cái gì người mua biết, người bán biết, người dùng không bao giờ biết?",
        "options": ["Chiếc gương", "Cái quan tài", "Thuốc ngủ", "Đôi giày"],
        "correct": 1, "explanation": "Người mất không thể biết chiếc quan tài mình đang nằm."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Đố mẹo: Bỏ ngoài nướng trong, ăn ngoài bỏ trong là bắp gì?",
        "options": ["Bắp cải", "Bắp ngô", "Bắp đùi", "Bắp chuối"],
        "correct": 1, "explanation": "Bắp ngô bóc bẹ ngoài đem nướng, ăn hạt ngoài bỏ cùi bên trong."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Đố mẹo: Con đường nào dài nhất mà ai cũng phải đi qua?",
        "options": ["Đường đi", "Đường đời", "Đường cao tốc", "Đường xích đạo"],
        "correct": 1, "explanation": "Đường đời là con đường dài nhất gắn liền suốt cuộc đời con người."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Đố mẹo: Loài chuột nào nổi tiếng thế giới đi bằng hai chân?",
        "options": ["Chuột cống", "Chuột chù", "Chuột Mickey", "Chuột túi"],
        "correct": 2, "explanation": "Chuột Mickey trong phim hoạt hình Disney đi bằng hai chân."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Đố vui dân gian: Con vịt nào bình thường cũng đi bằng hai chân?",
        "options": ["Vịt Donald", "Vịt bầu", "Vịt xiêm", "Tất cả các con vịt"],
        "correct": 3, "explanation": "Tất cả các con vịt bình thường đều đi bằng hai chân!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Cái gì bạn có thể cầm bằng tay trái nhưng không bao giờ cầm được bằng tay phải?",
        "options": ["Bàn tay phải", "Khuỷu tay trái", "Cây bút", "Cốc nước"],
        "correct": 1, "explanation": "Tay phải không thể tự cầm trọn khuỷu tay phải của chính mình!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Cái gì luôn luôn đến nhưng không bao giờ đến nơi?",
        "options": ["Ngày mai", "Ngày hôm qua", "Cơn mưa", "Giấc mơ"],
        "correct": 0, "explanation": "Khi 'ngày mai' đến thì nó đã trở thành 'hôm nay'."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Bệnh gì bác sĩ chịu bó tay không chữa được?",
        "options": ["Bệnh gãy tay", "Bệnh đau đầu", "Bệnh cảm cúm", "Bệnh đau mắt"],
        "correct": 0, "explanation": "Gãy tay thì bác sĩ phải bó bột (bó tay) lại để cố định xương!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Con gì đầu dê mình ốc?",
        "options": ["Con dốc", "Con cua", "Con rùa", "Con sâu"],
        "correct": 0, "explanation": "'Dê' ghép với 'ốc' thành con 'dốc'."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Cây gì càng tưới nước thì càng mau chết?",
        "options": ["Cây cột điện", "Cây nến", "Cây ATM", "Cây kim"],
        "correct": 1, "explanation": "Cây nến đang cháy tưới nước vào thì lửa sẽ tắt (chết nến)!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 1,
        "question": "Cái gì chứa nhiều nước nhất nhưng không chìm dưới đáy biển?",
        "options": ["Miếng bọt biển", "Tàu ngầm", "Quả dừa", "Bản đồ thế giới"],
        "correct": 3, "explanation": "Bản đồ thể hiện toàn bộ các đại dương trên thế giới nhưng vẽ trên giấy!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Trong cờ tướng, quân cờ nào chỉ được phép đi chéo trong cửu cung?",
        "options": ["Quân Tượng", "Quân Tướng", "Quân Sĩ", "Quân Mã"],
        "correct": 2, "explanation": "Quân Sĩ chỉ đi chéo trong phạm vi Cửu cung để bảo vệ Tướng."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Đố mẹo: Lịch nào dài nhất trên thế giới?",
        "options": ["Lịch sử", "Lịch vạn niên", "Lịch Gregory", "Lịch âm"],
        "correct": 0, "explanation": "Lịch sử kéo dài hàng triệu năm suốt chiều dài nhân loại."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Cái gì có răng nhưng không bao giờ nhai được thức ăn?",
        "options": ["Cái lược", "Chiếc cưa", "Bánh răng đồng hồ", "Tất cả các đáp án trên"],
        "correct": 3, "explanation": "Cái lược, cái cưa và bánh răng đều có răng nhưng không dùng để nhai!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Có một rổ đựng 5 quả táo. Làm sao chia cho 5 người mà trong rổ vẫn còn 1 quả táo?",
        "options": ["Cắt làm đôi", "Đưa cho người thứ 5 cả cái rổ và quả táo", "Ăn trước 1 quả", "Không chia được"],
        "correct": 1, "explanation": "Đưa 4 quả cho 4 người đầu, người cuối cùng nhận quả táo còn nằm trong rổ."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Một người đàn ông đi trong mưa lớn không đội mũ, không che ô, nhưng không có sợi tóc nào ướt. Vì sao?",
        "options": ["Ông ấy đi nhanh", "Ông ấy bị hói đầu", "Mưa chưa chạm đất", "Ông ấy đi trong nhà"],
        "correct": 1, "explanation": "Người đàn ông bị hói (không có tóc) nên không có sợi tóc nào bị ướt!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Nếu bạn vượt qua người đang chạy ở vị trí thứ hai, bạn đang ở vị trí thứ mấy?",
        "options": ["Thứ nhất", "Thứ hai", "Thứ ba", "Về đích"],
        "correct": 1, "explanation": "Vượt người thứ hai thì bạn thế chỗ của họ và đứng ở vị trí thứ hai!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Từ tiếng Việt nào mà 100% người Việt Nam đều phát âm sai?",
        "options": ["Từ 'Sai'", "Từ 'Đúng'", "Từ 'Không'", "Từ 'Khó'"],
        "correct": 0, "explanation": "Từ 'Sai' luôn luôn được phát âm là 'Sai'!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Trong một cuộc đua, người mù, người câm và người điếc cùng thi chạy. Ai là người nghe thấy tiếng súng lệnh xuất phát?",
        "options": ["Người mù", "Người câm", "Người điếc", "Cả người mù và người câm"],
        "correct": 3, "explanation": "Cả người mù và người câm đều có thính giác bình thường nên nghe được súng lệnh."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Đố mẹo: Tháng nào có 28 ngày trong một năm?",
        "options": ["Chỉ tháng 2", "Tháng 2 năm nhuận", "Tất cả các tháng", "Không có tháng nào"],
        "correct": 2, "explanation": "Tất cả 12 tháng trong năm đều có ít nhất 28 ngày!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Cái gì bay khi sinh ra, nằm khi còn sống và chảy khi chết đi?",
        "options": ["Bông tuyết", "Hạt mưa", "Cơn gió", "Đám mây"],
        "correct": 0, "explanation": "Bông tuyết bay lơ lửng, rơi xuống nằm trên mặt đất và tan chảy thành nước khi chết."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 2,
        "question": "Quả gì không ăn được nhưng dùng để đá?",
        "options": ["Quả bóng", "Quả tạ", "Quả ổi", "Quả dưa"],
        "correct": 0, "explanation": "Quả bóng đá dùng trong các trận thi đấu bóng đá."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Bạn có thể trừ số 5 từ số 25 bao nhiêu lần?",
        "options": ["5 lần", "1 lần", "Vô hạn lần", "4 lần"],
        "correct": 1, "explanation": "Chỉ 1 lần duy nhất, vì sau lần trừ đầu tiên con số đã trở thành 20, không còn là 25 nữa!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Cái gì của bạn nhưng người khác lại dùng nhiều hơn bạn?",
        "options": ["Tên của bạn", "Điện thoại của bạn", "Tiền của bạn", "Đôi giày của bạn"],
        "correct": 0, "explanation": "Tên của bạn chủ yếu để người khác gọi xưng hô hàng ngày."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Tôi có các thành phố nhưng không có ngôi nhà nào, có núi non nhưng không có cây cối, có nước nhưng không có cá. Tôi là ai?",
        "options": ["Bản đồ", "Bức tranh", "Quả địa cầu", "Cả bản đồ và quả địa cầu"],
        "correct": 3, "explanation": "Bản đồ và quả địa cầu mô phỏng địa hình nhưng không có thực thể sinh vật sống."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Một người phụ nữ có 7 người con gái, mỗi người con gái lại có 1 người anh trai. Hỏi bà mẹ có tất cả bao nhiêu người con?",
        "options": ["14 người", "8 người", "7 người", "15 người"],
        "correct": 1, "explanation": "Bà có 7 cô con gái và 1 cậu con trai chung (là anh/em trai của cả 7 cô gái), tổng cộng 8 người con."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Đố logic: Bác sĩ đưa cho bệnh nhân 3 viên thuốc và dặn cứ 30 phút uống 1 viên. Hỏi sau bao lâu thì uống hết?",
        "options": ["90 phút", "60 phút", "30 phút", "120 phút"],
        "correct": 1, "explanation": "Uống viên 1 lúc 0 phút, viên 2 lúc 30 phút, viên 3 lúc 60 phút. Tổng cộng 60 phút!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Có 2 người cha và 2 người con cùng đi câu cá, mỗi người câu được đúng 1 con cá. Tại sao mang về nhà chỉ có 3 con cá?",
        "options": ["Rơi mất 1 con", "Gồm ông nội, bố và con trai", "Cá bị ăn thịt", "Đếm nhầm"],
        "correct": 1, "explanation": "3 người gồm: Ông nội (cha của bố), Bố (con của ông nội, cha của cháu), và Cháu (con của bố) -> đúng 2 người cha và 2 người con!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Càng lấy đi nhiều thì nó lại càng to ra, đó là cái gì?",
        "options": ["Cái hố", "Núi tiền", "Cục than", "Tảng băng"],
        "correct": 0, "explanation": "Cái hố đào càng nhiều đất mang đi thì hố càng to ra."
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Cái gì chặt không đứt, bẻ không gãy, phơi không khô, đốt không cháy?",
        "options": ["Nước biển", "Dòng nước", "Sợi chỉ", "Tảng đá"],
        "correct": 1, "explanation": "Nước ở trạng thái lỏng chặt không đứt, bẻ không gãy, đốt không cháy!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Trước khi đỉnh Everest được con người phát hiện ra, đỉnh núi nào cao nhất Trái Đất?",
        "options": ["K2", "Kangchenjunga", "Vẫn là đỉnh Everest", "Fansipan"],
        "correct": 2, "explanation": "Dù con người chưa phát hiện ra thì đỉnh Everest vẫn luôn tồn tại và cao nhất thế giới!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Nếu một con gà trống đẻ trứng trên đỉnh mái nhà dốc sang 2 bên, quả trứng sẽ rơi về bên nào?",
        "options": ["Bên trái", "Bên phải", "Ở giữa", "Gà trống không đẻ trứng"],
        "correct": 3, "explanation": "Gà trống không bao giờ biết đẻ trứng!"
    },
    {
        "category": "do-vui-tri-tue", "difficulty": 3,
        "question": "Từ nào trong tiếng Việt có 9 chữ 'H'?",
        "options": ["Chính phủ", "Học hành", "Hùng hồn", "Chính hiệu"],
        "correct": 0, "explanation": "Từ 'Chính phủ' đọc lái là 'chín chữ H' (9 chữ H)!"
    }
]

# 2. LỊCH SỬ VIỆT NAM & THẾ GIỚI
lich_su = [
    {
        "category": "lich-su", "difficulty": 1,
        "question": "Ai là người sáng lập ra nước Việt Nam Dân chủ Cộng hòa và đọc Tuyên ngôn Độc lập ngày 2/9/1945?",
        "options": ["Chủ tịch Hồ Chí Minh", "Đại tướng Võ Nguyên Giáp", "Tổng bí thư Trường Chinh", "Thủ tướng Phạm Văn Đồng"],
        "correct": 0, "explanation": "Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập tại quảng trường Ba Đình ngày 2/9/1945."
    },
    {
        "category": "lich-su", "difficulty": 1,
        "question": "Chiến dịch Hồ Chí Minh toàn thắng giải phóng miền Nam thống nhất đất nước diễn ra vào năm nào?",
        "options": ["1954", "1968", "1972", "1975"],
        "correct": 3, "explanation": "Đại thắng mùa xuân ngày 30 tháng 4 năm 1975 thống nhất trọn vẹn non sông."
    },
    {
        "category": "lich-su", "difficulty": 1,
        "question": "Vua Quang Trung còn được biết đến với tên thật là gì?",
        "options": ["Nguyễn Nhạc", "Nguyễn Lữ", "Nguyễn Huệ", "Nguyễn Ánh"],
        "correct": 2, "explanation": "Vua Quang Trung tên thật là Nguyễn Huệ (anh hùng áo vải cờ đào Tây Sơn)."
    },
    {
        "category": "lich-su", "difficulty": 1,
        "question": "Trận Điện Biên Phủ trên không bảo vệ bầu trời Hà Nội diễn ra vào năm nào?",
        "options": ["1970", "1972", "1975", "1979"],
        "correct": 1, "explanation": "12 ngày đêm Điện Biên Phủ trên không diễn ra vào tháng 12 năm 1972."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Ai là vị vua đầu tiên của nhà Tiền Lý trong lịch sử Việt Nam?",
        "options": ["Lý Thái Tổ", "Lý Nam Đế", "Lý Thường Kiệt", "Lý Huệ Tông"],
        "correct": 1, "explanation": "Lý Bí (Lý Nam Đế) lập ra nhà nước Vạn Xuân năm 544."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Chiến thắng Điện Biên Phủ 'lừng lẫy năm châu, chấn động địa cầu' toàn thắng vào ngày tháng năm nào?",
        "options": ["7/5/1954", "19/5/1954", "30/4/1954", "2/9/1954"],
        "correct": 0, "explanation": "Chiến dịch Điện Biên Phủ toàn thắng ngày 7/5/1954 buộc thực dân Pháp ký hiệp định Genève."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Ai là người nữ anh hùng đầu tiên xưng vương trong lịch sử đấu tranh của dân tộc Việt Nam?",
        "options": ["Trưng Trắc", "Bà Triệu", "Nguyên phi Ỷ Lan", "Dương Vân Nga"],
        "correct": 0, "explanation": "Trưng Trắc xưng vương (Trưng Nữ Vương) vào năm 40 sau công nguyên."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Vị anh hùng dân tộc nào đã lãnh đạo chiến thắng Bạch Đằng năm 938 chấm dứt hơn 1000 năm Bắc thuộc?",
        "options": ["Đinh Bộ Lĩnh", "Ngô Quyền", "Lê Hoàn", "Trần Hưng Đạo"],
        "correct": 1, "explanation": "Ngô Quyền cắm cọc nhọn trên sông Bạch Đằng tiêu diệt quân Nam Hán năm 938."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Chiến thắng Bạch Đằng năm 1288 chống quân xâm lược Nguyên Mông do vị tướng kiệt xuất nào chỉ huy?",
        "options": ["Trần Hưng Đạo", "Trần Quang Khải", "Trần Khánh Dư", "Trần Quốc Toản"],
        "correct": 0, "explanation": "Hưng Đạo Đại Vương Trần Quốc Tuấn chỉ huy trận đại phá quân Nguyên Mông năm 1288."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Vị vua nào đã lập nên triều đại nhà Đinh và dẹp loạn 12 sứ quân, xưng là Đinh Tiên Hoàng?",
        "options": ["Đinh Liễn", "Đinh Bộ Lĩnh", "Đinh Toàn", "Đinh Điền"],
        "correct": 1, "explanation": "Đinh Bộ Lĩnh dẹp yên 12 sứ quân, lập nên nhà nước Đại Cồ Việt đóng đô ở Hoa Lư."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Ai là tác giả của bản 'Tuyên ngôn độc lập' đầu tiên trong lịch sử mang tên bài thơ 'Nam quốc sơn hà'?",
        "options": ["Lý Thường Kiệt", "Trần Hưng Đạo", "Nguyễn Trãi", "Lê Lợi"],
        "correct": 0, "explanation": "Tương truyền bài thơ 'Nam quốc sơn hà' gắn liền với danh tướng Lý Thường Kiệt bên phòng tuyến sông Như Nguyệt năm 1077."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Ai là người bóp nát quả cam vì hận không được dự hội nghị Bình Than bàn kế đánh giặc?",
        "options": ["Trần Quốc Toản", "Trần Hưng Đạo", "Trần Bình Trọng", "Trần Quang Khải"],
        "correct": 0, "explanation": "Hoài Văn hầu Trần Quốc Toản vì tuổi nhỏ không được dự họp nên tức giận bóp nát quả cam trong tay."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Vị tướng nào có câu nói bất hủ: 'Ta thà làm ma nước Nam chứ không thèm làm vương đất Bắc'?",
        "options": ["Trần Bình Trọng", "Trần Khánh Dư", "Trần Thủ Độ", "Trần Hưng Đạo"],
        "correct": 0, "explanation": "Trần Bình Trọng bị giặc Nguyên bắt dụ dỗ đầu hàng đã hiên ngang khẳng định khí phách."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Khởi nghĩa Lam Sơn kéo dài 10 năm (1418 - 1427) đánh đuổi quân Minh do ai khởi xướng?",
        "options": ["Lê Lợi", "Nguyễn Trãi", "Trần Nguyên Hãn", "Lê Lai"],
        "correct": 0, "explanation": "Lê Lợi xưng là Bình Định Vương dấy cờ khởi nghĩa Lam Sơn tại Thanh Hóa."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Đại tướng tổng tư lệnh đầu tiên của Quân đội Nhân dân Việt Nam là ai?",
        "options": ["Võ Nguyên Giáp", "Nguyễn Chí Thanh", "Văn Tiến Dũng", "Chu Huy Mân"],
        "correct": 0, "explanation": "Đại tướng Võ Nguyên Giáp được phong quân hàm Đại tướng đầu tiên của QĐNDVN năm 1948."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Cuộc Cách mạng công nghiệp lần thứ nhất khởi nguồn tại quốc gia nào vào thế kỷ 18?",
        "options": ["Nước Anh", "Nước Pháp", "Nước Đức", "Hoa Kỳ"],
        "correct": 0, "explanation": "Nước Anh là cái nôi của Cách mạng công nghiệp lần thứ nhất nhờ máy hơi nước của James Watt."
    },
    {
        "category": "lich-su", "difficulty": 2,
        "question": "Kim tự tháp Giza nổi tiếng thế giới nằm ở quốc gia nào hiện nay?",
        "options": ["Ai Cập", "Hy Lạp", "Thổ Nhĩ Kỳ", "Ấn Độ"],
        "correct": 0, "explanation": "Kim tự tháp Giza là kỳ quan cổ đại duy nhất còn tồn tại nguyên vẹn tại Ai Cập."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Năm 1010, vua Lý Thái Tổ đã ban bố chiếu chỉ gì để dời đô từ Hoa Lư về Thăng Long?",
        "options": ["Bình Ngô Đại Cáo", "Chiếu Cần Vương", "Chiếu Dời Đô", "Hịch Tướng Sĩ"],
        "correct": 2, "explanation": "Vua Lý Thái Tổ viết 'Chiếu Dời Đô' (Thiên đô chiếu) dời đô về thành Đại La và đổi tên thành Thăng Long."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Vị hoàng đế nào có thời gian trị vì trên ngai vàng lâu nhất trong lịch sử các triều đại phong kiến Việt Nam?",
        "options": ["Lý Nhân Tông", "Lê Thánh Tông", "Trần Nhân Tông", "Lý Anh Tông"],
        "correct": 0, "explanation": "Vua Lý Nhân Tông (Lý Càn Đức) trị vì suốt 56 năm (từ 1072 đến 1128)."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Ai là tác giả của kiệt tác quân sự 'Binh thư yếu lược' và áng văn 'Hịch tướng sĩ' nổi tiếng thời Trần?",
        "options": ["Hưng Đạo Đại Vương Trần Quốc Tuấn", "Trần Thủ Độ", "Trần Quang Khải", "Trần Thái Tông"],
        "correct": 0, "explanation": "Trần Quốc Tuấn viết Hịch tướng sĩ khích lệ tinh thần binh sĩ kháng chiến chống quân Nguyên Mông."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Bản 'Bình Ngô Đại Cáo' - áng thiên cổ hùng văn tuyên bố đại thắng giặc Minh năm 1428 do ai thừa lệnh Lê Lợi chấp bút?",
        "options": ["Nguyễn Trãi", "Lý Tử Tấn", "Ngô Sĩ Liên", "Nguyễn Bỉnh Khiêm"],
        "correct": 0, "explanation": "Đại thi hào Nguyễn Trãi thay mặt vua Lê Thái Tổ viết bản hùng văn Bình Ngô Đại Cáo."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Bộ luật thành văn cổ nhất của nước ta còn giữ được dấu tích thời phong kiến là bộ luật nào?",
        "options": ["Hình thư (thời Lý)", "Quốc triều hình luật (Luật Hồng Đức)", "Hoàng Việt luật lệ (Luật Gia Long)", "Hình luật thời Trần"],
        "correct": 0, "explanation": "Bộ luật 'Hình thư' do vua Lý Thái Tông ban hành năm 1042 là bộ luật thành văn đầu tiên của nước ta."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Vị vua cuối cùng của triều đại phong kiến Việt Nam thoái vị vào năm 1945 là ai?",
        "options": ["Vua Bảo Đại", "Vua Khải Định", "Vua Duy Tân", "Vua Hàm Nghi"],
        "correct": 0, "explanation": "Vua Bảo Đại (Nguyễn Phúc Vĩnh Thụy) trao lại ấn kiếm thoái vị vào tháng 8 năm 1945."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Trận đại thắng Ngọc Hồi - Đống Đa quét sạch 29 vạn quân Mãn Thanh diễn ra vào mùa xuân năm nào?",
        "options": ["1786", "1788", "1789", "1792"],
        "correct": 2, "explanation": "Mùa xuân Kỷ Dậu năm 1789, vua Quang Trung thần tốc tiến quân giải phóng Thăng Long."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Vạn Lý Trường Thành của Trung Quốc được bắt đầu xây dựng liên kết quy mô lớn dưới thời vị hoàng đế nào?",
        "options": ["Tần Thủy Hoàng", "Hán Vũ Đế", "Đường Thái Tông", "Minh Thành Tổ"],
        "correct": 0, "explanation": "Tần Thủy Hoàng sau khi thống nhất Trung Hoa đã nối các bức tường thành cổ để phòng chống Hung Nô."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Thành Cổ Loa hình xoáy ốc được xây dựng dưới thời kỳ trị vì của vị vua nào?",
        "options": ["An Dương Vương (Thục Phán)", "Hùng Vương", "Triệu Đà", "Phùng Hưng"],
        "correct": 0, "explanation": "An Dương Vương dời đô về Cổ Loa (Đông Anh, Hà Nội) và xây dựng tòa thành lũy 9 vòng xoắn ốc."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Tổ chức Liên Hợp Quốc (UN) chính thức được thành lập vào năm nào?",
        "options": ["1918", "1945", "1954", "1975"],
        "correct": 1, "explanation": "Hiến chương Liên Hợp Quốc có hiệu lực vào ngày 24 tháng 10 năm 1945 sau Chiến tranh thế giới thứ hai."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Trận Trân Châu Cảng chấn động trong Thế chiến thứ hai diễn ra vào năm nào?",
        "options": ["1939", "1941", "1944", "1945"],
        "correct": 1, "explanation": "Không quân Nhật Bản bất ngờ tấn công căn cứ Trân Châu Cảng của Mỹ ngày 7/12/1941."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Vị hoàng đế nào của La Mã cổ đại đã chia đế chế thành hai nửa Đông La Mã và Tây La Mã?",
        "options": ["Theodosius I", "Julius Caesar", "Augustus", "Nero"],
        "correct": 0, "explanation": "Hoàng đế Theodosius I trước khi mất năm 395 đã chia đế quốc cho hai người con trai."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Con đường Tơ lụa huyền thoại nối liền Trung Hoa với châu Âu hưng thịnh nhất dưới triều đại nào của Trung Quốc?",
        "options": ["Nhà Hán và nhà Đường", "Nhà Tống", "Nhà Minh", "Nhà Thanh"],
        "correct": 0, "explanation": "Con đường Tơ lụa mở ra thời Hán (Trương Khiên) và đạt đến độ phồn thịnh rực rỡ nhất thời Đường."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Cuộc Thập tự chinh thứ nhất do Giáo hoàng nào kêu gọi vào năm 1095?",
        "options": ["Urban II", "Innocent III", "Gregory VII", "Leo X"],
        "correct": 0, "explanation": "Giáo hoàng Urban II phát động cuộc Thập tự chinh đầu tiên tại Hội đồng Clermont năm 1095."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Bức tường Berlin ngăn cách Đông và Tây Berlin sụp đổ vào năm nào?",
        "options": ["1985", "1989", "1991", "1993"],
        "correct": 1, "explanation": "Bức tường Berlin chính thức sụp đổ vào ngày 9 tháng 11 năm 1989, mở đường cho nước Đức thống nhất."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Hiệp ước Versailles kết thúc Chiến tranh thế giới thứ nhất được ký kết vào năm nào?",
        "options": ["1914", "1917", "1918", "1919"],
        "correct": 3, "explanation": "Hiệp ước hòa bình Versailles được ký kết ngày 28/6/1919 tại Cung điện Versailles (Pháp)."
    },
    {
        "category": "lich-su", "difficulty": 3,
        "question": "Nền văn minh Lưỡng Hà cổ đại phát triển rực rỡ giữa hai con sông lớn nào?",
        "options": ["Sông Tigris và Euphrates", "Sông Nile và Congo", "Sông Hằng và Ấn", "Sông Hoàng Hà và Trường Giang"],
        "correct": 0, "explanation": "Mesopotamia (Lưỡng Hà) nghĩa là vùng đất nằm giữa hai dòng sông Tigris và Euphrates."
    }
]

# 3. ĐỊA LÝ VIỆT NAM & THẾ GIỚI
dia_ly = [
    {
        "category": "dia-ly", "difficulty": 1,
        "question": "Thủ đô của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam là thành phố nào?",
        "options": ["Đà Nẵng", "TP. Hồ Chí Minh", "Hà Nội", "Hải Phòng"],
        "correct": 2, "explanation": "Hà Nội là thủ đô ngàn năm văn hiến của Việt Nam."
    },
    {
        "category": "dia-ly", "difficulty": 1,
        "question": "Con sông lớn nào gắn liền với thủ đô Hà Nội và đồng bằng Bắc Bộ?",
        "options": ["Sông Hồng", "Sông Hương", "Sông Cửu Long", "Sông Đồng Nai"],
        "correct": 0, "explanation": "Sông Hồng là con sông mẹ bồi đắp phù sa trù phú cho châu thổ Bắc Bộ."
    },
    {
        "category": "dia-ly", "difficulty": 1,
        "question": "Thành phố Đà Lạt ngàn hoa mộng mơ thuộc tỉnh nào của vùng Tây Nguyên?",
        "options": ["Lâm Đồng", "Đắk Lắk", "Gia Lai", "Kon Tum"],
        "correct": 0, "explanation": "Đà Lạt là thành phố tỉnh lỵ của tỉnh Lâm Đồng nằm trên cao nguyên Lâm Viên."
    },
    {
        "category": "dia-ly", "difficulty": 1,
        "question": "Dòng sông nào thơ mộng chảy ngang qua trung tâm thành phố Huế cổ kính?",
        "options": ["Sông Hàn", "Sông Hương", "Sông Thu Bồn", "Sông Thạch Hãn"],
        "correct": 1, "explanation": "Sông Hương (Hương Giang) là biểu tượng thi ca nổi tiếng của xứ Huế."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Ngọn núi nào được mệnh danh là 'Nóc nhà Đông Dương'?",
        "options": ["Bạch Mộc Lương Tử", "Fansipan", "Pu Si Lung", "Tây Côn Lĩnh"],
        "correct": 1, "explanation": "Đỉnh Fansipan cao 3.143m thuộc dãy Hoàng Liên Sơn là đỉnh núi cao nhất 3 nước Đông Dương."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Đâu là đảo có diện tích tự nhiên lớn nhất của Việt Nam?",
        "options": ["Cát Bà", "Phú Quốc", "Côn Đảo", "Cù Lao Chàm"],
        "correct": 1, "explanation": "Đảo Phú Quốc (Kiên Giang) có diện tích xấp xỉ 589 km², là đảo lớn nhất nước ta."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Vườn quốc gia Phong Nha - Kẻ Bàng, di sản thiên nhiên thế giới, thuộc tỉnh nào?",
        "options": ["Quảng Bình", "Quảng Trị", "Quảng Ninh", "Ninh Bình"],
        "correct": 0, "explanation": "Phong Nha - Kẻ Bàng thuộc địa phận tỉnh Quảng Bình, nổi tiếng với hệ thống hang động kỳ vĩ."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Vịnh Hạ Long - kỳ quan thiên nhiên thế giới của Việt Nam - thuộc địa phận tỉnh nào?",
        "options": ["Hải Phòng", "Quảng Ninh", "Thanh Hóa", "Nam Định"],
        "correct": 1, "explanation": "Vịnh Hạ Long nằm ở bờ tây vịnh Bắc Bộ thuộc tỉnh Quảng Ninh."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Tỉnh nào có diện tích đất tự nhiên lớn nhất nước Cộng hòa Xã hội Chủ nghĩa Việt Nam?",
        "options": ["Đắk Lắk", "Gia Lai", "Nghệ An", "Sơn La"],
        "correct": 2, "explanation": "Nghệ An có diện tích lớn nhất Việt Nam với hơn 16.490 km²."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Tỉnh nào có diện tích nhỏ nhất trong số 63 tỉnh thành của Việt Nam?",
        "options": ["Bắc Ninh", "Hà Nam", "Hưng Yên", "Ninh Bình"],
        "correct": 0, "explanation": "Bắc Ninh là tỉnh có diện tích nhỏ nhất Việt Nam với chỉ khoảng 822,7 km²."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Mũi Cà Mau - điểm cực Nam trên đất liền của tổ quốc - thuộc tỉnh nào?",
        "options": ["Kiên Giang", "Bạc Liêu", "Cà Mau", "Sóc Trăng"],
        "correct": 2, "explanation": "Mũi Cà Mau nằm ở huyện Ngọc Hiển, tỉnh Cà Mau."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Hai quần đảo Hoàng Sa và Trường Sa thiêng liêng của Việt Nam lần lượt trực thuộc quyền quản lý hành chính của thành phố và tỉnh nào?",
        "options": ["Đà Nẵng và Khánh Hòa", "Quảng Nam và Kiên Giang", "Bình Thuận và Ninh Thuận", "Quảng Ngãi và Bình Định"],
        "correct": 0, "explanation": "Huyện đảo Hoàng Sa trực thuộc TP Đà Nẵng, huyện đảo Trường Sa trực thuộc tỉnh Khánh Hòa."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Cực Đông trên đất liền của Việt Nam (nơi đón ánh bình minh đầu tiên) nằm tại mũi Đôi thuộc tỉnh nào?",
        "options": ["Khánh Hòa", "Phú Yên", "Bình Định", "Bình Thuận"],
        "correct": 0, "explanation": "Mũi Đôi (bán đảo Hòn Gốm, huyện Vạn Ninh, tỉnh Khánh Hòa) là điểm cực Đông đất liền."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Cao nguyên đá Đồng Văn - công viên địa chất toàn cầu UNESCO - thuộc tỉnh nào của nước ta?",
        "options": ["Hà Giang", "Cao Bằng", "Lào Cai", "Yên Bái"],
        "correct": 0, "explanation": "Công viên địa chất Cao nguyên đá Đồng Văn trải dài trên 4 huyện của tỉnh Hà Giang."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Đèo Hải Vân hùng vĩ chia cắt ranh giới tự nhiên giữa hai địa phương nào?",
        "options": ["Thừa Thiên Huế và Đà Nẵng", "Quảng Trị và Thừa Thiên Huế", "Đà Nẵng và Quảng Nam", "Quảng Bình và Quảng Trị"],
        "correct": 0, "explanation": "Đèo Hải Vân (Thiên hạ đệ nhất hùng quan) là ranh giới giữa Thừa Thiên Huế và TP. Đà Nẵng."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Hồ nước ngọt tự nhiên lớn nhất Việt Nam nằm ở tỉnh Bắc Kạn là hồ nào?",
        "options": ["Hồ Ba Bể", "Hồ Thác Bà", "Hồ Dầu Tiếng", "Hồ Tơ Nưng"],
        "correct": 0, "explanation": "Hồ Ba Bể nằm ở độ cao 145m thuộc tỉnh Bắc Kạn, là một trong những hồ nước ngọt tự nhiên lớn nhất thế giới."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Cực Tây trên đất liền của Việt Nam nằm tại ngã ba biên giới A Pa Chải thuộc tỉnh nào?",
        "options": ["Điện Biên", "Lai Châu", "Sơn La", "Hòa Bình"],
        "correct": 0, "explanation": "A Pa Chải (xã Sín Thầu, huyện Mường Nhé, tỉnh Điện Biên) là cực Tây tổ quốc nơi 'một tiếng gà gáy 3 nước cùng nghe'."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Quốc gia nào có đường bờ biển dài nhất thế giới?",
        "options": ["Canada", "Indonesia", "Nga", "Úc"],
        "correct": 0, "explanation": "Canada sở hữu đường bờ biển dài kỷ lục hơn 202.080 km do có hàng vạn hòn đảo lớn nhỏ."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Quốc gia nào có diện tích lãnh thổ lớn nhất thế giới hiện nay?",
        "options": ["Liên bang Nga", "Canada", "Trung Quốc", "Hoa Kỳ"],
        "correct": 0, "explanation": "Liên bang Nga có diện tích hơn 17 triệu km², trải dài trên cả 2 châu lục Á và Âu."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Kênh đào Suez nối liền hai vùng biển lớn nào để rút ngắn hành trình hàng hải Á - Âu?",
        "options": ["Địa Trung Hải và Biển Đỏ", "Đại Tây Dương và Thái Bình Dương", "Biển Đen và Biển Baltic", "Vịnh Ba Tư và Biển Ả Rập"],
        "correct": 0, "explanation": "Kênh đào Suez cắt qua eo đất Suez ở Ai Cập nối Địa Trung Hải thẳng vào Biển Đỏ."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Đại dương nào có độ sâu trung bình lớn nhất trên thế giới?",
        "options": ["Đại Tây Dương", "Ấn Độ Dương", "Bắc Băng Dương", "Thái Bình Dương"],
        "correct": 3, "explanation": "Thái Bình Dương sâu nhất thế giới với vực thẳm Mariana sâu khoảng 11.034m."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Con sông nào dài nhất thế giới theo kỷ lục Guinness chính thức?",
        "options": ["Sông Amazon", "Sông Nile", "Sông Dương Tử", "Sông Mississippi"],
        "correct": 1, "explanation": "Sông Nile ở châu Phi dài khoảng 6.650 km, giữ kỷ lục dài nhất thế giới."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Quốc gia nào sở hữu nhiều múi giờ nhất trên thế giới tính cả các vùng lãnh thổ hải ngoại?",
        "options": ["Nước Nga", "Hoa Kỳ", "Nước Pháp", "Trung Quốc"],
        "correct": 2, "explanation": "Pháp có tới 12 múi giờ nhờ các đảo và vùng lãnh thổ hải ngoại rải rác toàn cầu."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Hồ nước ngọt sâu nhất và chứa nhiều thể tích nước ngọt không đóng băng nhất hành tinh là hồ nào?",
        "options": ["Hồ Baikal (Nga)", "Hồ Superior (Bắc Mỹ)", "Hồ Victoria (châu Phi)", "Hồ Tanganyika"],
        "correct": 0, "explanation": "Hồ Baikal ở Siberia sâu 1.642m và chứa tới 20% lượng nước ngọt tự nhiên mặt đất của thế giới."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Thác nước tự nhiên cao nhất thế giới không bị ngắt quãng là thác nước nào?",
        "options": ["Thác Angel (Venezuela)", "Thác Niagara", "Thác Iguazu", "Thác Victoria"],
        "correct": 0, "explanation": "Thác Angel (Salto Ángel) ở Venezuela cao tới 979m với dòng chảy thẳng đứng 807m."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Vùng sa mạc khô hạn nhất thế giới, nơi có những điểm hàng trăm năm chưa từng có mưa, là sa mạc nào?",
        "options": ["Sa mạc Atacama", "Sa mạc Sahara", "Sa mạc Gobi", "Sa mạc Kalahari"],
        "correct": 0, "explanation": "Sa mạc Atacama ở Chile là vùng đất phi cực khô cằn nhất trên Trái Đất."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Biển Chết (Dead Sea) nổi tiếng thế giới nằm ở ranh giới giữa hai quốc gia nào?",
        "options": ["Israel và Jordan", "Ai Cập và Ả Rập Xê Út", "Thổ Nhĩ Kỳ và Hy Lạp", "Iran và Iraq"],
        "correct": 0, "explanation": "Biển Chết là hồ muối nằm giữa Israel, Bờ Tây và Jordan, có độ mặn cực cao khiến sinh vật khó sống."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Quốc gia nào trên thế giới hoàn toàn nằm lọt thỏm bên trong lãnh thổ của thủ đô Rome (Ý)?",
        "options": ["Vatican", "San Marino", "Monaco", "Liechtenstein"],
        "correct": 0, "explanation": "Thành quốc Vatican rộng chỉ 0,49 km² nằm trọn vẹn bên trong lòng thủ đô Rome của nước Ý."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Vùng biển nào ấm nhất thế giới do lượng bức xạ nhiệt cao và ít được trao đổi nước?",
        "options": ["Vịnh Ba Tư", "Biển Đỏ", "Vịnh Mexico", "Biển Caribe"],
        "correct": 0, "explanation": "Vào mùa hè, nhiệt độ mặt nước Vịnh Ba Tư có thể vượt qua 35°C."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Sông Mê Kông bắt nguồn từ cao nguyên nào trước khi chảy qua 6 quốc gia ra Biển Đông?",
        "options": ["Cao nguyên Tây Tạng", "Cao nguyên Vân Quý", "Cao nguyên Mông Cổ", "Dãy Himalaya"],
        "correct": 0, "explanation": "Sông Mê Kông bắt nguồn từ vùng núi cao tuyết phủ trên cao nguyên Tây Tạng (Trung Quốc)."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Quần đảo Galapagos - nơi giúp Charles Darwin hoàn thiện thuyết tiến hóa - thuộc chủ quyền nước nào?",
        "options": ["Ecuador", "Peru", "Chile", "Colombia"],
        "correct": 0, "explanation": "Quần đảo núi lửa Galapagos ở Thái Bình Dương thuộc lãnh thổ của đất nước Ecuador."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Điểm thấp nhất trên bề mặt lục địa Trái Đất nằm ở đâu?",
        "options": ["Bờ Biển Chết", "Thung lũng Chết (Mỹ)", "Vùng trũng Danakil", "Vùng trũng Turpan"],
        "correct": 0, "explanation": "Bờ Biển Chết nằm thấp hơn mực nước biển thế giới tới khoảng 430 mét."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Quốc gia nào có nhiều đảo tự nhiên nhất trên thế giới?",
        "options": ["Thụy Điển", "Phần Lan", "Indonesia", "Philippines"],
        "correct": 0, "explanation": "Thụy Điển sở hữu hơn 267.570 hòn đảo, nhiều nhất thế giới (dù chỉ một phần nhỏ có người ở)."
    },
    {
        "category": "dia-ly", "difficulty": 2,
        "question": "Đèo nào được mệnh danh là 'Vua đèo vùng Tây Bắc' hiểm trở và dài nhất (khoảng 50km) nối liền Lai Châu và Lào Cai?",
        "options": ["Đèo Ô Quy Hồ", "Đèo Mã Pí Lèng", "Đèo Khau Phạ", "Đèo Pha Đin"],
        "correct": 0, "explanation": "Đèo Ô Quy Hồ (đèo Hoàng Liên Sơn) dài gần 50km, giữ kỷ lục đèo dài nhất Việt Nam."
    },
    {
        "category": "dia-ly", "difficulty": 3,
        "question": "Thành phố thủ đô của quốc gia nào nằm ở độ cao trung bình lớn nhất thế giới so với mực nước biển (trên 3.600m)?",
        "options": ["La Paz (Bolivia)", "Quito (Ecuador)", "Kathmandu (Nepal)", "Thimphu (Bhutan)"],
        "correct": 0, "explanation": "Thủ đô hành chính La Paz của Bolivia nằm ở độ cao hơn 3.640m so với mực nước biển."
    }
]

# 4. KHOA HỌC TỰ NHIÊN & VŨ TRỤ
khoa_hoc = [
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 1,
        "question": "Hành tinh nào nằm ở vị trí gần Mặt Trời nhất trong Hệ Mặt Trời?",
        "options": ["Sao Hỏa", "Sao Thủy", "Sao Kim", "Trái Đất"],
        "correct": 1, "explanation": "Sao Thủy (Mercury) là hành tinh nằm gần Mặt Trời nhất."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 1,
        "question": "Hành tinh nào được mệnh danh là 'Hành tinh Đỏ' trong Hệ Mặt Trời?",
        "options": ["Sao Hỏa", "Sao Thổ", "Sao Mộc", "Sao Kim"],
        "correct": 0, "explanation": "Sao Hỏa (Mars) có bề mặt giàu oxit sắt rỉ sét tạo nên màu đỏ cam đặc trưng."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 1,
        "question": "Cơ thể người trưởng thành bình thường có bao nhiêu chiếc xương?",
        "options": ["206 chiếc", "300 chiếc", "180 chiếc", "250 chiếc"],
        "correct": 0, "explanation": "Người trưởng thành có đúng 206 chiếc xương (trẻ sơ sinh có khoảng 270-300 chiếc xương rồi hợp nhất lại)."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 1,
        "question": "Nước tinh khiết đóng băng thành thể rắn ở nhiệt độ bao nhiêu độ C trong áp suất chuẩn?",
        "options": ["0°C", "-5°C", "10°C", "100°C"],
        "correct": 0, "explanation": "Nước tinh khiết đóng băng ở 0°C và sôi ở 100°C ở áp suất 1 atm."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 1,
        "question": "Động vật có vú nào là loài động vật lớn nhất từng sinh sống trên Trái Đất?",
        "options": ["Cá voi xanh", "Khủng long bạo chúa", "Voi châu Phi", "Cá mập Megalodon"],
        "correct": 0, "explanation": "Cá voi xanh có thể dài tới hơn 30 mét và nặng gần 200 tấn, là loài động vật lớn nhất hành tinh."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Loài chim nào là loài duy nhất có khả năng bay lùi và bay đứng một chỗ?",
        "options": ["Chim én", "Chim bói cá", "Chim ruồi", "Chim gõ kiến"],
        "correct": 2, "explanation": "Chim ruồi (Hummingbird) có cấu tạo khớp cánh đặc biệt giúp nó bay lùi và lơ lửng tại chỗ."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Nguyên tố hóa học nào phổ biến nhất tính theo khối lượng trong vỏ Trái Đất?",
        "options": ["Silicon (Si)", "Oxy (O)", "Nhôm (Al)", "Sắt (Fe)"],
        "correct": 1, "explanation": "Oxy chiếm khoảng 46.6% khối lượng vỏ Trái Đất dưới dạng các khoáng chất oxit."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Đơn vị đo cường độ dòng điện trong hệ đo lường quốc tế (SI) là gì?",
        "options": ["Volt (V)", "Watt (W)", "Ampe (A)", "Ohm (Ω)"],
        "correct": 2, "explanation": "Ampe (kí hiệu A) là đơn vị đo cường độ dòng điện tiêu chuẩn."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Trong cơ thể người, cơ quan nội tạng nào đảm nhiệm chức năng lọc máu và bài tiết nước tiểu?",
        "options": ["Gan", "Thận", "Tụy", "Dạ dày"],
        "correct": 1, "explanation": "Hai quả thận có chức năng lọc độc tố và chất thải từ máu để tạo ra nước tiểu."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Khí nào chiếm tỷ lệ thể tích lớn nhất trong bầu khí quyển Trái Đất?",
        "options": ["Khí Oxy", "Khí Nitơ", "Khí Cacbonic", "Khí Argon"],
        "correct": 1, "explanation": "Khí Nitơ (N2) chiếm khoảng 78.08% thể tích khí quyển, Oxy chiếm khoảng 20.95%."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Kim loại nào có độ dẫn điện và dẫn nhiệt tốt nhất trong tất cả các kim loại?",
        "options": ["Đồng (Cu)", "Vàng (Au)", "Bạc (Ag)", "Nhôm (Al)"],
        "correct": 2, "explanation": "Bạc (Ag) là kim loại dẫn điện và nhiệt tốt nhất, kế đến là đồng và vàng."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Vận tốc ánh sáng truyền trong chân không có giá trị xấp xỉ bằng bao nhiêu?",
        "options": ["300.000 km/s", "30.000 km/s", "3.000 km/s", "150.000 km/s"],
        "correct": 0, "explanation": "Vận tốc ánh sáng trong chân không là c ≈ 299.792 km/s (~300.000 km/s)."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Cơ quan nội tạng nào là cơ quan nội tạng lớn nhất và nặng nhất trong cơ thể con người?",
        "options": ["Tim", "Gan", "Phổi", "Não"],
        "correct": 1, "explanation": "Gan nặng khoảng 1.5kg, là cơ quan nội tạng lớn nhất (còn da là cơ quan lớn nhất bao phủ toàn thân)."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Loài thú duy nhất nào có khả năng bay thực sự như chim nhờ màng cánh?",
        "options": ["Dơi", "Sóc bay", "Chồn bay", "Cáo bay"],
        "correct": 0, "explanation": "Loài Dơi (bộ Chiroptera) là động vật có vú duy nhất có thể bay lượn chủ động bằng cánh."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Quá trình thực vật sử dụng ánh sáng Mặt Trời để tổng hợp chất dinh dưỡng và nhả khí Oxy gọi là gì?",
        "options": ["Hô hấp", "Quang hợp", "Thoát hơi nước", "Lên men"],
        "correct": 1, "explanation": "Quang hợp (Photosynthesis) là quá trình chuyển đổi năng lượng ánh sáng thành năng lượng hóa học."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Trong Hệ Mặt Trời, hành tinh nào có kích thước và khối lượng lớn nhất?",
        "options": ["Sao Thổ", "Sao Hải Vương", "Sao Mộc", "Sao Thiên Vương"],
        "correct": 2, "explanation": "Sao Mộc (Jupiter) là hành tinh lớn nhất, có khối lượng gấp 2.5 lần tổng khối lượng các hành tinh khác cộng lại."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Kim loại duy nhất nào ở trạng thái lỏng ở nhiệt độ phòng (25°C)?",
        "options": ["Thủy ngân (Hg)", "Chì (Pb)", "Gali (Ga)", "Kẽm (Zn)"],
        "correct": 0, "explanation": "Thủy ngân (Mercury - Hg) là kim loại duy nhất ở dạng lỏng ở điều kiện nhiệt độ phòng chuẩn."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Ai là người phụ nữ đầu tiên trên thế giới bay vào không gian vũ trụ?",
        "options": ["Valentina Tereshkova", "Sally Ride", "Svetlana Savitskaya", "Mae Jemison"],
        "correct": 0, "explanation": "Nữ phi hành gia Liên Xô Valentina Tereshkova bay vào vũ trụ ngày 16/6/1963 trên tàu Vostok 6."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Nhà bác học Hy Lạp nào từ thời cổ đại đã tính toán chu vi Trái Đất với độ sai số kinh ngạc dưới 2%?",
        "options": ["Archimedes", "Eratosthenes", "Pythagoras", "Aristotle"],
        "correct": 1, "explanation": "Eratosthenes (thế kỷ 3 TCN) đo góc bóng nắng tại Alexandria và Syene để tính chu vi Trái Đất."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Trong bảng tuần hoàn hóa học Mendeleev, chữ cái Latinh duy nhất nào không xuất hiện ở ký hiệu nguyên tố nào?",
        "options": ["Chữ J", "Chữ Q", "Chữ X", "Chữ Z"],
        "correct": 0, "explanation": "Chữ cái 'J' là ký tự duy nhất trong bảng chữ cái Latinh không có mặt trong bất kỳ ký hiệu nguyên tố nào."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Hiện tượng vật lý nào giải thích tại sao bầu trời vào ban ngày lại có màu xanh lam?",
        "options": ["Tán xạ Raman", "Tán xạ Rayleigh", "Khúc xạ ánh sáng", "Nhiễu xạ ánh sáng"],
        "correct": 1, "explanation": "Tán xạ Rayleigh làm tán xạ các ánh sáng bước sóng ngắn (xanh lam) mạnh hơn nhiều so với bước sóng dài."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Ai là người đầu tiên chế tạo và dùng kính thiên văn để quan sát các thiên thể vũ trụ năm 1609?",
        "options": ["Galileo Galilei", "Hans Lippershey", "Johannes Kepler", "Isaac Newton"],
        "correct": 0, "explanation": "Galileo Galilei hoàn thiện kính thiên văn và phát hiện ra 4 vệ tinh lớn của sao Mộc."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Ai là nhà khoa học duy nhất trong lịch sử từng nhận hai giải Nobel ở hai lĩnh vực khoa học khác nhau (Vật lý và Hóa học)?",
        "options": ["Marie Curie", "Albert Einstein", "Linus Pauling", "Niels Bohr"],
        "correct": 0, "explanation": "Marie Curie nhận Nobel Vật lý năm 1903 và Nobel Hóa học năm 1911 về nghiên cứu phóng xạ."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Vật liệu tự nhiên nào có độ cứng lớn nhất theo thang độ cứng Mohs?",
        "options": ["Kim cương", "Thạch anh", "Corundum (Sapphire)", "Topaz"],
        "correct": 0, "explanation": "Kim cương đạt điểm 10 tuyệt đối trên thang Mohs, là chất tự nhiên cứng nhất."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Nhiệt độ tuyệt đối 0 Kelvin (Độ 0 tuyệt đối) tương đương với bao nhiêu độ C?",
        "options": ["-273.15°C", "-100°C", "-200°C", "-373.15°C"],
        "correct": 0, "explanation": "0 K = -273.15°C, nơi mọi chuyển động nhiệt của các hạt nguyên tử đạt trạng thái cực tiểu."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Định luật Vạn vật Hấp dẫn nổi tiếng được nhà bác học vĩ đại nào công bố trong tác phẩm 'Principia' năm 1687?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Johannes Kepler"],
        "correct": 0, "explanation": "Sir Isaac Newton công bố định luật vạn vật hấp dẫn và ba định luật chuyển động kinh điển."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Cấu trúc xoắn kép của phân tử DNA được công bố bởi hai nhà khoa học nào vào năm 1953?",
        "options": ["James Watson và Francis Crick", "Charles Darwin và Mendel", "Pasteur và Koch", "Alexander Fleming và Florey"],
        "correct": 0, "explanation": "Watson và Crick (với dữ liệu của Rosalind Franklin) đã khám phá cấu trúc chuỗi xoắn kép DNA."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Hạt hạ nguyên tử nào mang điện tích âm và quay quanh hạt nhân nguyên tử?",
        "options": ["Electron", "Proton", "Neutron", "Positron"],
        "correct": 0, "explanation": "Electron (điện tử) mang điện tích âm e = -1.6 x 10^-19 C."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Khí trơ nào được sử dụng để bơm bóng bay vì nhẹ hơn không khí và không dễ cháy nổ như khí Hydro?",
        "options": ["Heli (He)", "Neon (Ne)", "Argon (Ar)", "Krypton (Kr)"],
        "correct": 0, "explanation": "Khí Heli (Helium) rất nhẹ và là khí trơ không bắt lửa, an toàn cho bóng bay."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Loài thực vật hạt kín nào có hạt có thể nảy mầm sau hàng nghìn năm bị chôn vùi dưới bùn sâu?",
        "options": ["Hạt sen cổ", "Hạt lúa gạo", "Hạt dưa hấu", "Hạt ngô"],
        "correct": 0, "explanation": "Hạt sen cổ có lớp vỏ sáp cứng bảo vệ phôi thai giúp nó nảy mầm sau hơn 1.000 năm."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Nguyên tố nào là thành phần cơ bản bắt buộc cấu tạo nên mọi hợp chất hữu cơ của sự sống trên Trái Đất?",
        "options": ["Cacbon (C)", "Lưu huỳnh (S)", "Photpho (P)", "Clo (Cl)"],
        "correct": 0, "explanation": "Hóa học hữu cơ là hóa học của các hợp chất của Cacbon với liên kết hóa trị linh hoạt."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 3,
        "question": "Thiên hà chứa Hệ Mặt Trời và Trái Đất của chúng ta có tên là gì?",
        "options": ["Dải Ngân Hà (Milky Way)", "Thiên hà Tiên Nữ (Andromeda)", "Thiên hà Tam Giác", "Đám Mây Magellan"],
        "correct": 0, "explanation": "Hệ Mặt Trời của chúng ta nằm ở một nhánh xoắn ốc của Dải Ngân Hà (Milky Way)."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 1,
        "question": "Hành tinh nào trong Hệ Mặt Trời sở hữu hệ thống vành đai rực rỡ và đồ sộ nhất dễ dàng quan sát qua kính thiên văn?",
        "options": ["Sao Mộc", "Sao Thổ", "Sao Thiên Vương", "Sao Hải Vương"],
        "correct": 1, "explanation": "Sao Thổ (Saturn) nổi tiếng nhất với hệ thống vành đai bụi băng đá tuyệt đẹp bao quanh."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 1,
        "question": "Loại vitamin nào cơ thể con người có khả năng tự tổng hợp tốt nhất khi da tiếp xúc với ánh nắng Mặt Trời buổi sớm?",
        "options": ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin B12"],
        "correct": 2, "explanation": "Tia UVB trong ánh nắng kích thích tiền chất dưới da tổng hợp thành Vitamin D cần thiết cho xương."
    },
    {
        "category": "khoa-hoc-tu-nhien", "difficulty": 2,
        "question": "Ai được tôn vinh là 'Cha đẻ của ngành di truyền học' với các định luật phân ly và phân ly độc lập trên cây đậu Hà Lan?",
        "options": ["Gregor Mendel", "Charles Darwin", "Louis Pasteur", "Thomas Hunt Morgan"],
        "correct": 0, "explanation": "Nhà tu sĩ người Áo Gregor Mendel công bố các quy luật di truyền nền tảng vào năm 1866."
    }
]

# 5. VĂN HỌC & NGHỆ THUẬT
van_hoc = [
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 1,
        "question": "Trong bảng chữ cái Tiếng Việt chính thức có bao nhiêu chữ cái?",
        "options": ["24 chữ cái", "26 chữ cái", "29 chữ cái", "32 chữ cái"],
        "correct": 2, "explanation": "Bảng chữ cái Tiếng Việt hiện hành có chính xác 29 chữ cái."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 1,
        "question": "Điền vào câu ca dao tục ngữ: 'Chuồn chuồn bay thấp thì mưa, bay cao thì...'?",
        "options": ["Râm", "Nắng", "Gió", "Bão"],
        "correct": 1, "explanation": "Câu tục ngữ trọn vẹn: 'Chuồn chuồn bay thấp thì mưa, bay cao thì nắng, bay vừa thì râm'."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 1,
        "question": "Nhạc sĩ tài hoa nào là tác giả của bài hát 'Tiến quân ca' (Quốc ca Việt Nam)?",
        "options": ["Văn Cao", "Phạm Tuyên", "Trịnh Công Sơn", "Hoàng Việt"],
        "correct": 0, "explanation": "Nhạc sĩ Văn Cao sáng tác 'Tiến quân ca' vào năm 1944."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 1,
        "question": "Truyện cổ tích nổi tiếng nào của Việt Nam kể về hai chị em mồ côi và quả thị rơi bị bà lão?",
        "options": ["Tấm Cám", "Thạch Sanh", "Cây tre trăm đốt", "Sọ Dừa"],
        "correct": 0, "explanation": "Truyện Tấm Cám là truyện cổ tích thần kỳ tiêu biểu của kho tàng dân gian Việt Nam."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 1,
        "question": "Ai là tác giả của tập truyện ngắn 'Dế Mèn phiêu lưu ký' gắn liền với tuổi thơ bao thế hệ?",
        "options": ["Tô Hoài", "Vũ Trọng Phụng", "Nam Cao", "Nguyễn Nhật Ánh"],
        "correct": 0, "explanation": "Nhà văn Tô Hoài sáng tác kiệt tác 'Dế Mèn phiêu lưu ký' xuất bản năm 1941."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 1,
        "question": "Điền từ còn thiếu vào thành ngữ dân gian: 'Ăn quả nhớ kẻ...'?",
        "options": ["Trồng cây", "Tưới cây", "Bón phân", "Gieo hạt"],
        "correct": 0, "explanation": "'Ăn quả nhớ kẻ trồng cây' khuyên răn truyền thống đạo lý uống nước nhớ nguồn."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Tác phẩm kiệt tác 'Truyện Kiều' của đại thi hào Nguyễn Du ban đầu có tên chữ Hán là gì?",
        "options": ["Kim Vân Kiều Truyện", "Đoạn Trường Tân Thanh", "Vương Thúy Kiều ký", "Thanh Hiên thi tập"],
        "correct": 1, "explanation": "Tên gốc của Truyện Kiều là 'Đoạn Trường Tân Thanh' (Tiếng kêu mới đứt ruột)."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Nhân vật 'Chí Phèo' và làng Vũ Đại là những hình tượng văn học bất hủ trong tác phẩm của nhà văn nào?",
        "options": ["Nam Cao", "Ngô Tất Tố", "Vũ Trọng Phụng", "Nguyễn Công Hoan"],
        "correct": 0, "explanation": "Nhà văn Nam Cao sáng tác truyện ngắn kinh điển Chí Phèo (ban đầu mang tên Cái lò gạch cũ) năm 1941."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Tác phẩm văn học nào được xem là cuốn truyện ngắn hiện đại đầu tiên viết bằng chữ Quốc ngữ ở nước ta?",
        "options": ["Thầy Lazaro Phiền", "Số đỏ", "Chí Phèo", "Tắt đèn"],
        "correct": 0, "explanation": "'Thầy Lazaro Phiền' của Nguyễn Trọng Quản xuất bản năm 1887 tại Sài Gòn."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Ai được mệnh danh là 'Bà chúa thơ Nôm' trong nền văn học cổ điển Việt Nam?",
        "options": ["Hồ Xuân Hương", "Bà Huyện Thanh Quan", "Đoàn Thị Điểm", "Sương Nguyệt Anh"],
        "correct": 0, "explanation": "Nữ sĩ Hồ Xuân Hương được tôn vinh là 'Bà chúa thơ Nôm' với phong cách thơ độc đáo, sắc sảo."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Bức tranh danh họa Mona Lisa của danh họa Leonardo da Vinci hiện được trưng bày tại bảo tàng nào?",
        "options": ["Bảo tàng Prado", "Bảo tàng Louvre (Pháp)", "Bảo tàng Anh", "Bảo tàng Vatican"],
        "correct": 1, "explanation": "Kiệt tác nụ cười bí ẩn Mona Lisa được trưng bày tại Bảo tàng Louvre ở thủ đô Paris, Pháp."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Loại hình nghệ thuật sân khấu truyền thống độc đáo nào của Việt Nam biểu diễn dưới nước?",
        "options": ["Múa rối nước", "Hát Tuồng", "Hát Chèo", "Cải lương"],
        "correct": 0, "explanation": "Múa rối nước là nghệ thuật dân gian độc nhất vô nhị ra đời từ nền văn minh lúa nước đồng bằng sông Hồng."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Ai là tác giả của tác phẩm tiểu thuyết hiện thực phê phán xuất sắc 'Số đỏ' với nhân vật Xuân Tóc Đỏ?",
        "options": ["Vũ Trọng Phụng", "Ngô Tất Tố", "Nguyễn Tuân", "Nguyên Hồng"],
        "correct": 0, "explanation": "Vũ Trọng Phụng (ông vua phóng sự đất Bắc) sáng tác tiểu thuyết trào phúng 'Số đỏ' năm 1936."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Nhạc sĩ thiên tài người Đức nào đã sáng tác bản 'Bản giao hưởng số 9' hùng tráng khi đã bị điếc hoàn toàn?",
        "options": ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Frederic Chopin"],
        "correct": 0, "explanation": "Beethoven hoàn thành Bản giao hưởng Định mệnh số 9 khi thính giác đã mất hoàn toàn."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Tập thơ chữ Hán 'Nhật ký trong tù' (Ngục trung nhật ký) là tác phẩm của ai?",
        "options": ["Hồ Chí Minh", "Phan Bội Châu", "Phan Châu Trinh", "Sóng Hồng"],
        "correct": 0, "explanation": "Chủ tịch Hồ Chí Minh sáng tác 133 bài thơ chữ Hán khi bị giam giữ tại các nhà tù Quảng Tây (Trung Quốc) 1942 - 1943."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Ai là tác giả của bộ tiểu thuyết sử thi kiếm hiệp 'Anh hùng xạ điêu' và 'Thần điêu đại hiệp'?",
        "options": ["Kim Dung", "Cổ Long", "Lương Vũ Sinh", "Ôn Thụy An"],
        "correct": 0, "explanation": "Đại văn hào Kim Dung là cây đại thụ của dòng tiểu thuyết võ hiệp Á Đông."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Nhà văn người Anh nào là tác giả của bộ tiểu thuyết kỳ ảo 'Harry Potter' nổi tiếng toàn cầu?",
        "options": ["J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin"],
        "correct": 0, "explanation": "Bà J.K. Rowling đã tạo nên thế giới phù thủy Harry Potter làm say mê hàng trăm triệu độc giả."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Vở kịch bi kịch kinh điển 'Hamlet' là kiệt tác của nhà soạn kịch vĩ đại nào?",
        "options": ["William Shakespeare", "Molière", "Victor Hugo", "Johann Wolfgang von Goethe"],
        "correct": 0, "explanation": "William Shakespeare là nhà soạn kịch lừng danh của nước Anh thời Phục hưng."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Ai là tác giả của tác phẩm tiểu thuyết bất hủ 'Những người khốn khổ' (Les Misérables)?",
        "options": ["Victor Hugo", "Alexandre Dumas", "Honoré de Balzac", "Gustave Flaubert"],
        "correct": 0, "explanation": "Đại văn hào người Pháp Victor Hugo xuất bản tiểu thuyết 'Những người khốn khổ' vào năm 1862."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Bức tranh danh tiếng 'Đêm đầy sao' (The Starry Night) là kiệt tác của họa sĩ thiên tài nào?",
        "options": ["Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Salvador Dalí"],
        "correct": 0, "explanation": "Danh họa người Hà Lan Vincent van Gogh vẽ kiệt tác The Starry Night vào năm 1889."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Nhà văn châu Á đầu tiên vinh dự đoạt giải Nobel Văn học vào năm 1913 là ai?",
        "options": ["Rabindranath Tagore", "Kawabata Yasunari", "Lỗ Tấn", "Mạc Ngôn"],
        "correct": 0, "explanation": "Đại thi hào Ấn Độ Rabindranath Tagore nhận giải Nobel Văn học 1913 nhờ tập thơ 'Lời dâng' (Gitanjali)."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Tập thơ 'Thơ thơ' (1938) mở đầu cho trào lưu Thơ Mới lãng mạn Việt Nam là của nhà thơ nào?",
        "options": ["Xuân Diệu", "Huy Cận", "Hàn Mặc Tử", "Chế Lan Viên"],
        "correct": 0, "explanation": "Xuân Diệu được Hoài Thanh xưng tụng là 'nhà thơ mới nhất trong các nhà thơ mới'."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Bức tượng cẩm thạch kiệt tác 'David' thời kỳ Phục hưng là tác phẩm điêu khắc của nghệ sĩ nào?",
        "options": ["Michelangelo", "Donatello", "Leonardo da Vinci", "Raphael"],
        "correct": 0, "explanation": "Michelangelo hoàn thành bức tượng điêu khắc David cao hơn 5 mét vào năm 1504 tại Florence."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Tác phẩm sử thi 'Iliad' và 'Odyssey' của Hy Lạp cổ đại tương truyền là của thi hào mù nào sáng tác?",
        "options": ["Homer", "Sophocles", "Hesiod", "Euripides"],
        "correct": 0, "explanation": "Thi hào Homer được coi là tác giả của hai bộ sử thi nền tảng của văn minh phương Tây."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Ai là tác giả của áng văn xuôi trữ tình nổi tiếng 'Một thứ quà của lúa non: Cốm'?",
        "options": ["Thạch Lam", "Nguyễn Tuân", "Vũ Bằng", "Nguyễn Đình Thi"],
        "correct": 0, "explanation": "Nhà văn Thạch Lam trong tập tùy bút 'Hà Nội ba mươi sáu phố phường' (1943)."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Giải thưởng danh giá nhất của ngành điện ảnh thế giới do Viện Hàn lâm Hoa Kỳ trao tặng hàng năm là gì?",
        "options": ["Giải Oscar", "Cành cọ Vàng", "Sư tử Vàng", "Quả cầu Vàng"],
        "correct": 0, "explanation": "Giải Oscar (Academy Awards) là giải thưởng điện ảnh danh giá và uy tín bậc nhất thế giới."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Vở opera kinh điển 'Cây sáo thần' (The Magic Flute) là sáng tác của nhà soạn nhạc thiên tài nào?",
        "options": ["Wolfgang Amadeus Mozart", "Antonio Vivaldi", "Giuseppe Verdi", "Richard Wagner"],
        "correct": 0, "explanation": "Mozart sáng tác vở opera nổi tiếng Die Zauberflöte (Cây sáo thần) vào năm 1791."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 3,
        "question": "Tác phẩm 'Chiến tranh và Hòa bình' (War and Peace) là kiệt tác văn học của văn hào Nga nào?",
        "options": ["Lev Tolstoy", "Fyodor Dostoevsky", "Anton Chekhov", "Alexander Pushkin"],
        "correct": 0, "explanation": "Bá tước Lev Tolstoy xuất bản tiểu thuyết sử thi vĩ đại Chiến tranh và Hòa bình năm 1869."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Vở kịch sân khấu kinh điển mang triết lý nhân sinh sâu sắc 'Hồn Trương Ba, da hàng thịt' là tác phẩm của ai?",
        "options": ["Lưu Quang Vũ", "Xuân Trình", "Đào Tấn", "Nguyễn Huy Tưởng"],
        "correct": 0, "explanation": "Nhà viết kịch tài hoa Lưu Quang Vũ sáng tác 'Hồn Trương Ba, da hàng thịt' năm 1981."
    },
    {
        "category": "van-hoc-nghe-thuat", "difficulty": 2,
        "question": "Ai là tác giả của kiệt tác tiểu thuyết chương hồi đồ sộ 'Tam Quốc Diễn Nghĩa' của văn học cổ điển phương Đông?",
        "options": ["La Quán Trung", "Thi Nại Am", "Ngô Thừa Ân", "Tào Tuyết Cần"],
        "correct": 0, "explanation": "La Quán Trung sống vào cuối thời Nguyên đầu thời Minh là tác giả của Tam Quốc Diễn Nghĩa."
    }
]

# 6. ĐỜI SỐNG, CÔNG NGHỆ & XÃ HỘI
doi_song = [
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Trái cây nào được mệnh danh là 'Vua của các loài trái cây' ở Đông Nam Á?",
        "options": ["Xoài cát", "Sầu riêng", "Măng cụt", "Chôm chôm"],
        "correct": 1, "explanation": "Sầu riêng được mệnh danh là King of Fruits, còn Măng cụt là Queen of Fruits."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Một năm dương lịch thông thường (không phải năm nhuận) có bao nhiêu ngày?",
        "options": ["364 ngày", "365 ngày", "366 ngày", "360 ngày"],
        "correct": 1, "explanation": "Năm thường có 365 ngày, năm nhuận có 366 ngày."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Tháng nào trong năm nhuận dương lịch có 29 ngày?",
        "options": ["Tháng 1", "Tháng 2", "Tháng 4", "Tháng 6"],
        "correct": 1, "explanation": "Tháng 2 có 28 ngày ở năm thường và 29 ngày ở năm nhuận."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Món ăn truyền thống đặc trưng không thể thiếu trên mâm cỗ Tết cổ truyền của người miền Bắc là gì?",
        "options": ["Bánh chưng", "Bánh tét", "Bánh xèo", "Bánh khọt"],
        "correct": 0, "explanation": "Bánh chưng vuông xanh lá dong tượng trưng cho Đất là biểu tượng Tết miền Bắc."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Ứng dụng video ngắn TikTok ban đầu có nguồn gốc từ công ty công nghệ nào?",
        "options": ["ByteDance", "Tencent", "Alibaba", "Baidu"],
        "correct": 0, "explanation": "ByteDance sáng lập và phát triển nền tảng TikTok (phiên bản quốc tế của Douyin)."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Cây cầu dây văng đầu tiên được xây dựng tại Việt Nam khánh thành năm 2000 là cây cầu nào?",
        "options": ["Cầu Mỹ Thuận", "Cầu Bãi Cháy", "Cầu Cần Thơ", "Cầu Nhật Tân"],
        "correct": 0, "explanation": "Cầu Mỹ Thuận bắc qua sông Tiền khánh thành năm 2000 là cây cầu dây văng đầu tiên ở Việt Nam."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Tập đoàn công nghệ nào chế tạo ra hệ điều hành Android ban đầu trước khi bán cho Google?",
        "options": ["Android Inc.", "Sun Microsystems", "Motorola", "Nokia"],
        "correct": 0, "explanation": "Android Inc. thành lập năm 2003 và được Google mua lại vào năm 2005."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Mạng Internet toàn cầu được truy cập công cộng lần đầu tiên thông qua giao thức WWW (World Wide Web) do ai phát minh?",
        "options": ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Vint Cerf"],
        "correct": 0, "explanation": "Sir Tim Berners-Lee phát minh ra World Wide Web (WWW) tại trung tâm CERN năm 1989."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Đội tuyển bóng đá nam quốc gia nào giành nhiều chức vô địch World Cup nhất trong lịch sử (5 lần)?",
        "options": ["Brazil", "Đức", "Ý", "Argentina"],
        "correct": 0, "explanation": "Đội tuyển Brazil (Những vũ công Samba) giữ kỷ lục 5 lần vô địch World Cup (1958, 1962, 1970, 1994, 2002)."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Đơn vị tiền tệ chung của Liên minh Châu Âu (EU) có tên gọi là gì?",
        "options": ["Euro (€)", "Bảng Anh (£)", "Franc", "Yên"],
        "correct": 0, "explanation": "Đồng Euro (€) được đưa vào lưu thông chính thức từ năm 2002."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Ai là người sáng lập tập đoàn phần mềm Microsoft và giữ vị trí người giàu nhất thế giới trong nhiều năm liền?",
        "options": ["Bill Gates", "Paul Allen", "Steve Jobs", "Elon Musk"],
        "correct": 0, "explanation": "Bill Gates cùng Paul Allen sáng lập Microsoft năm 1975."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Ngày Quốc tế Phụ nữ được tổ chức vào ngày nào hàng năm trên toàn thế giới?",
        "options": ["Ngày 8 tháng 3", "Ngày 20 tháng 10", "Ngày 1 tháng 5", "Ngày 1 tháng 6"],
        "correct": 0, "explanation": "Ngày 8 tháng 3 là ngày Quốc tế Phụ nữ kỷ niệm phong trào quyền lợi của phụ nữ toàn cầu."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Chiếc điện thoại thông minh iPhone thế hệ đầu tiên được cố CEO Steve Jobs giới thiệu vào năm nào?",
        "options": ["2005", "2007", "2009", "2010"],
        "correct": 1, "explanation": "Steve Jobs giới thiệu iPhone 2G lần đầu tại Macworld ngày 9/1/2007 mở ra kỷ nguyên smartphone."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Thế vận hội Olympic mùa hè hiện đại đầu tiên được tổ chức tại thành phố nào vào năm 1896?",
        "options": ["Athens (Hy Lạp)", "Paris (Pháp)", "London (Anh)", "Rome (Ý)"],
        "correct": 0, "explanation": "Thế vận hội hiện đại đầu tiên được phục hồi tại Athens năm 1896 do Pierre de Coubertin khởi xướng."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Định dạng ảnh động phổ biến trên internet viết tắt là GIF là viết tắt của từ gì?",
        "options": ["Graphics Interchange Format", "General Image File", "Global Internet Format", "Graphical Image Frame"],
        "correct": 0, "explanation": "GIF là viết tắt của Graphics Interchange Format được phát triển bởi CompuServe năm 1987."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 2,
        "question": "Tỉnh nào ở miền Tây Nam Bộ được mệnh danh là 'Xứ sở Dừa' của Việt Nam?",
        "options": ["Bến Tre", "Trà Vinh", "Tiền Giang", "Vĩnh Long"],
        "correct": 0, "explanation": "Bến Tre nổi tiếng với những rặng dừa bạt ngàn và các đặc sản từ dừa."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "CÂU HỎI RUNG CHUÔNG VÀNG: Cây cầu thép lịch sử đầu tiên bắc qua sông Hồng tại Hà Nội khánh thành năm 1902 là cầu nào?",
        "options": ["Cầu Long Biên", "Cầu Thăng Long", "Cầu Chương Dương", "Cầu Vĩnh Tuy"],
        "correct": 0, "explanation": "Cầu Long Biên (tên ban đầu là cầu Doumer) được khánh thành năm 1902."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Đồng tiền điện tử phi tập trung đầu tiên trên thế giới mang tên Bitcoin được tạo ra vào năm 2009 bởi nhân vật bí ẩn nào?",
        "options": ["Satoshi Nakamoto", "Vitalik Buterin", "Hal Finney", "Nick Szabo"],
        "correct": 0, "explanation": "Satoshi Nakamoto là bút danh của cá nhân hoặc tổ chức bí ẩn đã phát minh ra Bitcoin."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Ngôn ngữ lập trình Python được tạo ra bởi nhà khoa học máy tính người Hà Lan nào vào năm 1991?",
        "options": ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Bjarne Stroustrup"],
        "correct": 0, "explanation": "Guido van Rossum sáng tạo ngôn ngữ lập trình Python và đặt tên theo nhóm hài Monty Python."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Hệ điều hành mã nguồn mở nhân Linux đầu tiên được công bố bởi ai vào năm 1991?",
        "options": ["Linus Torvalds", "Richard Stallman", "Ken Thompson", "Dennis Ritchie"],
        "correct": 0, "explanation": "Chàng sinh viên 21 tuổi người Phần Lan Linus Torvalds viết kernel Linux năm 1991."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Ai là người đầu tiên trên thế giới phát minh ra mạng lưới ngân hàng máu và phương pháp lưu trữ huyết tương cứu sống hàng triệu người?",
        "options": ["Charles R. Drew", "Karl Landsteiner", "Alexander Fleming", "Edward Jenner"],
        "correct": 0, "explanation": "Bác sĩ Charles R. Drew là cha đẻ của các ngân hàng máu hiện đại trong Thế chiến thứ hai."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Chiếc máy bay có động cơ đầu tiên trên thế giới bay thành công vào năm 1903 là phát minh của ai?",
        "options": ["Anh em nhà Wright", "Alberto Santos-Dumont", "Louis Blériot", "Glenn Curtiss"],
        "correct": 0, "explanation": "Orville và Wilbur Wright thực hiện chuyến bay lịch sử đầu tiên tại Kitty Hawk năm 1903."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Giải đấu quần vợt (tennis) lâu đời và danh giá nhất trên mặt sân cỏ tự nhiên trên thế giới là giải nào?",
        "options": ["Wimbledon (Anh)", "US Open (Mỹ)", "Roland Garros (Pháp)", "Australian Open (Úc)"],
        "correct": 0, "explanation": "Giải Wimbledon khởi tranh lần đầu năm 1877 tại London, là giải Grand Slam cổ nhất."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Mô hình trí tuệ nhân tạo Transformer - nền móng cho ChatGPT và LLM hiện đại - được công bố trong bài báo khoa học nổi tiếng nào năm 2017 của Google?",
        "options": ["Attention Is All You Need", "Deep Residual Learning", "ImageNet Classification", "BERT Pre-training"],
        "correct": 0, "explanation": "Bài báo 'Attention Is All You Need' của nhóm nghiên cứu Google Brain/Research năm 2017 tạo nên cuộc cách mạng AI."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Tổ chức Y tế Thế giới (WHO) có trụ sở chính đặt tại thành phố nào?",
        "options": ["Geneva (Thụy Sĩ)", "New York (Mỹ)", "Vienna (Áo)", "Paris (Pháp)"],
        "correct": 0, "explanation": "Trụ sở của Tổ chức Y tế Thế giới (WHO) nằm tại thành phố Geneva, Thụy Sĩ."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Thương hiệu ô tô nào là hãng xe thương mại chế tạo ra dây đai an toàn 3 điểm vào năm 1959 và chia sẻ miễn phí bằng sáng chế cho toàn nhân loại?",
        "options": ["Volvo", "Mercedes-Benz", "Toyota", "Ford"],
        "correct": 0, "explanation": "Kỹ sư Nils Bohlin của Volvo phát minh dây đai an toàn 3 điểm và Volvo quyết định không thu tiền bản quyền để cứu mạng người."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 3,
        "question": "Thuật ngữ 'Debugging' (tìm và sửa lỗi phần mềm) trong ngành tin học bắt nguồn từ sự kiện một con bướm đêm (moth) bay vào máy tính nào năm 1947?",
        "options": ["Máy tính Mark II", "Máy tính ENIAC", "Máy tính UNIVAC", "Máy tính Colossus"],
        "correct": 0, "explanation": "Nữ lập trình viên Grace Hopper đã tìm thấy con bướm đêm gây đoản mạch trong rơ-le máy tính Mark II tại Harvard."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Môn thể thao nào được tôn vinh là 'Môn thể thao vua' thu hút lượng người theo dõi lớn nhất toàn cầu?",
        "options": ["Bóng rổ", "Bóng đá", "Quần vợt", "Điền kinh"],
        "correct": 1, "explanation": "Bóng đá là môn thể thao vua với hàng tỷ người hâm mộ khắp hành tinh."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Đơn vị tiền tệ chính thức của đất nước Mặt Trời mọc Nhật Bản là gì?",
        "options": ["Đồng Won", "Đồng Nhân dân tệ", "Đồng Yên (JPY)", "Đồng Baht"],
        "correct": 2, "explanation": "Đồng Yên (Yen - kí hiệu ¥) là đơn vị tiền tệ của Nhật Bản."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Ai là CEO kiêm nhà đồng sáng lập mạng xã hội Facebook (hiện nay là tập đoàn Meta)?",
        "options": ["Mark Zuckerberg", "Jack Dorsey", "Larry Page", "Sergey Brin"],
        "correct": 0, "explanation": "Mark Zuckerberg sáng lập Facebook vào năm 2004 tại Đại học Harvard."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Món phở truyền thống trứ danh của Việt Nam thường được phục vụ phổ biến nhất với hai loại thịt chính nào?",
        "options": ["Thịt bò và thịt gà", "Thịt bò và thịt heo", "Thịt vịt và thịt gà", "Thịt dê và thịt bò"],
        "correct": 0, "explanation": "Phở bò và phở gà là hai món phở quốc hồn quốc túy truyền thống của ẩm thực Việt Nam."
    },
    {
        "category": "doi-song-cong-nghe", "difficulty": 1,
        "question": "Hãng hàng không quốc gia của Việt Nam mang biểu tượng bông Hoa Sen Vàng là hãng nào?",
        "options": ["Vietnam Airlines", "Vietjet Air", "Bamboo Airways", "Pacific Airlines"],
        "correct": 0, "explanation": "Hãng hàng không Quốc gia Việt Nam (Vietnam Airlines) mang hình ảnh biểu tượng bông Sen Vàng sáu cánh."
    }
]

# Ghi từng file category
categories_map = {
    'do-vui-tri-tue.json': do_vui,
    'lich-su.json': lich_su,
    'dia-ly.json': dia_ly,
    'khoa-hoc-tu-nhien.json': khoa_hoc,
    'van-hoc-nghe-thuat.json': van_hoc,
    'doi-song-cong-nghe.json': doi_song,
}

total_count = 0
for filename, q_list in categories_map.items():
    file_path = os.path.join(CATEGORIES_DIR, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(q_list, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã ghi {len(q_list)} câu hỏi vào categories/{filename}")
    total_count += len(q_list)

print(f"\n🎉 TỔNG CỘNG ĐÃ KHỞI TẠO BATCH 1: {total_count} CÂU HỎI CHUẨN XÁC THEO 6 CHỦ ĐỀ!")
