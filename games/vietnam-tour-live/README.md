# 🇻🇳 GAME TIKTOK LIVE: GHÉ THĂM 63 TỈNH THÀNH VIỆT NAM (VIETNAM TOUR LIVE)

> Game tương tác TikTok Live chuyên nghiệp chuẩn dọc 9:16 (1080 x 1920 px), tích hợp bản đồ số hóa 63 tỉnh thành Việt Nam, camera pan/zoom mượt mà, hệ thống hàng đợi thường & VIP, giọng đọc AI tiếng Việt (TTS) và hỗ trợ chạy 24/7 trên Google Colab.

---

## 🌟 1. CÁC TÍNH NĂNG NỔI BẬT

- 🗺️ **Bản đồ số hóa 63 tỉnh thành & 2 Quần đảo Hoàng Sa, Trường Sa:** Tự động nhận diện ranh giới, đổi màu vàng neon phát sáng rực rỡ khi ghé thăm.
- 🎥 **Động cơ Camera Động (Smooth Pan & Zoom):** Tự động tính toán Bounding Box và lướt mượt mà vào trung tâm từng tỉnh thành khi đến lượt.
- 🗣️ **Giọng đọc tiếng Việt AI (TTS) tích hợp sẵn:** Xướng tên người xem và quê hương tự động không giật lag với bộ đệm MD5 disk-cache.
- ⚡ **Cơ chế Hàng đợi & Monetization chuẩn TikTok:**
  - **Bình luận:** Gõ tên tỉnh (có dấu, không dấu, viết tắt như `sg`, `hn`, `dn`...) -> Xếp vào hàng đợi thường.
  - **Mốc 50 xu (Bắn tim - Đọc nhanh):** Rút ngắn 50% thời gian chờ, ưu tiên trước hàng đợi thường.
  - **Mốc 200 xu (Hoa hồng lớn / Sư tử - Đọc trước):** **VIP Queue Jump**, nhảy thẳng lên vị trí số 1 để ghé thăm ngay lập tức kèm hiệu ứng pháo hoa neon bùng nổ.
  - **Quà nhỏ 1 xu (Hoa hồng):** Cộng điểm danh vọng (`+1`, `+5`) cho tỉnh hiện tại.
- 🎛️ **Bảng giả lập Mock Simulator (`/admin.html`):** Bấm nút thử nghiệm comment, tặng quà, thả tim, next tỉnh ngay trên trình duyệt mà không cần livestream thật.

---

## 🚀 2. HƯỚNG DẪN CHẠY TRÊN MÁY TÍNH CỤC BỘ (LOCAL)

```bash
# 1. Đi tới thư mục game
cd games/vietnam-tour-live

# 2. Cài đặt dependencies
npm install

# 3. Chạy server
npm start
```

- Màn hình Game cho OBS (Browser Source 1080x1920): `http://localhost:3000/index.html`
- Bảng điều khiển giả lập Admin: `http://localhost:3000/admin.html`

---

## ☁️ 3. HƯỚNG DẪN CHẠY TRÊN GOOGLE COLAB

### Chế độ A: Phát qua OBS / TikTok Live Studio (Dùng Cloudflare Tunnel)
```bash
python3 run_colab.py
```
*Hệ thống sẽ in ra đường link HTTPS công khai dạng `https://xxxx.trycloudflare.com/index.html` để dán thẳng vào OBS Browser Source.*

### Chế độ B: Phát ngầm RTMP 24/7 (Rảnh tay, không cần máy tính mở)
```bash
python3 live_ngam_tiktok.py --stream-key "YOUR_TIKTOK_STREAM_KEY" --tiktok-username "@your_username"
```
