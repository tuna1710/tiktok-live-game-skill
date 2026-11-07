# 📋 TIẾN ĐỘ DỰ ÁN GAME: BỐC QUẺ ĐẦU NĂM
> **Trạng thái:** ✅ Đã hoàn thành 100%

---

## 📌 THÔNG TIN TỔNG QUAN
- **Tên trò chơi:** Bốc Quẻ Đầu Năm (VIP Priority Queue & TTS)
- **Tỉ lệ khung hình:** Dọc 9:16 (1080 x 1920 px)
- **Cơ chế tương tác:** 
  - Comment: `xin que` hoặc `que` để vào hàng đợi thường.
  - Gift: Tặng hoa hồng hoặc bất kỳ quà nào để vào **Hàng đợi VIP (ưu tiên bốc trước)**.
  - TTS: Tự động xướng tên và đọc thơ quẻ đầu năm.
- **Trạng thái hiện tại:** `Hoàn thành nghiệm thu (All Phases Done)`

---

## 🗺️ MỤC LỤC & CHECKLIST CÔNG VIỆC TỪNG BƯỚC

### 🔹 PHASE 1: Khởi tạo, Đặc tả & Thiết kế Kiến trúc
- [x] Lập kế hoạch cơ chế 2 hàng đợi: Regular Queue & VIP Priority Queue.
- [x] Soạn thảo cơ sở dữ liệu 20 quẻ thơ may mắn (`data/que_database.json`).
- [x] Tạo file cấu hình `package.json`, `.env.example`.

### 🔹 PHASE 2: Xây dựng Backend & Giả lập Mock API
- [x] Viết `server.js` tích hợp TikTokLive connector, WebSocket hàng đợi, TTS proxy tiếng Việt.
- [x] Viết `public/admin.html` cho phép giả lập comment bốc quẻ thường, tặng quà VIP, xóa hàng đợi.

### 🔹 PHASE 3: Thiết kế Giao diện 9:16 & Hoạt ảnh Frontend
- [x] Thiết kế `public/index.html` với tỉ lệ dọc 9:16, ống xăm lộc và thẻ tre phát sáng.
- [x] Viết `public/style.css` phong cách Tết cổ truyền rực rỡ, chữ to dễ đọc trên điện thoại.
- [x] Viết `public/game.js` xử lý rút thẻ tre, lật mở quẻ, âm thanh TTS và chuyển tiếp người tiếp theo trong hàng đợi.

### 🔹 PHASE 4: Tích hợp Dual-Mode Colab & Kiểm thử
- [x] Viết `run_colab.py` mở Cloudflare Tunnel cho OBS.
- [x] Viết `live_ngam_tiktok.py` phát ngầm RTMP qua màn hình ảo Xvfb + ffmpeg.
- [x] Kiểm thử toàn diện flow hàng đợi và TTS.

---

## ⏱️ NHẬT KÝ CHECKPOINT & TIMEBOX
| Lần (Turn) | Phase thực hiện | Công việc đã hoàn thành | Trạng thái |
|---|---|---|---|
| Checkpoint 1 | Phase 1 | Cấu trúc dữ liệu quẻ thơ, package.json | ✅ Hoàn thành |
| Checkpoint 2 | Phase 2 | Backend server.js & trang admin.html | ✅ Hoàn thành |
| Checkpoint 3 | Phase 3 | Frontend giao diện Tết 9:16 & logic game.js | ✅ Hoàn thành |
| Checkpoint 4 | Phase 4 | Colab scripts và test nghiệm thu | ✅ Hoàn thành |
