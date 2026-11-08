# 📋 TIẾN ĐỘ DỰ ÁN GAME: RUNG CHUÔNG VÀNG TIKTOK LIVE
> **Cơ chế chống Timeout (Timebox 8 phút):** AI thực hiện từng Phase độc lập. Sau mỗi Phase (hoặc tối đa 8 phút), AI cập nhật file này, báo cáo người dùng và đợi lệnh tiếp tục.

---

## 📌 THÔNG TIN TỔNG QUAN
- **Tên trò chơi:** Rung Chuông Vàng TikTok Live (Golden Bell Interactive)
- **Tỉ lệ khung hình:** Dọc 9:16 (1080 x 1920 px)
- **Cơ chế tương tác:**
  - **Bình luận (Chat):** Tham gia sàn đấu, trả lời trắc nghiệm (`A`, `B`, `C`, `D` hoặc `1`, `2`, `3`, `4`).
  - **Quà tặng (Gift):** 
    - Tặng Hoa Hồng / Quà bất kỳ (>= 1 xu): Hồi sinh tức thì khi bị loại.
    - Tặng Quà VIP (>= 100 xu): Cứu trợ khẩn cấp toàn bộ sàn đấu hồi sinh.
  - **Thả tim (Like):** Tích lũy vào "Bình Năng Lượng Cứu Trợ". Đạt 1.000 tim tự động cứu ngẫu nhiên 3 người bị loại.
- **Mục tiêu người chơi:** Sống sót và vượt qua câu hỏi số 20 (hoặc câu cuối cùng) để bước lên bục **Rung Chuông Vàng**.
- **Trạng thái hiện tại:** `✅ Hoàn thành xuất sắc toàn bộ 4 Phase`
- **Khởi tạo lúc:** 2026-11-07
- **Cập nhật lần cuối:** 2026-11-07

---

## 🗺️ MỤC LỤC & CHECKLIST CÔNG VIỆC TỪNG BƯỚC

### 🔹 PHASE 1: Khởi tạo, Đặc tả & Thiết kế Kiến trúc (Dự kiến: 1 - 2 phút)
- [x] Phân tích luật chơi: Trả lời trắc nghiệm, bị loại khi sai, sống sót đến câu cuối để Rung Chuông Vàng.
- [x] Thiết lập file `PROGRESS.md` (Checklist chi tiết từ tổng quát đến cụ thể).
- [x] Khởi tạo thư mục dự án `games/rung-chuong-vang` và file cấu hình `.env.example`, `package.json`.
- [x] *Checkpoint 1: Báo cáo hoàn thành Phase 1, chờ người dùng duyệt để code Backend.*

---

### 🔹 PHASE 2: Xây dựng Backend & Giả lập Mock API (Dự kiến: 3 - 5 phút)
- [x] Cài đặt dependencies (`express`, `socket.io`, `tiktok-live-connector`, `cors`, `dotenv`).
- [x] Tạo file ngân hàng câu hỏi `data/questions.json` (chứa 20+ câu hỏi trắc nghiệm tiếng Việt phong phú, phân loại độ khó).
- [x] Viết `server.js`:
  - [x] Khởi tạo HTTP & Socket.IO server.
  - [x] Xây dựng Game Manager (Quản lý trạng thái sàn đấu, vòng câu hỏi, đếm ngược, chấm điểm, cứu trợ).
  - [x] Kết nối `TikTokLiveConnection` bắt sự kiện `chat`, `gift`, `like`, `member`.
  - [x] Tích hợp API proxy TTS tiếng Việt (`/api/tts`) đọc câu hỏi và đọc tên người thắng/hồi sinh.
  - [x] Tích hợp bộ nhận sự kiện giả lập: `mock:chat`, `mock:gift`, `mock:like`, `mock:start_game`, `mock:next_question`, `mock:reset_game`, `mock:rescue_all`, `mock:add_bots`, `mock:bots_answer`.
- [x] Viết trang điều khiển giả lập `public/admin.html` để kiểm thử toàn diện mọi tình huống.
- [x] *Checkpoint 2: Báo cáo hoàn thành Phase 2, chờ người dùng duyệt để làm Frontend.*

---

