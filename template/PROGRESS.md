# 📋 TIẾN ĐỘ DỰ ÁN GAME: [TÊN_GAME]
> **Cơ chế chống Timeout (Timebox 8 phút):** AI thực hiện từng Phase độc lập. Sau mỗi Phase (hoặc tối đa 8 phút), AI cập nhật file này, báo cáo người dùng và đợi lệnh tiếp tục.

---

## 📌 THÔNG TIN TỔNG QUAN
- **Tên trò chơi:** [Tên trò chơi của bạn]
- **Tỉ lệ khung hình:** Dọc 9:16 (1080 x 1920 px)
- **Cơ chế tương tác:** Comment (`...`) | Quà tặng (`Hoa hồng`, `Mũ`,...) | Thả tim
- **Trạng thái hiện tại:** `Đang thực hiện Phase 1` (hoặc `Hoàn thành`)
- **Khởi tạo lúc:** [Thời gian]
- **Cập nhật lần cuối:** [Thời gian]

---

## 🗺️ MỤC LỤC & CHECKLIST CÔNG VIỆC TỪNG BƯỚC

### 🔹 PHASE 1: Khởi tạo, Đặc tả & Thiết kế Kiến trúc (Dự kiến: 1 - 2 phút)
- [ ] Phân tích luật chơi, cơ chế tương tác (Chat, Gift, Like).
- [ ] Thiết lập file `PROGRESS.md` (Checklist chi tiết từ tổng quát đến cụ thể).
- [ ] Khởi tạo thư mục dự án và file cấu hình `.env.example`, `package.json`.
- [ ] *Checkpoint 1: Báo cáo hoàn thành Phase 1, chờ người dùng duyệt để code Backend.*

---

### 🔹 PHASE 2: Xây dựng Backend & Giả lập Mock API (Dự kiến: 3 - 5 phút)
- [ ] Cài đặt dependencies (`express`, `socket.io`, `tiktok-live-connector`, `cors`, `dotenv`).
- [ ] Viết `server.js`:
  - [ ] Khởi tạo HTTP & Socket.IO server.
  - [ ] Kết nối `TikTokLiveConnection` bắt sự kiện `chat`, `gift`, `like`, `member`.
  - [ ] Tích hợp API proxy TTS tiếng Việt (`/api/tts`).
  - [ ] Tích hợp bộ nhận sự kiện giả lập `mock:chat`, `mock:gift`, `mock:like`, `game:reset`.
- [ ] Viết trang điều khiển giả lập `public/admin.html` để kiểm thử độc lập.
- [ ] *Checkpoint 2: Báo cáo hoàn thành Phase 2, chờ người dùng duyệt để làm Frontend.*

---

### 🔹 PHASE 3: Thiết kế Giao diện 9:16 & Hoạt ảnh Frontend (Dự kiến: 5 - 7 phút)
- [ ] Thiết kế `public/index.html`: Khung nhìn chuẩn 1080x1920 responsive.
- [ ] Viết `public/style.css`: Giao diện phong cách TikTok Live (Neon, độ tương phản cao, chữ to rõ).
- [ ] Viết `public/game.js`:
  - [ ] Lắng nghe Socket.IO sự kiện (`chat`, `gift`, `like`, `gameState`).
  - [ ] Xử lý logic tính điểm, hiệu ứng avatar người chơi, bảng xếp hạng Top Donors.
  - [ ] Tích hợp phát âm thanh TTS khi có quà hoặc chiến thắng.
- [ ] *Checkpoint 3: Báo cáo hoàn thành Phase 3, chờ người dùng duyệt để tích hợp Colab.*

---

### 🔹 PHASE 4: Tích hợp Dual-Mode Colab & Kiểm thử nghiệm thu (Dự kiến: 3 - 5 phút)
- [ ] Viết `run_colab.py`: Khởi chạy Web Server + Cloudflare Tunnel (Cho OBS trên Laptop).
- [ ] Viết `live_ngam_tiktok.py`: Khởi chạy ảo `Xvfb` + Google Chrome + `ffmpeg` RTMP stream thẳng lên TikTok.
- [ ] Kiểm thử chạy thử nghiệm (`npm test` hoặc test server cục bộ) và kiểm tra bảng điều khiển admin.
- [ ] *Checkpoint 4: Báo cáo hoàn thành toàn bộ game, hướng dẫn người dùng chạy trên Colab.*

---

## ⏱️ NHẬT KÝ CHECKPOINT & TIMEBOX (Tối đa 8 phút / lần)

| Lần (Turn) | Thời điểm | Phase thực hiện | Công việc đã hoàn thành | Trạng thái | Ghi chú / Yêu cầu tiếp theo |
|---|---|---|---|---|---|
| Checkpoint 1 | --:-- | Phase 1 | Lập kế hoạch, tạo PROGRESS.md, package.json | ✅ Hoàn thành | Đợi xác nhận từ người dùng để làm Phase 2 |
| Checkpoint 2 | --:-- | Phase 2 | Code server.js và admin.html | ⏳ Chờ lệnh | Sẵn sàng triển khai backend |
| Checkpoint 3 | --:-- | Phase 3 | Code index.html, style.css, game.js | ⏳ Chờ lệnh | Chưa bắt đầu |
| Checkpoint 4 | --:-- | Phase 4 | Colab scripts & nghiệm thu | ⏳ Chờ lệnh | Chưa bắt đầu |

---

## 💬 GHI CHÚ QUYẾT ĐỊNH & THẢO LUẬN
- *(Ghi lại các điều chỉnh luật chơi hoặc ý kiến phản hồi của người dùng tại đây)*
