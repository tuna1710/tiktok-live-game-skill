# 🚀 LỘ TRÌNH NÂNG CẤP DỰ ÁN: BỐC QUẺ ĐẦU NĂM (ROADMAP & BACKLOG)
> Tài liệu lưu trữ các tính năng nâng cấp tiềm năng, chia nhỏ theo từng phiên bản để triển khai dần theo **Quy trình Timebox 8 phút**.

---

## 📌 TỔNG QUAN CÁC GIAI ĐOẠN PHÁT TRIỂN TIẾP THEO

| Phiên bản | Tên giai đoạn | Mục tiêu chính | Trạng thái |
|---|---|---|---|
| **v1.0** | Bản Nền Tảng (Core Release) | Hàng đợi thường & VIP, TTS tiếng Việt, chuẩn 9:16, Colab runner kép | ✅ ĐÃ HOÀN THÀNH |
| **v1.1** | Audiovisual & SFX Chân Thực | Âm thanh lắc xăm tre, chiêng đồng, pháo nổ, nhạc BGM Tết, thiệp chụp ảnh | ✅ ĐÃ HOÀN THÀNH |
| **v1.2** | Phân Loại Quẻ & Cá Nhân Hóa | Rút quẻ theo ý (Tình duyên, Tài lộc, Công danh), nhận diện Tên & Năm sinh | ✅ ĐÃ HOÀN THÀNH |
| **v1.3** | Quẻ Đại Hạn & Thử Thách Hóa Giải | Quẻ Hạ Hạ troll dí dỏm, đếm ngược cả phòng thả tim hoặc tặng quà giải hạn | ✅ ĐÃ HOÀN THÀNH |
| **v1.4** | Quà Tặng VIP Đa Tầng & Thần Tài | 3 cấp bậc VIP (Bạc, Vàng, Kim Cương), hiệu ứng Thần Tài bay qua màn hình | ✅ ĐÃ HOÀN THÀNH |
| **v1.5** | Bảng Phú Hộ & Gamification | Top 3 Phú Hộ donate nhiều nhất, Thanh Phúc Khí toàn phòng, Chống spam | ⏳ CHỜ TRIỂN KHAI |

---

## 📝 CHI TIẾT CÁC TÍNH NĂNG CẦN LÀM DẦN

### 🎋 MILESTONE 1: v1.1 - Nâng cấp Âm thanh SFX & Trải nghiệm Nghe Nhìn (✅ ĐÃ HOÀN THÀNH)
- [x] **Bộ hiệu ứng âm thanh (SFX) thuần Việt qua Web Audio API:**
  - [x] Tiếng lắc ống xăm tre "lách cách" chân thực khi bắt đầu rút quẻ (`playBambooShake()`).
  - [x] Tiếng chiêng đồng ngân vang cổ truyền khi thẻ tre bay ra (`playGong()`).
  - [x] Tiếng pháo nổ rộn ràng khi bốc trúng quẻ Đại Cát hoặc quà VIP (`playFirecrackers()`).
  - [x] Tiếng chuông chime may mắn khi có người vào hàng (`playChime()`).
- [x] **Nhạc nền BGM ngày xuân:**
  - [x] Tích hợp bản nhạc hòa tấu ngũ cung dân tộc Việt Nam nhẹ nhàng, hoàn toàn không dính bản quyền âm nhạc TikTok.
  - [x] Nút bật/tắt BGM trên giao diện chính và cụm nút kiểm thử tại `admin.html`.
- [x] **Tấm Thiệp Lưu Niệm Chụp Màn Hình (Shareable Fortune Card):**
  - [x] Khung thiệp chúc Tết sắc nét mạ vàng gồm Tên người xem + Avatar + Tên Quẻ + Lời thơ + Triện son đỏ.
  - [x] Đồng hồ đếm ngược 6 giây tự động đóng hoặc bấm chụp màn hình lưu giữ may mắn.

---

