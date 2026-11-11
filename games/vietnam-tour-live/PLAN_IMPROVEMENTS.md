# 📝 KẾ HOẠCH NÂNG CẤP & ĐIỀU CHỈNH GAME "VIETNAM TOUR LIVE"

> **Lưu ý:** Tài liệu này ghi nhận hướng giải quyết và kế hoạch chi tiết cho 3 yêu cầu cải tiến giao diện & luật chơi, chuẩn bị thực hiện theo từng bước. Không tự ý sửa code khi chưa có lệnh xác nhận.

---

## 📌 DANH SÁCH 3 MỤC CẦN ĐIỀU CHỈNH

### 1️⃣ Mục 1: Cố định bản đồ toàn cảnh, loại bỏ hiệu ứng di chuyển (Pan & Zoom), chỉ sáng đèn khi được điểm
- **Hiện trạng:**
  - Bản đồ đang dùng hiệu ứng Dynamic Camera (Pan & Zoom) liên tục mỗi khi chuyển tỉnh, làm khung nhìn nhảy vị trí, phóng to thu nhỏ gây rối mắt cho người xem livestream trên điện thoại.
- **Hướng xử lý đề xuất:**
  - **Cố định bản đồ toàn cảnh (Fixed Full Overview):** Bản đồ Việt Nam (từ Hà Giang đến Cà Mau, cùng Hoàng Sa & Trường Sa) luôn đứng yên trọn vẹn, căn giữa đẹp mắt trong khung hình 9:16.
  - **Loại bỏ hiệu ứng di chuyển camera:** Tắt toàn bộ biến đổi `translate(...) scale(...)` trong `game.js`. Bản đồ giữ nguyên tỉ lệ hiển thị tĩnh 100%.
  - **Cơ chế sáng đèn khi được điểm (Point-Triggered Glow):**
    - Khi một tỉnh/cụm tỉnh được ghé thăm hoặc cộng điểm: Cụm SVG path của tỉnh đó sẽ **sáng bừng lên** (hiệu ứng Neon Pulse / Flash sáng viền vàng hoặc cyan rực rỡ).
    - Các tỉnh còn lại giữ màu sẫm mờ để tạo độ tương phản nổi bật.
    - Ghim avatar/marker được cắm chính xác tại tọa độ thực của tỉnh đó trên bản đồ toàn cảnh (hoặc hiển thị thẻ vinh danh phía trên/dưới sân khấu).

---

### 2️⃣ Mục 2: Thiết kế lại Bảng Quy Tắc (Luật chơi) cho rõ ràng, dễ hiểu, dễ nhìn
- **Hiện trạng:**
  - Khung luật chơi ở chân màn hình hiện dùng nền hơi tối mờ, font chữ nhỏ (12-14px), chia 2 cột nhiều chữ và giải thích dài dòng, khó đọc lướt khi xem qua màn hình điện thoại/TikTok Live.
- **Hướng xử lý đề xuất:**
  - **Đơn giản hóa nội dung (Quy tắc 3 giây):** Cô đọng thành 4 dòng/thẻ Infographic súc tích, chữ to rõ ràng:
    1. 💬 **GÕ TÊN TỈNH / BIỂN SỐ** $\rightarrow$ Vào đoàn ủng hộ quê hương (+1đ).
    2. ❤️ **THẢ TIM & CHIA SẺ** $\rightarrow$ Tích lũy điểm yêu thương.
    3. 🌹 **1 XU = 30 ĐIỂM** $\rightarrow$ Tăng tốc Đua Top Bảng Vàng.
    4. 👑 **TẶNG QUÀ VIP** $\rightarrow$ Nhảy thẳng lên Top 1 hàng đợi.
  - **Nâng cấp độ tương phản thị giác (Visual & Contrast):**
    - Tăng cỡ chữ lên chuẩn mobile (16px - 18px), in đậm nổi bật các từ khóa chính.
    - Nền thẻ có độ mờ đục cao hơn, viền phát sáng nổi bật để không bị chìm vào nền.
    - Áp dụng màu sắc phân loại trực quan (Xanh comment, Đỏ tim/like, Vàng kim 1 xu, Tím neon VIP).

---

### 3️⃣ Mục 3: Giữ nguyên cấu trúc gộp 34 đơn vị hành chính (Không tách ra 63 tỉnh lẻ)
- **Xác nhận kiến trúc:**
  - Giữ nguyên cấu trúc dữ liệu **34 cụm tỉnh thành** trong `data/provinces.json` và bảng ánh xạ biển số xe `LICENSE_PLATE_MAP` trong `server.js`.
  - Không phân rã thành 63 tỉnh riêng lẻ.
  - Khi người xem bình luận tên một tỉnh thành viên hoặc biển số xe (ví dụ: Bình Dương, Bà Rịa, Yên Bái...): Toàn bộ cụm sáp nhập tương ứng sẽ cùng sáng đèn đồng bộ trên bản đồ và hiển thị tên đại diện chuẩn xác.

---

## 🗺️ LỘ TRÌNH THỰC HIỆN TỪNG BƯỚC (ROADMAP)

- [x] **Bước 1:** Thiết kế lại giao diện Bản đồ tĩnh & cơ chế sáng đèn neon (`game.js` & `style.css`) - ĐÃ HOÀN THÀNH.
- [x] **Bước 2:** Thiết kế lại Bảng Quy Tắc luật chơi dạng Infographic chữ to, dễ nhìn (`index.html` & `style.css`) - ĐÃ HOÀN THÀNH.
- [x] **Bước 3:** Kiểm tra và hoàn thiện độ đồng bộ khi nhận diện tên tỉnh / biển số của 34 cụm sáp nhập (`game.js` & `provinces.json`) - ĐÃ HOÀN THÀNH.
- [ ] **Bước 4:** Kiểm thử trực quan trên giao diện mô phỏng 9:16 và nghiệm thu.
