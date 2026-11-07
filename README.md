# 🎮 TIKTOK LIVE INTERACTIVE GAME SKILL
> **AI-Ready Framework & Starter Kit chuyên biệt cho Google Antigravity tạo Game TikTok Live tương tác, chạy hoàn hảo trên Google Colab.**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tuna1710/tiktok-live-game-skill/blob/main/run_in_colab.ipynb)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green?logo=nodedotjs)](https://nodejs.org/)
[![Socket.IO](https://img.shields.io/badge/Socket.IO-Realtime-010101?logo=socketdotio)](https://socket.io/)
[![TikTok Live Connector](https://img.shields.io/badge/TikTokLive-Connector-black?logo=tiktok)](https://github.com/zerodytrash/TikTok-Live-Connector)

---

## 🌟 1. GIỚI THIỆU
Repo này là một **"Skill Repository"** chuẩn hóa. Bạn chỉ cần đưa đường dẫn repo này cho **Google Antigravity** (hoặc Claude / Cursor / GPT) kèm theo mô tả ý tưởng trò chơi, AI sẽ đọc hiểu toàn bộ kiến trúc trong file [`SKILL.md`](SKILL.md) và tự động sinh ra mã nguồn một game tương tác hoàn chỉnh, chuẩn kích thước 9:16 và tương thích 100% với Google Colab.

### ✨ Điểm nổi bật:
- ⚡ **Google Antigravity Native:** Cung cấp tài liệu quy chuẩn [`SKILL.md`](SKILL.md) rõ ràng, giúp AI hiểu ngay cấu trúc dự án và sinh code không lỗi.
- 📱 **Chuẩn màn hình dọc 9:16:** Thiết kế tối ưu cho livestream TikTok (1080 x 1920 px), chữ to rõ, đồ họa neon nổi bật.
- 🔄 **Chế độ phát kép (Dual-Mode Colab):**
  - **Chế độ A (OBS Web):** Sinh link Cloudflare Tunnel HTTPS an toàn để dán thẳng vào Browser Source trên OBS Studio / TikTok Live Studio.
  - **Chế độ B (Phát ngầm trực tiếp RTMP - Rảnh tay):** Tự động tạo màn hình ảo `Xvfb` + mở Chrome + dùng `ffmpeg` đẩy luồng RTMP thẳng lên TikTok Live mà không cần mở laptop.
- 🎛️ **Bộ Giả lập sự kiện (Mock Simulator):** Đi kèm `public/admin.html` cho phép kiểm thử comment, tặng quà, thả tim kể cả khi chưa phát sóng trực tiếp.
- 🗣️ **Tích hợp Giọng đọc tiếng Việt (TTS):** Có sẵn endpoint proxy `/api/tts` với bộ đệm MD5 giúp đọc tên người tặng quà mượt mà.
- ⏱️ **Cơ chế chống Timeout Antigravity (Timebox 8 phút):** Tích hợp quy chuẩn chia nhỏ dự án thành 4 Phase độc lập và file theo dõi tiến độ `PROGRESS.md`, loại bỏ hoàn toàn lỗi timeout khi AI sinh code.

---

## 🤖 2. CÁCH SỬ DỤNG VỚI GOOGLE ANTIGRAVITY (CHỐNG TIMEOUT)

Để tránh lỗi **TIMEOUT** do AI cố gắng sinh toàn bộ dự án cùng lúc, hãy sử dụng quy trình **4-Phase & Timebox 8 phút** dưới đây:

### 💬 Bước 1: Khởi động & Lập kế hoạch (Phase 1)
Cung cấp link repo này cho **Google Antigravity** kèm câu lệnh:

```text
Hãy đọc kỹ kiến trúc trong file SKILL.md của repo này.
Tôi muốn làm một Game TikTok Live mới có tên: [Tên trò chơi của bạn]

Mô tả luật chơi:
- Giao diện: [Mô tả hình ảnh, chủ đề game]
- Comment: [Ví dụ: Gõ '1' để chọn phe Đỏ, gõ '2' để chọn phe Xanh]
- Tặng Hoa hồng (1 xu): [Ví dụ: Tăng điểm, triệu hồi lính]
- Tặng quà lớn (>10 xu): [Ví dụ: Triệu hồi Rồng lửa]
- Thả tim: [Ví dụ: Nạp năng lượng]

TUÂN THỦ QUY TẮC CHỐNG TIMEOUT TRONG SKILL.MD:
1. Hãy bắt đầu bằng PHASE 1: Tạo thư mục game, lập file PROGRESS.md chi tiết (mục lục các việc cần làm từ tổng quát đến cụ thể) và package.json.
2. Làm việc tối đa trong 8 phút. Sau khi xong Phase 1 hãy dừng lại, báo cáo tiến độ và CHỜ TÔI ĐỒNG Ý thì mới làm tiếp Phase 2.
```

### 💬 Bước 2, 3, 4: Xác nhận làm tiếp từng Phase
Khi Antigravity báo cáo hoàn thành từng Phase (Phase 1 -> Phase 2 Backend -> Phase 3 Frontend -> Phase 4 Colab), bạn chỉ cần gõ:

```text
Tốt lắm, tôi đồng ý. Hãy tiếp tục làm Phase tiếp theo theo đúng checklist trong PROGRESS.md. Làm xong phase này hãy dừng lại và báo cáo tiếp.
```


---

## 🚀 3. HƯỚNG DẪN CHẠY TRÊN GOOGLE COLAB

Bạn có thể mở trực tiếp file [`run_in_colab.ipynb`](run_in_colab.ipynb) trên Google Colab hoặc chạy thủ công bằng các lệnh sau:

### ⚙️ Bước 1: Chuẩn bị môi trường trên Colab
```bash
!apt-get update -qq && apt-get install -y -qq nodejs npm xvfb ffmpeg pulseaudio
!git clone https://github.com/tuna1710/tiktok-live-game-skill.git
%cd /content/tiktok-live-game-skill/template
```

---

### 🖥️ Bước 2 (Chế độ A): Chạy qua Cloudflare Tunnel cho OBS trên Laptop
Nếu bạn muốn mở giao diện game trên máy tính để tùy biến qua OBS Studio hoặc TikTok Live Studio:

```bash
import os
os.environ['TIKTOK_USERNAME'] = '@your_tiktok_username'  # Điền tài khoản TikTok của bạn
!python3 run_colab.py
```
👉 Terminal sẽ in ra đường dẫn dạng:
- `Màn hình game (OBS): https://xxxx.trycloudflare.com/index.html`
- `Bảng điều khiển giả lập: https://xxxx.trycloudflare.com/admin.html`

Copy link game và dán vào **OBS -> Add Source -> Browser Source** (Đặt kích thước: **1080 x 1920**).

---

### 📡 Bước 2 (Chế độ B): Phát ngầm trực tiếp bằng RTMP (Không cần mở laptop)
Nếu bạn muốn Colab tự động stream thẳng lên TikTok Live:

1. Vào TikTok Live Studio hoặc TikTok Web Live -> Lấy **URL Máy chủ** và **Khóa luồng (Stream Key)**.
2. Chạy lệnh:
```bash
import os
os.environ['TIKTOK_STREAM_KEY'] = 'your_stream_key_here'
os.environ['TIKTOK_USERNAME'] = '@your_tiktok_username'
!python3 live_ngam_tiktok.py
```
🔥 Luồng video 1080x1920 chất lượng cao sẽ được bắn trực tiếp vào kênh TikTok Live của bạn!

---

## 📂 4. CẤU TRÚC REPOSITORY

```text
tiktok-live-game-skill/
├── SKILL.md                   # 🧠 ĐẶC TẢ SKILL DÀNH CHO GOOGLE ANTIGRAVITY
├── README.md                  # Tài liệu hướng dẫn sử dụng
├── requirements.md            # Bảng ghi nhận yêu cầu & kiến trúc đã thống nhất
├── run_in_colab.ipynb         # Sổ tay Colab chạy 1-click
├── .gitignore                 # Bảo mật (loại bỏ token, env, logs)
│
├── template/                  # 📦 STARTER KIT CHUẨN ĐỂ NHÂN BẢN
│   ├── package.json
│   ├── server.js              # Node.js + TikTokLiveConnector + Socket.IO + TTS + REST Mock
│   ├── .env.example
│   ├── run_colab.py           # Chế độ A: OBS Cloudflare Tunnel
│   ├── live_ngam_tiktok.py    # Chế độ B: RTMP Stream ngầm rảnh tay
│   └── public/
│       ├── index.html         # Khung nhìn dọc 9:16
│       ├── style.css          # Giao diện Neon Live
│       ├── game.js            # Engine vòng lặp game + hiệu ứng
│       └── admin.html         # Bảng test sự kiện quà/chat
│
└── games/
    ├── boc-que-dau-nam/       # 🎋 GAME: BỐC QUẺ ĐẦU NĂM (TẾT TRUYỀN THỐNG)
    │   ├── data/que_database.json # Cơ sở dữ liệu quẻ Đại Cát, Thượng Cát
    │   ├── server.js          # Quản lý Hàng đợi VIP & Thường, TTS đọc quẻ
    │   ├── run_colab.py
    │   ├── live_ngam_tiktok.py
    │   └── public/ (index.html, game.js, style.css, admin.html)
    │
    └── battle-red-vs-blue/    # ⚔️ GAME: ĐẠI CHIẾN ĐỎ VS XANH
        ├── server.js          # Cơ chế kéo co 2 phe
        ├── run_colab.py
        ├── live_ngam_tiktok.py
        └── public/ (index.html, game.js, style.css, admin.html)
```

---

## 🎁 5. DANH SÁCH SỰ KIỆN TIKTOK LIVE HỖ TRỢ

| Sự kiện | Tên Event | Mô tả |
|---|---|---|
| **Chat / Comment** | `chat` | Bắt nội dung bình luận, tên người chat và avatar. |
| **Quà tặng (Gift)** | `gift` | Tên quà, số lượng xu (`diamondCount`), số lần combo (`repeatCount`). |
| **Thả tim (Like)** | `like` | Số lượng tim vừa thả và tổng tim phòng Live. |
| **Người vào phòng** | `member` | Chào mừng người xem mới. |
| **Thử nghiệm** | `mock:*` | Giả lập toàn bộ các sự kiện trên qua giao diện `admin.html`. |

---

## 🔒 6. BẢO MẬT & BẢN QUYỀN
- **Tuyệt đối không lưu trữ Tokens / Keys trong mã nguồn.** Mọi khóa luồng và thông tin xác thực đều được truyền qua biến môi trường (`os.environ`).
- Dự án phát triển dựa trên chuẩn mở MIT License. Tự do sáng tạo và triển khai game!
