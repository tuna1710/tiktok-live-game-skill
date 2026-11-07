# YÊU CẦU & THIẾT KẾ DỰ ÁN: TIKTOK LIVE GAME SKILL
*(Tài liệu ghi nhận yêu cầu và đặc tả hệ thống cho Google Antigravity & AI Agents)*

## 1. Mục tiêu dự án
Xây dựng một **Skill / Framework** chuẩn hóa để đưa lên GitHub. Repo này đóng vai trò là "bộ chỉ dẫn và khung mẫu" (AI-Ready Skill & Starter Kit) để khi người dùng cung cấp repo cho **Google Antigravity** kèm theo mô tả ý tưởng (ví dụ: *Làm game thả bóng Plinko, hoặc Đua xe đối kháng bằng quà tặng*), AI Antigravity có thể đọc hiểu toàn bộ quy tắc, cấu trúc và tự động sinh ra game hoàn chỉnh hoạt động mượt mà.

---

## 2. Thông số kỹ thuật & Loại hình game
- **Loại hình:** TikTok Live Interactive Game (Game tương tác màn hình dọc 9:16).
- **Cơ chế tương tác:** Người xem livestream tương tác trực tiếp qua:
  - **Comment:** Gõ đáp án, chọn đội, bình chọn, spam lệnh...
  - **Gift (Quà tặng):** Tặng hoa hồng, tim, quà đặc biệt để kích hoạt vật phẩm, tăng điểm, triệu hồi hiệu ứng...
  - **Like / Follow / Share:** Tăng tốc độ, mở khóa mốc thưởng...
- **Môi trường chạy:** Google Colab (CPU hoặc T4 GPU), tối ưu tài nguyên nhẹ nhàng, ổn định.

---

## 3. Kiến trúc hệ thống (Được tối ưu từ Game mẫu `vua-tieng-viet`)
Dự án áp dụng kiến trúc **Web HTML5 + Node.js Backend + Colab Python Runner**:
1. **Backend:** Node.js (`express`, `socket.io`, `tiktok-live-connector`).
   - Kết nối tới TikTok Live thông qua TikTok username hoặc TikTok Session ID.
   - Bắt các sự kiện Webcast (Gift, Chat, Like, Member).
   - Quản lý trạng thái game, phòng chơi, tính điểm, phát âm thanh TTS qua Google Translate TTS proxy.
2. **Frontend:** HTML5 / CSS3 / JavaScript (Canvas hoặc DOM).
   - Tối ưu chuẩn hiển thị dọc 9:16 (1080 x 1920) phù hợp cho màn hình điện thoại TikTok.
   - Nhận sự kiện thời gian thực qua Socket.IO để cập nhật đồ họa, hiệu ứng và bảng xếp hạng.
3. **Môi trường vận hành kép (Dual-Mode Colab):**
   - **Chế độ A (Web / OBS):** Colab mở Web Server + tạo Cloudflare Tunnel công khai (`run_colab.py`). Người dùng copy link vào OBS Browser Source hoặc TikTok Live Studio trên laptop.
   - **Chế độ B (Phát ngầm trực tiếp RTMP - Rảnh tay):** Colab tự khởi chạy màn hình ảo `Xvfb` + mở Google Chrome toàn màn hình + dùng `ffmpeg` thu màn hình và stream trực tiếp bằng RTMP Stream Key lên TikTok Live mà không cần mở laptop (`live_ngam_tiktok.py`).

---

## 4. Công cụ hỗ trợ bắt buộc
- **Mock / Simulator Panel (`admin.html`):** Giao diện điều khiển giả lập sự kiện (bấm nút để gửi comment thử nghiệm, tặng quà giả lập) giúp kiểm tra game ngay trong Colab kể cả khi chưa bật Live TikTok thật.
- **Tài liệu Skill cho AI Antigravity (`SKILL.md` / `PROMPT_GUIDE.md`):** Quy định rõ:
  - Cấu trúc thư mục chuẩn của mỗi game mới.
  - Các sự kiện Socket.IO chuẩn.
  - Quy chuẩn kích thước giao diện 9:16, màu sắc, font chữ hỗ trợ tiếng Việt.
  - Hướng dẫn step-by-step để AI tạo game mới mà không bị lỗi.

---

## 5. Tham chiếu
- Repository tham khảo: `https://github.com/tuna1710/TikTok-Live-Interactive-Game` (Đặc biệt là game `vua-tieng-viet` và script phát ngầm `live_ngam_youtube.py`).
