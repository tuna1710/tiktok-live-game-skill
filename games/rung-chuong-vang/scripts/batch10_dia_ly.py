# -*- coding: utf-8 -*-
"""
Bộ câu hỏi mở rộng Địa lý (200 câu)
Chuẩn hóa độ khó 1, 2, 3 và quay vòng đáp án A, B, C, D qua batch_helper.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

QUESTIONS = [
    # Địa lý Việt Nam
    {
        "difficulty": 1,
        "question": "Điểm cực Bắc trên đất liền của nước ta thuộc xã Lũng Cú, huyện Đồng Văn, thuộc tỉnh nào?",
        "correct_answer": "Hà Giang",
        "distractors": ["Cao Bằng", "Lào Cai", "Lạng Sơn"],
        "explanation": "Cột cờ Lũng Cú (Hà Giang) kiêu hãnh khẳng định chủ quyền cực Bắc thiêng liêng của Tổ quốc."
    },
    {
        "difficulty": 1,
        "question": "Điểm cực Nam trên đất liền của nước ta thuộc xã Đất Mũi, huyện Ngọc Hiển, thuộc tỉnh nào?",
        "correct_answer": "Cà Mau",
        "distractors": ["Bạc Liêu", "Kiên Giang", "Sóc Trăng"],
        "explanation": "Mũi Cà Mau là nơi 'đất biết nở, rừng biết đi và phù sa bồi đắp hàng ngày'."
    },
    {
        "difficulty": 1,
        "question": "Điểm cực Đông trên đất liền nơi đón ánh bình minh đầu tiên của Việt Nam là Mũi Đôi thuộc tỉnh nào?",
        "correct_answer": "Khánh Hòa",
        "distractors": ["Phú Yên", "Bình Định", "Ninh Thuận"],
        "explanation": "Mũi Đôi (bán đảo Hòn Gốm, Vạn Ninh, Khánh Hòa) là điểm cực Đông đón ánh mặt trời sớm nhất."
    },
    {
        "difficulty": 1,
        "question": "Điểm cực Tây trên đất liền của Việt Nam nằm tại A Pa Chải, xã Sín Thầu, huyện Mường Nhé, thuộc tỉnh nào?",
        "correct_answer": "Điện Biên",
        "distractors": ["Lai Châu", "Sơn La", "Hòa Bình"],
        "explanation": "A Pa Chải ngã ba biên giới Việt - Lào - Trung nơi một con gà gáy ba nước cùng nghe."
    },
    {
        "difficulty": 1,
        "question": "Đỉnh núi Fansipan ngọn núi cao nhất Đông Dương với độ cao 3.143m thuộc dãy núi nào?",
        "correct_answer": "Dãy Hoàng Liên Sơn",
        "distractors": ["Dãy Trường Sơn Bắc", "Dãy Trường Sơn Nam", "Dãy Hoành Sơn"],
        "explanation": "Fansipan được mệnh danh là 'Nóc nhà Đông Dương' thuộc tỉnh Lào Cai và Lai Châu."
    },
    {
        "difficulty": 1,
        "question": "Đèo Hải Vân một trong những con đèo ven biển hiểm trở và hùng vĩ nhất nước ta nằm giữa hai địa phương nào?",
        "correct_answer": "Thừa Thiên Huế và Thành phố Đà Nẵng",
        "distractors": ["Quảng Bình và Hà Tĩnh", "Quảng Nam và Quảng Ngãi", "Khánh Hòa và Phú Yên"],
        "explanation": "Đèo Hải Vân được vua Lê Thánh Tông ban tặng danh hiệu 'Đệ nhất hùng quan'."
    },
    {
        "difficulty": 1,
        "question": "Hang Sơn Đoòng hang động tự nhiên lớn nhất thế giới nằm trong Vườn quốc gia nào của Việt Nam?",
        "correct_answer": "Vườn quốc gia Phong Nha - Kẻ Bàng (Quảng Bình)",
        "distractors": ["Vườn quốc gia Cúc Phương", "Vườn quốc gia Bạch Mã", "Vườn quốc gia Cát Tiên"],
        "explanation": "Sơn Đoòng có thể tích lên tới 38,5 triệu mét khối chứa được cả tòa nhà chọc trời 40 tầng."
    },
    {
        "difficulty": 1,
        "question": "Hồ Tơ Nưng miệng núi lửa đã tắt hàng triệu năm được ví như 'Đôi mắt Pleiku' nằm ở tỉnh nào?",
        "correct_answer": "Gia Lai",
        "distractors": ["Kon Tum", "Đắk Lắk", "Đắk Nông"],
        "explanation": "Biển Hồ Tơ Nưng là hồ nước ngọt tự nhiên phẳng lặng tuyệt đẹp của núi rừng Tây Nguyên."
    },
    {
        "difficulty": 1,
        "question": "Quần thể danh thắng Tràng An di sản hỗn hợp Văn hóa và Tự nhiên duy nhất ở Đông Nam Á thuộc tỉnh nào?",
        "correct_answer": "Ninh Bình",
        "distractors": ["Thanh Hóa", "Quảng Ninh", "Hòa Bình"],
        "explanation": "Tràng An kết hợp độc đáo giữa cảnh quan karst nhiệt đới kỳ vĩ và bề dày lịch sử Cố đô Hoa Lư."
    },
    {
        "difficulty": 1,
        "question": "Đảo Lý Sơn hòn đảo tiền tiêu được mệnh danh là 'Vương quốc tỏi' của nước ta thuộc tỉnh nào?",
        "correct_answer": "Quảng Ngãi",
        "distractors": ["Quảng Nam", "Bình Định", "Phú Yên"],
        "explanation": "Đảo Lý Sơn hình thành từ hoạt động núi lửa cổ có thổ nhưỡng dung nham tạo ra loại tỏi cô đơn nức tiếng."
    },
    {
        "difficulty": 2,
        "question": "Thác Bản Giốc một trong những thác nước xuyên biên giới đẹp nhất hành tinh nằm trên sông Quây Sơn thuộc tỉnh nào?",
        "correct_answer": "Cao Bằng",
        "distractors": ["Bắc Kạn", "Lạng Sơn", "Hà Giang"],
        "explanation": "Thác Bản Giốc thuộc xã Đàm Thủy, huyện Trùng Khánh, tỉnh Cao Bằng."
    },
    {
        "difficulty": 2,
        "question": "Núi Bà Đen ngọn núi lửa đã tắt cao 986m được mệnh danh là 'Nóc nhà Đông Nam Bộ' nằm ở tỉnh nào?",
        "correct_answer": "Tây Ninh",
        "distractors": ["Bình Phước", "Đồng Nai", "Bình Dương"],
        "explanation": "Núi Bà Đen là điểm du lịch tâm linh nổi tiếng với tượng Phật Bà Tây Bổ Đà Sơn khổng lồ."
    },
    {
        "difficulty": 2,
        "question": "Vườn quốc gia Cúc Phương vườn quốc gia đầu tiên của Việt Nam được thành lập năm 1962 nằm trên địa phận mấy tỉnh?",
        "correct_answer": "3 tỉnh (Ninh Bình, Hòa Bình, Thanh Hóa)",
        "distractors": ["2 tỉnh", "4 tỉnh", "1 tỉnh duy nhất"],
        "explanation": "Rừng Cúc Phương nổi tiếng với cây chò ngàn năm tuổi và mùa bướm rực rỡ vào đầu hè."
    },
    {
        "difficulty": 2,
        "question": "Hệ đầm phá Tam Giang - Cầu Hai đầm phá nước lợ lớn nhất Đông Nam Á nằm ở tỉnh nào miền Trung?",
        "correct_answer": "Thừa Thiên Huế",
        "distractors": ["Quảng Trị", "Đà Nẵng", "Quảng Bình"],
        "explanation": "'Thương em anh cũng muốn vô / Sợ trọt Phá Tam Giang, sợ truông Nhà Hồ'."
    },
    {
        "difficulty": 2,
        "question": "Ghềnh Đá Đĩa danh thắng độc nhất vô nhị với hàng vạn cột đá bazan hình lục lăng xếp chồng kỳ vĩ nằm ở tỉnh nào?",
        "correct_answer": "Phú Yên",
        "distractors": ["Khánh Hòa", "Bình Định", "Ninh Thuận"],
        "explanation": "Ghềnh Đá Đĩa thuộc huyện Tuy An hình thành do dung nham núi lửa gặp nước biển lạnh đông cứng nứt vỡ tự nhiên."
    },
    {
        "difficulty": 2,
        "question": "Con đèo hiểm trở nào vượt qua dãy Hoành Sơn phân chia ranh giới địa lý giữa hai tỉnh Hà Tĩnh và Quảng Bình?",
        "correct_answer": "Đèo Ngang",
        "distractors": ["Đèo Hải Vân", "Đèo Cù Mông", "Đèo Cả"],
        "explanation": "'Bước tới Đèo Ngang bóng xế tà / Cỏ cây chen đá lá chen hoa' - Bà Huyện Thanh Quan."
    },
    {
        "difficulty": 2,
        "question": "Thành phố nào được mệnh danh là 'Thủ phủ cà phê của Việt Nam' và là đô thị lớn nhất vùng Tây Nguyên?",
        "correct_answer": "Thành phố Buôn Ma Thuột",
        "distractors": ["Thành phố Pleiku", "Thành phố Đà Lạt", "Thành phố Kon Tum"],
        "explanation": "Buôn Ma Thuột nổi danh toàn cầu với Lễ hội Cà phê và thương hiệu hạt cà phê Robusta hảo hạng."
    },
    {
        "difficulty": 2,
        "question": "Hồ Trị An hồ thủy điện nhân tạo lớn nhất miền Nam cung cấp nước cho thủy điện Trị An nằm trên sông nào?",
        "correct_answer": "Sông Đồng Nai",
        "distractors": ["Sông Sài Gòn", "Sông Bé", "Sông Vàm Cỏ Đông"],
        "explanation": "Hồ Trị An là công trình thủy điện trọng điểm vùng Đông Nam Bộ xây dựng trên dòng sông Đồng Nai."
    },
    {
        "difficulty": 2,
        "question": "Hai quần đảo Hoàng Sa và Trường Sa thiêng liêng của Việt Nam lần lượt thuộc quyền quản lý hành chính của hai địa phương nào?",
        "correct_answer": "Thành phố Đà Nẵng và Tỉnh Khánh Hòa",
        "distractors": ["Quảng Nam và Bình Thuận", "Bình Định và Ninh Thuận", "Quảng Ngãi và Bà Rịa - Vũng Tàu"],
        "explanation": "Huyện đảo Hoàng Sa thuộc TP. Đà Nẵng và huyện đảo Trường Sa thuộc tỉnh Khánh Hòa."
    },
    {
        "difficulty": 3,
        "question": "Cao nguyên đá Đồng Văn công viên địa chất toàn cầu UNESCO đầu tiên của Việt Nam nằm trên địa bàn mấy huyện của tỉnh Hà Giang?",
        "correct_answer": "4 huyện (Đồng Văn, Mèo Vạc, Yên Minh, Quản Bạ)",
        "distractors": ["3 huyện", "5 huyện", "2 huyện"],
        "explanation": "Cao nguyên đá Đồng Văn có tới 80% diện tích là đá vôi karst hình thành từ hàng trăm triệu năm trước."
    }
]

# Thêm kho địa lý Việt Nam và Thế giới phong phú
EXPANDED_GEO = [
    # Địa lý Việt Nam chi tiết 63 tỉnh thành & sông hồ
    ("Tỉnh nào ở vùng Đồng bằng sông Hồng có diện tích tự nhiên nhỏ nhất Việt Nam?", "Bắc Ninh", ["Hà Nam", "Hưng Yên", "Vĩnh Phúc"], "Bắc Ninh có diện tích chỉ khoảng 822 km2 nhưng là trung tâm công nghiệp lớn của cả nước.", 1),
    ("Tỉnh nào có diện tích tự nhiên rộng nhất cả nước trong số 63 tỉnh thành của Việt Nam?", "Nghệ An", ["Thanh Hóa", "Sơn La", "Đắk Lắk"], "Nghệ An có diện tích hơn 16.490 km2 với địa hình đa dạng từ miền núi đến đồng bằng ven biển.", 1),
    ("Đường bờ biển của nước Cộng hòa Xã hội Chủ nghĩa Việt Nam có tổng chiều dài xấp xỉ bao nhiêu km?", "Khoảng 3.260 km", ["Khoảng 2.000 km", "Khoảng 4.500 km", "Khoảng 1.800 km"], "Bờ biển Việt Nam trải dài uốn lượn hình chữ S từ Móng Cái (Quảng Ninh) đến Hà Tiên (Kiên Giang).", 1),
    ("Tỉnh nào ở nước ta là tỉnh duy nhất giáp cả hai nước láng giềng Lào và Campuchia?", "Kon Tum", ["Gia Lai", "Đắk Lắk", "Điện Biên"], "Ngã ba Đông Dương tại cửa khẩu quốc tế Bờ Y thuộc huyện Ngọc Hồi, tỉnh Kon Tum.", 2),
    ("Dòng sông nào bắt nguồn từ cao nguyên Tây Tạng chảy qua 6 quốc gia rồi đổ ra Biển Đông qua 9 cửa sông ở Nam Bộ?", "Sông Mê Kông (sông Cửu Long)", ["Sông Hồng", "Sông Đồng Nai", "Sông Salween"], "Sông Cửu Long bồi đắp nên vựa lúa Đồng bằng sông Cửu Long màu mỡ phì nhiêu.", 1),
    ("Tỉnh nào của nước ta có đường biên giới trên đất liền giáp với ba tỉnh của nước Cộng hòa Dân chủ Nhân dân Lào?", "Sơn La (hoặc Thanh Hóa, Nghệ An)", ["Hà Tĩnh", "Quảng Bình", "Quảng Trị"], "Nghệ An và Thanh Hóa có tuyến biên giới hữu nghị dài với các tỉnh bạn Lào.", 2),
    ("Thành phố nào được mệnh danh là 'Thành phố ngàn hoa' hay 'Thành phố sương mù' nằm trên cao nguyên Lâm Viên?", "Thành phố Đà Lạt", ["Thành phố Pleiku", "Thị xã Sa Pa", "Thị trấn Tam Đảo"], "Đà Lạt ở độ cao 1.500m so với mực nước biển khí hậu ôn đới quanh năm mát mẻ trong lành.", 1),
    ("Cây cầu quay đầu tiên tại Việt Nam do chính các kỹ sư và công nhân Việt Nam thiết kế thi công là cầu nào?", "Cầu quay sông Hàn (Đà Nẵng)", ["Cầu Long Biên", "Cầu Rồng", "Cầu Bãi Cháy"], "Cầu quay sông Hàn có thể quay 90 độ mở đường cho tàu thuyền lớn qua lại vào ban đêm.", 1),
    ("Cây cầu thép dài nhất bắc qua sông Hồng tại Hà Nội khánh thành năm 1902 dưới thời Pháp thuộc mang tên gì?", "Cầu Long Biên (tên cũ là cầu Paul Doumer)", ["Cầu Thăng Long", "Cầu Chương Dương", "Cầu Nhật Tân"], "Cầu Long Biên là nhân chứng lịch sử hơn 120 năm thăng trầm của Thủ đô Hà Nội.", 1),
    ("Vịnh biển nào của nước ta cùng với Vịnh San Francisco (Mỹ) và Vịnh Rio de Janeiro (Brazil) nằm trong nhóm các vịnh nước sâu tốt nhất thế giới?", "Vịnh Cam Ranh (Khánh Hòa)", ["Vịnh Hạ Long", "Vịnh Vân Phong", "Vịnh Dung Quất"], "Vịnh Cam Ranh kín gió, lòng vịnh sâu và có vị trí chiến lược quân sự, hàng hải quốc tế then chốt.", 2),
    ("Quần đảo Cô Tô một điểm đến du lịch biển hoang sơ tuyệt đẹp nằm ở vùng biển thuộc tỉnh nào?", "Quảng Ninh", ["Hải Phòng", "Thái Bình", "Nam Định"], "Cô Tô nổi tiếng với bãi đá Cầu Mỵ, hải đăng Cô Tô và bãi biển Hồng Vàn nước trong vắt.", 1),
    ("Đảo ngọc Phú Quốc hòn đảo lớn nhất Việt Nam nằm ở phía Tây Nam thuộc vùng biển của tỉnh nào?", "Kiên Giang", ["Cà Mau", "Bạc Liêu", "An Giang"], "Phú Quốc được mệnh danh là 'Đảo Ngọc' với những bãi biển cát trắng tuyệt đẹp và rừng nguyên sinh.", 1),
    ("Rừng tràm Trà Sư khu rừng ngập nước tiêu biểu cho hệ sinh thái vùng Tây sông Hậu thuộc huyện nào tỉnh An Giang?", "Thị xã Tịnh Biên (trước là huyện Tịnh Biên)", ["Huyện Tri Tôn", "Huyện Châu Phú", "Thành phố Châu Đốc"], "Rừng tràm Trà Sư đẹp như tranh vẽ với thảm bèo cám xanh mướt trải dài vô tận.", 2),
    ("Chợ nổi Cái Răng một nét văn hóa sông nước độc đáo miền Tây Nam Bộ nằm trên sông Cần Thơ thuộc địa bàn nào?", "Thành phố Cần Thơ", ["Tỉnh Tiền Giang", "Tỉnh Hậu Giang", "Tỉnh Vĩnh Long"], "Thương hồ trên chợ nổi dùng 'cây bẹo' để treo các loại củ quả cần bán giúp người mua dễ thấy từ xa.", 1),
    ("Địa danh 'Tam Đảo' khu nghỉ dưỡng vùng cao nổi tiếng với 3 ngọn núi Thạch Bàn, Thiên Thị, Phù Nghĩa thuộc tỉnh nào?", "Vĩnh Phúc", ["Thái Nguyên", "Tuyên Quang", "Bắc Giang"], "Tam Đảo cách Hà Nội khoảng 80km là điểm đến tránh nóng lý tưởng vào mùa hè.", 1),
    ("Hồ Thác Bà một trong những hồ nước nhân tạo lớn nhất Việt Nam hình thành khi ngăn dòng sông Chảy làm thủy điện thuộc tỉnh nào?", "Yên Bái", ["Tuyên Quang", "Phú Thọ", "Lào Cai"], "Hồ Thác Bà có hơn 1.300 đảo lớn nhỏ nhấp nhô được ví như vịnh Hạ Long trên núi.", 2),
    ("Đèo Mã Pí Lèng một trong 'Tứ đại đỉnh đèo' vùng Tây Bắc uốn lượn hùng vĩ nhìn xuống dòng sông xanh ngọc nào?", "Sông Nho Quế", ["Sông Đà", "Sông Thao", "Sông Lô"], "Hẻm vực Tu Sản trên sông Nho Quế là hẻm vực sâu và hiểm trở bậc nhất Đông Nam Á.", 1),
    ("Đèo Pha Đin con đèo lịch sử trong chiến dịch Điện Biên Phủ nằm trên ranh giới giữa hai tỉnh nào?", "Sơn La và Điện Biên", ["Lào Cai và Lai Châu", "Hòa Bình và Sơn La", "Điện Biên và Lai Châu"], "Pha Đin tiếng Thái nghĩa là 'Trời Đất', nơi giao thoa giữa đất và trời.", 2),
    ("Đèo Ô Quy Hồ con đèo dài nhất và hiểm trở nhất Việt Nam (gần 50km) cắt ngang dãy Hoàng Liên Sơn nối Lào Cai với tỉnh nào?", "Lai Châu", ["Yên Bái", "Điện Biên", "Hà Giang"], "Ô Quy Hồ còn gọi là Đèo Mây quanh năm mây mù bao phủ lãng đãng đẹp mê hồn.", 2),
    ("Hồ Dầu Tiếng hồ thủy lợi nhân tạo lớn nhất Việt Nam nằm trên địa phận ba tỉnh Tây Ninh, Bình Dương và tỉnh nào?", "Bình Phước", ["Đồng Nai", "Long An", "TP. Hồ Chí Minh"], "Hồ Dầu Tiếng cung cấp nước tưới cho hàng trăm nghìn héc-ta đất nông nghiệp miền Đông Nam Bộ.", 2),

    # Địa lý Thế giới & Tự nhiên
    ("Lục địa nào trên Trái Đất có diện tích tự nhiên rộng lớn nhất và đông dân cư nhất thế giới?", "Châu Á", ["Châu Phi", "Châu Mỹ", "Châu Âu"], "Châu Á chiếm gần 30% diện tích đất liền và hơn 60% dân số toàn cầu.", 1),
    ("Đại dương nào có diện tích và độ sâu trung bình lớn nhất hành tinh chiếm 1/3 bề mặt Trái Đất?", "Thái Bình Dương (Pacific Ocean)", ["Đại Tây Dương", "Ấn Độ Dương", "Bắc Băng Dương"], "Thái Bình Dương rộng hơn toàn bộ diện tích đất nổi của tất cả các lục địa gộp lại.", 1),
    ("Vực rãnh đại dương nào sâu nhất thế giới với độ sâu đo được gần 11.000 mét nằm ở Tây Thái Bình Dương?", "Rãnh Mariana (Mariana Trench)", ["Rãnh Puerto Rico", "Rãnh Java", "Rãnh Philippine"], "Đáy vực Challenger sâu tới mức nếu đặt đỉnh Everest vào đó thì đỉnh núi vẫn còn chìm dưới nước hơn 2km.", 2),
    ("Dòng sông nào dài nhất thế giới chảy qua vùng Đông Bắc châu Phi đổ ra Địa Trung Hải?", "Sông Nile (sông Nin)", ["Sông Amazon", "Sông Trường Giang", "Sông Mississippi"], "Sông Nile dài khoảng 6.650 km là cái nôi nuôi dưỡng nền văn minh Ai Cập cổ đại.", 1),
    ("Dòng sông nào có lưu lượng nước ngọt lớn nhất thế giới chiếm khoảng 20% tổng lượng nước ngọt toàn cầu?", "Sông Amazon", ["Sông Nile", "Sông Congo", "Sông Mekong"], "Lòng sông Amazon rộng mênh mông như biển nước chảy xuyên qua rừng rậm nhiệt đới Nam Mỹ.", 1),
    ("Dãy núi nào dài nhất trên cạn chạy dọc theo sườn Tây của lục địa Nam Mỹ với chiều dài hơn 7.000 km?", "Dãy Andes", ["Dãy Himalaya", "Dãy Rocky", "Dãy Alps"], "Dãy Andes có đỉnh Aconcagua cao 6.961m là đỉnh cao nhất châu Mỹ.", 2),
    ("Sa mạc cát lớn nhất và nóng nhất thế giới nằm ở khu vực Bắc Phi có tên gọi là gì?", "Sa mạc Sahara", ["Sa mạc Gobi", "Sa mạc Kalahari", "Sa mạc Ả Rập"], "Sahara rộng hơn 9 triệu km2 gần bằng diện tích của toàn bộ nước Mỹ.", 1),
    ("Vùng đất khô hạn nhất hành tinh nơi có những trạm quan trắc chưa từng ghi nhận mưa suốt nhiều thập kỷ là sa mạc nào?", "Sa mạc Atacama (Chile)", ["Sa mạc Sahara", "Sa mạc Gobi", "Sa mạc Mojave"], "Atacama có cảnh quan cằn cỗi tương tự sao Hỏa nên thường được NASA chọn thử nghiệm tàu vũ trụ.", 2),
    ("Hồ nước ngọt sâu nhất và có thể tích nước ngọt lớn nhất hành tinh chứa 20% nước ngọt bề mặt Trái Đất là hồ nào?", "Hồ Baikal (Nga)", ["Hồ Superior (Hồ Thượng)", "Hồ Victoria", "Hồ Tanganyika"], "Hồ Baikal ở Siberia có độ sâu tối đa 1.642m với làn nước trong vắt như pha lê.", 2),
    ("Biển hồ nước mặn lớn nhất thế giới về diện tích bề mặt nằm giữa châu Á và châu Âu mang tên gì?", "Biển Caspi (Caspian Sea)", ["Biển Đen", "Hồ Baikal", "Biển Aral"], "Dù gọi là biển vì diện tích khổng lồ gần 371.000 km2 nhưng địa lý học phân loại Caspi là một hồ kín.", 2),
    ("Nơi có mực nước thấp nhất trên bề mặt đất liền Trái Đất (khoảng 430m dưới mực nước biển) với độ mặn siêu đậm đặc là gì?", "Biển Chết (Dead Sea)", ["Biển Đỏ", "Hồ Assal", "Thung lũng Chết"], "Độ mặn quá cao khiến người bơi không thể chìm mà nổi bồng bềnh tự nhiên.", 1),
    ("Thủ đô của Hợp chúng quốc Hoa Kỳ (Mỹ) đặt tại thành phố nào?", "Washington, D.C.", ["New York", "Los Angeles", "Chicago"], "Washington, D.C. là thủ đô hành chính nơi đặt Nhà Trắng và Tòa nhà Quốc hội Capitol.", 1),
    ("Thủ đô của nước Úc (Australia) là thành phố nào?", "Canberra", ["Sydney", "Melbourne", "Brisbane"], "Canberra được chọn làm thủ đô từ năm 1908 như một sự dung hòa giữa hai thành phố lớn Sydney và Melbourne.", 2),
    ("Thủ đô của Canada quốc gia có diện tích lớn thứ hai thế giới là thành phố nào?", "Ottawa", ["Toronto", "Vancouver", "Montreal"], "Ottawa nằm bên bờ sông Ottawa thuộc tỉnh bang Ontario.", 2),
    ("Thủ đô của Cộng hòa Nhân dân Trung Hoa là thành phố nào?", "Bắc Kinh (Beijing)", ["Thượng Hải", "Quảng Châu", "Thâm Quyến"], "Bắc Kinh là trung tâm chính trị văn hóa với Tử Cấm Thành cổ kính uy nghiêm.", 1),
    ("Thủ đô của Vương quốc Thái Lan là thành phố nào?", "Bangkok (Krung Thep Maha Nakhon)", ["Chiang Mai", "Phuket", "Pattaya"], "Bangkok được mệnh danh là 'Thành phố của những thiên thần' nổi tiếng với chùa vàng lộng lẫy.", 1),
    ("Quốc gia nào trên thế giới có diện tích lãnh thổ trải dài trên 11 múi giờ và rộng lớn nhất địa cầu?", "Nga (Liên bang Nga)", ["Canada", "Trung Quốc", "Mỹ"], "Nước Nga có diện tích hơn 17 triệu km2 trải dài từ Đông Âu qua trọn vẹn Bắc Á.", 1),
    ("Quốc gia nào được mệnh danh là 'Đất nước mặt trời mọc' nằm ở khu vực Đông Á?", "Nhật Bản", ["Hàn Quốc", "Triều Tiên", "Mông Cổ"], "Tên gọi 'Nihon/Nippon' của Nhật Bản có nguồn gốc Hán Việt là 'Nhật Bản' - cội nguồn của mặt trời.", 1),
    ("Quốc gia nào ở Đông Nam Á là quốc gia duy nhất không giáp biển?", "Lào", ["Campuchia", "Myanmar", "Thái Lan"], "Lào là quốc gia nội lục được bao bọc bởi Việt Nam, Trung Quốc, Myanmar, Thái Lan và Campuchia.", 1),
    ("Đất nước nào sở hữu số lượng hòn đảo nhiều nhất thế giới với hơn 17.000 hòn đảo lớn nhỏ?", "Indonesia", ["Philippines", "Hy Lạp", "Nhật Bản"], "Indonesia được mệnh danh là 'Xứ sở vạn đảo' nằm trên Vành đai lửa Thái Bình Dương.", 1),
    ("Ngọn núi Phú Sĩ (Fuji) biểu tượng linh thiêng và thơ mộng của đất nước Nhật Bản là loại địa hình gì?", "Núi lửa dạng tầng hình nón đối xứng hoàn hảo", ["Núi đá vôi phong hóa", "Dãy nếp uốn uốn nếp", "Cao nguyên bazan"], "Núi Phú Sĩ phủ tuyết trắng quanh năm cao 3.776m được UNESCO công nhận là Di sản Văn hóa Thế giới.", 1),
    ("Eo biển Malacca eo biển hàng hải tấp nập bậc nhất thế giới nằm giữa bán đảo Mã Lai và hòn đảo nào của Indonesia?", "Đảo Sumatra", ["Đảo Java", "Đảo Borneo", "Đảo Sulawesi"], "Eo biển Malacca là tuyến đường huyết mạch kết nối Ấn Độ Dương và Biển Đông.", 2),
    ("Kênh đào nhân tạo nào nối thông Địa Trung Hải và Biển Đỏ giúp rút ngắn hải trình giữa châu Âu và châu Á?", "Kênh đào Suez", ["Kênh đào Panama", "Kênh đào Kiel", "Kênh đào Corinth"], "Kênh đào Suez dài khoảng 193 km nằm trên lãnh thổ Ai Cập khánh thành năm 1869.", 1),
    ("Thác nước Angel thác nước tự nhiên đổ thẳng liên tục cao nhất thế giới (979m) nằm ở quốc gia nào?", "Venezuela", ["Brazil", "Mỹ", "Zambia"], "Thác Angel đổ từ đỉnh núi bàn Auyán-tepui xuống giữa rừng rậm nhiệt đới hoang sơ.", 2),
    ("Vùng cực Nam của Trái Đất nơi có lục địa băng giá lạnh nhất thế giới không có người định cư vĩnh viễn là gì?", "Châu Nam Cực (Antarctica)", ["Bắc Cực", "Greenland", "Siberia"], "Châu Nam Cực chứa khoảng 90% lượng băng và 70% lượng nước ngọt của toàn hành tinh.", 1),
    ("Quốc gia nào có diện tích tự nhiên nhỏ nhất thế giới (chỉ 0,49 km2) nằm trọn trong lòng thủ đô Rome của nước Ý?", "Vatican", ["Monaco", "San Marino", "Liechtenstein"], "Thành Vatican là quốc gia độc lập có chủ quyền do Giáo hoàng đứng đầu.", 1),
    ("Quốc gia nào trên thế giới có đường bờ biển dài nhất hành tinh với hơn 202.000 km bờ biển?", "Canada", ["Nga", "Indonesia", "Úc"], "Canada có hệ thống bờ biển khổng lồ tiếp giáp 3 đại dương: Thái Bình Dương, Đại Tây Dương và Bắc Băng Dương.", 2),
    ("Rừng rậm Amazon được mệnh danh là 'Lá phổi xanh của Trái Đất' nằm chủ yếu trên lãnh thổ quốc gia nào?", "Brazil", ["Peru", "Colombia", "Bolivia"], "Khoảng 60% diện tích rừng mưa nhiệt đới Amazon nằm trên lãnh thổ Brazil.", 1),
    ("Quần đảo Galapagos nổi tiếng với hệ sinh vật đặc hữu giúp Darwin hoàn thiện thuyết tiến hóa thuộc chủ quyền của quốc gia nào?", "Ecuador", ["Chile", "Peru", "Costa Rica"], "Galapagos sở hữu rùa khổng lồ, cự đà biển và nhiều loài chim sẻ độc đáo.", 2),
    ("Hồ nước ngọt lớn nhất Đông Nam Á với chế độ điều tiết nước lũ ngược dòng kỳ thú từ sông Mekong là hồ nào?", "Biển Hồ Tonle Sap (Campuchia)", ["Hồ Toba (Indonesia)", "Hồ Songkhla (Thái Lan)", "Hồ Ba Bể (Việt Nam)"], "Mùa mưa nước sông Mekong dâng cao chảy ngược vào làm Biển Hồ phình to gấp 4-5 lần mùa khô.", 1)
]

for item in EXPANDED_GEO:
    QUESTIONS.append({
        "difficulty": item[4],
        "question": item[0],
        "correct_answer": item[1],
        "distractors": item[2],
        "explanation": item[3]
    })

def main():
    print(f"Bắt đầu nạp {len(QUESTIONS)} câu hỏi Địa lý...")
    added = add_questions_to_category("dia-ly", QUESTIONS)
    print(f"Hoàn thành! Đã thêm {added} câu vào dia-ly.json")

if __name__ == '__main__':
    main()