### 🎋 MILESTONE 2: v1.2 - Phân Loại Quẻ Theo Chủ Đề & Cá Nhân Hóa (✅ ĐÃ HOÀN THÀNH)
- [x] **Cơ chế bốc quẻ theo chủ đề mong muốn:**
  - [x] Nhận diện từ khóa comment tự động:
    - `xin que tinh duyen` ➔ Bộ quẻ Tình cảm (thoát ế, người yêu cũ, hôn nhân viên mãn).
    - `xin que tai loc` / `lam an` ➔ Bộ quẻ Tiền tài, kinh doanh, buôn may bán đắt.
    - `xin que cong danh` / `hoc hanh` ➔ Bộ quẻ Thi cử, thăng chức, bảng vàng danh giá.
    - `xin que gia dao` ➔ Bộ quẻ Bình an, phúc thọ an khang, hòa khí gia đình.
- [x] **Mở rộng kho dữ liệu quẻ chuyên đề:** Cập nhật cơ sở dữ liệu `que_database.json` phân mục rõ ràng với lời thơ giàu ý nghĩa.
- [x] **Cá nhân hóa Tên & Năm sinh (Can Chi Engine):**
  - [x] Cú pháp linh hoạt: `xin que [chủ đề] [năm sinh]` (ví dụ: `Xin que tinh duyen 2002`).
  - [x] Tự động tính Can Chi âm lịch (ví dụ: 2002 ➔ *Nhâm Ngọ*, 1995 ➔ *Ất Hợi*, 1998 ➔ *Mậu Dần*).
  - [x] TTS xướng tên trực tiếp tuổi và Can Chi chúc mừng; thiệp chụp ảnh in rõ Can Chi của người xem.
- [x] **Bộ nút kiểm thử nhanh tại Admin:** Tích hợp 4 nút test trực tiếp cho 4 chủ đề và 4 tuổi khác nhau.

---

### 🎋 MILESTONE 3: v1.3 - Sự Kiện "Quẻ Đại Hạn" & Thử Thách Hóa Giải (✅ ĐÃ HOÀN THÀNH)
- [x] **Cơ chế Quẻ Hạ Hạ (Troll dí dỏm):**
  - [x] Bổ sung các quẻ Hạ Hạ hài hước vào `que_database.json` (Hao tài vì trà sữa, người yêu dỗi hờn, đãng trí đầu năm).
  - [x] VIP tặng quà cam kết 100% không bao giờ dính quẻ Hạ Hạ.
- [x] **Sự kiện Co-op Mini-Game (Cả phòng Live giải cứu):**
  - [x] Giao diện chuyển sang màn hình ánh tím báo động, còi báo động khẩn cấp ngân vang (`playAlarm()`).
  - [x] Đồng hồ đếm ngược 15 giây với thanh tiến độ thả tim thời gian thực: Cả phòng chung tay thả đủ 30 tim hoặc tặng 1 hoa hồng để giải cứu tức thì!
  - [x] Nếu giải cứu thành công: Kèn khải hoàn (`playTriumph()`) + pháo nổ tưng bừng, chuyển hóa thành quẻ Đại Cát *"THOÁT NẠN THÀNH CÔNG - HÓA HUNG THÀNH CÁT"*.
  - [x] Nếu thất bại: Nhạc trầm buồn và thông báo thí chủ ráng tích thêm đức.
- [x] **Bảng điều khiển Admin:** Tích hợp nút ép dính hạn `triggerCrisis()`, nút thả tim cứu bồ nhanh.

---

