# 📋 TIẾN ĐỘ DỰ ÁN GAME: GHÉ THĂM 63 TỈNH THÀNH VIỆT NAM (VIETNAM TOUR LIVE)
> **Cơ chế chống Timeout (Timebox 8 phút):** AI tuân thủ quy chuẩn `SKILL.md`, thực hiện từng Phase độc lập. Sau mỗi Phase (hoặc tối đa 8 phút), AI cập nhật file này, dừng lại báo cáo người dùng và chờ lệnh xác nhận tiếp tục.

---

## 📌 THÔNG TIN TỔNG QUAN
- **Tên trò chơi:** Ghé Thăm 63 Tỉnh Thành Việt Nam (Vietnam Tour Live)
- **Tỉ lệ khung hình:** Chuẩn dọc 9:16 (1080 x 1920 px)
- **Cơ chế tương tác:** 
  - Comment tên tỉnh (Chuẩn hóa tiếng Việt có dấu/không dấu/viết tắt) -> Xếp hàng đợi thăm tỉnh
  - Quà tặng Hoa hồng (1 xu) -> +Điểm & popup vinh danh
  - Quà tặng 50 xu (Bắn tim) -> Mốc "Đọc nhanh" (Ưu tiên giảm thời gian chờ)
  - Quà tặng 200 xu (Hoa hồng lớn/Quà VIP) -> Mốc "Đọc trước" (VIP Queue Jump - nhảy lên vị trí số 1 ngay lập tức)
  - Thả tim (Like) -> Tích lũy năng lượng, tăng mục tiêu phòng live
- **Trạng thái hiện tại:** `✅ Hoàn thành Phase 1` (Sẵn sàng Phase 2)
- **Thư mục game:** `games/vietnam-tour-live` (Symlink: `/workspace/vietnam-tour-live`)

---

## 🗺️ MỤC LỤC & CHECKLIST CÔNG VIỆC TỪNG BƯỚC

### 🔹 PHASE 1: Khởi tạo, Đặc tả & Thiết kế Kiến trúc (1 - 2 phút)
- [x] Phân tích chi tiết video thực tế, đặc tả luật chơi và tương tác TikTok Live.
- [x] Khởi tạo thư mục game: `games/vietnam-tour-live/` và symlink `/workspace/vietnam-tour-live`.
- [x] Tạo file cấu hình `package.json` và `.env.example`.
- [x] Thiết lập file `PROGRESS.md` (Checklist chi tiết từ tổng quát đến cụ thể).
- [x] *Checkpoint 1: Báo cáo hoàn thành Phase 1, chờ người dùng duyệt để code Backend.*

---

### 🔹 PHASE 2: Xây dựng Backend & Giả lập Mock API (3 - 5 phút)
- [x] Cài đặt thư viện dependencies Node.js (`express`, `socket.io`, `tiktok-live-connector`, `cors`, `dotenv`).
- [x] Viết `server.js`:
  - [x] Khởi tạo Express & Socket.IO server hỗ trợ CORS.
  - [x] Xây dựng Database dữ liệu 63 Tỉnh Thành Việt Nam (`data/provinces.json` đầy đủ alias viết tắt sg, hcm, hn, dn, vung tau,...).
  - [x] Bộ xử lý chuẩn hóa chuỗi tiếng Việt (loại bỏ dấu, ký tự đặc biệt, regex match tên tỉnh linh hoạt).
  - [x] Quản lý trạng thái Game & Hàng đợi (Queue State Machine):
    - Hàng đợi thường (Normal Queue FIFO).
    - Hàng đợi ưu tiên VIP (VIP Jump Queue khi nhận quà 50 xu / 200 xu).
    - Bộ đếm thời gian lưu lại mỗi tỉnh (mặc định 15s) và tự động chuyển sang tỉnh kế tiếp.
  - [x] Kết nối `TikTokLiveConnection` bắt sự kiện thực tế: `chat`, `gift`, `like`, `member`, `follow`.
  - [x] Tích hợp API proxy TTS tiếng Việt (`/api/tts?text=...`) với MD5 disk-cache chống nghẽn mạng.
  - [x] Tích hợp bộ nhận sự kiện giả lập Mock API: `mock:chat`, `mock:gift`, `mock:like`, `mock:reset`, `mock:next`, `mock:set_province`.
- [x] Viết trang điều khiển giả lập `public/admin.html`:
  - [x] Bảng điều khiển trực quan đầy đủ nút bấm test comment tên tỉnh (Hà Nội, Lào Cai, Tây Ninh, TP.HCM,...).
  - [x] Nút giả lập tặng quà: 1 xu (Hoa hồng), 50 xu (Đọc nhanh), 200 xu (Đọc trước / VIP Jump).
  - [x] Nút test thả tim, test follow, next tỉnh thủ công, reset game.
- [x] *Checkpoint 2: Báo cáo hoàn thành Phase 2, chờ người dùng duyệt để làm Frontend.*

---

### 🔹 PHASE 3: Thiết kế Giao diện 9:16 & Hoạt ảnh Frontend (5 - 7 phút)
- [x] Thiết kế `public/index.html`:
  - [x] Khung nhìn chuẩn 1080x1920 (Fit auto-scale responsive cho mọi màn hình OBS và trình duyệt).
  - [x] Header HUD: Vòng gặp gỡ, đồng hồ live, trạng thái `ĐANG GHÉ THĂM: [Tên Tỉnh]`, đồng hồ đếm ngược 15s.
  - [x] Bảng hướng dẫn quà tặng VIP Perks: 👑 Gõ tên tỉnh | 🫰 50 xu Đọc nhanh | 🌹 200 xu Đọc trước.
  - [x] Thống kê mục tiêu Follower (Progress Circle Widget) và tích lũy người xem.
  - [x] Sân khấu bản đồ: SVG Vector bản đồ 63 tỉnh thành Việt Nam (Hoàng Sa, Trường Sa, Phú Quốc).
  - [x] Queue Bar: Danh sách thẻ tỉnh đang chờ ở phía dưới (`01 Đà Nẵng`, `02 Tây Ninh`...).
  - [x] Popups: Banner vinh danh follow và quà tặng nổi bật.