### 🔹 PHASE 3: Thiết kế Giao diện 9:16 & Hoạt ảnh Frontend (Dự kiến: 5 - 7 phút)
- [x] Thiết kế `public/index.html`: Khung nhìn chuẩn 1080x1920 dọc, tối ưu cho OBS / màn hình live.
- [x] Viết `public/style.css`: Giao diện phong cách gameshow Rung Chuông Vàng (Màu vàng kim / Đỏ hoàng gia, hiệu ứng neon rực rỡ, chữ to dễ đọc).
- [x] Viết `public/game.js`:
  - [x] Lưới sàn đấu 100 vị trí (Arena Grid) hiển thị Avatar + Tên người chơi sống sót / bị loại.
  - [x] Hoạt ảnh: Thí sinh rơi vào sàn, chọn đáp án A/B/C/D, hiệu ứng sét đánh khi bị loại, lửa hồi sinh khi được cứu.
  - [x] Hoạt cảnh đỉnh cao: Bục vinh danh và hiệu ứng lắc Chuông Vàng cực mạnh với pháo hoa ngập tràn khi có người chiến thắng.
  - [x] Âm thanh kịch tính (tiếng đếm ngược, chuông reo, tiếng sét, nhạc chúc mừng) + TTS giọng đọc tiếng Việt.
  - [x] Bảng xếp hạng Top Thần Đồng & Top Nhà Cứu Trợ.
- [x] *Checkpoint 3: Báo cáo hoàn thành Phase 3, chờ người dùng duyệt để tích hợp Colab.*

---

### 🔹 PHASE 4: Tích hợp Dual-Mode Colab & Kiểm thử nghiệm thu (Dự kiến: 3 - 5 phút)
- [x] Viết `run_colab.py`: Khởi chạy Web Server + Cloudflare Tunnel (Cho OBS trên Laptop).
- [x] Viết `live_ngam_tiktok.py`: Khởi chạy ảo `Xvfb` + Google Chrome 1080x1920 + `ffmpeg` RTMP stream thẳng lên TikTok Live.
- [x] Kiểm thử kiểm tra syntax Node.js và chạy thử nghiệm server.
- [x] *Checkpoint 4: Báo cáo hoàn thành toàn bộ game, hướng dẫn người dùng chạy trên Colab.*

---

## ⏱️ NHẬT KÝ CHECKPOINT & TIMEBOX (Tối đa 8 phút / lần)

| Lần (Turn) | Thời điểm | Phase thực hiện | Công việc đã hoàn thành | Trạng thái | Ghi chú / Yêu cầu tiếp theo |
|---|---|---|---|---|---|
| Checkpoint 1 | 2026-11-07 | Phase 1 | Lập kế hoạch chi tiết, tạo PROGRESS.md, package.json, .env.example | ✅ Hoàn thành | Đợi xác nhận từ người dùng để làm Phase 2 |
| Checkpoint 2 | 2026-11-07 | Phase 2 | Code server.js, data/questions.json và public/admin.html | ✅ Hoàn thành | Đợi xác nhận từ người dùng để làm Phase 3 |
| Checkpoint 3 | 2026-11-07 | Phase 3 | Code index.html, style.css, game.js hoạt ảnh 100 thí sinh | ✅ Hoàn thành | Đợi xác nhận từ người dùng để làm Phase 4 |
| Checkpoint 4 | 2026-11-07 | Phase 4 | Tạo run_colab.py, live_ngam_tiktok.py & kiểm thử nghiệm thu 100% | ✅ Hoàn thành | Toàn bộ dự án đã sẵn sàng bàn giao |

---

## 💬 GHI CHÚ QUYẾT ĐỊNH & THẢO LUẬN
- **Quyết định ngày 2026-11-07:** Thống nhất chọn mục tiêu: *"Sống sót đến câu hỏi cuối cùng để Rung Chuông Vàng"*. Tích hợp vòng Cứu trợ bằng Tim và Quà tặng Hoa hồng khi số lượng thí sinh trên sàn bị loại nhiều hoặc về 0.
- **Kế hoạch mở rộng kho câu hỏi (265 -> 10.000 câu):** Xem chi tiết tại `QUESTION_ROADMAP.md`. Đợt 2 đặt mục tiêu nâng tổng số câu hỏi từ 265 lên mốc 500 câu.