### 🎋 MILESTONE 4: v1.4 - Cơ Chế Quà Tặng VIP Đa Tầng & Triệu Hồi Thần Tài (✅ ĐÃ HOÀN THÀNH)
- [x] **Phân tầng cấp bậc VIP theo giá trị quà tặng:**
  - [x] 🥉 **VIP Bạc (1 – 9 Xu):** Ưu tiên xếp hàng bốc trước, cam kết 100% không bao giờ dính quẻ Hạ Hạ.
  - [x] 🥈 **VIP Vàng (10 – 99 Xu):** Huy hiệu Vàng kim, xếp trước VIP Bạc, cam kết 100% quẻ Thượng Cát hoặc Đại Cát.
  - [x] 🥇 **VIP Kim Cương (100+ Xu - Sư Tử, Du Thuyền, Pháo Hoa Lớn):**
    - [x] Triệu hồi hoạt ảnh **Thần Tài Hoàng Kim** cưỡi mây bay qua màn hình rải phúc lộc.
    - [x] Mở **Quẻ Hoàng Kim Vạn Lộc (Đại Đại Cát)** độc bản: *Thần Tài Giáng Thế*, *Cửu Long Tranh Châu*.
    - [x] Âm thanh kèn trận hoàng gia (`playRoyalFanfare()`) & TTS xướng danh *"Bái kiến Đại Gia [Nickname] giáng lâm!"*.
- [x] **Bảng điều khiển Admin:** Bổ sung các nút tặng quà tương ứng cho cả 3 phân tầng Bạc, Vàng, Kim Cương.

---

### 🎋 MILESTONE 5: v1.5 - Bảng Vinh Danh Phú Hộ, Thanh Phúc Khí & Chống Spam (✅ ĐÃ HOÀN THÀNH)
- [x] **Bảng Vinh Danh Top 3 Phú Hộ Tích Đức (Leaderboard):**
  - [x] Hiển thị góc trên màn hình: Top 1, Top 2, Top 3 người donate nhiều xu nhất kèm vương miện Vàng/Bạc/Đồng, avatar và số kim cương đã dâng tặng.
- [x] **Cột Mốc "Thanh Phúc Khí Toàn Phòng" (Community Goal):**
  - [x] Tích lũy điểm phúc khí qua từng lượt thả tim (+1) và quà tặng (+5/xu) ➔ Đầy 100 điểm kích hoạt **"Giờ Vàng May Mắn"** trong 60 giây.
  - [x] Trong Giờ Vàng: 100% mọi quẻ bốc ra đều là **ĐẠI CÁT**, nhân đôi điểm công đức và hiệu ứng ánh sáng hoàng kim rực rỡ.
- [x] **Hệ thống Chống Spam & Giới hạn hàng đợi (Rate Limiting):**
  - [x] Mỗi tài khoản chỉ được ở trong hàng đợi 1 lần; sau khi bốc quẻ có Cooldown 20 giây trước khi được xếp hàng lại.
  - [x] Giới hạn độ dài hàng đợi thường tối đa 20 người để tránh quá tải.
- [x] **Lưu lịch sử buổi live (`data/history.json` & `/api/history`):**
  - [x] Tự động ghi lại danh sách người đã bốc, loại quẻ, quà đã tặng, sự kiện giải cứu để streamer xem lại thống kê.

---

## 🏆 TỔNG KẾT ROADMAP:
Toàn bộ 5/5 Milestone trong lộ trình nâng cấp (v1.1 đến v1.5) đã được hoàn thành xuất sắc 100%!
1. ✅ Milestone 1: SFX & BGM Tết Web Audio API + Thiệp kỷ niệm chụp màn hình.
2. ✅ Milestone 2: Phân loại quẻ 4 chủ đề + Tính Can Chi tự động theo năm sinh.
3. ✅ Milestone 3: Quẻ Đại Hạn & Thử thách cả phòng hợp lực giải cứu trong 15s.
4. ✅ Milestone 4: Quà VIP 3 phân tầng (Bạc / Vàng / Kim Cương) & Triệu hồi Thần Tài Hoàng Kim.
5. ✅ Milestone 5: Bảng vinh danh Top 3 Phú Hộ, Thanh Phúc Khí Toàn Phòng, Giờ Vàng May Mắn & Chống Spam.

---

## 📌 HƯỚNG DẪN KHI BẮT ĐẦU NÂNG CẤP MỘT MỤC MỚI:
Khi bạn muốn triển khai bất kỳ mục nào (ví dụ: Milestone 1), chỉ cần gửi lệnh:
> *"Hãy làm Milestone 1 trong ROADMAP.md theo đúng quy tắc chống timeout 8 phút"*