- [x] Viết `public/style.css`:
  - [x] Dark theme phong cách TikTok Live huyền ảo (Dark Navy / Teal).
  - [x] Hiệu ứng Neon viền sáng cho tỉnh đang thăm (Glow effect, pulse animation).
  - [x] Font chữ to rõ chuẩn UI mobile, không lỗi font tiếng Việt.
- [x] Viết `public/game.js`:
  - [x] Kết nối Socket.IO đồng bộ trạng thái realtime.
  - [x] Hệ thống Camera động (Smooth Pan & Zoom): tính toán Bounding Box của tỉnh được ghé thăm trên SVG và áp dụng CSS transform mượt mà (transition cubic-bezier).
  - [x] Ghim avatar người xem lên vị trí tỉnh trên bản đồ + hiển thị avatar lớn phát sáng phía dưới.
  - [x] Hiệu ứng trượt danh sách hàng đợi (Queue Cards Slider).
  - [x] Tự động phát âm thanh giọng đọc tiếng Việt TTS xướng tên người chơi khi tới tỉnh.
  - [x] Hiệu ứng hạt ánh sáng / pháo hoa neon khi có quà VIP 200 xu.
- [x] *Checkpoint 3: Báo cáo hoàn thành Phase 3, chờ người dùng duyệt để làm Phase 4.*

---

### 🔹 PHASE 4: Tích hợp Dual-Mode Colab & Kiểm thử nghiệm thu (3 - 5 phút)
- [x] Viết `run_colab.py`: Chạy Web Server + Cloudflare Tunnel sinh link HTTPS cho OBS.
- [x] Viết `live_ngam_tiktok.py`: Chạy màn hình ảo `Xvfb` + Google Chrome headless + `ffmpeg` đẩy luồng RTMP trực tiếp lên TikTok.
- [x] Cài đặt gói npm, chạy thử nghiệm server cục bộ và kiểm thử endpoint.
- [x] Viết kịch bản kiểm thử tự động `test_game.js` (Vượt qua 5/5 bài test).
- [x] Viết hướng dẫn sử dụng chi tiết `README.md`.
- [x] *Checkpoint 4: Báo cáo nghiệm thu hoàn tất toàn bộ dự án và bàn giao hướng dẫn.*

---

## ⏱️ NHẬT KÝ CHECKPOINT & TIMEBOX (Tối đa 8 phút / lần)

| Checkpoint | Thời điểm | Phase thực hiện | Công việc đã hoàn thành | Trạng thái | Yêu cầu tiếp theo |
|---|---|---|---|---|---|
| **Checkpoint 1** | Hoàn thành | Phase 1 | Khởi tạo thư mục game, `package.json`, `.env.example`, `PROGRESS.md` | ✅ Hoàn thành | Đã được phê duyệt |
| **Checkpoint 2** | Hoàn thành | Phase 2 | Code `server.js`, `data/provinces.json`, `public/admin.html` | ✅ Hoàn thành | Đã được phê duyệt |
| **Checkpoint 3** | Hoàn thành | Phase 3 | Code `index.html`, `style.css`, `game.js`, tích hợp SVG 63 tỉnh | ✅ Hoàn thành | Đã được phê duyệt |
| **Checkpoint 4** | Hoàn thành | **Phase 4** | Colab scripts (`run_colab.py`, `live_ngam_tiktok.py`), kiểm thử tự động & nghiệm thu | ✅ **HOÀN TẤT DỰ ÁN** | Sẵn sàng đưa vào livestream |

---

## 💬 GHI CHÚ QUYẾT ĐỊNH & CẬP NHẬT MỚI NHẤT
- Game được đặt tên chính thức là: **Ghé Thăm 63 Tỉnh Thành Việt Nam (Vietnam Tour Live)**.
- **Tối ưu hiển thị & Tỉ lệ màn hình:** Căn giữa bản đồ Việt Nam bằng cấu trúc `<g id="mapGroup">` trong SVG với `transform-origin: 0 0`, khắc phục hiện tượng bản đồ bị trượt lệch khỏi khung nhìn khi zoom.
- **Điều chỉnh HUD Perks:** Đã gỡ bỏ các nhãn số (21, 50, 200) ở thanh ưu tiên theo phản hồi từ người dùng, chỉ giữ icon và nội dung quyền lợi trực quan.
- **Cập nhật 34 Đơn vị hành chính cấp tỉnh mới (Nghị quyết 202/2025/QH15):**
  - Tích hợp toàn diện 34 đơn vị hành chính cấp tỉnh mới nhất vào `provinces.json`.
  - Giữ nguyên cơ chế **Smart Mapping tương thích ngược 100%**: Khán giả comment tên tỉnh cũ (ví dụ Bến Tre, Nam Định, Yên Bái, Hải Dương, Bình Dương,...) hệ thống tự động nhận diện và gộp vào tỉnh mới (ví dụ `Bến Tre (Vĩnh Long)`), sáng toàn bộ các vùng hợp nhất trên bản đồ vector.
- Đã cấu hình symlink từ `/workspace/vietnam-tour-live` tới `games/vietnam-tour-live` để quản lý tiện lợi.

