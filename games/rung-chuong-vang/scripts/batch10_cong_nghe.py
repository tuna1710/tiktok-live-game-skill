# -*- coding: utf-8 -*-
"""
Bộ câu hỏi mở rộng Đời sống - Công nghệ (100+ câu)
Ẩm thực đặc sản, Thể thao đỉnh cao, Công nghệ thông tin & Đời sống số.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

QUESTIONS = [
    # Ẩm thực đặc sản
    {
        "difficulty": 1,
        "question": "Món ăn đường phố Việt Nam nổi tiếng toàn cầu kẹp nhân pate, thịt xá xíu, chả lụa, dưa leo và rau mùi là món gì?",
        "correct_answer": "Bánh mì Việt Nam",
        "distractors": ["Bánh bao", "Bánh giò", "Bánh xèo"],
        "explanation": "Từ 'Banh mi' đã được thêm chính thức vào từ điển tiếng Anh Oxford như một danh từ riêng chỉ món bánh mì đặc sắc của Việt Nam."
    },
    {
        "difficulty": 1,
        "question": "Món ăn truyền thống Hà Nội gồm bún tươi, chả nướng than hoa chấm nước mắm chua ngọt ăn kèm đu đủ giòn là món gì?",
        "correct_answer": "Bún chả",
        "distractors": ["Bún thang", "Bún đậu", "Bún ốc"],
        "explanation": "Năm 2016 Tổng thống Mỹ Barack Obama từng cùng đầu bếp Anthony Bourdain thưởng thức bún chả tại phố Lê Văn Hưu, Hà Nội."
    },
    {
        "difficulty": 1,
        "question": "Đặc sản 'Chả cá Lã Vọng' trứ danh của mảnh đất kinh kỳ Hà Nội được chế biến chủ yếu từ loài cá nước ngọt nào?",
        "correct_answer": "Cá lăng (hoặc cá anh vũ)",
        "distractors": ["Cá trắm đen", "Cá chép giòn", "Cá mè"],
        "explanation": "Cá lăng thịt ngọt, ít xương dăm, xào cùng hành hoa và thì là thơm phức ăn kèm bánh đa nướng và mắm tôm."
    },
    {
        "difficulty": 1,
        "question": "Món đặc sản mùa thu Hà Nội thơm mùi lúa non được gói cẩn thận trong hai lớp lá sen tươi và buộc bằng rơm nếp là gì?",
        "correct_answer": "Cốm Làng Vòng",
        "distractors": ["Bánh cốm", "Xôi xéo", "Bánh phu thê"],
        "explanation": "Cốm Vòng dẻo thơm, ngọt dịu là thức quà tinh tế gắn liền với mùa thu lãng mạn đất Tràng An."
    },
    {
        "difficulty": 1,
        "question": "Tỉnh Hưng Yên nổi tiếng khắp cả nước với loại trái cây đặc sản tiến vua trứ danh nào?",
        "correct_answer": "Nhãn lồng Hưng Yên",
        "distractors": ["Vải thiều", "Bưởi da xanh", "Thanh long ruột đỏ"],
        "explanation": "Nhãn lồng Hưng Yên cùi dày, ráo nước, giòn ngọt và thơm ngát hương vị đất phù sa châu thổ sông Hồng."
    },
    {
        "difficulty": 2,
        "question": "Món 'Cao lầu' đặc sản nức tiếng của phố cổ Hội An (Quảng Nam) có sợi mì màu vàng đục được làm từ nước ngâm tro của loại cây nào?",
        "correct_answer": "Tro củi lấy từ Cù Lao Chàm",
        "distractors": ["Tro củi tre gai", "Tro cây tràm", "Tro vỏ dừa xiêm"],
        "explanation": "Nước ngâm tro củi Cù Lao Chàm kết hợp với nước giếng Bá Lễ tạo nên độ giòn dai đặc trưng không nơi nào có được."
    },
    {
        "difficulty": 2,
        "question": "Món canh chua đặc sản mùa nước nổi của người dân miền Tây Nam Bộ thường kết hợp cá linh với loài hoa dại màu vàng nào?",
        "correct_answer": "Bông điên điển",
        "distractors": ["Bông so đũa", "Bông súng", "Bông thiên lý"],
        "explanation": "Canh chua cá linh non nấu bông điên điển mang trọn hương vị phù sa mùa nước nổi miền Tây."
    },
    {
        "difficulty": 2,
        "question": "Tỉnh Tiền Giang nổi tiếng khắp cả nước với giống xoài ngọt thơm, vỏ mỏng hạt dẹp mang tên gọi là gì?",
        "correct_answer": "Xoài cát Hòa Lộc",
        "distractors": ["Xoài cát Chu", "Xoài Tượng", "Xoài Úc"],
        "explanation": "Xoài cát Hòa Lộc xuất xứ từ xã Hòa Hưng (huyện Cái Bè, Tiền Giang) là một trong những giống xoài ngon nhất thế giới."
    },
    {
        "difficulty": 2,
        "question": "Món phô mai tươi Mozzarella truyền thống làm từ sữa trâu nước là thành phần cốt lõi của món bánh nướng nổi tiếng nào của nước Ý?",
        "correct_answer": "Pizza",
        "distractors": ["Lasagna", "Tiramisu", "Risotto"],
        "explanation": "Pizza Margherita mang ba màu sắc quốc kỳ Ý: đỏ (cà chua), trắng (phô mai Mozzarella) và xanh (lá húng quế Basil)."
    },

    # Thể thao đỉnh cao
    {
        "difficulty": 1,
        "question": "Vận động viên đầu tiên trong lịch sử thể thao Việt Nam đoạt Huy chương Vàng tại một kỳ Thế vận hội Olympic là ai?",
        "correct_answer": "Xạ thủ Hoàng Xuân Vinh (Olympic Rio 2016)",
        "distractors": ["Võ sĩ Trần Hiếu Ngân", "Lực sĩ Hoàng Anh Tuấn", "Ánh Viên"],
        "explanation": "Hoàng Xuân Vinh xuất sắc giành HCV môn 10m súng ngắn hơi nam tại Olympic Rio 2016 thiết lập kỷ lục Olympic mới."
    },
    {
        "difficulty": 1,
        "question": "Biểu tượng của Thế vận hội Olympic quốc tế bao gồm bao nhiêu vòng tròn đan lồng vào nhau?",
        "correct_answer": "5 vòng tròn đại diện cho 5 châu lục",
        "distractors": ["4 vòng tròn", "6 vòng tròn", "7 vòng tròn"],
        "explanation": "Năm vòng tròn màu xanh lam, vàng, đen, xanh lá và đỏ tượng trưng cho tình đoàn kết thể thao của 5 châu lục."
    },
    {
        "difficulty": 1,
        "question": "Đội tuyển bóng đá nam quốc gia nào đang giữ kỷ lục vô địch World Cup nhiều lần nhất trong lịch sử (5 lần)?",
        "correct_answer": "Đội tuyển Brazil",
        "distractors": ["Đội tuyển Đức", "Đội tuyển Ý", "Đội tuyển Argentina"],
        "explanation": "Xứ sở Samba Brazil vô địch World Cup vào các năm 1958, 1962, 1970, 1994 và 2002."
    },
    {
        "difficulty": 1,
        "question": "Cầu thủ bóng đá nào đang nắm giữ kỷ lục giành nhiều danh hiệu Quả bóng vàng (Ballon d'Or) nhất lịch sử với 8 lần đoạt giải?",
        "correct_answer": "Lionel Messi",
        "distractors": ["Cristiano Ronaldo", "Pele", "Diego Maradona"],
        "explanation": "Messi đoạt Quả bóng vàng thứ 8 vào năm 2023 sau khi cùng Argentina vô địch World Cup 2022."
    },
    {
        "difficulty": 2,
        "question": "Bốn giải đấu quần vợt (tennis) danh giá bậc nhất thế giới hợp thành hệ thống gì?",
        "correct_answer": "Grand Slam (Úc mở rộng, Roland Garros, Wimbledon, Mỹ mở rộng)",
        "distractors": ["ATP 1000", "Davis Cup", "Olympic Tennis", "Masters Cup"],
        "explanation": "Grand Slam là đỉnh cao danh giá nhất trong sự nghiệp của mọi tay vợt chuyên nghiệp."
    },
    {
        "difficulty": 2,
        "question": "Kỳ thủ cờ vua số 1 Việt Nam từng vô địch cờ chớp thế giới năm 2013 và lọt Top kỳ thủ hàng đầu thế giới là ai?",
        "correct_answer": "Đại kiện tướng Lê Quang Liêm",
        "distractors": ["Nguyễn Ngọc Trường Sơn", "Đào Thiên Hải", "Trần Tuấn Minh"],
        "explanation": "Lê Quang Liêm là niềm tự hào lớn của trí tuệ thể thao cờ vua Việt Nam trên đấu trường quốc tế."
    },

    # Công nghệ thông tin & Đời sống số
    {
        "difficulty": 1,
        "question": "Tên viết tắt của dịch vụ mạng toàn cầu 'WWW' được nhà khoa học Tim Berners-Lee phát minh năm 1989 là gì?",
        "correct_answer": "World Wide Web",
        "distractors": ["World Wide Word", "Wide Web World", "World Web Wireless"],
        "explanation": "World Wide Web mở ra thời kỳ bùng nổ thông tin kết nối các trang siêu văn bản trên toàn thế giới qua Internet."
    },
    {
        "difficulty": 1,
        "question": "Hệ điều hành dành cho điện thoại thông minh mã nguồn mở dựa trên nhân Linux do Google phát triển có tên là gì?",
        "correct_answer": "Android",
        "distractors": ["iOS", "Windows Phone", "Symbian"],
        "explanation": "Android là hệ điều hành di động phổ biến nhất hành tinh chiếm hơn 70% thị phần thiết bị di động."
    },
    {
        "difficulty": 1,
        "question": "Bộ phận nào trong máy tính được coi là 'Bộ não trung tâm' thực hiện mọi phép tính toán và điều khiển của máy tính?",
        "correct_answer": "CPU (Central Processing Unit)",
        "distractors": ["RAM", "Ổ cứng HDD", "Card đồ họa GPU"],
        "explanation": "CPU là bộ vi xử lý thực thi các lệnh của chương trình máy tính."
    },
    {
        "difficulty": 1,
        "question": "Bộ nhớ tạm thời trong máy tính bị mất sạch dữ liệu khi ngắt nguồn điện được gọi là gì?",
        "correct_answer": "RAM (Random Access Memory)",
        "distractors": ["ROM", "Ổ SSD", "Thẻ nhớ Flash"],
        "explanation": "RAM lưu trữ dữ liệu tạm thời để CPU truy xuất cực nhanh trong lúc ứng dụng đang chạy."
    },
    {
        "difficulty": 2,
        "question": "Công nghệ kết nối không dây tầm ngắn phổ biến kết nối tai nghe, loa và điện thoại mang tên 'Bluetooth' được đặt theo tên của ai?",
        "correct_answer": "Vị vua Viking Harald Bluetooth của Đan Mạch",
        "distractors": ["Nhà phát minh Alexander Graham Bell", "Kỹ sư Bluetooth người Thụy Điển", "Thần thoại Hy Lạp"],
        "explanation": "Vua Harald Bluetooth có công hợp nhất các bộ tộc Đan Mạch cũng như công nghệ này giúp hợp nhất các thiết bị giao tiếp với nhau."
    },
    {
        "difficulty": 2,
        "question": "Giao thức truyền tải siêu văn bản an toàn có mã hóa chứng chỉ bảo mật SSL/TLS hiển thị ổ khóa xanh trên trình duyệt web là gì?",
        "correct_answer": "HTTPS (Hypertext Transfer Protocol Secure)",
        "distractors": ["HTTP", "FTP", "SMTP"],
        "explanation": "HTTPS mã hóa lưu lượng dữ liệu giữa máy khách và máy chủ giúp bảo vệ mật khẩu và thông tin tài khoản."
    },
    {
        "difficulty": 2,
        "question": "Đơn vị thông tin cơ bản nhất trong khoa học máy tính chỉ có hai trạng thái 0 hoặc 1 được gọi là gì?",
        "correct_answer": "Bit (Binary digit)",
        "distractors": ["Byte", "Pixel", "Hertz"],
        "explanation": "1 Byte bằng 8 bit. Hệ nhị phân 0 và 1 là nền tảng hoạt động của toàn bộ mạch điện tử kỹ thuật số."
    },
    {
        "difficulty": 3,
        "question": "Địa chỉ mạng giao thức Internet thế hệ mới IPv6 sử dụng độ dài bao nhiêu bit để giải quyết tình trạng cạn kiệt địa chỉ IPv4?",
        "correct_answer": "128 bit",
        "distractors": ["32 bit", "64 bit", "256 bit"],
        "explanation": "IPv4 chỉ có 32 bit (khoảng 4,3 tỷ địa chỉ), trong khi IPv6 có 128 bit cung cấp hàng tỷ tỷ địa chỉ cho vạn vật kết nối Internet (IoT)."
    }
]

# Mở rộng thêm 50 câu Đời sống - Công nghệ
MORE_TECH = [
    ("Món kẹo đặc sản nổi tiếng của xứ Huế làm từ mè rang (vừng), đậu phộng và mạch nha có tên gọi là gì?", "Mè xửng Huế", ["Kẹo cu đơ", "Kẹo dừa", "Kẹo sìu dâu"], "Kẹo mè xửng dẻo quánh thơm lừng ăn kèm nhâm nhi chén trà sen Huế.", 1),
    ("Bánh pía món bánh ngàn lớp nhân sầu riêng trứng muối thơm ngọt nức tiếng là đặc sản của tỉnh nào?", "Sóc Trăng", ["Bến Tre", "Trà Vinh", "Vĩnh Long"], "Bánh pía Vũng Thơm mang đậm nét giao thoa văn hóa ẩm thực người Hoa và người Khmer.", 1),
    ("Huyện đảo Phú Quốc (Kiên Giang) và huyện đảo Cát Hải (Hải Phòng) nức tiếng với loại gia vị truyền thống nào của Việt Nam?", "Nước mắm truyền thống ủ chượp cá cơm", ["Tương bần", "Rượu nếp cái hoa vàng", "Dấm gạo"], "Nước mắm Phú Quốc độ đạm tự nhiên cao được bảo hộ chỉ dẫn địa lý tại Liên minh châu Âu (EU).", 1),
    ("Món 'Cu đơ' kẹp bánh tráng nướng nhân mật mía gừng cay giòn rụm là đặc sản của tỉnh nào miền Trung?", "Hà Tĩnh", ["Nghệ An", "Quảng Bình", "Quảng Trị"], "Kẹo cu đơ Hà Tĩnh ngọt đậm vị mật mía, cay nồng vị gừng già ăn cùng chè xanh nóng hổi.", 1),
    ("Làng gốm Bát Tràng làng nghề gốm sứ truyền thống có lịch sử hơn 700 năm thuộc huyện nào của Hà Nội?", "Huyện Gia Lâm", ["Huyện Đông Anh", "Huyện Thanh Trì", "Huyện Mê Linh"], "Gốm Bát Tràng tinh xảo với các dòng men lam, men rạn danh tiếng xuất khẩu khắp thế giới.", 1),
    ("Làng hoa Sa Đéc vựa hoa kiểng lớn nhất vùng Tây Nam Bộ thuộc địa bàn tỉnh nào?", "Đồng Tháp", ["An Giang", "Tiền Giang", "Bến Tre"], "Làng hoa Tân Quy Đông (Sa Đéc) rực rỡ sắc màu mỗi độ Tết đến xuân về.", 1),
    ("Vị giác của con người có thể cảm nhận được 5 vị cơ bản: ngọt, chua, mặn, đắng và vị thứ năm thơm ngon đậm đà mang tên là gì?", "Vị Umami (vị ngọt thịt / mì chính)", ["Vị cay", "Vị chát", "Vị nồng"], "Vị Umami do giáo sư Nhật Bản Kikunae Ikeda phát hiện năm 1908 kích thích thụ thể glutamate.", 2),
    ("Nguyên liệu nào là thành phần chính tạo nên vị cay xé lưỡi trong các quả ớt tươi?", "Capsaicin", ["Piperine", "Curcumin", "Menthol"], "Capsaicin kích thích thụ thể nhiệt cảm giác đau rát khiến não bộ giải phóng endorphin tạo cảm giác hưng phấn.", 2),
    ("Cây gia vị nào có tinh dầu Menthol mang lại cảm giác mát lạnh sảng khoái trong kem đánh răng và kẹo cao su?", "Cây bạc hà (Mint)", ["Cây quế", "Cây hồi", "Cây đinh hương"], "Menthol kích hoạt thụ thể cảm nhận lạnh TRPM8 trên các đầu dây thần kinh da và niêm mạc miệng.", 1),
    ("Thủ môn huyền thoại nào của đội tuyển bóng đá Liên Xô là thủ môn duy nhất trong lịch sử từng giành Quả bóng vàng (1963)?", "Lev Yashin (Biệt danh 'Nhện đen')", ["Dino Zoff", "Gianluigi Buffon", "Iker Casillas"], "Lev Yashin nổi tiếng với phản xạ phi thường trong trang phục màu đen huyền thoại.", 2),
    ("Môn thể thao nào được mệnh danh là 'Môn thể thao của các vị vua' (Sport of Kings) xuất phát từ quý tộc Anh?", "Quần vợt hoặc Đua ngựa", ["Bóng đá", "Bóng rổ", "Bơi lội"], "Môn quần vợt và đua ngựa quý tộc được coi là những môn thể thao hoàng gia sang trọng.", 2),
    ("Kích thước tiêu chuẩn của một bàn cờ vua quốc tế bao gồm bao nhiêu ô vuông đen trắng xen kẽ?", "64 ô vuông (8x8 ô)", ["100 ô vuông", "32 ô vuông", "81 ô vuông"], "Bàn cờ vua gồm 8 hàng ngang và 8 cột dọc với 32 quân trắng và 32 quân đen lúc ban đầu.", 1),
    ("Môn thể thao nào mà các đấu thủ dùng vợt lưới đánh quả cầu lông bay qua tấm lưới căng ngang giữa sân?", "Cầu lông (Badminton)", ["Quần vợt", "Bóng bàn", "Bóng chuyền"], "Tốc độ quả cầu lông sau cú đập smash có thể vượt qua 400 km/h, nhanh nhất trong mọi môn thể thao dùng vợt.", 1),
    ("Ai là người đồng sáng lập tập đoàn công nghệ Microsoft cùng với Paul Allen vào năm 1975?", "Bill Gates", ["Steve Jobs", "Mark Zuckerberg", "Larry Page"], "Bill Gates từng nhiều năm giữ vị trí người giàu nhất hành tinh nhờ sự thống trị của hệ điều hành Windows.", 1),
    ("Hãng công nghệ nào gắn liền với logo quả táo cắn dở và các dòng sản phẩm iPhone, iPad, MacBook?", "Apple Inc.", ["Samsung", "Sony", "Google"], "Apple được sáng lập bởi Steve Jobs, Steve Wozniak và Ronald Wayne năm 1976.", 1),
    ("Trí tuệ nhân tạo (AI) viết tắt từ cụm từ tiếng Anh nào?", "Artificial Intelligence", ["Automatic Internet", "Applied Information", "Advanced Interface"], "AI mô phỏng khả năng tư duy, học tập và giải quyết vấn đề của con người trên máy tính.", 1),
    ("Công nghệ blockchain chuỗi khối bảo mật phân tán là nền tảng công nghệ cho sự ra đời của đồng tiền kỹ thuật số nào đầu tiên (năm 2009)?", "Bitcoin (BTC)", ["Ethereum", "Ripple", "Litecoin"], "Bitcoin do nhân vật ẩn danh mang tên Satoshi Nakamoto sáng lập.", 2),
    ("Hệ số đo mật độ điểm ảnh trên màn hình điện thoại hoặc máy tính thể hiện độ sắc nét được viết tắt là gì?", "PPI (Pixels Per Inch)", ["FPS", "DPI", "Hz"], "Chỉ số PPI càng cao thì hình ảnh hiển thị càng mịn màng không thấy các hạt điểm ảnh răng cưa.", 2),
    ("Tần số quét màn hình điện thoại 120Hz có nghĩa là gì?", "Màn hình làm mới hình ảnh 120 lần trong một giây", ["Độ sáng 120 nit", "Tốc độ mạng 120 Mbps", "Độ phân giải 120 megapixel"], "Tần số quét 120Hz giúp các thao tác vuốt cuộn và chơi game mượt mà vượt trội.", 1),
    ("Cáp quang truyền dữ liệu Internet xuyên đại dương bằng loại tín hiệu nào với tốc độ gần bằng ánh sáng?", "Tín hiệu ánh sáng (quang học)", ["Sóng vô tuyến", "Xung điện từ", "Sóng siêu âm"], "Sợi cáp quang bằng thủy tinh tinh khiết truyền chùm tia laser dựa trên nguyên lý phản xạ toàn phần.", 2)
]

for item in MORE_TECH:
    QUESTIONS.append({
        "difficulty": item[4],
        "question": item[0],
        "correct_answer": item[1],
        "distractors": item[2],
        "explanation": item[3]
    })

def main():
    print(f"Bắt đầu nạp {len(QUESTIONS)} câu hỏi Đời sống - Công nghệ...")
    added = add_questions_to_category("doi-song-cong-nghe", QUESTIONS)
    print(f"Hoàn thành! Đã thêm {added} câu vào doi-song-cong-nghe.json")

if __name__ == '__main__':
    main()
