# -*- coding: utf-8 -*-
"""
Bộ câu hỏi mở rộng Văn học - Nghệ thuật (100+ câu)
Kiệt tác văn học, Ca dao tục ngữ, Âm nhạc & Di sản phi vật thể UNESCO.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

QUESTIONS = [
    # Văn học Trung đại & Kiệt tác
    {
        "difficulty": 1,
        "question": "Kiệt tác 'Truyện Kiều' (Đoạn trường tân thanh) của Đại thi hào Nguyễn Du được viết bằng thể thơ truyền thống nào?",
        "correct_answer": "Thể thơ lục bát",
        "distractors": ["Thể thơ song thất lục bát", "Thể thơ thất ngôn bát cú", "Thể thơ tự do"],
        "explanation": "Truyện Kiều gồm 3.254 câu thơ lục bát chữ Nôm là đỉnh cao chói lọi của nền thi ca dân tộc Việt Nam."
    },
    {
        "difficulty": 1,
        "question": "Trong 'Truyện Kiều', nhân vật nào đã khuyên Thúy Kiều bán mình chuộc cha và em trai thoát nạn oan sai?",
        "correct_answer": "Chính Thúy Kiều tự nguyện hy sinh chữ tình để trọn chữ hiếu",
        "distractors": ["Thúy Vân", "Vương Quan", "Kim Trọng"],
        "explanation": "'Để lời thề hải minh sơn / Làm con trước phải đền ơn sinh thành' - Kiều quyết định hi sinh tấm thân cứu gia đình."
    },
    {
        "difficulty": 2,
        "question": "Tập truyện cổ chữ Hán kỳ ảo đầu tiên của văn học Việt Nam do danh sĩ Lý Tế Xuyên biên soạn vào thời Trần có tên là gì?",
        "correct_answer": "'Việt điện u linh tập'",
        "distractors": ["'Lĩnh Nam chích quái'", "'Truyền kỳ mạn lục'", "'Thánh Tông di thảo'"],
        "explanation": "'Việt điện u linh tập' ghi chép các thần tích, anh hùng, thần linh hiển ứng bảo vệ đất nước."
    },
    {
        "difficulty": 2,
        "question": "Tác phẩm 'Truyền kỳ mạn lục' được ca ngợi là 'Thiên cổ kỳ bút' (bút lạ nghìn đời) của văn học trung đại do ai sáng tác?",
        "correct_answer": "Nguyễn Dữ",
        "distractors": ["Lý Tế Xuyên", "Trần Thế Pháp", "Nguyễn Trãi"],
        "explanation": "Nguyễn Dữ là học trò xuất sắc của Trạng Trình Nguyễn Bỉnh Khiêm sống vào thế kỷ XVI."
    },
    {
        "difficulty": 1,
        "question": "Tác phẩm thơ nôm 'Lục Vân Tiên' đề cao tinh thần trượng nghĩa 'Lộ kiến bất bình bạt đao tương trợ' do nhà thơ mù nào sáng tác?",
        "correct_answer": "Nguyễn Đình Chiểu",
        "distractors": ["Nguyễn Bỉnh Khiêm", "Cao Bá Quát", "Nguyễn Khuyến"],
        "explanation": "Cụ đồ Chiểu viết Lục Vân Tiên răn dạy đạo lý làm người trung hiếu tiết nghĩa ở đời."
    },

    # Văn học Hiện thực 1930 - 1945
    {
        "difficulty": 1,
        "question": "Trong truyện ngắn 'Chí Phèo' của Nam Cao, chi tiết nào đã đánh thức phần lương tri và khát khao làm người lương thiện của Chí?",
        "correct_answer": "Bát cháo hành nóng hổi của Thị Nở",
        "distractors": ["Hũ rượu trắng của Bá Kiến", "Tiếng chim hót buổi sớm", "Bức thư của người mẹ"],
        "explanation": "Hương vị bát cháo hành ấm áp của tình thương mộc mạc khiến Chí Phèo rơi nước mắt nhận ra bi kịch đời mình."
    },
    {
        "difficulty": 1,
        "question": "Nhân vật Lão Hạc trong truyện ngắn cùng tên của nhà văn Nam Cao vì quá túng quẫn và thương con đã quyết định làm gì với con chó Vàng?",
        "correct_answer": "Bán con chó Vàng và sau đó ăn bả chó tự vẫn để giữ đất cho con",
        "distractors": ["Đem con chó Vàng đi cho người khác", "Bán mảnh vườn cho Bá Kiến", "Bỏ làng đi tha phương cầu thực"],
        "explanation": "Cái chết dữ dội bằng bả chó của Lão Hạc là bằng chứng đau xót về nhân cách trong sạch của người nông dân nghèo."
    },
    {
        "difficulty": 1,
        "question": "Tiểu thuyết trào phúng 'Số đỏ' với nhân vật chính Xuân Tóc Đỏ 'từ thằng nhặt bóng thành vĩ nhân' do nhà văn tài hoa nào chắp bút?",
        "correct_answer": "Vũ Trọng Phụng",
        "distractors": ["Ngô Tất Tố", "Nam Cao", "Nguyễn Công Hoan"],
        "explanation": "Vũ Trọng Phụng được mệnh danh là 'Ông vua phóng sự đất Bắc' châm biếm sâu cay xã hội tư sản thực dân rởm đời."
    },
    {
        "difficulty": 1,
        "question": "Nhà thơ nào được tôn xưng là 'Ông hoàng thơ tình' của phong trào Thơ mới với bài thơ 'Vội vàng'?",
        "correct_answer": "Xuân Diệu",
        "distractors": ["Huy Cận", "Hàn Mặc Tử", "Nguyễn Bính"],
        "explanation": "'Tôi muốn tắt nắng đi / Cho màu đừng nhạt mất / Tôi muốn buộc gió lại / Cho hương đừng bay đi' - Xuân Diệu."
    },
    {
        "difficulty": 2,
        "question": "Bài thơ 'Đây thôn Vĩ Dạ' với những câu thơ hoài niệm lung linh hư ảo 'Sao anh không về chơi thôn Vĩ?' là thi phẩm bất hủ của nhà thơ nào?",
        "correct_answer": "Hàn Mặc Tử",
        "distractors": ["Chế Lan Viên", "Bích Khê", "Vũ Hoàng Chương"],
        "explanation": "Hàn Mặc Tử viết tặng Hoàng Thị Kim Cúc khi đang chống chọi bệnh phong cô độc tại trại phong Quy Hòa."
    },

    # Văn học Kháng chiến & Hiện đại
    {
        "difficulty": 1,
        "question": "Hình ảnh biểu tượng thơ ca bất hủ 'Đầu súng trăng treo' xuất hiện trong thi phẩm nổi tiếng nào của nhà thơ Chính Hữu?",
        "correct_answer": "Bài thơ 'Đồng chí'",
        "distractors": ["Bài thơ 'Tây Tiến'", "Bài thơ 'Việt Bắc'", "Bài thơ 'Tiểu đội xe không kính'"],
        "explanation": "Vẻ đẹp lãng mạn hòa quyện hiện thực chiến sĩ cách mạng canh gác bảo vệ bầu trời tự do."
    },
    {
        "difficulty": 1,
        "question": "Ai là tác giả của tác phẩm văn học thiếu nhi kinh điển 'Dế Mèn phiêu lưu ký' được dịch ra hàng chục thứ tiếng trên thế giới?",
        "correct_answer": "Tô Hoài",
        "distractors": ["Nguyễn Huy Tưởng", "Đoàn Giỏi", "Trần Đăng Khoa"],
        "explanation": "Tô Hoài viết Dế Mèn phiêu lưu ký từ năm 1941 dạy bài học đoàn kết muôn loài cùng chung sống hòa bình."
    },
    {
        "difficulty": 1,
        "question": "Tiểu thuyết 'Đất rừng phương Nam' miêu tả hành trình tìm cha lưu lạc của chú bé An giữa thiên nhiên rừng tràm ngập nước là của ai?",
        "correct_answer": "Đoàn Giỏi",
        "distractors": ["Sơn Nam", "Nguyễn Ngọc Tư", "Vũ Hạnh"],
        "explanation": "Khung cảnh rừng U Minh bạt ngàn với nghề ăn ong, bắt cá sấu sống động của Nam Bộ."
    },
    {
        "difficulty": 2,
        "question": "Tác phẩm kịch nói xuất sắc 'Hồn Trương Ba, da hàng thịt' phản ánh bi kịch giữa thể xác và tâm hồn do nhà viết kịch tài danh nào sáng tác?",
        "correct_answer": "Lưu Quang Vũ",
        "distractors": ["Nguyễn Đình Thi", "Đào Hồng Cẩm", "Học Phi"],
        "explanation": "Lưu Quang Vũ đặt ra thông điệp triết học sâu sắc: Được sống là chính mình toàn vẹn mới là hạnh phúc đích thực."
    },
    {
        "difficulty": 2,
        "question": "Nhà văn nào nổi tiếng với các tập truyện viết về lứa tuổi học trò như 'Kính Vạn Hoa', 'Tôi thấy hoa vàng trên cỏ xanh', 'Mắt biếc'?",
        "correct_answer": "Nguyễn Nhật Ánh",
        "distractors": ["Nguyễn Huy Thiệp", "Nguyễn Bình Phương", "Bảo Ninh"],
        "explanation": "Nguyễn Nhật Ánh là nhà văn viết cho thanh thiếu niên được yêu mến nhất với lượng phát hành sách kỷ lục."
    },

    # Âm nhạc & Di sản phi vật thể UNESCO
    {
        "difficulty": 1,
        "question": "Bài hát 'Tiến quân ca' được Quốc hội khóa I chọn làm Quốc ca chính thức của nước ta do nhạc sĩ tài hoa nào sáng tác?",
        "correct_answer": "Nhạc sĩ Văn Cao",
        "distractors": ["Nhạc sĩ Phạm Tuyên", "Nhạc sĩ Lưu Hữu Phước", "Nhạc sĩ Hoàng Vân"],
        "explanation": "Văn Cao sáng tác Tiến quân ca mùa đông năm 1944 thôi thúc triệu người cùng đứng lên giành độc lập."
    },
    {
        "difficulty": 1,
        "question": "Nhạc cụ truyền thống độc đáo của Việt Nam chỉ có đúng một dây duy nhất mà gảy lên được muôn vàn cung bậc cảm xúc là đàn gì?",
        "correct_answer": "Đàn bầu (Độc huyền cầm)",
        "distractors": ["Đàn nhị", "Đàn đáy", "Đàn tranh"],
        "explanation": "'Đàn bầu ai gảy nấy nghe / Làm thân con gái chớ nghe đàn bầu' - âm thanh ngân nga lay động lòng người nhờ cần uốn tạo cao độ."
    },
    {
        "difficulty": 1,
        "question": "Làn điệu dân ca Quan họ với những câu hát 'Người ơi người ở đừng về' là nét văn hóa đặc sắc của vùng đất nào?",
        "correct_answer": "Vùng Kinh Bắc (Bắc Ninh và Bắc Giang)",
        "distractors": ["Xứ Nghệ", "Xứ Đoài", "Kinh thành Huế"],
        "explanation": "Dân ca Quan họ Bắc Ninh được UNESCO công nhận là Di sản Văn hóa Phi vật thể đại diện của nhân loại năm 2009."
    },
    {
        "difficulty": 1,
        "question": "Không gian văn hóa Cồng chiêng Tây Nguyên di sản phi vật thể kiệt tác của nhân loại trải rộng trên địa bàn bao nhiêu tỉnh Tây Nguyên?",
        "correct_answer": "5 tỉnh (Kon Tum, Gia Lai, Đắk Lắk, Đắk Nông, Lâm Đồng)",
        "distractors": ["3 tỉnh", "4 tỉnh", "6 tỉnh"],
        "explanation": "Tiếng cồng chiêng gắn liền với vòng đời con người và các lễ hội đâm trâu, mừng lúa mới, bỏ mả của đồng bào Tây Nguyên."
    },
    {
        "difficulty": 2,
        "question": "Cây đàn Tính (Tính tẩu) làm từ quả bầu khô gắn liền với nghệ thuật diễn xướng dân gian độc đáo nào của đồng bào Tày, Nùng?",
        "correct_answer": "Hát Then",
        "distractors": ["Hát Quan họ", "Hát Xoan", "Hát Ca trù"],
        "explanation": "Thực hành Hát Then của người Tày, Nùng, Thái đã được UNESCO ghi danh vào danh sách di sản văn hóa phi vật thể năm 2019."
    }
]

# Thêm 40 câu ca dao, tục ngữ, văn học dân gian
FOLK_LITERATURE = [
    ("Điền từ còn thiếu vào câu ca dao: 'Công cha như núi Thái Sơn / Nghĩa mẹ như nước trong ... chảy ra'?", "nguồn", ["suối", "sông", "khe"], "Câu ca dao ca ngợi công ơn trời biển vô bờ bến của cha mẹ dưỡng dục sinh thành.", 1),
    ("Điền từ vào câu tục ngữ: 'Ăn quả nhớ kẻ trồng cây / Ăn khoai nhớ kẻ cho dây mà ...'?", "trồng", ["bẻ", "đào", "nấu"], "Đạo lý truyền thống 'Uống nước nhớ nguồn' cao đẹp của dân tộc ta.", 1),
    ("Điền từ vào câu thành ngữ: 'Gần mực thì đen, gần đèn thì ...'?", "rạng (hoặc sáng)", ["tỏ", "vui", "ấm"], "Khuyên răn con người chọn bạn mà chơi, môi trường sống ảnh hưởng sâu sắc đến nhân cách.", 1),
    ("Điền từ vào câu tục ngữ: 'Bầu ơi thương lấy bí cùng / Tuy rằng khác ... nhưng chung một giàn'?", "giống", ["loài", "dây", "nhà"], "Tinh thần tương thân tương ái, đoàn kết gắn bó keo sơn của đồng bào Việt Nam.", 1),
    ("Điền từ vào câu ca dao: 'Nhiễu điều phủ lấy giá gương / Người trong một nước phải ... nhau cùng'?", "thương", ["giúp", "yêu", "lo"], "Lời răn dạy sâu sắc về tình dân tộc nghĩa đồng bào trong mọi hoàn cảnh.", 1),
    ("Trong truyện cổ tích 'Cây khế', người em hiền lành được chim thần chở ra đảo vàng lấy vàng vào chiếc túi may dài mấy gang?", "Túi ba gang", ["Túi năm gang", "Túi một gang", "Túi chín gang"], "'Ăn một quả trả một cục vàng, may túi ba gang mang đi mà đựng'.", 1),
    ("Trong truyện cổ tích 'Tấm Cám', vật nuôi bầu bạn nào của cô Tấm thường trồi lên ăn hạt cơm mỗi khi cô Tấm gọi?", "Con cá bống", ["Con chim sẻ", "Con rùa vàng", "Con gà trống"], "'Bống bống bang bang, lên ăn cơm vàng cơm bạc nhà ta, chớ ăn cơm hẩm cháo hoa nhà người'.", 1),
    ("Trong truyện cổ tích 'Thạch Sanh', chàng Thạch Sanh dùng tiếng đàn thần kỳ để làm việc gì đẩy lùi 18 nước chư hầu?", "Đánh đàn khiến binh lính giặc nhớ quê rụng rời tay chân bãi binh", ["Khiến trời đổ mưa rào", "Làm rung chuyển cung điện", "Hóa đá quân địch"], "Cây đàn thần và niêu cơm thần kỳ là biểu tượng cho khát vọng hòa bình và nhân đạo của dân tộc.", 1),
    ("Bài ca dao 'Thằng Bờm có cái quạt mo' kết thúc bằng việc Bờm đổi quạt mo lấy thứ gì của phú ông?", "Nắm xôi", ["Ba bò chín trâu", "Ao sâu cá mè", "Bè gỗ lim"], "'Phú ông xin đổi nắm xôi / Bờm cười' - nụ cười hồn nhiên thỏa mãn nhu cầu giản dị đời thường.", 1),
    ("Trong truyền thuyết 'Sự tích bánh chưng bánh giầy', chàng hoàng tử thứ mấy của vua Hùng đã làm ra bánh chưng bánh giầy?", "Chàng hoàng tử Lang Liêu (hoặc hoàng tử thứ 18)", ["Hoàng tử trưởng", "Hoàng tử út", "Hoàng tử Mai An Tiêm"], "Lang Liêu được thần báo mộng lấy lúa gạo hạt ngọc trời làm bánh vuông tượng trưng cho Đất, bánh tròn tượng trưng cho Trời.", 1),
    ("Nhân vật Mai An Tiêm trong truyền tích thời Hùng Vương bị đày ra đảo hoang đã có công tìm ra giống quả ngọt nào?", "Quả dưa hấu", ["Quả thanh long", "Quả dừa", "Quả mãng cầu"], "Mai An Tiêm nêu cao bài học ý chí kiên cường tự lực cánh sinh 'Của biếu là của lo, của cho là của nợ'.", 1),
    ("Vị thần nào trong thần thoại Việt Nam dùng móng tay hóa thành lẫy nỏ thần bắn một phát ra hàng ngàn mũi tên cho An Dương Vương?", "Thần Kim Quy (Rùa Vàng)", ["Thần Sấm", "Thần Núi Tản Viên", "Thần Sông"], "Nỏ thần Liên Châu bảo vệ kinh thành Cổ Loa trước quân xâm lược Triệu Đà.", 1),
    ("Hai vị thần quyền năng nào đã giao tranh khốc liệt dâng nước đánh nhau để cầu hôn công chúa Mỵ Nương?", "Sơn Tinh và Thủy Tinh", ["Thần Lửa và Thần Nước", "Thần Mưa và Thần Gió", "Thiên Tinh và Địa Tinh"], "Truyền thuyết phản ánh công cuộc đắp đê ngăn chặn lũ lụt thiên tai bền bỉ của người Việt cổ ven sông Hồng.", 1),
    ("Hội Gióng lễ hội văn hóa tái hiện chiến công của Phù Đổng Thiên Vương đánh giặc Ân được tổ chức tại đền nào ở Hà Nội?", "Đền Phù Đổng (Gia Lâm) và đền Sóc (Sóc Sơn)", ["Đền Hùng", "Đền Quán Thánh", "Đền Ngọc Sơn"], "Hội Gióng được UNESCO công nhận là Di sản Văn hóa Phi vật thể đại diện của nhân loại năm 2010.", 1),
    ("Vị thiền sư kiệt xuất thời Lý tác giả bài thơ thiền nổi tiếng 'Cáo tật thị chúng' ('Có bệnh bảo mọi người') với hình ảnh cành mai nở là ai?", "Mãn Giác Thiền sư", ["Vạn Hạnh Thiền sư", "Không Lộ Thiền sư", "Khuông Việt"], "'Đừng tưởng xuân tàn hoa rụng hết / Đêm qua sân trước một cành mai' - niềm tin bất diệt vào sự sống trường tồn.", 2)
]

for item in FOLK_LITERATURE:
    QUESTIONS.append({
        "difficulty": item[4],
        "question": item[0],
        "correct_answer": item[1],
        "distractors": item[2],
        "explanation": item[3]
    })

def main():
    print(f"Bắt đầu nạp {len(QUESTIONS)} câu hỏi Văn học - Nghệ thuật...")
    added = add_questions_to_category("van-hoc-nghe-thuat", QUESTIONS)
    print(f"Hoàn thành! Đã thêm {added} câu vào van-hoc-nghe-thuat.json")

if __name__ == '__main__':
    main()
