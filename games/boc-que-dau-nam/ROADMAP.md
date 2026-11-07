# 🚀 LỘ TRÌNH NÂNG CẤP DỰ ÁN: BỐC QUẺ ĐẦU NĂM (ROADMAP & BACKLOG)
> Tài liệu lưu trữ các tính năng nâng cấp tiềm năng, chia nhỏ theo từng phiên bản để triển khai dần theo **Quy trình Timebox 8 phút**.

---

## 📌 TỔNG QUAN CÁC GIAI ĐOẠN PHÁT TRIỂN TIẾP THEO

| Phiên bản | Tên giai đoạn | Mục tiêu chính | Trạng thái |
|---|---|---|---|
| **v1.0** | Bản Nền Tảng (Core Release) | Hàng đợi thường & VIP, TTS tiếng Việt, chuẩn 9:16, Colab runner kép | ✅ ĐÃ HOÀN THÀNH |
| **v1.1** | Audiovisual & SFX Chân Thực | Âm thanh lắc xăm tre, chiêng đồng, pháo nổ, nhạc BGM Tết, thiệp chụp ảnh | ✅ ĐÃ HOÀN THÀNH |
| **v1.2** | Phân Loại Quẻ & Cá Nhân Hóa | Rút quẻ theo ý (Tình duyên, Tài lộc, Công danh), nhận diện Tên & Năm sinh | ✅ ĐÃ HOÀN THÀNH |
| **v1.3** | Quẻ Đại Hạn & Thử Thách Hóa Giải | Quẻ Hạ Hạ troll dí dỏm, đếm ngược cả phòng thả tim hoặc tặng quà giải hạn | ⏳ CHỜ TRIỂN KHAI |
| **v1.4** | Quà Tặng VIP Đa Tầng & Thần Tài | 3 cấp bậc VIP (Bạc, Vàng, Kim Cương), hiệu ứng Thần Tài bay qua màn hình | ⏳ CHỜ TRIỂN KHAI |
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

### 🎋 MILESTONE 3: v1.3 - Sự Kiện "Quẻ Đại Hạn" & Thử Thách Hóa Giải
- [ ] **Cơ chế Quẻ Hạ Hạ (Troll hài hước):**
  - [ ] Tỷ lệ 10% người bốc sẽ trúng quẻ "Hạ Hạ" (lời thơ dí dỏm về thói quen xấu, hao tài vì trà sữa, cẩn thận người yêu giận...).
- [ ] **Sự kiện Co-op Mini-Game (Cả phòng Live giải cứu):**
  - [ ] Màn hình chuyển sang hiệu ứng ánh tím huyền bí và tiếng chuông báo động.
  - [ ] Đồng hồ đếm ngược 15 giây: *"Cả phòng Live hãy thả gấp 300 Tim HOẶC tặng 1 Hoa Hồng để HÓA GIẢI vận hạn cho bạn [Nickname]!"*.
  - [ ] Nếu giải hạn thành công: Pháo hoa nổ tung, chuyển hóa thành quẻ Đại Cát + tặng danh hiệu "Thoát Nạn Thành Công".

---

### 🎋 MILESTONE 4: v1.4 - Cơ Chế Quà Tặng VIP Đa Tầng & Triệu Hồi Thần Tài
- [ ] **Phân tầng cấp bậc VIP theo giá trị quà tặng:**
  - [ ] 🥉 **VIP Bạc (1 – 9 Xu):** Ưu tiên xếp hàng bốc trước.
  - [ ] 🥈 **VIP Vàng (10 – 99 Xu):** Khung thẻ quẻ mạ vàng lấp lánh, hiệu ứng pháo hoa toàn màn hình, cam kết 100% bốc ra quẻ Thượng Cát.
  - [ ] 🥇 **VIP Kim Cương (100+ Xu - Sư tử, Thiên nga, Du thuyền):**
    - [ ] Triệu hồi hoạt ảnh **Thần Tài Hoàng Kim** cưỡi mây bay qua màn hình.
    - [ ] Mở **Quẻ Hoàng Kim Vạn Lộc** độc bản.
    - [ ] TTS đổi sang nhạc nền hào hùng và xướng danh *"Đại Gia [Nickname] đại phú đại quý"*.

---

### 🎋 MILESTONE 5: v1.5 - Bảng Vinh Danh Phú Hộ, Thanh Phúc Khí & Chống Spam
- [ ] **Bảng Vinh Danh Top 3 Phú Hộ Tích Đức (Leaderboard):**
  - [ ] Hiển thị góc trên màn hình: Top 1, Top 2, Top 3 người donate nhiều xu nhất kèm vương miện Vàng/Bạc/Đồng và avatar.
- [ ] **Cột Mốc "Thanh Phúc Khí Toàn Phòng" (Community Goal):**
  - [ ] Cứ mỗi 1.000 tim hoặc 50 phần quà tích lũy ➔ Kích hoạt **"Giờ Vàng May Mắn"** (Mọi quẻ bốc trong 60s đều nhân đôi hiệu ứng tài lộc).
- [ ] **Hệ thống Chống Spam & Giới hạn hàng đợi (Rate Limiting):**
  - [ ] Mỗi tài khoản chỉ được ở trong hàng đợi 1 lần; bốc xong mới được xếp hàng lại.
  - [ ] Giới hạn độ dài hàng đợi tối đa 20 người để tránh tắc nghẽn.
- [ ] **Lưu lịch sử buổi live (`data/history.json`):**
  - [ ] Tự động ghi lại danh sách người đã bốc, loại quẻ, quà đã tặng để streamer xem lại thống kê.

---

## 📌 HƯỚNG DẪN KHI BẮT ĐẦU NÂNG CẤP MỘT MỤC MỚI:
Khi bạn muốn triển khai bất kỳ mục nào (ví dụ: Milestone 1), chỉ cần gửi lệnh:
> *"Hãy làm Milestone 1 trong ROADMAP.md theo đúng quy tắc chống timeout 8 phút"*
