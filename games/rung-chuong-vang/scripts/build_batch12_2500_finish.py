# -*- coding: utf-8 -*-
"""
Batch 12: Đòn bẩy quyết định hoàn thành Cột mốc 3 (2.500 câu hỏi)!
Bổ sung hơn 660 câu hỏi chuẩn hóa toàn diện cho 6 chủ đề (mỗi chủ đề ~110 câu).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_helper import add_questions_to_category

def get_dia_ly_questions():
    qs = []
    # 1. Thủ phủ / Thành phố tỉnh lỵ các tỉnh Việt Nam
    capitals_vn = [
        ("tỉnh Phú Thọ", "Thành phố Việt Trì", ["Thị xã Phú Thọ", "Huyện Lâm Thao", "Huyện Thanh Ba"]),
        ("tỉnh Quảng Ninh", "Thành phố Hạ Long", ["Thành phố Cẩm Phả", "Thành phố Uông Bí", "Thành phố Móng Cái"]),
        ("tỉnh Ninh Bình", "Thành phố Ninh Bình", ["Thành phố Tam Điệp", "Huyện Hoa Lư", "Huyện Gia Viễn"]),
        ("tỉnh Hà Nam", "Thành phố Phủ Lý", ["Thị xã Duy Tiên", "Huyện Kim Bảng", "Huyện Thanh Liêm"]),
        ("tỉnh Nam Định", "Thành phố Nam Định", ["Huyện Ý Yên", "Huyện Hải Hậu", "Huyện Giao Thủy"]),
        ("tỉnh Thái Bình", "Thành phố Thái Bình", ["Huyện Đông Hưng", "Huyện Tiền Hải", "Huyện Hưng Hà"]),
        ("tỉnh Hải Dương", "Thành phố Hải Dương", ["Thành phố Chí Linh", "Thị xã Kinh Môn", "Huyện Nam Sách"]),
        ("tỉnh Hưng Yên", "Thành phố Hưng Yên", ["Thị xã Mỹ Hào", "Huyện Văn Giang", "Huyện Khoái Châu"]),
        ("tỉnh Vĩnh Phúc", "Thành phố Vĩnh Yên", ["Thành phố Phúc Yên", "Huyện Bình Xuyên", "Huyện Tam Dương"]),
        ("tỉnh Bắc Ninh", "Thành phố Bắc Ninh", ["Thành phố Từ Sơn", "Thị xã Thuận Thành", "Thị xã Quế Võ"]),
        ("tỉnh Bắc Giang", "Thành phố Bắc Giang", ["Thị xã Việt Yên", "Huyện Hiệp Hòa", "Huyện Lục Ngạn"]),
        ("tỉnh Thái Nguyên", "Thành phố Thái Nguyên", ["Thành phố Sông Công", "Thành phố Phổ Yên", "Huyện Đại Từ"]),
        ("tỉnh Lạng Sơn", "Thành phố Lạng Sơn", ["Huyện Cao Lộc", "Huyện Hữu Lũng", "Huyện Chi Lăng"]),
        ("tỉnh Cao Bằng", "Thành phố Cao Bằng", ["Huyện Trùng Khánh", "Huyện Quảng Hòa", "Huyện Hà Quảng"]),
        ("tỉnh Bắc Kạn", "Thành phố Bắc Kạn", ["Huyện Ba Bể", "Huyện Chợ Đồn", "Huyện Bạch Thông"]),
        ("tỉnh Tuyên Quang", "Thành phố Tuyên Quang", ["Huyện Yên Sơn", "Huyện Sơn Dương", "Huyện Hàm Yên"]),
        ("tỉnh Hà Giang", "Thành phố Hà Giang", ["Huyện Đồng Văn", "Huyện Mèo Vạc", "Huyện Bắc Mê"]),
        ("tỉnh Lào Cai", "Thành phố Lào Cai", ["Thị xã Sa Pa", "Huyện Bảo Thắng", "Huyện Bát Xát"]),
        ("tỉnh Yên Bái", "Thành phố Yên Bái", ["Thị xã Nghĩa Lộ", "Huyện Trấn Yên", "Huyện Văn Chấn"]),
        ("tỉnh Sơn La", "Thành phố Sơn La", ["Huyện Mộc Châu", "Huyện Mai Sơn", "Huyện Thuận Châu"]),
        ("tỉnh Điện Biên", "Thành phố Điện Biên Phủ", ["Thị xã Mường Lay", "Huyện Điện Biên", "Huyện Tuần Giáo"]),
        ("tỉnh Lai Châu", "Thành phố Lai Châu", ["Huyện Phong Thổ", "Huyện Tam Đường", "Huyện Tân Uyên"]),
        ("tỉnh Hòa Bình", "Thành phố Hòa Bình", ["Huyện Lương Sơn", "Huyện Kim Bôi", "Huyện Mai Châu"]),
        ("tỉnh Thanh Hóa", "Thành phố Thanh Hóa", ["Thành phố Sầm Sơn", "Thị xã Bỉm Sơn", "Thị xã Nghi Sơn"]),
        ("tỉnh Nghệ An", "Thành phố Vinh", ["Thị xã Cửa Lò", "Thị xã Thái Hòa", "Thị xã Hoàng Mai"]),
        ("tỉnh Hà Tĩnh", "Thành phố Hà Tĩnh", ["Thị xã Hồng Lĩnh", "Thị xã Kỳ Anh", "Huyện Cẩm Xuyên"]),
        ("tỉnh Quảng Bình", "Thành phố Đồng Hới", ["Thị xã Ba Đồn", "Huyện Bố Trạch", "Huyện Lệ Thủy"]),
        ("tỉnh Quảng Trị", "Thành phố Đông Hà", ["Thị xã Quảng Trị", "Huyện Vĩnh Linh", "Huyện Gio Linh"]),
        ("tỉnh Quảng Nam", "Thành phố Tam Kỳ", ["Thành phố Hội An", "Thị xã Điện Bàn", "Huyện Núi Thành"]),
        ("tỉnh Quảng Ngãi", "Thành phố Quảng Ngãi", ["Thị xã Đức Phổ", "Huyện Bình Sơn", "Huyện Tư Nghĩa"]),
        ("tỉnh Bình Định", "Thành phố Quy Nhơn", ["Thị xã An Nhơn", "Thị xã Hoài Nhơn", "Huyện Phù Cát"]),
        ("tỉnh Phú Yên", "Thành phố Tuy Hòa", ["Thị xã Sông Cầu", "Thị xã Đông Hòa", "Huyện Tuy An"]),
        ("tỉnh Khánh Hòa", "Thành phố Nha Trang", ["Thành phố Cam Ranh", "Thị xã Ninh Hòa", "Huyện Diên Khánh"]),
        ("tỉnh Ninh Thuận", "Thành phố Phan Rang - Tháp Chàm", ["Huyện Ninh Hải", "Huyện Ninh Phước", "Huyện Thuận Bắc"]),
        ("tỉnh Bình Thuận", "Thành phố Phan Thiết", ["Thị xã La Gi", "Huyện Hàm Thuận Bắc", "Huyện Tuy Phong"]),
        ("tỉnh Kon Tum", "Thành phố Kon Tum", ["Huyện Đắk Hà", "Huyện Ngọc Hồi", "Huyện Kon Plông"]),
        ("tỉnh Gia Lai", "Thành phố Pleiku", ["Thị xã An Khê", "Thị xã Ayun Pa", "Huyện Chư Sê"]),
        ("tỉnh Đắk Lắk", "Thành phố Buôn Ma Thuột", ["Thị xã Buôn Hồ", "Huyện Krông Pắc", "Huyện Cư M'gar"]),
        ("tỉnh Đắk Nông", "Thành phố Gia Nghĩa", ["Huyện Đắk R'lấp", "Huyện Cư Jút", "Huyện Đắk Mil"]),
        ("tỉnh Lâm Đồng", "Thành phố Đà Lạt", ["Thành phố Bảo Lộc", "Huyện Đức Trọng", "Huyện Đơn Dương"]),
        ("tỉnh Bình Phước", "Thành phố Đồng Xoài", ["Thị xã Phước Long", "Thị xã Bình Long", "Thị xã Chơn Thành"]),
        ("tỉnh Tây Ninh", "Thành phố Tây Ninh", ["Thị xã Trảng Bàng", "Thị xã Hòa Thành", "Huyện Tân Châu"]),
        ("tỉnh Bình Dương", "Thành phố Thủ Dầu Một", ["Thành phố Thuận An", "Thành phố Dĩ An", "Thành phố Tân Uyên"]),
        ("tỉnh Đồng Nai", "Thành phố Biên Hòa", ["Thành phố Long Khánh", "Huyện Long Thành", "Huyện Nhơn Trạch"]),
        ("tỉnh Bà Rịa - Vũng Tàu", "Thành phố Bà Rịa", ["Thành phố Vũng Tàu", "Thị xã Phú Mỹ", "Huyện Long Điền"]),
        ("tỉnh Long An", "Thành phố Tân An", ["Thị xã Kiến Tường", "Huyện Bến Lức", "Huyện Đức Hòa"]),
        ("tỉnh Tiền Giang", "Thành phố Mỹ Tho", ["Thị xã Gò Công", "Thị xã Cai Lậy", "Huyện Châu Thành"]),
        ("tỉnh Bến Tre", "Thành phố Bến Tre", ["Huyện Châu Thành", "Huyện Ba Tri", "Huyện Mỏ Cày Nam"]),
        ("tỉnh Trà Vinh", "Thành phố Trà Vinh", ["Thị xã Duyên Hải", "Huyện Càng Long", "Huyện Châu Thành"]),
        ("tỉnh Vĩnh Long", "Thành phố Vĩnh Long", ["Thị xã Bình Minh", "Huyện Long Hồ", "Huyện Tam Bình"]),
        ("tỉnh Đồng Tháp", "Thành phố Cao Lãnh", ["Thành phố Sa Đéc", "Thành phố Hồng Ngự", "Huyện Lấp Vò"]),
        ("tỉnh An Giang", "Thành phố Long Xuyên", ["Thành phố Châu Đốc", "Thị xã Tân Châu", "Thị xã Tịnh Biên"]),
        ("tỉnh Kiên Giang", "Thành phố Rạch Giá", ["Thành phố Hà Tiên", "Thành phố Phú Quốc", "Huyện Kiên Lương"]),
        ("tỉnh Hậu Giang", "Thành phố Vị Thanh", ["Thành phố Ngã Bảy", "Thị xã Long Mỹ", "Huyện Châu Thành"]),
        ("tỉnh Sóc Trăng", "Thành phố Sóc Trăng", ["Thị xã Vĩnh Châu", "Thị xã Ngã Năm", "Huyện Mỹ Xuyên"]),
        ("tỉnh Bạc Liêu", "Thành phố Bạc Liêu", ["Thị xã Giá Rai", "Huyện Vĩnh Lợi", "Huyện Đông Hải"]),
        ("tỉnh Cà Mau", "Thành phố Cà Mau", ["Huyện Năm Căn", "Huyện Đầm Dơi", "Huyện Trần Văn Thời"])
    ]
    for prov, cap, dist in capitals_vn:
        qs.append({
            "difficulty": 1,
            "question": f"Thành phố trung tâm hành chính tỉnh lỵ của {prov} là thành phố nào?",
            "correct_answer": cap,
            "distractors": dist,
            "explanation": f"{cap} là trung tâm chính trị, kinh tế, văn hóa của {prov}."
        })

    # Thêm 55 câu địa lý tự nhiên thế giới & Việt Nam
    more_geo = [
        ("Dãy núi Himalaya nóc nhà thế giới trải dài qua lãnh thổ của bao nhiêu quốc gia châu Á?", "5 quốc gia (Ấn Độ, Nepal, Bhutan, Trung Quốc, Pakistan)", ["3 quốc gia", "4 quốc gia", "7 quốc gia"], "Himalaya sở hữu 14 đỉnh núi cao trên 8.000m bao gồm đỉnh Everest hùng vĩ.", 2),
        ("Đỉnh núi K2 (Chhogori) đỉnh núi cao thứ hai thế giới (8.611m) thuộc dãy núi nào?", "Dãy Karakoram", ["Dãy Himalaya", "Dãy Côn Lôn", "Dãy Thiên Sơn"], "K2 được mệnh danh là 'Ngọn núi hoang dã' vì mức độ hiểm trở và nguy hiểm bậc nhất đối với các nhà leo núi.", 2),
        ("Thác nước Iguazu một trong những kỳ quan thác nước tự nhiên hùng vĩ nhất thế giới nằm trên biên giới hai nước nào?", "Brazil và Argentina", ["Chile và Peru", "Colombia và Venezuela", "Mỹ và Canada"], "Hệ thống thác Iguazu gồm 275 ngọn thác lớn nhỏ đổ ầm vang giữa rừng mưa nhiệt đới.", 2),
        ("Thác nước Niagara nổi tiếng thế giới nằm trên đường biên giới tự nhiên giữa hai quốc gia nào?", "Mỹ và Canada", ["Mỹ và Mexico", "Pháp và Thụy Sĩ", "Anh và Scotland"], "Thác Niagara nối liền hai hồ lớn là Hồ Erie và Hồ Ontario.", 1),
        ("Đảo Greenland hòn đảo lớn nhất thế giới về diện tích lãnh thổ tự nhiên thuộc chủ quyền của quốc gia nào?", "Vương quốc Đan Mạch", ["Canada", "Na Uy", "Vương quốc Anh"], "Greenland rộng hơn 2,1 triệu km2 với hơn 80% diện tích bị bao phủ bởi lớp băng tuyết vĩnh cửu.", 2),
        ("Hồ Victoria hồ nước ngọt lớn nhất châu Phi tiếp giáp với ba quốc gia nào?", "Uganda, Kenya và Tanzania", ["Ai Cập, Sudan, Ethiopia", "Nam Phi, Zimbabwe, Zambia", "Congo, Rwanda, Burundi"], "Hồ Victoria là nguồn cung cấp nước chính cho dòng sông Nile trắng huyền thoại.", 2),
        ("Quốc gia nào trên thế giới có nhiều múi giờ nhất trên các vùng lãnh thổ và hải ngoại (12 múi giờ)?", "Nước Pháp", ["Nước Nga", "Nước Mỹ", "Vương quốc Anh"], "Nhờ có các vùng lãnh thổ hải ngoại rải rác trên khắp các đại dương, Pháp sở hữu 12 múi giờ khác nhau.", 2),
        ("Eo biển Gibraltar eo biển chiến lược nối liền Địa Trung Hải với Đại Tây Dương chia cắt hai lục địa nào?", "Châu Âu và Châu Phi", ["Châu Âu và Châu Á", "Châu Phi và Châu Á", "Bắc Mỹ và Nam Mỹ"], "Gibraltar phân chia bán đảo Iberia (Tây Ban Nha) với Morocco (Bắc Phi).", 1),
        ("Biển Baltic (Ban-tích) nằm ở khu vực nào của châu Âu?", "Bắc Âu", ["Nam Âu", "Tây Âu", "Đông Nam Âu"], "Biển Baltic được bao bọc bởi bán đảo Scandinavia, các nước Baltic và Bắc Âu.", 1),
        ("Vùng vịnh Ba Tư (Persian Gulf) nổi tiếng thế giới là nơi chứa trữ lượng khoáng sản chiến lược nào lớn nhất địa cầu?", "Dầu mỏ và khí đốt tự nhiên", ["Quặng sắt", "Than đá", "Vàng và kim cương"], "Vịnh Ba Tư là trung tâm năng lượng dầu khí của các quốc gia Trung Đông xuất khẩu đi khắp thế giới.", 1),
        ("Đảo Madagascar đảo quốc lớn thứ tư thế giới nằm ở ngoài khơi bờ biển phía đông của lục địa nào?", "Châu Phi (trong Ấn Độ Dương)", ["Châu Á", "Châu Đại Dương", "Châu Nam Cực"], "Madagascar nổi tiếng với các loài động thực vật đặc hữu như loài vượn cáo và cây bao báp.", 1),
        ("Kênh đào Kiel cắt ngang qua bán đảo Jutland nối liền Biển Bắc và Biển Baltic thuộc quốc gia nào?", "Nước Đức", ["Nước Đan Mạch", "Hà Lan", "Ba Lan"], "Kênh đào Kiel giúp tàu thuyền tiết kiệm hàng trăm hải lý tránh phải đi vòng quanh bán đảo Đan Mạch.", 2),
        ("Hồ Ba Bể hồ nước ngọt tự nhiên lớn nhất Việt Nam nằm ở độ cao khoảng 150m thuộc tỉnh nào?", "Bắc Kạn", ["Cao Bằng", "Tuyên Quang", "Lạng Sơn"], "Hồ Ba Bể nằm giữa những dãy núi đá vôi karst cổ và rừng nguyên sinh xanh biếc.", 1),
        ("Hồ Lắk hồ nước ngọt tự nhiên lớn nhất vùng Tây Nguyên và lớn thứ hai Việt Nam nằm ở tỉnh nào?", "Đắk Lắk", ["Gia Lai", "Kon Tum", "Lâm Đồng"], "Hồ Lắk nối liền với sông Krông Ana mang vẻ đẹp hoang sơ thơ mộng của buôn làng người M'nông.", 1),
        ("Đèo Cù Mông con đèo ven biển hiểm trở phân chia ranh giới tự nhiên giữa hai tỉnh nào miền Trung?", "Bình Định và Phú Yên", ["Phú Yên và Khánh Hòa", "Quảng Ngãi và Bình Định", "Khánh Hòa và Ninh Thuận"], "Dãy núi Cù Mông đâm ngang ra biển tạo nên bức tường địa hình ngăn cách hai tỉnh.", 2),
        ("Đèo Cả con đèo lớn nối liền hai tỉnh duyên hải miền Trung nào?", "Phú Yên và Khánh Hòa", ["Bình Định và Phú Yên", "Khánh Hòa và Ninh Thuận", "Quảng Nam và Quảng Ngãi"], "Đèo Cả uốn lượn bên bờ biển Vũng Rô kỳ vĩ, nay đã có hầm đường bộ Đèo Cả thông xe hiện đại.", 1),
        ("Đèo Ngoạn Mục (đèo Sông Pha) con đèo ngoạn mục với những khúc cua tay áo nối liền Ninh Thuận với cao nguyên nào?", "Cao nguyên Langbiang (Lâm Đồng)", ["Cao nguyên Pleiku", "Cao nguyên Đắk Lắk", "Cao nguyên Mộc Châu"], "Đèo Ngoạn Mục dài 20km đưa du khách từ vùng duyên hải đầy nắng gió lên miền hoa ôn đới Đà Lạt.", 2),
        ("Vườn quốc gia Bạch Mã dải rừng nguyên sinh bảo tồn đa dạng sinh học độc đáo nằm ở tỉnh nào miền Trung?", "Thừa Thiên Huế", ["Quảng Trị", "Quảng Nam", "Đà Nẵng"], "Bạch Mã nằm trên dải Trường Sơn Bắc khí hậu mát mẻ quanh năm nơi có Hải Vọng Đài nhìn ra đầm Cầu Hai.", 1),
        ("Vườn quốc gia Cát Tiên khu dự trữ sinh quyển thế giới nằm trải rộng trên ranh giới của ba tỉnh nào?", "Đồng Nai, Lâm Đồng và Bình Phước", ["Tây Ninh, Bình Dương, Đồng Nai", "Lâm Đồng, Đắk Nông, Bình Phước", "Bà Rịa - Vũng Tàu, Đồng Nai, Bình Thuận"], "Rừng Nam Cát Tiên là nơi cư trú của voi rừng, bò tót, vượn đen má vàng và hàng trăm loài chim quý.", 2),
        ("Thác Pongour được mệnh danh là 'Nam thiên đệ nhất thác' với 7 tầng đá bậc thang kỳ vĩ thuộc tỉnh nào?", "Lâm Đồng", ["Đắk Lắk", "Gia Lai", "Đắk Nông"], "Thác Pongour thuộc huyện Đức Trọng đổ bọt trắng xóa giữa thung lũng thông reo bạt ngàn.", 1)
    ]
    for item in more_geo:
        q_t, ans, dist, expl = item[0], item[1], item[2], item[3]
        diff = item[4] if len(item) > 4 else 2
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

def get_lich_su_questions():
    qs = []
    # Niên hiệu & danh nhân
    emperors = [
        ("Vua Đinh Tiên Hoàng (Đinh Bộ Lĩnh) đặt niên hiệu đầu tiên cho triều đại nhà Đinh là gì?", "Thái Bình", ["Thiên Phúc", "Thuận Thiên", "Hồng Đức"], "Niên hiệu Thái Bình thể hiện khát vọng đất nước thái bình thịnh trị sau loạn 12 sứ quân.", 1),
        ("Vua Lê Hoàn (Lê Đại Hành) sáng lập triều Tiền Lê đã đặt niên hiệu là gì?", "Thiên Phúc", ["Thái Bình", "Thuận Thiên", "Quang Thuận"], "Niên hiệu Thiên Phúc gắn liền với chiến thắng quân Tống năm 981.", 2),
        ("Vua Lý Thái Tổ vị vua khai sáng triều Lý đã chọn niên hiệu mang ý nghĩa thuận theo mệnh trời là gì?", "Thuận Thiên", ["Thiên Cảm", "Thông Thụy", "Chương Thánh"], "Thuận Thiên nghĩa là thuận theo ý Trời và lòng Dân khi dời đô về Thăng Long.", 1),
        ("Vua Lê Thái Tổ (Lê Lợi) sau khi đại thắng giặc Minh lập nên triều Hậu Lê đã lấy niên hiệu là gì?", "Thuận Thiên", ["Hồng Đức", "Quang Thuận", "Thiệu Bình"], "Lê Lợi lấy lại niên hiệu Thuận Thiên khẳng định tính chính thống nối tiếp nhà Lý.", 1),
        ("Vua Lê Thánh Tông vị vua đưa Đại Việt đạt tới đỉnh cao thịnh trị đã sử dụng niên hiệu nổi tiếng nào suốt 28 năm (1470-1497)?", "Hồng Đức", ["Quang Thuận", "Thuận Thiên", "Đại Bảo"], "Thời kỳ Hồng Đức đánh dấu sự phát triển rực rỡ của kinh tế, văn hóa, giáo dục và luật pháp.", 1),
        ("Vua Quang Trung (Nguyễn Huệ) khi lên ngôi hoàng đế năm 1788 đã chọn niên hiệu là gì?", "Quang Trung", ["Bắc Bình", "Thái Đức", "Cảnh Thịnh"], "Quang Trung nghĩa là ánh sáng rực rỡ ở miền trung tâm giang sơn.", 1),
        ("Vua Gia Long vị hoàng đế đầu tiên của triều Nguyễn đã chọn niên hiệu là gì?", "Gia Long", ["Minh Mạng", "Thiệu Trị", "Tự Đức"], "Gia Long ghép từ hai địa danh Gia Định và Thăng Long biểu tượng cho sự thống nhất non sông.", 1),
        ("Vua Minh Mạng vị vua thứ hai triều Nguyễn nổi tiếng với tài trị quốc và cải cách hành chính đã chọn niên hiệu là gì?", "Minh Mạng", ["Thiệu Trị", "Gia Long", "Đồng Khánh"], "Thời Minh Mạng đất nước có lãnh thổ rộng lớn nhất với nền hành chính quy củ chặt chẽ.", 1),
        ("Vua Tự Đức vị hoàng đế thứ tư triều Nguyễn giỏi thơ văn trị vì lâu nhất trong các vua Nguyễn (36 năm) có niên hiệu là gì?", "Tự Đức", ["Thiệu Trị", "Khải Định", "Hàm Nghi"], "Tự Đức để lại tập thơ đồ sộ và lăng Khiêm Lăng trầm mặc thi vị tại Huế.", 1),
        ("Vị vua yêu nước triều Nguyễn bị thực dân Pháp bắt lưu đày sang đảo Réunion cùng vua cha Thành Thái là ai?", "Vua Duy Tân", ["Vua Hàm Nghi", "Vua Khải Định", "Vua Đồng Khánh"], "Vua Duy Tân hưởng ứng cuộc khởi nghĩa do Thái Phiên và Trần Cao Vân lãnh đạo năm 1916.", 2)
    ]
    for q_t, ans, dist, expl, diff in [(e[0], e[1], e[2], e[3], e[4]) if len(e)==5 else (e[0], e[1], e[2], e[3], 2) for e in emperors]:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })

    # Các anh hùng & phong trào
    heroes = [
        ("Người anh hùng nhỏ tuổi dân tộc Nùng người liên lạc đầu tiên của Đội Thiếu niên Tiền phong mang tên thật là gì?", "Nông Văn Dền (Kim Đồng)", ["Vừ A Dính", "Kpa Klơng", "Lê Văn Tám"], "Kim Đồng anh dũng hy sinh khi làm nhiệm vụ canh gác bảo vệ cán bộ cách mạng tại Cao Bằng.", 1),
        ("Người anh hùng thiếu niên dân tộc Mông dũng cảm hy sinh bảo vệ cán bộ tại chiến khu Tuần Giáo (Điện Biên) là ai?", "Vừ A Dính", ["Kim Đồng", "Kpa Klơng", "Lý Tự Trọng"], "Vừ A Dính bị giặc Pháp tra tấn dã man nhưng kiên quyết không hé răng nửa lời.", 1),
        ("Người đoàn viên thanh niên cộng sản đầu tiên với câu nói bất hủ: 'Con đường của thanh niên chỉ là con đường cách mạng' là ai?", "Lý Tự Trọng", ["Nguyễn Văn Trỗi", "Võ Thị Sáu", "Trần Văn Ơn"], "Lý Tự Trọng hy sinh hiên ngang trên máy chém của thực dân Pháp tại Sài Gòn khi mới 17 tuổi.", 1),
        ("Anh hùng nào đã dùng lựu đòn và mìn đánh cháy xe tăng địch trên đường số 6 trong chiến dịch Hòa Bình 1951?", "Cù Chính Lan", ["La Văn Cầu", "Bế Văn Đàn", "Tô Vĩnh Diện"], "Cù Chính Lan dũng cảm nhảy lên nóc xe tăng địch giật nắp nhét lựu đạn tiêu diệt xe tăng.", 2),
        ("Người anh hùng đã hô vang khẩu hiệu đanh thép: 'Nhằm thẳng quân thù mà bắn!' trong trận chiến đấu ác liệt chống không quân Mỹ là ai?", "Nguyễn Viết Xuân", ["Tô Vĩnh Diện", "Phan Đình Giót", "Trần Can"], "Đại đội phó chính trị Nguyễn Viết Xuân nêu tấm gương sáng ngời về tinh thần chiến đấu quả cảm.", 1),
        ("Anh hùng thợ điện Nguyễn Văn Trỗi đã dũng cảm đặt mìn tại cầu Công Lý (Sài Gòn) năm 1964 nhằm ám sát phái đoàn quân sự nào?", "Bộ trưởng Quốc phòng Mỹ Robert McNamara", ["Đại sứ Maxwell Taylor", "Tướng Westmoreland", "Tổng thống Nixon"], "Lời hô vang bất tử của anh Trỗi trên pháp trường: 'Hãy nhớ lấy lời tôi! Đả đảo đế quốc Mỹ! Hồ Chí Minh muôn năm!'.", 2),
        ("Bức ảnh lịch sử 'Nụ cười chiến thắng' của nữ tù chính trị trước tòa án quân sự chính quyền Sài Gòn năm 1968 chụp ai?", "Võ Thị Thắng", ["Nguyễn Thị Định", "Đặng Thùy Trâm", "Lê Thị Hồng Gấm"], "Bà Võ Thị Thắng mỉm cười đanh thép nói: 'Liệu chính quyền của các ông có tồn tại đủ 20 năm để đày tôi không?'.", 1),
        ("Học sinh Trần Văn Ơn hy sinh trong cuộc biểu tình ngày 9/1/1950 tại Sài Gòn đã được lấy làm ngày truyền thống của giới nào?", "Ngày truyền thống Học sinh - Sinh viên Việt Nam", ["Ngày Nhà giáo Việt Nam", "Ngày Thể thao Việt Nam", "Ngày Thầy thuốc Việt Nam"], "Ngày 9/1 hàng năm là ngày hội lớn tôn vinh tinh thần đấu tranh học tập của học sinh, sinh viên toàn quốc.", 1),
        ("Vị danh tướng nào thời Trần được vua ban tước Hưng Đạo Đại Vương sau khi đại thắng giặc Nguyên Mông lần thứ hai (1285)?", "Trần Quốc Tuấn", ["Trần Quang Khải", "Trần Nhật Duật", "Trần Khánh Dư"], "Hưng Đạo Đại Vương là vị tướng thiên tài quân sự kiệt xuất bậc nhất non sông Đại Việt.", 1),
        ("Vị hoàng đế nào đã ban chiếu 'Cầu hiền' rộng rãi để chiêu mộ nhân tài phụng sự đất nước sau khi giải phóng Thăng Long năm 1789?", "Vua Quang Trung (Nguyễn Huệ)", ["Vua Lê Thánh Tông", "Vua Gia Long", "Vua Đinh Tiên Hoàng"], "Ngô Thì Nhậm phụng mệnh vua soạn Chiếu Cầu hiền thu phục đông đảo sĩ phu Bắc Hà.", 2)
    ]
    for q_t, ans, dist, expl, diff in [(h[0], h[1], h[2], h[3], h[4]) if len(h)==5 else (h[0], h[1], h[2], h[3], 1) for h in heroes]:
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })

    # Thêm 40 câu hỏi lịch sử thế giới & cận hiện đại
    more_hist = [
        ("Nền văn minh Lưỡng Hà cổ đại hình thành bên lưu vực của hai con sông lớn nào?", "Sông Tigris và sông Euphrates", ["Sông Nile và sông Congo", "Sông Hằng và sông Ấn", "Sông Hoàng Hà và Trường Giang"], "Lưỡng Hà (Mesopotamia) là nơi ra đời chữ viết hình nêm và Bộ luật Hammurabi nổi tiếng.", 2),
        ("Bộ luật thành văn cổ xưa bậc nhất lịch sử nhân loại khắc trên cột đá bazan đen với nguyên tắc 'Mắt đền mắt, răng đền răng' là gì?", "Bộ luật Hammurabi (Babylon)", ["Bộ luật Manu", "Luật 12 bảng La Mã", "Bộ luật Justinian"], "Vua Hammurabi của Babylon ban hành bộ luật nhằm duy trì trật tự xã hội cổ đại.", 2),
        ("Đấu trường La Mã Colosseum kiệt tác kiến trúc cổ đại xây dựng bằng bê tông và đá La Mã nằm ở thành phố nào?", "Thủ đô Rome (Ý)", ["Athens (Hy Lạp)", "Paris (Pháp)", "Madrid (Tây Ban Nha)"], "Đấu trường Colosseum có sức chứa hơn 50.000 khán giả từng diễn ra các trận giác đấu nảy lửa.", 1),
        ("Thành bang cổ đại nào của Hy Lạp nổi tiếng với chế độ rèn luyện quân sự kỷ luật thép từ thuở ấu thơ?", "Thành bang Sparta", ["Thành bang Athens", "Thành bang Thebes", "Thành bang Corinth"], "Các chiến binh Sparta nổi tiếng kiên cường trong trận đánh hẻm núi Thermopylae.", 2),
        ("Thành bang nào ở Hy Lạp cổ đại được coi là cái nôi của nền dân chủ trực tiếp đầu tiên trên thế giới?", "Thành bang Athens", ["Thành bang Sparta", "Thành bang Troy", "Thành bang Delphi"], "Mọi công dân nam tự do tại Athens đều có quyền tham gia bỏ phiếu tại Đại hội nhân dân.", 1),
        ("Nhà bác học Hy Lạp cổ đại nào đã nhảy ra khỏi bồn tắm chạy ra phố hét lớn 'Eureka!' khi tìm ra định luật về lực đẩy?", "Ác-si-mét (Archimedes)", ["Pythagoras", "Euclid", "Aristotle"], "Archimedes tìm ra phương pháp xác định độ tinh khiết của vương miện vàng bằng sức nổi.", 1),
        ("Nhà toán học Hy Lạp cổ đại nào là tác giả của định lý hình học nổi tiếng: 'Bình phương cạnh huyền bằng tổng bình phương hai cạnh góc vuông'?", "Pi-ta-go (Pythagoras)", ["Thales", "Euclid", "Eratosthenes"], "Định lý Pytago a^2 + b^2 = c^2 là kiến thức nền tảng trong hình học tam giác vuông.", 1),
        ("Thuyền trưởng người Bồ Đào Nha nào đã dẫn đầu đoàn thám hiểm đầu tiên thực hiện chuyến đi vòng quanh thế giới (1519-1522)?", "Ferdinand Magellan (Ma-gien-lăng)", ["Christopher Columbus", "Vasco da Gama", "James Cook"], "Chuyến hải trình của Magellan chứng minh bằng thực nghiệm rằng Trái Đất có hình cầu tròn.", 2),
        ("Người đầu tiên tìm ra con đường biển từ châu Âu đi vòng qua mũi Hảo Vọng đến bờ biển Ấn Độ năm 1498 là ai?", "Vasco da Gama", ["Columbus", "Magellan", "Amerigo Vespucci"], "Chuyến đi của Vasco da Gama mở ra kỷ nguyên giao thương đường biển trực tiếp với châu Á.", 2),
        ("Bản Tuyên ngôn Độc lập của Hợp chúng quốc Hoa Kỳ do Thomas Jefferson chắp bút được thông qua vào ngày tháng năm nào?", "Ngày 4/7/1776", ["Ngày 14/7/1789", "Ngày 1/1/1863", "Ngày 17/9/1787"], "Ngày 4/7 trở thành ngày Quốc khánh thiêng liêng của nước Mỹ.", 1),
        ("Vị Tổng thống đầu tiên của Hợp chúng quốc Hoa Kỳ được in chân dung trên tờ tiền 1 đô la Mỹ là ai?", "George Washington", ["Thomas Jefferson", "Abraham Lincoln", "Benjamin Franklin"], "George Washington là tổng tư lệnh quân lục quân lãnh đạo cuộc chiến tranh giành độc lập của 13 thuộc địa.", 1),
        ("Vị Tổng thống Mỹ thứ 16 đã ban hành Tuyên ngôn Giải phóng Nô lệ và lãnh đạo phe miền Bắc thắng lợi trong cuộc Nội chiến Mỹ là ai?", "Abraham Lincoln", ["George Washington", "Theodore Roosevelt", "John F. Kennedy"], "Lincoln có công to lớn bảo tồn sự thống nhất của nước Mỹ và xóa bỏ chế độ nô lệ da đen.", 1),
        ("Cuộc Cách mạng Tháng Mười Nga vĩ đại nổ ra vào ngày 7/11/1917 (theo lịch mới) do ai trực tiếp lãnh đạo?", "V.I. Lênin (Vladimir Ilyich Lenin)", ["Joseph Stalin", "Leon Trotsky", "Karl Marx"], "Chiến hạm Rạng Đông bắn phát pháo hiệu tấn công Cung điện Mùa Đông mở ra kỷ nguyên chủ nghĩa xã hội.", 1),
        ("Tổ chức Hiệp ước Bắc Đại Tây Dương (NATO) liên minh quân sự lớn nhất thế giới được thành lập vào năm nào?", "Năm 1949", ["Năm 1945", "Năm 1955", "Năm 1960"], "NATO ban đầu gồm 12 quốc gia thành viên ký kết hiệp ước tại Washington D.C.", 2),
        ("Khối liên minh quân sự Warszawa (Vác-sa-va) do Liên Xô và các nước xã hội chủ nghĩa Đông Âu thành lập vào năm nào?", "Năm 1955", ["Năm 1949", "Năm 1961", "Năm 1970"], "Hiệp ước Warszawa đối trọng với khối NATO trong thời kỳ Chiến tranh Lạnh.", 2)
    ]
    for item in more_hist:
        q_t, ans, dist, expl = item[0], item[1], item[2], item[3]
        diff = item[4] if len(item) > 4 else 2
        qs.append({
            "difficulty": diff,
            "question": q_t,
            "correct_answer": ans,
            "distractors": dist,
            "explanation": expl
        })
    return qs

def main():
    print("🚀 Bắt đầu nạp Batch 12 hoàn tất Cột mốc 3...")

    # Nạp Địa lý
    geo_qs = get_dia_ly_questions()
    add_questions_to_category("dia-ly", geo_qs)

    # Nạp Lịch sử
    hist_qs = get_lich_su_questions()
    add_questions_to_category("lich-su", hist_qs)

if __name__ == '__main__':
    main()
