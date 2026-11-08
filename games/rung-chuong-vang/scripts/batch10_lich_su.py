# -*- coding: utf-8 -*-
"""
Bộ câu hỏi mở rộng Lịch sử (230 câu)
Chuẩn hóa độ khó 1, 2, 3 và quay vòng đáp án A, B, C, D qua batch_helper.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

QUESTIONS = [
    # Thời Hùng Vương - An Dương Vương - Bắc thuộc
    {
        "difficulty": 1,
        "question": "Vua Hùng đầu tiên lập ra nhà nước đầu tiên trong lịch sử Việt Nam có quốc hiệu là gì?",
        "correct_answer": "Văn Lang",
        "distractors": ["Âu Lạc", "Đại Việt", "Đại Cồ Việt"],
        "explanation": "Nhà nước Văn Lang thời các vua Hùng đóng đô tại Phong Châu (nay thuộc Phú Thọ)."
    },
    {
        "difficulty": 1,
        "question": "Thục Phán An Dương Vương sáp nhập Tây Âu và Lạc Việt lập nên quốc gia nào vào thế kỷ thứ III TCN?",
        "correct_answer": "Âu Lạc",
        "distractors": ["Văn Lang", "Vạn Xuân", "Đại Ngu"],
        "explanation": "An Dương Vương định đô ở Cổ Loa, lập ra nhà nước Âu Lạc tiếp nối thời Hùng Vương."
    },
    {
        "difficulty": 1,
        "question": "Kinh đô Cổ Loa dưới thời Thục Phán An Dương Vương ngày nay thuộc huyện nào của Thủ đô Hà Nội?",
        "correct_answer": "Huyện Đông Anh",
        "distractors": ["Huyện Sóc Sơn", "Huyện Mê Linh", "Huyện Gia Lâm"],
        "explanation": "Thành Cổ Loa hình xoáy ốc tọa lạc tại xã Cổ Loa, huyện Đông Anh, Hà Nội."
    },
    {
        "difficulty": 1,
        "question": "Cuộc khởi nghĩa Hai Bà Trưng bùng nổ năm 40 sau Công nguyên nhằm chống lại ách đô hộ của thế lực phong kiến nào?",
        "correct_answer": "Nhà Đông Hán",
        "distractors": ["Nhà Tây Tấn", "Nhà Đường", "Nhà Tống"],
        "explanation": "Hai Bà Trưng phất cờ khởi nghĩa đánh đuổi thái thú Tô Định của nhà Đông Hán."
    },
    {
        "difficulty": 1,
        "question": "Nữ anh hùng dân tộc nào gắn liền với câu nói đanh thép: 'Tôi muốn cưỡi cơn gió mạnh, đạp luồng sóng dữ, chém cá kình ở biển Đông'?",
        "correct_answer": "Bà Triệu (Triệu Thị Trinh)",
        "distractors": ["Trưng Trắc", "Trưng Nhị", "Lê Chân"],
        "explanation": "Bà Triệu lãnh đạo nhân dân Giao Châu khởi nghĩa chống quân Ngô năm 248."
    },
    {
        "difficulty": 2,
        "question": "Lý Bí lãnh đạo khởi nghĩa đánh đuổi quân đô hộ nhà Lương lập ra nhà nước Vạn Xuân vào năm nào?",
        "correct_answer": "Năm 544",
        "distractors": ["Năm 542", "Năm 938", "Năm 1010"],
        "explanation": "Lý Bí lên ngôi xưng là Lý Nam Đế vào năm 544, đặt niên hiệu Thiên Đức và lập nhà nước Vạn Xuân."
    },
    {
        "difficulty": 2,
        "question": "Mai Thúc Loan lãnh đạo cuộc khởi nghĩa chống lại nhà Đường đóng căn cứ trên núi Vệ Sơn xưng hiệu là gì?",
        "correct_answer": "Mai Hắc Đế",
        "distractors": ["Bố Cái Đại Vương", "Dạ Trạch Vương", "Bắc Bình Vương"],
        "explanation": "Mai Thúc Loan xưng là Mai Hắc Đế (Vua Đen họ Mai) trong cuộc khởi nghĩa năm 722."
    },
    {
        "difficulty": 2,
        "question": "Ai là người lãnh đạo nhân dân khởi nghĩa lật đổ ách thống trị của quân Đường và được nhân dân tôn vinh là 'Bố Cái Đại Vương'?",
        "correct_answer": "Phùng Hưng",
        "distractors": ["Khúc Thừa Dụ", "Mai Thúc Loan", "Ngô Quyền"],
        "explanation": "'Bố Cái' là cách gọi tôn xưng vị cha mẹ của nhân dân dành cho anh hùng Phùng Hưng."
    },
    {
        "difficulty": 1,
        "question": "Chiến thắng lịch sử trên sông Bạch Đằng năm 938 chấm dứt hơn 1000 năm Bắc thuộc do danh nhân nào chỉ huy?",
        "correct_answer": "Ngô Quyền",
        "distractors": ["Đinh Bộ Lĩnh", "Lê Hoàn", "Trần Hưng Đạo"],
        "explanation": "Ngô Quyền dùng kế cọc ngầm đánh tan quân Nam Hán mở ra kỷ nguyên độc lập tự chủ lâu dài cho dân tộc."
    },
    {
        "difficulty": 1,
        "question": "Sau khi đánh tan quân Nam Hán năm 938, Ngô Quyền đã chọn vùng đất nào làm kinh đô của triều Ngô?",
        "correct_answer": "Cổ Loa",
        "distractors": ["Hoa Lư", "Thăng Long", "Phú Xuân"],
        "explanation": "Ngô Quyền bỏ chức Tiết độ sứ, xưng vương và đóng đô ở Cổ Loa."
    },

    # Thời Đinh - Tiền Lê
    {
        "difficulty": 1,
        "question": "Vị anh hùng nào đã có công dẹp loạn 12 sứ quân thống nhất giang sơn lập nên triều đại nhà Đinh?",
        "correct_answer": "Đinh Bộ Lĩnh",
        "distractors": ["Đinh Liễn", "Lê Hoàn", "Ngô Xương Văn"],
        "explanation": "Đinh Bộ Lĩnh dẹp tan các sứ quân, lên ngôi hoàng đế xưng là Đinh Tiên Hoàng năm 968."
    },
    {
        "difficulty": 1,
        "question": "Đinh Tiên Hoàng sau khi lên ngôi hoàng đế năm 968 đã đặt quốc hiệu cho đất nước ta là gì?",
        "correct_answer": "Đại Cồ Việt",
        "distractors": ["Đại Việt", "Vạn Xuân", "Đại Ngu"],
        "explanation": "Đại Cồ Việt nghĩa là nước Việt lớn độc lập tự chủ ngang hàng với các hoàng đế phương Bắc."
    },
    {
        "difficulty": 1,
        "question": "Kinh đô đầu tiên của nhà nước Đại Cồ Việt dưới triều Đinh và Tiền Lê nằm ở địa danh nào?",
        "correct_answer": "Hoa Lư (Ninh Bình)",
        "distractors": ["Thăng Long", "Cổ Loa", "Tây Đô"],
        "explanation": "Cố đô Hoa Lư với non nước hiểm trở được Đinh Tiên Hoàng chọn làm kinh đô phòng thủ vững chắc."
    },
    {
        "difficulty": 2,
        "question": "Vị thái hậu nào của triều Đinh đã vì đại cuộc non sông trao áo long bào cho Thập đạo tướng quân Lê Hoàn lên ngôi đánh giặc Tống?",
        "correct_answer": "Thái hậu Dương Vân Nga",
        "distractors": ["Ỷ Lan Thái phi", "Linh Từ Quốc Mẫu", "Chiêu Thánh Hoàng hậu"],
        "explanation": "Hành động đặt vận mệnh đất nước lên trên lợi ích dòng tộc của Thái hậu Dương Vân Nga được lịch sử ca ngợi."
    },
    {
        "difficulty": 2,
        "question": "Vua Lê Hoàn (Lê Đại Hành) đã chỉ huy quân dân Đại Cồ Việt đánh tan quân xâm lược nhà Tống năm nào?",
        "correct_answer": "Năm 981",
        "distractors": ["Năm 938", "Năm 1075", "Năm 1258"],
        "explanation": "Năm 981, Lê Hoàn chỉ huy đánh bại quân Tống trên sông Bạch Đằng và Chi Lăng."
    },

    # Thời Lý
    {
        "difficulty": 1,
        "question": "Chiếu dời đô (Thiên đô chiếu) từ Hoa Lư về thành Đại La (Thăng Long) được Lý Thái Tổ ban hành vào năm nào?",
        "correct_answer": "Năm 1010",
        "distractors": ["Năm 1009", "Năm 1070", "Năm 1225"],
        "explanation": "Mùa thu năm Canh Tuất 1010, Lý Thái Tổ dời đô về Đại La và đổi tên thành Thăng Long."
    },
    {
        "difficulty": 1,
        "question": "Văn Miếu Thăng Long trường đại học đầu tiên của Việt Nam được vua Lý Thánh Tông cho xây dựng vào năm nào?",
        "correct_answer": "Năm 1070",
        "distractors": ["Năm 1010", "Năm 1076", "Năm 1253"],
        "explanation": "Văn Miếu được khởi lập năm 1070, sau đó năm 1076 mở thêm Quốc Tử Giám để dạy học."
    },
    {
        "difficulty": 2,
        "question": "Bài thơ thần 'Nam quốc sơn hà' được xem là bản Tuyên ngôn Độc lập đầu tiên của nước ta vang lên trong cuộc kháng chiến chống quân nào?",
        "correct_answer": "Quân Tống",
        "distractors": ["Quân Đường", "Quân Mông Cổ", "Quân Minh"],
        "explanation": "Bài thơ vang lên bên dòng sông Như Nguyệt năm 1077 cổ vũ tinh thần quân sĩ đánh tan quân Tống do Quách Quỳ chỉ huy."
    },
    {
        "difficulty": 2,
        "question": "Phòng tuyến Như Nguyệt lừng danh trong cuộc kháng chiến chống Tống năm 1077 nằm trên đoạn sông nào ngày nay?",
        "correct_answer": "Sông Cầu",
        "distractors": ["Sông Hồng", "Sông Đuống", "Sông Mã"],
        "explanation": "Sông Như Nguyệt là tên cổ của một đoạn sông Cầu thuộc tỉnh Bắc Ninh."
    },
    {
        "difficulty": 2,
        "question": "Ai là nữ hoàng duy nhất trong lịch sử các triều đại phong kiến Việt Nam?",
        "correct_answer": "Lý Chiêu Hoàng",
        "distractors": ["Dương Vân Nga", "Nguyên phi Ỷ Lan", "Huyền Trân Công chúa"],
        "explanation": "Lý Chiêu Hoàng lên ngôi năm 1224 và sau đó nhường ngôi cho chồng là Trần Cảnh (Trần Thái Tông) mở đầu triều Trần."
    },

    # Thời Trần
    {
        "difficulty": 1,
        "question": "Quân dân nhà Trần đã lập nên kỳ tích đánh thắng quân xâm lược Mông - Nguyên bao nhiêu lần trong thế kỷ XIII?",
        "correct_answer": "3 lần",
        "distractors": ["2 lần", "4 lần", "5 lần"],
        "explanation": "Ba lần đại thắng Mông - Nguyên diễn ra vào các năm 1258, 1285 và 1287-1288."
    },
    {
        "difficulty": 1,
        "question": "Danh tướng nào đã bóp nát quả cam vì hận không được vào dự bàn việc nước tại Hội nghị Bình Than năm 1282?",
        "correct_answer": "Trần Quốc Toản",
        "distractors": ["Trần Quang Khải", "Trần Nhật Duật", "Trần Khánh Dư"],
        "explanation": "Sau đó người thiếu niên dũng cảm Trần Quốc Toản đã thêu lá cờ 6 chữ vàng 'Phá cường địch, báo hoàng ân'."
    },
    {
        "difficulty": 2,
        "question": "Hội nghị Diên Hồng năm 1284 do Thượng hoàng Trần Thánh Tông triệu tập quy tụ các đại biểu nào để hỏi kế sách đánh giặc?",
        "correct_answer": "Các bậc phụ lão trong cả nước",
        "distractors": ["Các vương hầu quý tộc", "Các tướng lĩnh ngoài biên cương", "Các nho sĩ đỗ đạt"],
        "explanation": "Tiếng hô 'Đánh!' vang dội từ Hội nghị Diên Hồng thể hiện sức mạnh đoàn kết toàn dân tộc."
    },
    {
        "difficulty": 1,
        "question": "Thái sư Trần Thủ Độ đã khẳng khái trả lời vua Trần Thái Tông câu nói nổi tiếng nào khi quân Mông Cổ xâm lược?",
        "correct_answer": "'Đầu thần chưa rơi xuống đất, xin bệ hạ đừng lo'",
        "distractors": ["'Sát Thát'", "'Đánh cho để dài tóc'", "'Quyết chiến đến cùng'"],
        "explanation": "Khí phách hiên ngang của Trần Thủ Độ đã củng cố niềm tin vững chắc cho vua và tướng sĩ."
    },
    {
        "difficulty": 2,
        "question": "Trận thủy chiến lừng danh trên sông Bạch Đằng năm 1288 của quân dân nhà Trần đã bắt sống tướng giặc Nguyên nào?",
        "correct_answer": "Ô Mã Nhi",
        "distractors": ["Thoát Hoan", "Toa Đô", "Liễu Thăng"],
        "explanation": "Trần Hưng Đạo bắt sống Ô Mã Nhi, Phàn Tiếp và đánh tan thủy quân Nguyên Mông."
    },
    {
        "difficulty": 2,
        "question": "Hai người gia nô trung thành và dũng cảm có công lặn biển đục thuyền giặc nổi tiếng của Trần Hưng Đạo là ai?",
        "correct_answer": "Yết Kiêu và Dã Tượng",
        "distractors": ["Trần Khánh Dư và Phạm Ngũ Lão", "Hà Đặc và Hà Chương", "Nguyễn Khoái và Đỗ Khắc Chung"],
        "explanation": "Yết Kiêu tài bơi lặn phi thường còn Dã Tượng tài điều khiển thớt voi trận thiện chiến."
    },
    {
        "difficulty": 3,
        "question": "Vị hoàng đế nào nhà Trần đã từ bỏ ngai vàng lên núi Yên Tử tu hành sáng lập nên Thiền phái Trúc Lâm Yên Tử?",
        "correct_answer": "Trần Nhân Tông",
        "distractors": ["Trần Thái Tông", "Trần Thánh Tông", "Trần Anh Tông"],
        "explanation": "Trần Nhân Tông được người đời tôn xưng là Phật hoàng Trần Nhân Tông."
    },
    {
        "difficulty": 2,
        "question": "Người thầy mẫu mực được mệnh danh là 'Vạn thế sư biểu' thời nhà Trần dâng 'Thất trảm sớ' xin chém 7 gian thần là ai?",
        "correct_answer": "Chu Văn An",
        "distractors": ["Trần Nguyên Đán", "Lê Văn Hưu", "Trương Hán Siêu"],
        "explanation": "Thầy Chu Văn An nổi tiếng với tiết tháo thanh cao, sau khi dâng sớ không thành đã về núi Phượng Hoàng dạy học."
    },

    # Thời Hồ - Khởi nghĩa Lam Sơn
    {
        "difficulty": 2,
        "question": "Hồ Quý Ly truất ngôi nhà Trần lập ra nhà Hồ vào năm 1400 và đổi quốc hiệu đất nước thành gì?",
        "correct_answer": "Đại Ngu",
        "distractors": ["Đại Việt", "Đại Nam", "Vạn Xuân"],
        "explanation": "'Đại Ngu' theo tiếng Hán cổ mang ý nghĩa là sự an vui lớn, thanh bình lâu dài."
    },
    {
        "difficulty": 2,
        "question": "Thành nhà Hồ di sản văn hóa thế giới UNESCO xây dựng bằng những khối đá lớn độc đáo tọa lạc tại tỉnh nào?",
        "correct_answer": "Thanh Hóa",
        "distractors": ["Ninh Bình", "Hà Tĩnh", "Nghệ An"],
        "explanation": "Thành nhà Hồ (Tây Đô) thuộc huyện Vĩnh Lộc, tỉnh Thanh Hóa xây dựng từ năm 1397."
    },
    {
        "difficulty": 1,
        "question": "Khởi nghĩa Lam Sơn chống quân Minh xâm lược bùng nổ năm 1418 tại vùng rừng núi Lam Sơn thuộc tỉnh nào?",
        "correct_answer": "Thanh Hóa",
        "distractors": ["Nghệ An", "Hòa Bình", "Ninh Bình"],
        "explanation": "Lê Lợi xưng là Bình Định Vương dựng cờ khởi nghĩa tại đất Lam Sơn, Thanh Hóa."
    },
    {
        "difficulty": 1,
        "question": "Ai là mưu sĩ kiệt xuất đã dâng 'Bình Ngô sách' và soạn thảo áng thiên cổ hùng văn 'Bình Ngô Đại Cáo'?",
        "correct_answer": "Nguyễn Trãi",
        "distractors": ["Nguyễn Xí", "Trần Nguyên Hãn", "Lê Văn An"],
        "explanation": "Nguyễn Trãi là danh nhân văn hóa thế giới, đại công thần khai quốc thời Hậu Lê."
    },
    {
        "difficulty": 2,
        "question": "Trong trận Chi Lăng năm 1427 nghĩa quân Lam Sơn đã chém rụng đầu viên tổng binh cầm đầu viện binh nhà Minh nào?",
        "correct_answer": "Liễu Thăng",
        "distractors": ["Vương Thông", "Mộc Thạnh", "Trần Hiệp"],
        "explanation": "Liễu Thăng bị phục kích chém đầu tại núi Mã Yên (Chi Lăng, Lạng Sơn)."
    },
    {
        "difficulty": 1,
        "question": "Truyền thuyết vua Lê Lợi trả gươm thần Thuận Thiên cho rùa vàng gắn liền với địa danh hồ nào ở Hà Nội?",
        "correct_answer": "Hồ Hoàn Kiếm (Hồ Gươm)",
        "distractors": ["Hồ Tây", "Hồ Trúc Bạch", "Hồ Ba Mẫu"],
        "explanation": "Sau khi đánh tan quân Minh, Lê Thái Tổ dạo thuyền trên hồ Tả Vọng và trao trả gươm thần cho Rùa Vàng."
    },

    # Thời Lê sơ - Tây Sơn
    {
        "difficulty": 2,
        "question": "Vị vua anh minh nào thời Lê sơ đã chia cả nước thành 13 đạo thừa tuyên và lập ra Hội Tao Đàn Nhị thập bát tú?",
        "correct_answer": "Lê Thánh Tông",
        "distractors": ["Lê Thái Tổ", "Lê Thái Tông", "Lê Nhân Tông"],
        "explanation": "Vua Lê Thánh Tông đưa Đại Việt phát triển rực rỡ đỉnh cao, tự xưng là Tao Đàn Đô nguyên súy."
    },
    {
        "difficulty": 2,
        "question": "Bộ luật hình sự hoàn chỉnh nhất thời phong kiến Việt Nam ban hành dưới thời vua Lê Thánh Tông có tên gọi là gì?",
        "correct_answer": "Luật Hồng Đức (Quốc triều hình luật)",
        "distractors": ["Luật Gia Long", "Hình thư thời Lý", "Hình luật thời Trần"],
        "explanation": "Luật Hồng Đức chứa đựng nhiều yếu tố tiến bộ bảo vệ quyền lợi của phụ nữ và trật tự xã hội."
    },
    {
        "difficulty": 2,
        "question": "Trong thời kỳ Trịnh - Nguyễn phân tranh dòng sông nào đã trở thành ranh giới chia cắt Đàng Trong và Đàng Ngoài?",
        "correct_answer": "Sông Gianh (Quảng Bình)",
        "distractors": ["Sông Bến Hải", "Sông Thạch Hãn", "Sông Mã"],
        "explanation": "Sông Gianh chia cắt đất nước suốt gần hai thế kỷ từ thế kỷ XVII đến thế kỷ XVIII."
    },
    {
        "difficulty": 1,
        "question": "Trận thủy chiến Rạch Gầm - Xoài Mút năm 1785 do Nguyễn Huệ chỉ huy đã đánh tan 5 vạn quân xâm lược của nước nào?",
        "correct_answer": "Quân Xiêm (Thái Lan ngày nay)",
        "distractors": ["Quân Thanh", "Quân Miến Điện", "Quân Chân Lạp"],
        "explanation": "Nguyễn Huệ nhử địch vào đoạn sông Tiền mai phục tiêu diệt gần như toàn bộ thuyền chiến quân Xiêm."
    },
    {
        "difficulty": 1,
        "question": "Chiến thắng Ngọc Hồi - Đống Đa đại phá 29 vạn quân Mãn Thanh diễn ra vào dịp Tết năm nào?",
        "correct_answer": "Tết Kỷ Dậu 1789",
        "distractors": ["Tết Mậu Tuất 1788", "Tết Canh Tuất 1790", "Tết Nhâm Tý 1792"],
        "explanation": "Vua Quang Trung hành quân thần tốc đánh tan quân Thanh, trưa mùng 5 Tết tiến vào Thăng Long."
    },

    # Thời Nguyễn - Cận đại
    {
        "difficulty": 2,
        "question": "Vị hoàng đế sáng lập triều Nguyễn đặt quốc hiệu nước ta là Việt Nam vào năm 1804 là ai?",
        "correct_answer": "Gia Long (Nguyễn Ánh)",
        "distractors": ["Minh Mạng", "Thiệu Trị", "Tự Đức"],
        "explanation": "Vua Gia Long lên ngôi năm 1802 định đô ở Phú Xuân (Huế) và đặt quốc hiệu là Việt Nam năm 1804."
    },
    {
        "difficulty": 2,
        "question": "Vua Minh Mạng đã tiến hành cải cách hành chính vào các năm 1831-1832 chia cả nước thành bao nhiêu tỉnh và 1 phủ?",
        "correct_answer": "30 tỉnh và 1 phủ Thừa Thiên",
        "distractors": ["20 tỉnh", "25 tỉnh", "36 tỉnh"],
        "explanation": "Cải cách của vua Minh Mạng đặt nền móng vững chắc cho hệ thống quản lý hành chính tỉnh huyện."
    },
    {
        "difficulty": 1,
        "question": "Thực dân Pháp nổ súng chính thức mở đầu cuộc xâm lược Việt Nam tại đâu vào ngày 1/9/1858?",
        "correct_answer": "Bán đảo Sơn Trà (Đà Nẵng)",
        "distractors": ["Cửa biển Thuận An (Huế)", "Gia Định (Sài Gòn)", "Cửa biển Hải Phòng"],
        "explanation": "Liên quân Pháp - Tây Ban Nha nã đại bác tấn công Đà Nẵng mở đầu cuộc xâm lược Việt Nam."
    },
    {
        "difficulty": 1,
        "question": "Ai là tác giả câu nói bất hủ: 'Bao giờ người Tây nhổ hết cỏ nước Nam thì mới hết người Nam đánh Tây'?",
        "correct_answer": "Nguyễn Trung Trực",
        "distractors": ["Trương Định", "Phan Đình Phùng", "Hoàng Hoa Thám"],
        "explanation": "Anh hùng Nguyễn Trung Trực đã đốt cháy tàu Espérance (Hy Vọng) của Pháp trên sông Nhật Tảo."
    },
    {
        "difficulty": 2,
        "question": "Vị thủ lĩnh kiên cường lãnh đạo cuộc khởi nghĩa Yên Thế chống thực dân Pháp kéo dài gần 30 năm được mệnh danh là gì?",
        "correct_answer": "Hoàng Hoa Thám (Hùm xám Yên Thế)",
        "distractors": ["Phan Đình Phùng", "Đinh Công Tráng", "Nguyễn Thiện Thuật"],
        "explanation": "Đề Thám (Hoàng Hoa Thám) xây dựng căn cứ Phồn Xương khiến quân Pháp nhiều phen bạt vía."
    },
    {
        "difficulty": 2,
        "question": "Phong trào Đông Du đưa thanh niên Việt Nam sang Nhật Bản du học đầu thế kỷ XX do chí sĩ yêu nước nào khởi xướng?",
        "correct_answer": "Phan Bội Châu",
        "distractors": ["Phan Châu Trinh", "Huỳnh Thúc Kháng", "Lương Văn Can"],
        "explanation": "Cụ Phan Bội Châu thành lập Hội Duy Tân năm 1904 và tổ chức phong trào Đông Du."
    },

    # Thời kỳ Cách mạng & Hai cuộc kháng chiến
    {
        "difficulty": 1,
        "question": "Người thanh niên Nguyễn Tất Thành rời bến cảng Nhà Rồng ra đi tìm đường cứu nước vào ngày tháng năm nào?",
        "correct_answer": "Ngày 5/6/1911",
        "distractors": ["Ngày 2/9/1945", "Ngày 3/2/1930", "Ngày 19/8/1945"],
        "explanation": "Bác Hồ lấy tên là Văn Ba lên con tàu Đô đốc Latouche-Tréville bắt đầu hành trình cứu nước."
    },
    {
        "difficulty": 1,
        "question": "Đảng Cộng sản Việt Nam được thành lập vào ngày 3/2/1930 tại thành phố nào?",
        "correct_answer": "Hương Cảng (Hồng Kông, Trung Quốc)",
        "distractors": ["Quảng Châu (Trung Quốc)", "Băng Cốc (Thái Lan)", "Paris (Pháp)"],
        "explanation": "Nguyễn Ái Quốc chủ trì Hội nghị hợp nhất ba tổ chức cộng sản tại Hương Cảng."
    },
    {
        "difficulty": 1,
        "question": "Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập khai sinh nước Việt Nam Dân chủ Cộng hòa tại Quảng trường Ba Đình vào ngày nào?",
        "correct_answer": "Ngày 2/9/1945",
        "distractors": ["Ngày 19/8/1945", "Ngày 27/7/1947", "Ngày 30/4/1975"],
        "explanation": "Ngày 2/9 trở thành ngày Quốc khánh thiêng liêng của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam."
    },
    {
        "difficulty": 1,
        "question": "Lời kêu gọi Toàn quốc kháng chiến của Chủ tịch Hồ Chí Minh được phát động vào ngày tháng năm nào?",
        "correct_answer": "Ngày 19/12/1946",
        "distractors": ["Ngày 2/9/1945", "Ngày 22/12/1944", "Ngày 7/5/1954"],
        "explanation": "'Chúng ta thà hy sinh tất cả, chứ nhất định không chịu mất nước, nhất định không chịu làm nô lệ!'."
    },
    {
        "difficulty": 2,
        "question": "Anh hùng nào đã nhờ đồng đội chặt đứt cánh tay bị thương để tiếp tục xông lên phá lô cốt địch trong Chiến dịch Biên giới 1950?",
        "correct_answer": "La Văn Cầu",
        "distractors": ["Bế Văn Đàn", "Phan Đình Giót", "Cù Chính Lan"],
        "explanation": "Anh hùng La Văn Cầu trở thành tấm gương sáng ngời của tinh thần quyết chiến quyết thắng."
    },
    {
        "difficulty": 1,
        "question": "Chiến dịch Điện Biên Phủ 'lừng lẫy năm châu, chấn động địa cầu' toàn thắng vào ngày tháng năm nào?",
        "correct_answer": "Ngày 7/5/1954",
        "distractors": ["Ngày 13/3/1954", "Ngày 20/7/1954", "Ngày 30/4/1975"],
        "explanation": "Lá cờ 'Quyết chiến Quyết thắng' tung bay trên nóc hầm tướng chỉ huy De Castries chiều ngày 7/5/1954."
    },
    {
        "difficulty": 2,
        "question": "Anh hùng nào đã lấy thân mình chèn bánh pháo trên dốc cao hiểm trở trong chiến dịch Điện Biên Phủ 1954?",
        "correct_answer": "Tô Vĩnh Diện",
        "distractors": ["Bế Văn Đàn", "Phan Đình Giót", "Trần Can"],
        "explanation": "Tô Vĩnh Diện hy sinh thân mình cứu khẩu pháo cao xạ an toàn."
    },
    {
        "difficulty": 2,
        "question": "Anh hùng nào đã lấy thân mình lấp lỗ châu mai mở đường cho đồng đội xông lên tiêu diệt cứ điểm Him Lam?",
        "correct_answer": "Phan Đình Giót",
        "distractors": ["Bế Văn Đàn", "Tô Vĩnh Diện", "Võ Thị Sáu"],
        "explanation": "Tấm gương dũng cảm lấp lỗ châu mai của Phan Đình Giót mãi là biểu tượng bất tử."
    },
    {
        "difficulty": 1,
        "question": "Chiến dịch Hồ Chí Minh lịch sử giải phóng hoàn toàn miền Nam, thống nhất đất nước kết thúc thắng lợi vào ngày nào?",
        "correct_answer": "Ngày 30/4/1975",
        "distractors": ["Ngày 1/5/1975", "Ngày 26/3/1975", "Ngày 2/9/1975"],
        "explanation": "11 giờ 30 phút ngày 30/4/1975, xe tăng húc đổ cổng Dinh Độc Lập, cờ giải phóng tung bay trên nóc dinh."
    },
    {
        "difficulty": 2,
        "question": "Chiếc xe tăng đầu tiên mang số hiệu nào húc đổ cổng chính Dinh Độc Lập trưa ngày 30/4/1975?",
        "correct_answer": "Xe tăng 390",
        "distractors": ["Xe tăng 843", "Xe tăng 555", "Xe tăng 701"],
        "explanation": "Xe tăng T-59 số hiệu 390 do trung úy Vũ Đăng Toàn chỉ huy húc tung cổng chính Dinh Độc Lập."
    },

    # Lịch sử thế giới
    {
        "difficulty": 1,
        "question": "Kim tự tháp Kê-ốp (Khufu) công trình kỳ quan thế giới cổ đại duy nhất còn tồn tại nằm ở quốc gia nào?",
        "correct_answer": "Ai Cập",
        "distractors": ["Hy Lạp", "Ấn Độ", "Iraq"],
        "explanation": "Quần thể kim tự tháp Giza bên dòng sông Nile là kiệt tác kiến trúc cổ đại của Ai Cập."
    },
    {
        "difficulty": 2,
        "question": "Người đầu tiên bay vào vũ trụ quanh quỹ đạo Trái Đất vào ngày 12/4/1961 là phi hành gia nước nào?",
        "correct_answer": "Yuri Gagarin (Liên Xô)",
        "distractors": ["Neil Armstrong (Mỹ)", "Phạm Tuân (Việt Nam)", "Dương Lợi Vĩ (Trung Quốc)"],
        "explanation": "Yuri Gagarin lái con tàu Vostok 1 mở ra kỷ nguyên chinh phục không gian của loài người."
    },
    {
        "difficulty": 2,
        "question": "Phi hành gia người Mỹ nào là người đầu tiên đặt chân lên bề mặt Mặt Trăng vào ngày 20/7/1969?",
        "correct_answer": "Neil Armstrong",
        "distractors": ["Buzz Aldrin", "Michael Collins", "Alan Shepard"],
        "explanation": "Armstrong phát biểu câu nói lịch sử: 'Đây là bước đi nhỏ bé của một người, nhưng là bước tiến khổng lồ của nhân loại'."
    },
    {
        "difficulty": 1,
        "question": "Tổ chức quốc tế Liên Hợp Quốc (UN) được chính thức thành lập vào năm nào sau Thế chiến thứ hai?",
        "correct_answer": "Năm 1945",
        "distractors": ["Năm 1939", "Năm 1950", "Năm 1918"],
        "explanation": "Hiến chương Liên Hợp Quốc có hiệu lực từ ngày 24/10/1945 nhằm duy trì hòa bình và an ninh quốc tế."
    },
    {
        "difficulty": 2,
        "question": "Ai là người phát minh ra máy hơi nước hoàn chỉnh vào năm 1769 tạo tiền đề cho cuộc Cách mạng công nghiệp?",
        "correct_answer": "James Watt",
        "distractors": ["Thomas Edison", "George Stephenson", "Henry Ford"],
        "explanation": "Máy hơi nước của James Watt đã thúc đẩy sản xuất công nghiệp và giao thông đường sắt phát triển vượt bậc."
    }
]

# Sinh thêm tự động các câu hỏi lịch sử có chiều sâu trải khắp các giai đoạn
HISTORICAL_FACTS = [
    ("Đinh Bộ Lĩnh chọn loài cờ lau làm binh khí tập trận giả lúc còn chăn trâu ở đâu?", "Thung Lau (Hoa Lư, Ninh Bình)", ["Thung Nham", "Tràng An", "Yên Khánh"], "Trò chơi cờ lau tập trận rèn luyện tài cầm quân của Đinh Bộ Lĩnh từ thuở thiếu thời.", 1),
    ("Vị tướng nào thời Tiền Lê được vua cử làm chánh sứ sang cống nhà Tống và dùng thơ đối đáp sắc sảo?", "Giang Văn Minh", ["Lương Thế Vinh", "Mạc Đĩnh Chi", "Nguyễn Biểu"], "Giang Văn Minh được mệnh danh là danh sứ 'khẳng khái không làm nhục mệnh vua'.", 2),
    ("Lý Thường Kiệt cho đục tượng rùa vàng đội bia đá ở chùa nào tại Thanh Hóa?", "Chùa Báo Ân", ["Chùa Hương", "Chùa Bái Đính", "Chùa Một Cột"], "Bia chùa Báo Ân ghi lại nhiều công tích của Thái úy Lý Thường Kiệt.", 3),
    ("Hội nghị quân sự Bình Than năm 1282 được tổ chức trên bến sông nào?", "Sông Đuống (sông Thiên Đức)", ["Sông Bạch Đằng", "Sông Cầu", "Sông Hồng"], "Hội nghị bàn kế đánh giặc Nguyên Mông quy tụ các vương hầu nhà Trần.", 2),
    ("Trần Bình Trọng nổi tiếng với câu nói thà làm quỷ nước Nam chứ không thèm làm gì đất Bắc?", "Thà làm quỷ nước Nam chứ không thèm làm vương đất Bắc", ["Làm tướng đất Bắc", "Làm tôi đất Bắc", "Làm lính đất Bắc"], "Trần Bình Trọng bị giặc Nguyên bắt và hiên ngang hy sinh bảo vệ khí tiết dân tộc.", 1),
    ("Vị danh y nào thời Trần được tôn là ông tổ của ngành thuốc Nam Việt Nam với câu nói 'Thuốc Nam trị người Nam'?", "Thiền sư Tuệ Tĩnh", ["Hải Thượng Lãn Ông", "Lê Hữu Trác", "Lê Quý Đôn"], "Bộ sách 'Nam dược thần hiệu' của Tuệ Tĩnh là di sản y học vô giá.", 1),
    ("Trận quyết chiến Đống Đa xuân Kỷ Dậu 1789 khiến tướng giặc nào của quân Thanh phải thắt cổ tự tử?", "Sầm Nghi Đống", ["Tôn Sĩ Nghị", "Hứa Thế Hanh", "Lưu Hoằng Tháo"], "Chủ tướng Sầm Nghi Đống khiếp sợ thắt cổ tự vẫn tại gò Đống Đa.", 2),
    ("Vị tổng đốc Hà Nội nào đã tuẫn tiết theo thành khi Hà Nội thất thủ vào tay thực dân Pháp năm 1873?", "Nguyễn Tri Phương", ["Hoàng Diệu", "Phan Đình Phùng", "Tôn Thất Thuyết"], "Tổng đốc Nguyễn Tri Phương thà chết đói chứ không chịu nhận sự cứu chữa của giặc Pháp.", 2),
    ("Tổng đốc Hoàng Diệu đã tuẫn tiết tại đâu khi quân Pháp đánh chiếm thành Hà Nội lần thứ hai năm 1882?", "Cửa Bắc (Võ Miếu)", ["Cửa Nam", "Cột Cờ Hà Nội", "Cửa Đông"], "Hoàng Diệu thắt cổ tự tử giữ tròn khí tiết tại Võ Miếu cạnh Cửa Bắc.", 2),
    ("Vua Hàm Nghi ban chiếu Cần Vương kêu gọi nhân dân phò vua đánh Pháp vào năm nào?", "Năm 1885", ["Năm 1883", "Năm 1888", "Năm 1890"], "Chiếu Cần Vương phát động phong trào đấu tranh vũ trang yêu nước sôi nổi cuối thế kỷ XIX.", 2),
    ("Ai là tác giả của 'Hải Thượng y tông tâm lĩnh' bộ bách khoa toàn thư y học cổ truyền Việt Nam?", "Hải Thượng Lãn Ông (Lê Hữu Trác)", ["Tuệ Tĩnh", "Phan Phù Tiên", "Chu Văn An"], "Đại danh y Lê Hữu Trác quê ở Hải Dương, sống và bốc thuốc tại Hương Sơn, Hà Tĩnh.", 1),
    ("Tờ báo cách mạng đầu tiên của nước ta mang tên 'Thanh niên' do Nguyễn Ái Quốc sáng lập số đầu tiên ra ngày nào?", "Ngày 21/6/1925", ["Ngày 3/2/1930", "Ngày 2/9/1945", "Ngày 19/8/1945"], "Ngày 21/6 hàng năm được chọn làm Ngày Báo chí Cách mạng Việt Nam.", 2),
    ("Đội Việt Nam Tuyên truyền Giải phóng quân tiền thân của Quân đội Nhân dân Việt Nam thành lập ngày 22/12/1944 tại khu rừng nào?", "Khu rừng Trần Hưng Đạo (Cao Bằng)", ["Pác Bó (Cao Bằng)", "Tân Trào (Tuyên Quang)", "Định Hóa (Thái Nguyên)"], "Đội gồm 34 chiến sĩ do đồng chí Võ Nguyên Giáp trực tiếp chỉ huy thành lập.", 1),
    ("Tỉnh lỵ đầu tiên được giải phóng trong Chiến dịch Tây Nguyên mở màn cuộc Tổng tiến công và nổi dậy mùa Xuân 1975 là gì?", "Buôn Ma Thuột", ["Pleiku", "Kon Tum", "Đà Lạt"], "Trận đột phá mở màn Buôn Ma Thuột ngày 10/3/1975 làm rung chuyển toàn bộ hệ thống phòng thủ địch.", 2),
    ("Hiệp định Paris về chấm dứt chiến tranh, lập lại hòa bình ở Việt Nam được ký kết vào năm nào?", "Năm 1973", ["Năm 1954", "Năm 1972", "Năm 1975"], "Hiệp định buộc quân đội Mỹ và đồng minh phải rút toàn bộ quân về nước.", 1),
    ("Đại hội đại biểu toàn quốc lần thứ VI của Đảng khởi xướng công cuộc Đổi Mới toàn diện đất nước diễn ra vào năm nào?", "Năm 1986", ["Năm 1980", "Năm 1990", "Năm 1995"], "Đại hội VI (tháng 12/1986) mở ra bước ngoặt lịch sử đưa nền kinh tế đất nước cất cánh.", 1),
    ("Việt Nam chính thức gia nhập Hiệp hội các quốc gia Đông Nam Á (ASEAN) vào năm nào?", "Năm 1995", ["Năm 1990", "Năm 1998", "Năm 2000"], "Ngày 28/7/1995, Việt Nam chính thức trở thành thành viên thứ 7 của ASEAN.", 1),
    ("Việt Nam chính thức trở thành thành viên thứ 150 của Tổ chức Thương mại Thế giới (WTO) vào năm nào?", "Năm 2007", ["Năm 2005", "Năm 2008", "Năm 2010"], "Việt Nam gia nhập WTO mở ra thời kỳ hội nhập sâu rộng vào kinh tế toàn cầu.", 2),
    ("Ai là vị nữ tướng tài ba chỉ huy đội quân tóc dài trong phong trào Đồng Khởi Bến Tre năm 1960?", "Nguyễn Thị Định", ["Võ Thị Thắng", "Võ Thị Sáu", "Lê Thị Hồng Gấm"], "Bà Nguyễn Thị Định sau này trở thành nữ Thiếu tướng đầu tiên của Quân đội Nhân dân Việt Nam.", 1),
    ("Nữ anh hùng miền Đất Đỏ Võ Thị Sáu hy sinh kiên cường tại nhà tù Côn Đảo vào năm nào?", "Năm 1952", ["Năm 1950", "Năm 1954", "Năm 1947"], "Chị Võ Thị Sáu ngẩng cao đầu hát vang bài Tiến quân ca trước họng súng kẻ thù.", 1)
]

for item in HISTORICAL_FACTS:
    QUESTIONS.append({
        "difficulty": item[4],
        "question": item[0],
        "correct_answer": item[1],
        "distractors": item[2],
        "explanation": item[3]
    })

# Mở rộng thêm 160 câu hỏi lịch sử đa dạng, phong phú
EXPANDED_HISTORY = [
    # Cổ - Trung đại
    ("Trận Bạch Đằng năm 938 diễn ra vào thời điểm nào trong ngày để tận dụng thủy triều?", "Khi thủy triều bắt đầu rút xuống", ["Khi thủy triều dâng cao nhất", "Nửa đêm", "Bình minh khi sương mù dày đặc"], "Ngô Quyền nhử thuyền chiến giặc vượt qua bãi cọc khi nước triều lên, rồi phản công khi triều rút làm thuyền giặc mắc cọc vỡ nát.", 2),
    ("Ai là người đầu tiên xưng đế và đặt tên nước là Vạn Xuân trong lịch sử nước ta?", "Lý Nam Đế (Lý Bí)", ["Triệu Đà", "Đinh Tiên Hoàng", "Ngô Quyền"], "Lý Nam Đế mong muốn đất nước ta sẽ mãi mãi trường tồn vạn mùa xuân tươi đẹp.", 1),
    ("Lê Phụng Hiểu danh tướng thời Lý nổi tiếng với hội thi vật và lệ thưởng đất đai nào?", "Lệ ném đao chia ruộng (Thác đao điền)", ["Thưởng vàng ròng", "Phong tước vương", "Cho đúc chuông đồng"], "Ông đứng trên núi ném đao, đao rơi đến đâu thì triều đình ban đất cho đến đấy.", 3),
    ("Nguyên phi Ỷ Lan hai lần nhiếp chính giúp nước thái bình dưới triều vua Lý nào?", "Lý Thánh Tông và Lý Nhân Tông", ["Lý Thái Tổ", "Lý Thái Tông", "Lý Cao Tông"], "Bà được dân gian tôn kính gọi là 'Quan Âm Nữ' vì lòng nhân hậu và tài trị nước.", 2),
    ("Quốc Tử Giám trường đại học đầu tiên của nước ta được mở ra năm 1076 dưới thời vua nào?", "Lý Nhân Tông", ["Lý Thái Tổ", "Lý Thái Tông", "Lý Thánh Tông"], "Vua Lý Nhân Tông cho lập Quốc Tử Giám để đào tạo nhân tài cho đất nước.", 2),
    ("Thủ khoa đầu tiên trong kỳ thi Nho học đầu tiên của nước ta năm 1075 là ai?", "Lê Văn Thịnh", ["Mạc Đĩnh Chi", "Chu Văn An", "Nguyễn Hiền"], "Khoa thi Minh kinh bác học năm 1075 do triều Lý tổ chức tuyển chọn nhân tài.", 2),
    ("Trạng nguyên trẻ tuổi nhất trong lịch sử khoa bảng Việt Nam đỗ trạng nguyên năm 13 tuổi là ai?", "Nguyễn Hiền", ["Lê Văn Thịnh", "Lương Thế Vinh", "Mạc Đĩnh Chi"], "Nguyễn Hiền quê Nam Định nổi tiếng thông minh đỗ Trạng nguyên năm 1247 thời vua Trần Thái Tông.", 2),
    ("Danh nhân nào được phong là 'Lưỡng quốc Trạng nguyên' sau chuyến đi sứ sang triều Nguyên?", "Mạc Đĩnh Chi", ["Nguyễn Trực", "Lương Thế Vinh", "Phùng Khắc Khoan"], "Mạc Đĩnh Chi nổi tiếng với bài phú 'Hoa sen trong giếng ngọc' khiến vua quan nhà Nguyên thán phục phong trạng nguyên.", 2),
    ("Nhà toán học kiệt xuất thời Hậu Lê tác giả cuốn 'Đại thành toán pháp' và cân voi cho sứ Tàu là ai?", "Lương Thế Vinh (Trạng Lường)", ["Lê Quý Đôn", "Nguyễn Bỉnh Khiêm", "Phan Huy Chú"], "Trạng Lường Lương Thế Vinh dùng phương pháp thả thuyền đo mực nước để cân voi chính xác.", 1),
    ("Trạng Trình Nguyễn Bỉnh Khiêm nổi tiếng với lời sấm truyền nào giúp chúa Nguyễn mở mang bờ cõi phía Nam?", "'Hoành Sơn nhất đái, vạn đại dung thân'", ["'Nam quốc sơn hà'", "'Thuận thiên giả tồn'", "'Bắc Bình quy nhất'"], "Lời khuyên của Trạng Trình giúp Nguyễn Hoàng vào trấn thủ xứ Thuận Hóa khai phá phương Nam.", 2),
    ("Thành phố Hải Phòng gắn liền với nữ tướng nào của cuộc khởi nghĩa Hai Bà Trưng lập trang An Biên?", "Nữ tướng Lê Chân", ["Nữ tướng Bát Nàn", "Thánh Thiên công chúa", "Thiều Hoa công chúa"], "Nữ tướng Lê Chân có công khai phá vùng đất Hải Phòng ngày nay.", 2),
    ("Vị tướng nào thời Trần chỉ huy trận Vân Đồn năm 1288 đánh chìm toàn bộ đoàn thuyền lương của Trương Văn Hổ?", "Trần Khánh Dư", ["Trần Quang Khải", "Trần Nhật Duật", "Phạm Ngũ Lão"], "Trận phục kích Vân Đồn cắt đứt nguồn lương thảo khiến quân Nguyên lâm vào cảnh đói khát khốn đốn.", 2),
    ("Phạm Ngũ Lão ngồi đan sọt bên đường bị giáo đâm vào đùi không biết vì mải mê suy nghĩ điều gì?", "Binh thư và việc nước", ["Làm thơ vịnh cảnh", "Tính kế kinh doanh", "Học võ nghệ"], "Hưng Đạo Vương Trần Hưng Đạo nhận thấy tài năng xuất chúng bèn thu nạp và gả con gái nuôi cho ông.", 1),
    ("Trần Nhật Duật dùng tài hiểu biết ngôn ngữ và phong tục để thu phục tù trưởng người Man nào trong kháng chiến chống Nguyên?", "Trịnh Giác Mật", ["Hà Đặc", "Đỗ Vĩ", "Lưu Kế Hưng"], "Trần Nhật Duật uyên bác tinh thông nhiều thứ tiếng dân tộc và ngoại ngữ.", 3),
    ("Ai là người chế tạo súng Thần cơ và thuyền chiến Cổ Lâu dưới triều nhà Hồ?", "Hồ Nguyên Trừng", ["Hồ Hán Thương", "Hồ Quý Ly", "Trần Khát Chân"], "Hồ Nguyên Trừng là nhà quân sự và nhà kỹ thuật quân khí kiệt xuất của dân tộc ta.", 2),
    ("Hội thề Lũng Nhai năm 1416 gồm bao nhiêu vị tướng lĩnh cùng Lê Lợi cắt máu ăn thề đánh giặc Minh?", "19 người (kể cả Lê Lợi)", ["12 người", "24 người", "36 người"], "Hội thề Lũng Nhai đánh dấu bước chuẩn bị then chốt cho khởi nghĩa Lam Sơn bùng nổ.", 3),
    ("Sau hội thề Lũng Nhai, ai là người tự nguyện đóng giả Lê Lợi đem quân liều mình cứu chúa tại núi Chí Linh?", "Lê Lai", ["Nguyễn Xí", "Đinh Lễ", "Trần Nguyên Hãn"], "Tấm gương hy sinh quả cảm của Lê Lai cứu chủ tướng Lê Lợi được người đời ca ngợi 'Lê Lai liều mình cứu chúa'.", 1),
    ("Nguyễn Trãi sau khi đất nước thái bình đã lui về ẩn dật tại ngọn núi non thanh tịnh nào?", "Côn Sơn (Chí Linh, Hải Dương)", ["Yên Tử (Quảng Ninh)", "Ba Vì (Hà Nội)", "Hương Tích (Hà Tĩnh)"], "Côn Sơn suối chảy rì rầm / Ta nghe như tiếng đàn cầm bên tai.", 1),
    ("Kỳ thi tuyển chọn quan lại nào thời phong kiến nước ta được tổ chức 3 năm một lần ở cấp trung ương tại kinh đô?", "Thi Hội và thi Đình", ["Thi Hương", "Thi Huyện", "Thi Khảo"], "Thi Hương tổ chức tại các địa phương, người đỗ cao vào kinh đô dự thi Hội và thi Đình.", 2),
    ("Bia đá đầu tiên khắc tên các tiến sĩ tại Văn Miếu Thăng Long được dựng vào năm 1484 dưới thời vua nào?", "Lê Thánh Tông", ["Lê Thái Tổ", "Lý Thánh Tông", "Trần Nhân Tông"], "Thân Nhân Trung phụng mệnh vua soạn câu bất hủ: 'Hiền tài là nguyên khí của quốc gia'.", 2),
    ("Vị tướng quân đội Tây Sơn nào chỉ huy mũi tiến công bất ngờ đánh đồn Khương Thượng khiến giặc Thanh đại bại?", "Đô đốc Đặng Tiến Đông (hoặc Đặng Xuân Bảo)", ["Đô đốc Long", "Ngô Văn Sở", "Phan Văn Lân"], "Trận Khương Thượng khiến tướng giặc Sầm Nghi Đống phải treo cổ tự vẫn tại gò Đống Đa.", 3),
    ("Nguyễn Huệ làm lễ tế cáo trời đất lên ngôi Hoàng đế lấy niên hiệu là Quang Trung tại ngọn núi nào ở Huế?", "Núi Bân", ["Núi Ngự Bình", "Núi Bạch Mã", "Núi Kim Phụng"], "Núi Bân (An Tây, Huế) là nơi Nguyễn Huệ đăng quang trước khi thần tốc tiến quân ra Bắc diệt giặc Thanh.", 2),
    ("Chiếc áo chiến bào màu đỏ của vua Quang Trung khi tiến vào Thăng Long ngày mùng 5 Tết có đặc điểm gì nổi bật?", "Nhuộm đen khói súng vì trực tiếp xông pha trận mạc", ["Dát vàng lấp lánh", "Thêu rồng vàng nguyên vẹn", "Đính ngọc bích"], "Hình ảnh vua Quang Trung áo bào sạm khói súng dẫn đầu đại quân là biểu tượng khí phách của dân tộc anh hùng.", 2),
    ("Cuộc cải cách hành chính năm 1831 của vua Minh Mạng đã đổi tên kinh thành Thăng Long thành tỉnh gì?", "Tỉnh Hà Nội", ["Tỉnh Bắc Ninh", "Tỉnh Sơn Tây", "Tỉnh Hải Dương"], "Tên gọi 'Hà Nội' (vùng đất nằm trong các con sông) chính thức xuất hiện từ năm 1831.", 2),
    ("Tỉnh nào ở Nam Bộ là tỉnh cuối cùng của Nam Kỳ Lục Tỉnh rơi vào tay thực dân Pháp năm 1867?", "Hà Tiên (cùng Vĩnh Long, Châu Đốc)", ["Gia Định", "Định Tường", "Biên Hòa"], "Pháp chiếm 3 tỉnh miền Đông năm 1862 và lấn chiếm nốt 3 tỉnh miền Tây năm 1867.", 3),
    ("Ai là tác giả của 'Văn tế nghĩa sĩ Cần Giuộc' bài ca ca ngợi những người nông dân mặc áo vải cầm giáo mác đánh giặc?", "Nguyễn Đình Chiểu", ["Phan Văn Trị", "Nguyễn Thông", "Hồ Huân Nghiệp"], "Cụ đồ Chiểu để lại áng văn bi tráng ca ngợi tinh thần xả thân vì nghĩa của người nghĩa sĩ nông dân.", 1),
    ("Trận phục kích giết chết viên đại úy Pháp Francis Garnier năm 1873 diễn ra tại địa danh nào ở Hà Nội?", "Cầu Giấy", ["Cửa Bắc", "Đống Đa", "Ô Cầu Dền"], "Đội quân cờ đen do Lưu Vĩnh Phúc chỉ huy phối hợp quân triều đình tiêu diệt giặc tại Cầu Giấy.", 2),
    ("Viên quan đại thần kiên quyết chủ chiến tổ chức tấn công quân Pháp tại kinh thành Huế đêm 5/7/1885 là ai?", "Tôn Thất Thuyết", ["Nguyễn Văn Tường", "Trần Tiễn Thành", "Phan Thanh Giản"], "Tôn Thất Thuyết sau đó phò tá vua Hàm Nghi ra sơn phòng Quảng Trị phát động phong trào Cần Vương.", 2),
    ("Căn cứ Ba Đình trong phong trào Cần Vương do Phạm Bành và Đinh Công Tráng chỉ huy thuộc tỉnh nào?", "Thanh Hóa", ["Nghệ An", "Hà Tĩnh", "Quảng Bình"], "Chiến khu Ba Đình được bao bọc bởi lũy tre dày đặc và hệ thống hầm hào liên hoàn kiên cố.", 2),
    ("Khởi nghĩa Hương Khê cuộc khởi nghĩa tiêu biểu và bền bỉ nhất trong phong trào Cần Vương do ai lãnh đạo?", "Phan Đình Phùng và Cao Thắng", ["Đinh Công Tráng", "Nguyễn Thiện Thuật", "Nguyễn Quang Bích"], "Cao Thắng là tướng tài đã tự chế tạo thành công súng trường theo mẫu súng Pháp 1874.", 2),

    # Lịch sử Hiện đại Việt Nam
    ("Nguyễn Ái Quốc gửi bản 'Yêu sách của nhân dân An Nam' đến Hội nghị Versailles vào năm nào?", "Năm 1919", ["Năm 1911", "Năm 1920", "Năm 1925"], "Bản yêu sách 8 điểm đòi quyền tự do dân chủ cho dân tộc Việt Nam gây tiếng vang lớn.", 2),
    ("Nguyễn Ái Quốc bỏ phiếu tán thành gia nhập Quốc tế III và tham gia sáng lập Đảng Cộng sản Pháp tại Đại hội Tours năm nào?", "Năm 1920", ["Năm 1919", "Năm 1923", "Năm 1925"], "Người trở thành người cộng sản Việt Nam đầu tiên đánh dấu bước chuyển từ chủ nghĩa yêu nước đến chủ nghĩa Mác - Lênin.", 2),
    ("Tổ chức tiền thân trực tiếp của Đảng Cộng sản Việt Nam do Nguyễn Ái Quốc thành lập năm 1925 tại Quảng Châu là gì?", "Hội Việt Nam Cách mạng Thanh niên", ["Tâm tâm xã", "Việt Nam Quang phục hội", "Đông Dương Cộng sản Đảng"], "Hội đã xuất bản tờ báo Thanh niên và cuốn sách lý luận bất hủ 'Đường Kách mệnh'.", 2),
    ("Sau 30 năm bôn ba tìm đường cứu nước, Bác Hồ trở về Tổ quốc vào mùa xuân năm nào tại cột mốc 108?", "Năm 1941", ["Năm 1930", "Năm 1945", "Năm 1946"], "Mùa xuân năm 1941, Bác về đến Pác Bó (Hà Quảng, Cao Bằng) trực tiếp lãnh đạo cách mạng Việt Nam.", 1),
    ("Mặt trận Việt Minh (Việt Nam Độc lập Đồng minh) được thành lập vào tháng 5/1941 tại đâu?", "Pác Bó (Cao Bằng)", ["Tân Trào (Tuyên Quang)", "Hương Cảng", "Định Hóa (Thái Nguyên)"], "Mặt trận Việt Minh tập hợp mọi tầng lớp nhân dân yêu nước đứng lên đánh Pháp, đuổi Nhật.", 2),
    ("Ủy ban Dân tộc Giải phóng Việt Nam được Quốc dân Đại hội Tân Trào bầu ra vào tháng 8/1945 do ai làm Chủ tịch?", "Hồ Chí Minh", ["Trường Chinh", "Võ Nguyên Giáp", "Phạm Văn Đồng"], "Quốc dân Đại hội Tân Trào là tiền thân của Quốc hội đầu tiên của nước ta.", 1),
    ("Cuộc Tổng khởi nghĩa giành chính quyền ở Hà Nội trong Cách mạng Tháng Tám diễn ra vào ngày nào?", "Ngày 19/8/1945", ["Ngày 23/8/1945", "Ngày 25/8/1945", "Ngày 2/9/1945"], "Nhân dân Hà Nội mít tinh tại Nhà hát Lớn và đánh chiếm các cơ quan đầu não của chính quyền tay sai.", 1),
    ("Vị hoàng đế cuối cùng của chế độ phong kiến Việt Nam tuyên bố thoái vị tại kinh thành Huế tháng 8/1945 là ai?", "Vua Bảo Đại", ["Vua Khải Định", "Vua Duy Tân", "Vua Hàm Nghi"], "Bảo Đại tuyên bố: 'Thà làm dân một nước độc lập hơn làm vua một nước nô lệ'.", 1),
    ("Kỳ bầu cử Quốc hội khóa I đầu tiên trong lịch sử nước Việt Nam Dân chủ Cộng hòa diễn ra vào ngày tháng năm nào?", "Ngày 6/1/1946", ["Ngày 2/9/1945", "Ngày 19/12/1946", "Ngày 3/2/1946"], "Toàn dân từ 18 tuổi trở lên nô nức đi bỏ phiếu thực hiện quyền làm chủ đất nước.", 2),
    ("Chiến dịch phản công nào đã phá tan hoàn toàn kế hoạch đánh nhanh thắng nhanh của thực dân Pháp lên căn cứ địa cách mạng năm 1947?", "Chiến dịch Việt Bắc Thu - Đông 1947", ["Chiến dịch Biên giới 1950", "Chiến dịch Hòa Bình 1951", "Chiến dịch Tây Bắc 1952"], "Quân và dân ta bắn chìm nhiều tàu chiến Pháp trên sông Lô và đánh tan quân dù địch ở Chợ Đồn, Chợ Mới.", 2),
    ("Đại tướng Võ Nguyên Giáp đã quyết định chuyển phương châm tác chiến tại Điện Biên Phủ từ 'Đánh nhanh thắng nhanh' sang phương châm gì?", "'Đánh chắc, tiến chắc'", ["'Đánh du kích'", "'Vây hãm cô lập'", "'Đánh bộc phá'"], "Đây được coi là quyết định lịch sử khó khăn nhất trong cuộc đời cầm quân của Đại tướng.", 2),
    ("Đồi A1 cứ điểm phòng ngự kiên cố bậc nhất của Pháp tại Điện Biên Phủ bị quân ta giật sập bởi khối bộc phá nặng bao nhiêu cân?", "Khối bộc phá gần 1 tấn (khoảng 960 kg)", ["500 kg", "200 kg", "2 tấn"], "Tiếng nổ của khối bộc phá đêm 6/5/1954 là hiệu lệnh tổng công kích tiêu diệt tập đoàn cứ điểm Điện Biên Phủ.", 2),
    ("Đoàn tàu không số gắn liền với tuyến đường vận tải chi viện vũ khí huyền thoại nào trên biển trong kháng chiến chống Mỹ?", "Đường Hồ Chí Minh trên biển", ["Đường Trường Sơn", "Đường 1A", "Đường 9"], "Những con tàu không số vượt qua sóng to gió lớn và sự bao vây của hải quân địch để chi viện cho chiến trường miền Nam.", 1),
    ("Ai là nữ bác sĩ liệt sĩ anh dũng hy sinh tại chiến trường Đức Phổ (Quảng Ngãi) tác giả cuốn nhật ký lay động triệu trái tim?", "Đặng Thùy Trâm", ["Lê Thị Hồng Gấm", "Võ Thị Tần", "Bùi Thị Cúc"], "Cuốn 'Nhật ký Đặng Thùy Trâm' tỏa sáng lý tưởng cách mạng trong sáng của tuổi trẻ Việt Nam.", 1),
    ("10 cô gái thanh niên xung phong ngã ba Đồng Lộc anh dũng hy sinh vì mạch máu giao thông thông suốt thuộc tỉnh nào?", "Hà Tĩnh", ["Quảng Bình", "Nghệ An", "Quảng Trị"], "Ngã ba Đồng Lộc là tọa độ lửa ghi dấu chiến công bất tử của tiểu đội 4 anh hùng do Võ Thị Tần làm tiểu đội trưởng.", 1),
    ("Chiến dịch 'Hà Nội - Điện Biên Phủ trên không' cuối tháng 12 năm 1972 đã bắn rơi bao nhiêu pháo đài bay B-52 của không quân Mỹ?", "34 máy bay B-52", ["15 máy bay B-52", "50 máy bay B-52", "20 máy bay B-52"], "Quân dân miền Bắc đập tan chiến dịch Linebacker II buộc Mỹ phải ký Hiệp định Paris.", 2),
    ("Địa đạo Củ Chi công trình phòng thủ ngầm kỳ vĩ được mệnh danh là 'Thành đồng đất thép' thuộc địa bàn thành phố nào?", "Thành phố Hồ Chí Minh", ["Tây Ninh", "Bình Dương", "Đồng Nai"], "Hệ thống địa đạo dài hàng trăm km trong lòng đất gồm trạm xá, phòng họp, bếp Hoàng Cầm, kho vũ khí.", 1),
    ("Chiến dịch giải phóng hoàn toàn miền Nam mùa Xuân năm 1975 ban đầu mang tên gì trước khi được đổi thành Chiến dịch Hồ Chí Minh?", "Chiến dịch Giải phóng Sài Gòn - Gia Định", ["Chiến dịch Tây Nguyên", "Chiến dịch Huế - Đà Nẵng", "Chiến dịch Xuân Lộc"], "Bộ Chính trị quyết định đổi tên chiến dịch mang tên Bác Hồ kính yêu vào ngày 14/4/1975.", 2),
    ("Người chiến sĩ cắm cờ Mặt trận Dân tộc Giải phóng miền Nam trên nóc Dinh Độc Lập trưa ngày 30/4/1975 là ai?", "Bùi Quang Thận", ["Vũ Đăng Toàn", "Nguyễn Văn Tập", "Lê Văn Phượng"], "Đại đội trưởng Bùi Quang Thận chỉ huy xe tăng 843 lên cắm cờ giải phóng.", 2),

    # Văn hóa Lịch sử & Thế giới
    ("Tác phẩm lịch sử đầu tiên ghi chép hoàn chỉnh lịch sử nước ta từ thời Hồng Bàng đến đời vua Lý Chiêu Hoàng là gì?", "'Đại Việt sử ký' của Lê Văn Hưu", ["'Đại Việt sử lược'", "'Khâm định Việt sử'", "'Đại Nam thực lục'"], "Lê Văn Hưu soạn xong bộ Đại Việt sử ký gồm 30 quyển vào năm 1272 đời vua Trần Thánh Tông.", 2),
    ("Tập thơ chữ Hán 'Nhật ký trong tù' (Ngục trung nhật ký) được Chủ tịch Hồ Chí Minh sáng tác trong khoảng thời gian nào?", "1942 - 1943", ["1930 - 1931", "1945 - 1946", "1954 - 1955"], "Bác sáng tác tập thơ gồm 133 bài trong nhà lao của chính quyền Tưởng Giới Thạch ở Quảng Tây.", 1),
    ("Quần thể di tích Cố đô Huế được UNESCO vinh danh là Di sản Văn hóa Thế giới đầu tiên của Việt Nam vào năm nào?", "Năm 1993", ["Năm 1999", "Năm 2003", "Năm 2010"], "Cố đô Huế với hệ thống cung điện, lăng tẩm triều Nguyễn là di sản văn hóa vật thể vô giá.", 2),
    ("Hoàng thành Thăng Long được UNESCO công nhận là Di sản Văn hóa Thế giới đúng vào dịp kỷ niệm nào?", "Đại lễ 1000 năm Thăng Long - Hà Nội (2010)", ["Kỷ niệm 990 năm Thăng Long", "Năm du lịch quốc gia 2005", "Đại lễ 950 năm Thăng Long"], "Hoàng thành Thăng Long minh chứng cho bề dày nghìn năm lịch sử tụ khí non sông.", 1),
    ("Vạn Lý Trường Thành kỳ quan phòng thủ quân sự dài nhất thế giới được khởi công xây dựng từ thời hoàng đế nào của Trung Quốc?", "Tần Thủy Hoàng", ["Hán Vũ Đế", "Đường Thái Tông", "Minh Thành Tổ"], "Tần Thủy Hoàng nối liền và mở rộng các bức tường thành để ngăn chặn các bộ tộc du mục phương Bắc.", 1),
    ("Thành phố cổ Pompeii của La Mã cổ đại bị chôn vùi trong tro bụi bởi thảm họa phun trào của núi lửa nào năm 79 SCN?", "Núi lửa Vesuvius", ["Núi lửa Etna", "Núi lửa Fuji", "Núi lửa Krakatoa"], "Pompeii bị bảo quản gần như nguyên vẹn dưới lớp tro bụi dung nham suốt hàng nghìn năm.", 2),
    ("Ai là vị danh họa thời Phục hưng tác giả của hai kiệt tác bất hủ 'Mona Lisa' và 'Bữa ăn tối cuối cùng'?", "Leonardo da Vinci", ["Michelangelo", "Raphael", "Donatello"], "Leonardo da Vinci là thiên tài toàn năng người Ý trong thời kỳ Phục hưng.", 1),
    ("Cuộc Cách mạng công nghiệp lần thứ nhất bắt đầu tại quốc gia nào vào nửa cuối thế kỷ XVIII?", "Nước Anh", ["Nước Pháp", "Nước Đức", "Nước Mỹ"], "Nước Anh là cái nôi của cách mạng công nghiệp nhờ phát minh máy dệt và máy hơi nước.", 1),
    ("Tuyên ngôn Nhân quyền và Dân quyền nổi tiếng với khẩu hiệu 'Tự do - Bình đẳng - Bác ái' ra đời trong cuộc cách mạng nào?", "Cách mạng tư sản Pháp 1789", ["Cách mạng tư sản Anh", "Chiến tranh giành độc lập Mỹ", "Cách mạng Tháng Mười Nga"], "Bản Tuyên ngôn đặt nền tảng cho quyền con người trong thời kỳ cận - hiện đại.", 1),
    ("Kênh đào Suez nối liền Địa Trung Hải và Biển Đỏ được khánh thành đưa vào sử dụng vào năm nào?", "Năm 1869", ["Năm 1914", "Năm 1850", "Năm 1900"], "Kênh đào Suez rút ngắn hàng nghìn hải lý đường biển giữa châu Âu và châu Á.", 2),
    ("Kênh đào Panama nối liền Đại Tây Dương và Thái Bình Dương chính thức khánh thành năm nào?", "Năm 1914", ["Năm 1869", "Năm 1920", "Năm 1945"], "Kênh đào Panama là kỳ tích kỹ thuật vĩ đại của thế kỷ XX giúp tàu bè tránh phải vòng qua mũi Horn.", 2),
    ("Chiến tranh thế giới thứ nhất bùng nổ vào năm 1914 và kết thúc vào năm nào?", "Năm 1918", ["Năm 1917", "Năm 1919", "Năm 1920"], "Hiệp ước đình chiến Compiègne được ký kết vào ngày 11/11/1918 kết thúc Thế chiến thứ nhất.", 1),
    ("Chiến tranh thế giới thứ hai chính thức bùng nổ khi phát xít Đức tấn công quốc gia nào vào ngày 1/9/1939?", "Ba Lan", ["Pháp", "Liên Xô", "Tiệp Khắc"], "Cuộc tấn công Ba Lan của quân Đức khơi mào cho cuộc chiến tranh tàn khốc nhất lịch sử.", 1),
    ("Trận Stalingrad (1942 - 1943) được coi là bước ngoặt quyết định của Thế chiến thứ hai diễn ra tại quốc gia nào?", "Liên Xô", ["Đức", "Anh", "Pháp"], "Hồng quân Liên Xô bao vây và tiêu diệt tập đoàn quân số 6 của tướng Paulus bẻ gãy ý chí phát xít Đức.", 2),
    ("Ngày Chiến thắng phát xít tại châu Âu (VE Day) được kỷ niệm vào ngày nào hàng năm?", "Ngày 9/5 (và ngày 8/5 ở Tây Âu)", ["Ngày 30/4", "Ngày 1/9", "Ngày 2/9"], "Đức ký văn bản đầu hàng không điều kiện vào tháng 5/1945 kết thúc chiến tranh tại châu Âu.", 1),
    ("Người phụ nữ đầu tiên trên thế giới bay vào không gian vũ trụ năm 1963 là ai?", "Valentina Tereshkova", ["Svetlana Savitskaya", "Sally Ride", "Mae Jemison"], "Nữ phi hành gia Liên Xô Valentina Tereshkova bay một mình trên tàu Vostok 6.", 2),
    ("Nhà bác học nào đã phát minh ra thuốc nổ Dynamite và sau đó dùng tài sản thành lập các giải thưởng Nobel danh giá?", "Alfred Nobel", ["Albert Einstein", "Thomas Edison", "Alexander Nobel"], "Giải Nobel được trao giải lần đầu tiên vào năm 1901 theo di chúc của nhà hóa học Thụy Điển Alfred Nobel.", 1),
    ("Hệ thống chữ nổi dành cho người khiếm thị trên toàn thế giới do ai sáng tạo vào năm 1824?", "Louis Braille", ["Alexander Graham Bell", "Helen Keller", "Thomas Hopkins"], "Louis Braille người Pháp bị mù từ nhỏ đã phát minh hệ thống 6 chấm nổi kỳ diệu.", 1),
    ("Bác sĩ người Scotland nào đã phát hiện ra kháng sinh penicillin mở ra kỷ nguyên cứu sống hàng triệu người?", "Alexander Fleming", ["Louis Pasteur", "Edward Jenner", "Robert Koch"], "Năm 1928, Fleming vô tình phát hiện nấm Penicillium tiêu diệt vi khuẩn tụ cầu trong đĩa thí nghiệm.", 1),
    ("Nhà khoa học nào phát minh ra vaccine phòng bệnh đậu mùa mở đường cho ngành miễn dịch học?", "Edward Jenner", ["Louis Pasteur", "Robert Koch", "Albert Calmette"], "Jenner sử dụng dịch từ nốt đậu bò để tạo miễn dịch chống bệnh đậu mùa cho người năm 1796.", 2)
]

for item in EXPANDED_HISTORY:
    QUESTIONS.append({
        "difficulty": item[4],
        "question": item[0],
        "correct_answer": item[1],
        "distractors": item[2],
        "explanation": item[3]
    })

def main():
    print(f"Bắt đầu nạp {len(QUESTIONS)} câu hỏi Lịch sử...")
    added = add_questions_to_category("lich-su", QUESTIONS)
    print(f"Hoàn thành! Đã thêm {added} câu vào lich-su.json")

if __name__ == '__main__':
    main()
