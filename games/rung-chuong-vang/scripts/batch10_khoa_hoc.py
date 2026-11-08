# -*- coding: utf-8 -*-
"""
Bộ câu hỏi mở rộng Khoa học Tự nhiên (120+ câu)
Vật lý, Hóa học, Sinh học, Thiên văn học, Cơ thể người.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

QUESTIONS = [
    # Vật lý học
    {
        "difficulty": 1,
        "question": "Vận tốc truyền của ánh sáng trong môi trường chân không xấp xỉ bằng bao nhiêu?",
        "correct_answer": "Khoảng 300.000 km/giây",
        "distractors": ["Khoảng 340 m/giây", "Khoảng 150.000 km/giây", "Khoảng 1.000 km/giờ"],
        "explanation": "Vận tốc ánh sáng trong chân không là c = 299.792.458 m/s, giới hạn tốc độ tối đa của vũ trụ."
    },
    {
        "difficulty": 1,
        "question": "Âm thanh truyền đi nhanh nhất trong môi trường vật chất nào sau đây?",
        "correct_answer": "Môi trường chất rắn",
        "distractors": ["Môi trường chất lỏng", "Môi trường chất khí", "Môi trường chân không"],
        "explanation": "Trong chất rắn mật độ phân tử liên kết rất sít sao nên dao động âm thanh lan truyền nhanh nhất."
    },
    {
        "difficulty": 1,
        "question": "Âm thanh hoàn toàn không thể truyền qua được môi trường nào?",
        "correct_answer": "Môi trường chân không",
        "distractors": ["Nước biển", "Thanh sắt", "Không khí ẩm"],
        "explanation": "Sóng âm là sóng cơ học cần môi trường vật chất đàn hồi để truyền dao động, do đó không truyền trong chân không."
    },
    {
        "difficulty": 1,
        "question": "Bầu trời ban ngày có màu xanh da trời chủ yếu là do hiện tượng quang học nào của khí quyển?",
        "correct_answer": "Tán xạ Rayleigh",
        "distractors": ["Khúc xạ ánh sáng", "Phản xạ toàn phần", "Nhiễu xạ ánh sáng"],
        "explanation": "Các phân tử khí trong khí quyển tán xạ ánh sáng bước sóng ngắn (xanh lam, tím) mạnh hơn nhiều so với ánh sáng đỏ."
    },
    {
        "difficulty": 1,
        "question": "Cầu vồng rực rỡ xuất hiện sau cơn mưa hình thành do các hạt nước mưa đã làm gì với ánh sáng mặt trời?",
        "correct_answer": "Khúc xạ, phản xạ và tán sắc ánh sáng",
        "distractors": ["Hấp thụ toàn bộ ánh sáng", "Tán xạ Compton", "Phát quang sinh học"],
        "explanation": "Hạt nước mưa đóng vai trò như một lăng kính khúc xạ và tách chùm sáng trắng thành dải 7 sắc rực rỡ."
    },
    {
        "difficulty": 2,
        "question": "Nhiệt độ thấp nhất trên lý thuyết mà mọi chuyển động nhiệt của phân tử đều ngừng lại (0 Kelvin) tương đương bao nhiêu độ C?",
        "correct_answer": "-273,15 độ C",
        "distractors": ["-100 độ C", "-200 độ C", "-300 độ C"],
        "explanation": "Nhiệt độ không tuyệt đối (0 K = -273,15 °C) là mốc nhiệt độ giới hạn thấp nhất trong vũ trụ."
    },
    {
        "difficulty": 2,
        "question": "Lực đẩy Ác-si-mét (Archimedes) tác dụng lên một vật nhúng chìm trong chất lỏng có độ lớn bằng gì?",
        "correct_answer": "Trọng lượng của khối chất lỏng bị vật đó chiếm chỗ",
        "distractors": ["Khối lượng của bản thân vật đó", "Trọng lượng riêng của vật", "Áp suất đáy bình"],
        "explanation": "Định luật Ác-si-mét: F_A = d . V, giải thích vì sao những con tàu sắt khổng lồ có thể nổi trên mặt nước."
    },
    {
        "difficulty": 2,
        "question": "Người bị tật cận thị khi nhìn xa muốn nhìn rõ mắt phải đeo loại thấu kính nào?",
        "correct_answer": "Thấu kính phân kỳ",
        "distractors": ["Thấu kính hội tụ", "Gương cầu lồi", "Gương phẳng"],
        "explanation": "Mắt cận hội tụ ảnh trước võng mạc, thấu kính phân kỳ giúp kéo điểm tụ ảnh lùi về đúng màng lưới võng mạc."
    },
    {
        "difficulty": 2,
        "question": "Dụng cụ gia đình nào hoạt động dựa trên tác dụng nhiệt của dòng điện để bảo vệ an toàn mạch điện khi bị quá tải?",
        "correct_answer": "Cầu chì (hoặc Aptomat)",
        "distractors": ["Công tắc", "Ổ cắm", "Đồng hồ đo điện"],
        "explanation": "Khi dòng điện vượt quá giới hạn an toàn, dây chì sẽ nóng chảy ngắt mạch ngăn ngừa cháy nổ chập điện."
    },
    {
        "difficulty": 3,
        "question": "Đơn vị đo 'Năm ánh sáng' (Light-year) trong thiên văn học thực chất dùng để đo đại lượng nào?",
        "correct_answer": "Khoảng cách trong vũ trụ",
        "distractors": ["Thời gian trôi qua", "Vận tốc ánh sáng", "Khối lượng của ngôi sao"],
        "explanation": "1 năm ánh sáng là quãng đường ánh sáng đi được trong chân không suốt một năm (khoảng 9.460 tỷ km)."
    },

    # Hóa học
    {
        "difficulty": 1,
        "question": "Chất khí nào chiếm tỷ lệ lớn nhất trong thành phần khí quyển bao quanh Trái Đất (khoảng 78%)?",
        "correct_answer": "Khí Nitơ (N2)",
        "distractors": ["Khí Oxy (O2)", "Khí Cacbonic (CO2)", "Khí Argon (Ar)"],
        "explanation": "Không khí gồm ~78% Nitơ, ~21% Oxy, gần 1% Argon và một lượng nhỏ hơi nước, CO2."
    },
    {
        "difficulty": 1,
        "question": "Kim loại duy nhất ở thể lỏng trong điều kiện nhiệt độ phòng bình thường là kim loại nào?",
        "correct_answer": "Thủy ngân (Hg)",
        "distractors": ["Chì (Pb)", "Thiếc (Sn)", "Nhôm (Al)"],
        "explanation": "Thủy ngân có nhiệt độ nóng chảy rất thấp (-38,83 °C) nên tồn tại ở dạng lỏng ở nhiệt độ thường."
    },
    {
        "difficulty": 1,
        "question": "Kim loại nào có khả năng dẫn điện và dẫn nhiệt tốt nhất trong tất cả các kim loại?",
        "correct_answer": "Bạc (Ag)",
        "distractors": ["Đồng (Cu)", "Vàng (Au)", "Nhôm (Al)"],
        "explanation": "Thứ tự dẫn điện giảm dần: Bạc > Đồng > Vàng > Nhôm > Sắt."
    },
    {
        "difficulty": 1,
        "question": "Thành phần hóa học chính của muối ăn tinh khiết sử dụng nấu nướng hàng ngày là gì?",
        "correct_answer": "Natri clorua (NaCl)",
        "distractors": ["Natri bicacbonat", "Canxi cacbonat", "Kali clorua"],
        "explanation": "Muối biển kết tinh chủ yếu chứa Natri clorua cần thiết cho cân bằng điện giải cơ thể."
    },
    {
        "difficulty": 2,
        "question": "Khoáng vật tự nhiên nào có độ cứng cao nhất theo thang độ cứng Mohs (đạt mức 10/10)?",
        "correct_answer": "Kim cương",
        "distractors": ["Thạch anh", "Topaz", "Corundum (Ruby/Sapphire)"],
        "explanation": "Kim cương là dạng thù hình của cacbon với mạng tinh thể tứ diện cực kỳ bền vững."
    },
    {
        "difficulty": 2,
        "question": "Axit nào có mặt tự nhiên trong dịch vị dạ dày giúp phân hủy thức ăn và tiêu diệt vi khuẩn có hại?",
        "correct_answer": "Axit clohidric (HCl)",
        "distractors": ["Axit sunfuric (H2SO4)", "Axit axetic (CH3COOH)", "Axit nitric (HNO3)"],
        "explanation": "Dịch vị dạ dày có độ pH khoảng 1,5 đến 3,5 nhờ sự hiện diện của axit HCl nồng độ loãng."
    },
    {
        "difficulty": 2,
        "question": "Giấm ăn nấu nướng quen thuộc trong gian bếp gia đình thực chất là dung dịch loãng của axit nào?",
        "correct_answer": "Axit axetic (CH3COOH khoảng 2% - 5%)",
        "distractors": ["Axit fomic (HCOOH)", "Axit xitric", "Axit oxalic"],
        "explanation": "Giấm ăn lên men tự nhiên từ rượu hoặc tinh bột tạo ra axit axetic dịu nhẹ."
    },
    {
        "difficulty": 2,
        "question": "Khí nào còn được gọi là 'Băng khô' (Dry ice) khi được nén lạnh đóng băng ở thể rắn ở -78,5 độ C?",
        "correct_answer": "Khí Cacbonic (CO2 rắn)",
        "distractors": ["Khí Oxy lỏng", "Khí Nitơ đông đặc", "Khí Metan"],
        "explanation": "Đá khô thăng hoa trực tiếp từ thể rắn sang thể khí tạo làn khói trắng làm lạnh thực phẩm hoặc tạo hiệu ứng sân khấu."
    },
    {
        "difficulty": 3,
        "question": "Khí hiếm nào nhẹ thứ hai trong vũ trụ và được ứng dụng bơm bóng bay hoặc khí cầu an toàn không bắt cháy?",
        "correct_answer": "Khí Heli (He)",
        "distractors": ["Khí Hydro (H2)", "Khí Neon (Ne)", "Khí Argon (Ar)"],
        "explanation": "Heli là khí trơ không bắt lửa, rất an toàn để bơm bóng bay thay thế khí Hydro dễ gây nổ."
    },
    {
        "difficulty": 3,
        "question": "Hợp chất Canxi cacbonat (CaCO3) là thành phần cấu tạo chính của loại đá tự nhiên nào?",
        "correct_answer": "Đá vôi (và vỏ sò, vỏ ốc, đá hoa cương cẩm thạch)",
        "distractors": ["Đá bazan", "Đá granit", "Cát thạch anh"],
        "explanation": "CaCO3 nung ở nhiệt độ cao sinh ra vôi sống CaO dùng trong xây dựng và công nghiệp."
    },

    # Sinh học & Cơ thể người
    {
        "difficulty": 1,
        "question": "Cơ quan nội tạng nào trong cơ thể con người đảm nhiệm vai trò lọc máu và đào thải chất cặn bã qua nước tiểu?",
        "correct_answer": "Quả thận (hai quả thận)",
        "distractors": ["Lá lách", "Dạ dày", "Túi mật"],
        "explanation": "Mỗi ngày hai quả thận lọc khoảng 180 lít máu để thải các chất độc hại qua đường nước tiểu."
    },
    {
        "difficulty": 1,
        "question": "Cơ quan nội tạng có khối lượng lớn nhất trong ổ bụng cơ thể người là cơ quan nào?",
        "correct_answer": "Gan",
        "distractors": ["Dạ dày", "Phổi", "Trực tràng"],
        "explanation": "Gan nặng khoảng 1,4 - 1,6 kg là 'nhà máy hóa chất' chuyển hóa dinh dưỡng và giải độc cho cơ thể."
    },
    {
        "difficulty": 1,
        "question": "Bộ xương của một người trưởng thành bình thường bao gồm tổng cộng bao nhiêu chiếc xương?",
        "correct_answer": "206 chiếc xương",
        "distractors": ["150 chiếc xương", "300 chiếc xương", "250 chiếc xương"],
        "explanation": "Trẻ sơ sinh có khoảng 270 chiếc xương, khi lớn lên nhiều xương hợp nhất lại còn đúng 206 chiếc."
    },
    {
        "difficulty": 1,
        "question": "Xương nào dài nhất, nặng nhất và chịu lực khỏe nhất trong cơ thể con người?",
        "correct_answer": "Xương đùi",
        "distractors": ["Xương cẳng chân", "Xương cột sống", "Xương cánh tay"],
        "explanation": "Xương đùi có thể chịu được tải trọng gấp nhiều lần trọng lượng cơ thể khi chạy nhảy."
    },
    {
        "difficulty": 2,
        "question": "Trong hệ nhóm máu ABO, nhóm máu nào được gọi là 'Nhóm máu chuyên cho' có thể truyền cho tất cả các nhóm còn lại?",
        "correct_answer": "Nhóm máu O (đặc biệt O-)",
        "distractors": ["Nhóm máu A", "Nhóm máu B", "Nhóm máu AB"],
        "explanation": "Hồng cầu nhóm máu O không có kháng nguyên A hay B nên không bị hệ miễn dịch người nhận ngưng kết."
    },
    {
        "difficulty": 2,
        "question": "Trong hệ nhóm máu ABO, nhóm máu nào được gọi là 'Nhóm máu chuyên nhận' có thể nhận máu từ mọi nhóm khác?",
        "correct_answer": "Nhóm máu AB (đặc biệt AB+)",
        "distractors": ["Nhóm máu O", "Nhóm máu A", "Nhóm máu B"],
        "explanation": "Huyết tương nhóm AB không chứa kháng thể chống A hay B nên nhận được tế bào hồng cầu từ mọi nhóm máu."
    },
    {
        "difficulty": 2,
        "question": "Tế bào nào trong máu chịu trách nhiệm vận chuyển khí Oxy từ phổi đến các mô cơ quan nhờ sắc tố Hemoglobin?",
        "correct_answer": "Tế bào hồng cầu (Red blood cells)",
        "distractors": ["Tế bào bạch cầu", "Tiểu cầu", "Tế bào lympho"],
        "explanation": "Hồng cầu hình đĩa lõm hai mặt chứa sắt trong phân tử hemoglobin tạo nên màu đỏ tươi khi kết hợp với oxy."
    },
    {
        "difficulty": 2,
        "question": "Loài thú biển nào là loài động vật lớn nhất từng sinh sống trên Trái Đất, lớn hơn cả những loài khủng long khổng lồ cổ đại?",
        "correct_answer": "Cá voi xanh (Blue whale)",
        "distractors": ["Cá nhà táng", "Cá mập Megalodon", "Khủng long bạo chúa T-Rex"],
        "explanation": "Cá voi xanh có thể dài tới 30 mét và nặng gần 200 tấn, riêng quả tim đã nặng bằng một chiếc xe hơi!"
    },
    {
        "difficulty": 1,
        "question": "Loài chim nào giữ kỷ lục có tốc độ di chuyển nhanh nhất thế giới khi bổ nhào bắt mồi với vận tốc trên 320 km/h?",
        "correct_answer": "Chim cắt lớn (Peregrine Falcon)",
        "distractors": ["Đại bàng đầu trắng", "Chim én", "Đà điểu"],
        "explanation": "Chim cắt lớn khép cánh bổ nhào đạt vận tốc kinh hoàng hơn 380 km/h xé toạc không khí."
    },
    {
        "difficulty": 1,
        "question": "Loài động vật có vú chạy trên mặt đất nhanh nhất hành tinh có thể tăng tốc từ 0 lên 100 km/h chỉ trong 3 giây là gì?",
        "correct_answer": "Báo săn (Cheetah / Báo hoa mai săn mồi)",
        "distractors": ["Sư tử", "Linh dương đầu bò", "Ngựa vằn"],
        "explanation": "Báo săn Cheetah có cấu tạo xương sống dẻo dai và móng vuốt bám đất giúp nó đạt tốc độ 110-120 km/h."
    },

    # Thiên văn & Trái Đất
    {
        "difficulty": 1,
        "question": "Hành tinh nào có kích thước và khối lượng lớn nhất trong Hệ Mặt Trời của chúng ta?",
        "correct_answer": "Sao Mộc (Jupiter)",
        "distractors": ["Sao Thổ (Saturn)", "Sao Hỏa (Mars)", "Sao Kim (Venus)"],
        "explanation": "Sao Mộc là hành tinh khí khổng lồ có thể tích chứa được hơn 1.300 Trái Đất bên trong."
    },
    {
        "difficulty": 1,
        "question": "Hành tinh nào trong Hệ Mặt Trời được mệnh danh là 'Hành tinh Đỏ' do bề mặt chứa nhiều oxit sắt (gỉ sét)?",
        "correct_answer": "Sao Hỏa (Mars)",
        "distractors": ["Sao Thủy", "Sao Kim", "Sao Mộc"],
        "explanation": "Bụi oxit sắt bay lơ lửng trong bầu khí quyển mỏng tạo cho sao Hỏa sắc đỏ cam đặc trưng."
    },
    {
        "difficulty": 1,
        "question": "Hành tinh nào có vành đai bụi băng đá rộng lớn và lộng lẫy rõ rệt nhất quan sát được qua kính viễn vọng?",
        "correct_answer": "Sao Thổ (Saturn)",
        "distractors": ["Sao Hải Vương", "Sao Thiên Vương", "Sao Mộc"],
        "explanation": "Vành đai sao Thổ gồm hàng triệu mảnh đá và tảng băng quay xung quanh hành tinh."
    },
    {
        "difficulty": 2,
        "question": "Hiện tượng Nhật thực diễn ra khi vị trí của ba thiên thể nằm trên một đường thẳng theo thứ tự nào?",
        "correct_answer": "Mặt Trời - Mặt Trăng - Trái Đất",
        "distractors": ["Mặt Trời - Trái Đất - Mặt Trăng", "Mặt Trăng - Mặt Trời - Trái Đất", "Trái Đất - Mặt Trời - Sao Kim"],
        "explanation": "Mặt Trăng đi vào giữa Mặt Trời và Trái Đất che khuất ánh sáng mặt trời tạo thành bóng tối trên mặt đất."
    },
    {
        "difficulty": 2,
        "question": "Hiện tượng Nguyệt thực diễn ra khi vị trí của ba thiên thể nằm trên một đường thẳng theo thứ tự nào?",
        "correct_answer": "Mặt Trời - Trái Đất - Mặt Trăng",
        "distractors": ["Mặt Trời - Mặt Trăng - Trái Đất", "Mặt Trăng - Trái Đất - Sao Hỏa", "Trái Đất - Mặt Trăng - Sao Thủy"],
        "explanation": "Trái Đất chắn giữa Mặt Trời và Mặt Trăng khiến bóng tối của Trái Đất phủ lên bề mặt Mặt Trăng."
    },
    {
        "difficulty": 1,
        "question": "Hiện tượng thủy triều lên xuống hàng ngày trên các đại dương Trái Đất chủ yếu do lực hấp dẫn của thiên thể nào?",
        "correct_answer": "Mặt Trăng (và một phần của Mặt Trời)",
        "distractors": ["Sao Mộc", "Sao Kim", "Gió mùa"],
        "explanation": "Mặt Trăng ở gần Trái Đất nhất nên lực hấp dẫn của nó kéo nước biển dâng lên tạo nên thủy triều."
    },
    {
        "difficulty": 2,
        "question": "Khí nào gây ra hiệu ứng nhà kính mạnh nhất trên khí quyển Sao Kim khiến nhiệt độ bề mặt lên tới gần 470 độ C?",
        "correct_answer": "Khí Cacbonic (CO2 chiếm hơn 96%)",
        "distractors": ["Khí Oxy", "Khí Metan", "Khí Nitơ"],
        "explanation": "Bầu khí quyển CO2 dày đặc bẫy nhiệt độ khiến Sao Kim là hành tinh nóng nhất Hệ Mặt Trời (dù không ở gần Mặt Trời nhất)."
    },
    {
        "difficulty": 3,
        "question": "Vùng ranh giới xung quanh một Lỗ đen (Black Hole) mà một khi ánh sáng vượt qua đó sẽ không bao giờ thoát ra được gọi là gì?",
        "correct_answer": "Chân trời sự kiện (Event Horizon)",
        "distractors": ["Điểm kỳ dị (Singularity)", "Đĩa bồi tụ", "Vùng quang cầu"],
        "explanation": "Tại Chân trời sự kiện, vận tốc thoát ly bằng vận tốc ánh sáng nên ngay cả hạt photon ánh sáng cũng bị giam cầm vĩnh viễn."
    }
]

# Thêm 40 câu mở rộng sinh học và hóa lý tự nhiên
MORE_SCIENCE = [
    ("Tế bào thực vật có cấu trúc nào bao bọc ngoài màng tế bào giúp cây đứng vững chắc?", "Thành tế bào (Cell wall làm từ cellulose)", ["Không bào lớn", "Ty thể", "Lục lạp"], "Thành tế bào cellulose tạo độ bền vững cơ học cho thân cây.", 1),
    ("Bào quan nào trong tế bào được ví như 'nhà máy năng lượng' tổng hợp phân tử ATP cung cấp năng lượng cho tế bào?", "Ty thể (Mitochondria)", ["Ribosome", "Lưới nội chất", "Bộ máy Golgi"], "Ty thể thực hiện quá trình hô hấp tế bào phân giải glucose thành ATP.", 2),
    ("Chất diệp lục (Chlorophyll) trong lá cây hấp thụ mạnh nhất hai vùng ánh sáng có màu nào?", "Ánh sáng đỏ và ánh sáng xanh lam", ["Ánh sáng xanh lá cây", "Ánh sáng vàng", "Tia hồng ngoại"], "Diệp lục phản xạ lại ánh sáng xanh lục nên mắt ta nhìn thấy lá cây có màu xanh.", 2),
    ("Thực vật hút nước và muối khoáng từ đất chủ yếu nhờ bộ phận nào ở rễ cây?", "Miền lông hút của rễ", ["Miền sinh trưởng", "Chóp rễ", "Miền trưởng thành"], "Hàng triệu lông hút li ti giúp tăng tối đa diện tích bề mặt tiếp xúc hút nước.", 1),
    ("Động vật có vú duy nhất có khả năng bay lượn thực sự trên bầu trời là loài nào?", "Loài dơi", ["Sóc bay", "Chồn bay", "Cá bay"], "Cánh dơi là màng da mỏng nối giữa các xương ngón tay dài linh hoạt.", 1),
    ("Loài thú nào ở châu Úc đẻ trứng thay vì đẻ con nhưng vẫn nuôi con bằng sữa mẹ?", "Thú mỏ vịt (và Nhím mỏ ngắn)", ["Chuột túi Kangaroo", "Gấu túi Koala", "Chó dingo"], "Thú mỏ vịt là loài thú đơn huyệt nguyên thủy vô cùng độc đáo.", 2),
    ("Bạch tuộc sở hữu bao nhiêu trái tim trong cơ thể để bơm máu đi nuôi các cơ quan?", "3 trái tim", ["1 trái tim", "2 trái tim", "4 trái tim"], "Bạch tuộc có hai tim mang và một tim chính, máu của chúng có màu xanh lam do chứa đồng (hemocyanin).", 2),
    ("Côn trùng hô hấp bằng cơ quan nào thay vì dùng phổi như động vật có xương sống?", "Hệ thống ống khí dẫn khắp cơ thể", ["Mang ngoài", "Da ẩm ướt", "Túi khí"], "Hệ thống ống khí mở ra các lỗ thở trên bề mặt thân đốt của côn trùng.", 2),
    ("Vitamin nào được cơ thể con người tự tổng hợp dưới da khi tiếp xúc với ánh nắng mặt trời buổi sớm?", "Vitamin D", ["Vitamin C", "Vitamin A", "Vitamin B12"], "Vitamin D giúp cơ thể hấp thụ canxi tốt hơn phòng chống còi xương và loãng xương.", 1),
    ("Căn bệnh thiếu máu thường do cơ thể thiếu hụt nguyên tố vi lượng nào cần thiết cho tạo máu?", "Nguyên tố Sắt (Fe)", ["Canxi", "Magie", "Kẽm"], "Sắt là nhân của huyết sắc tố Hemoglobin trong hồng cầu.", 1),
    ("Tuyến nội tiết nào lớn nhất trong cơ thể người nằm ở vùng cổ phía trước khí quản?", "Tuyến giáp", ["Tuyến tụy", "Tuyến yên", "Tuyến thượng thận"], "Tuyến giáp tiết hormone thyroxine điều hòa tốc độ trao đổi chất.", 2),
    ("Hormone Insulin do tuyến nào trong cơ thể tiết ra giúp điều hòa và hạ lượng đường trong máu?", "Tuyến tụy", ["Gan", "Thận", "Tuyến giáp"], "Thiếu hụt hoặc kháng insulin là nguyên nhân gây ra bệnh tiểu đường (đái tháo đường).", 1),
    ("Lớp men răng bảo vệ bên ngoài răng là mô cứng nhất trong cơ thể chứa hợp chất của nguyên tố nào?", "Canxi và Phốt-pho (Hydroxyapatite)", ["Sắt", "Silic", "Kẽm"], "Men răng có độ cứng gần bằng đá thạch anh bảo vệ răng khỏi mài mòn cơ học.", 2),
    ("Nguyên tử bao gồm hạt nhân ở giữa và các hạt nào mang điện tích âm chuyển động xung quanh?", "Các electron (e-)", ["Các proton", "Các neutron", "Các photon"], "Hạt nhân gồm proton mang điện dương và neutron không mang điện.", 1),
    ("Khí nào gây ra hiện tượng mưa axit phá hủy rừng cây và công trình kim loại xây dựng?", "Lưu huỳnh đioxit (SO2) và oxit nitơ (NOx)", ["Khí Oxy", "Khí Metan", "Khí Nitơ"], "SO2 và NOx phản ứng với hơi nước trong khí quyển tạo thành axit sunfuric và axit nitric.", 2),
    ("Phản ứng hóa học tỏa nhiệt giải phóng ánh sáng và nhiệt độ khi chất cháy kết hợp với khí oxy gọi là gì?", "Sự cháy", ["Sự phân hủy", "Sự quang hợp", "Sự điện phân"], "Điều kiện duy trì sự cháy: chất cháy, nguồn nhiệt và khí oxy.", 1),
    ("Kim loại kiềm nào phản ứng cực kỳ mãnh liệt với nước nổ tung và giải phóng khí hydro?", "Natri (Na) và Kali (K)", ["Sắt (Fe)", "Đồng (Cu)", "Chì (Pb)"], "Do đó Natri và Kali trong phòng thí nghiệm luôn phải được bảo quản ngâm chìm trong dầu hỏa.", 2),
    ("Thang đo độ pH dùng để đo tính axit hay bazơ của dung dịch có giá trị chạy từ bao nhiêu đến bao nhiêu?", "Từ 0 đến 14", ["Từ 1 đến 10", "Từ 0 đến 100", "Từ -10 đến 10"], "pH = 7 là trung tính; pH < 7 là môi trường axit; pH > 7 là môi trường bazơ (kiềm).", 1),
    ("Chất chỉ thị màu nào chuyển sang màu đỏ khi gặp axit và chuyển sang màu xanh khi gặp bazơ?", "Giấy quỳ tím", ["Phenolphthalein", "Nước cất", "Dung dịch iot"], "Quỳ tím là chất chỉ thị axit-bazơ quen thuộc nhất trong hóa học phổ thông.", 1),
    ("Hiện tượng một chất chuyển trực tiếp từ thể rắn sang thể khí mà không qua thể lỏng gọi là gì?", "Sự thăng hoa", ["Sự ngưng tụ", "Sự nóng chảy", "Sự bay hơi"], "Ví dụ thăng hoa của băng khô (CO2 rắn), băng phiến (long não), iot tinh thể.", 2)
]

for item in MORE_SCIENCE:
    QUESTIONS.append({
        "difficulty": item[4],
        "question": item[0],
        "correct_answer": item[1],
        "distractors": item[2],
        "explanation": item[3]
    })

def main():
    print(f"Bắt đầu nạp {len(QUESTIONS)} câu hỏi Khoa học Tự nhiên...")
    added = add_questions_to_category("khoa-hoc-tu-nhien", QUESTIONS)
    print(f"Hoàn thành! Đã thêm {added} câu vào khoa-hoc-tu-nhien.json")

if __name__ == '__main__':
    main()
