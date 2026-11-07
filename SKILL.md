# SKILL: TIKTOK LIVE INTERACTIVE GAME GENERATOR (GOOGLE ANTIGRAVITY)

> **Mục tiêu của Skill:** Hướng dẫn AI (Google Antigravity / Claude / GPT / Cursor) tự động thiết kế, lập trình và xuất ra một Game tương tác TikTok Live (TikTok Live Interactive Game) hoàn chỉnh, chạy được ngay trên Google Colab với cả 2 chế độ: OBS Web Source và Phát ngầm trực tiếp RTMP.

---

## 1. VAI TRÒ CỦA AI (ROLE DEFINITION)
Khi người dùng yêu cầu làm một game TikTok Live (ví dụ: *"Làm game đập bóng Plinko"*, *"Làm game đua xe Đỏ vs Xanh"*, *"Làm game giải đố chữ"*), AI Antigravity sẽ đóng vai trò là một **Kỹ sư Game Web & TikTok Live Full-Stack**.

AI phải tuân thủ nghiêm ngặt:
1. **Kiến trúc chuẩn:** Frontend Web (HTML5 Canvas/CSS) + Backend Node.js (`express`, `socket.io`, `tiktok-live-connector`) + Colab Runner kép (`run_colab.py` và `live_ngam_tiktok.py`).
2. **Kích thước chuẩn TikTok:** Giao diện thiết kế theo **tỉ lệ dọc 9:16 (1080 x 1920 px)**, tự động co giãn vừa khung hình (responsive fit).
3. **Chế độ phát:**
   - **Mode A (OBS / Studio):** Chạy `run_colab.py` -> sinh link Cloudflare Tunnel HTTPS -> Streamer dán vào OBS Browser Source.
   - **Mode B (Live ngầm RTMP - Rảnh tay):** Chạy `live_ngam_tiktok.py` -> khởi tạo màn hình ảo `Xvfb` + mở Chrome fullscreen + dùng `ffmpeg` đẩy luồng RTMP thẳng lên TikTok Live bằng Stream URL & Stream Key.
4. **Luôn có bộ Giả lập (Mock Admin Panel):** File `public/admin.html` cho phép bấm nút gửi comment, thả tim, tặng quà thử nghiệm mà không cần live thật.

---

## 2. QUY CHUẨN CẤU TRÚC THƯ MỤC CỦA MỖI DỰ ÁN GAME
Mỗi khi AI tạo ra một game mới, AI phải tổ chức đúng cấu trúc sau:

```text
my-tiktok-game/
├── PROGRESS.md                # [BẮT BUỘC] Bảng mục lục tiến độ, checklist chống timeout 8 phút
├── package.json               # Cấu hình dự án & thư viện Node.js
├── server.js                  # Backend: TikTokLive connector, WebSocket, TTS proxy, Mock API
├── .env.example               # Mẫu biến môi trường (TIKTOK_USERNAME, PORT, ...)
├── run_colab.py               # Chạy trên Colab với Cloudflare Tunnel (Cho OBS)
├── live_ngam_tiktok.py        # Chạy trên Colab phát ngầm RTMP (Không cần máy tính)
└── public/
    ├── index.html             # Màn hình game chính (Tỉ lệ 9:16)
    ├── style.css              # Giao diện phong cách Live rực rỡ, độ tương phản cao
    ├── game.js                # Logic game, hoạt ảnh Canvas, xử lý Socket.IO
    ├── admin.html             # Bảng điều khiển giả lập sự kiện (Mock Simulator)
    └── assets/                # (Tùy chọn) Âm thanh, hình ảnh, icon
```

---

## 3. ĐẶC TẢ SỰ KIỆN TIKTOK LIVE (SOCKET.IO EVENTS)

Server và Client giao tiếp với nhau qua **Socket.IO** bằng các sự kiện chuẩn sau:

### 3.1. Sự kiện từ TikTok Live tới Client (`server.js` -> `game.js`)
| Sự kiện | Dữ liệu truyền (Payload) | Ý nghĩa & Cách ứng dụng |
|---|---|---|
| `chat` | `{ uniqueId, nickname, comment, profilePictureUrl }` | Người xem bình luận. Dùng để gõ lệnh, đoán chữ, chọn đội (`1` hoặc `2`). |
| `gift` | `{ uniqueId, nickname, giftId, giftName, diamondCount, repeatCount, profilePictureUrl }` | Người xem tặng quà. Dùng để cộng điểm lớn, triệu hồi quái, kích hoạt tuyệt chiêu, thả bóng... |
| `like` | `{ uniqueId, nickname, likeCount, totalLikes }` | Người xem thả tim. Dùng để tích lũy năng lượng, tăng tốc độ nhân vật. |
| `member` | `{ uniqueId, nickname }` | Người mới vào phòng livestream. Hiển thị chào mừng. |
| `gameState` | `{ ...toàn bộ trạng thái game hiện tại... }` | Đồng bộ dữ liệu khi client kết nối lại. |
| `playTts` | `{ text, audioUrl }` | Phát giọng đọc thông báo hoặc chúc mừng. |

### 3.2. Sự kiện từ Bộ Giả Lập (`admin.html` -> `server.js`)
- `mock:chat`: Gửi bình luận giả lập.
- `mock:gift`: Gửi quà tặng giả lập (Hoa hồng, Trái tim, Pháo hoa, Sư tử...).
- `mock:like`: Gửi lượt thả tim giả lập.
- `game:reset`: Đặt lại ván chơi mới.

---

## 4. QUY TẮC THIẾT KẾ GIAO DIỆN & GAMEPLAY (UI/UX GUIDELINES)

1. **Khung nhìn cố định 9:16:**
   - Dùng container chính có kích thước logic: `1080px x 1920px`.
   - Căn giữa màn hình bằng CSS `transform: scale(calc(...))` hoặc `object-fit: contain` để vừa vặn trên mọi độ phân giải trình duyệt hoặc OBS.
2. **Độ tương phản và kích thước chữ:**
   - Người xem TikTok xem trên điện thoại với màn hình nhỏ, do đó:
     - Font chữ tiêu đề và điểm số tối thiểu 36px - 60px, in đậm.
     - Màu sắc: Nền tối (Dark theme: `#0d0f17`, `#16192b`) kết hợp màu Neon nổi bật (Vàng `#ffd700`, Đỏ `#ff3b5c`, Xanh Neon `#00f2fe`).
     - Hỗ trợ đầy đủ tiếng Việt không lỗi font (sử dụng font hệ thống `system-ui, sans-serif` hoặc Google Fonts `Be Vietnam Pro`).
3. **Phản hồi tức thì (Instant Feedback):**
   - Khi có quà tặng hoặc comment đúng: Phải có hiệu ứng visual nổi bật ngay lập tức (Floating avatar, nổ hạt particle, chữ nhảy số).
   - Tích hợp giọng đọc TTS tiếng Việt thông qua endpoint `/api/tts?text=...` để đọc tên người tặng quà (tăng kích thích tương tác).
4. **Bảng xếp hạng (Top Donors / Top Scorers):**
   - Luôn dành góc trên hoặc góc dưới để vinh danh Top 3 hoặc Top 5 người đóng góp nhiều nhất.

---

## 5. BỘ MÃ NGUỒN MẪU CHUẨN (RECIPE CODE)

Khi AI Antigravity sinh mã nguồn cho một game mới, hãy tuân thủ các đoạn mã nền tảng sau:

### 5.1. `package.json`
```json
{
  "name": "my-tiktok-game",
  "version": "1.0.0",
  "description": "TikTok Live Interactive Game for Colab",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "dotenv": "^16.4.5",
    "express": "^4.19.2",
    "socket.io": "^4.7.5",
    "tiktok-live-connector": "^1.1.8"
  }
}
```

### 5.2. `server.js` (Kết nối TikTok, Socket.IO & Mock Engine)
```javascript
require('dotenv').config();
const path = require('path');
const http = require('http');
const express = require('express');
const cors = require('cors');
const { Server } = require('socket.io');
const { TikTokLiveConnection } = require('tiktok-live-connector');

const PORT = Number(process.env.PORT) || 3000;
const TIKTOK_USERNAME = process.env.TIKTOK_USERNAME || '';

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

// TTS Proxy tiếng Việt
app.get('/api/tts', (req, res) => {
  const text = (req.query.text || '').toString().trim().slice(0, 150);
  if (!text) return res.status(400).send('Missing text');
  const googleTtsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=vi&client=tw-ob&q=${encodeURIComponent(text)}`;
  res.redirect(googleTtsUrl);
});

// Kết nối TikTok Live
let tiktokLive = null;
if (TIKTOK_USERNAME) {
  try {
    tiktokLive = new TikTokLiveConnection(TIKTOK_USERNAME);
    tiktokLive.connect()
      .then(state => console.log(`Connected to TikTok Live: ${state.roomId}`))
      .catch(err => console.log(`TikTokLive error: ${err.message}`));

    tiktokLive.on('chat', data => {
      io.emit('chat', {
        uniqueId: data.uniqueId,
        nickname: data.nickname,
        comment: data.comment,
        profilePictureUrl: data.profilePictureUrl
      });
    });

    tiktokLive.on('gift', data => {
      io.emit('gift', {
        uniqueId: data.uniqueId,
        nickname: data.nickname,
        giftId: data.giftId,
        giftName: data.giftName,
        diamondCount: data.diamondCount,
        repeatCount: data.repeatCount,
        profilePictureUrl: data.profilePictureUrl
      });
    });

    tiktokLive.on('like', data => {
      io.emit('like', {
        uniqueId: data.uniqueId,
        nickname: data.nickname,
        likeCount: data.likeCount,
        totalLikes: data.totalLikes
      });
    });
  } catch (e) {
    console.error('Failed to init TikTokLive:', e);
  }
}

// Xử lý sự kiện giả lập từ admin.html
io.on('connection', socket => {
  socket.on('mock:chat', data => io.emit('chat', data));
  socket.on('mock:gift', data => io.emit('gift', data));
  socket.on('mock:like', data => io.emit('like', data));
});

server.listen(PORT, () => {
  console.log(`Game server running on http://localhost:${PORT}`);
});
```

---

## 6. PROTOCOL BẮT BUỘC: CHIA NHỎ CÔNG VIỆC & CHECKPOINT 8 PHÚT (CHỐNG TIMEOUT)

> ⚠️ **CẢNH BÁO NGUY HIỂM VỀ TIMEOUT:**  
> Autonomous Agent (Google Antigravity) thường gặp lỗi **TIMEOUT** nếu cố gắng viết toàn bộ game (8-10 file mã nguồn) trong 1 lượt duy nhất.  
> **QUY TẮC BẮT BUỘC:** AI **TUYỆT ĐỐI KHÔNG** được tạo toàn bộ dự án trong 1 lượt chạy. Phải tuân thủ nghiêm ngặt **Protocol 4-Phase & Timebox 8 phút** dưới đây.

### ⏱️ Cơ chế Timebox 8 Phút & Checkpoint:
- **Ngưỡng thời gian:** Mỗi phiên làm việc của AI chỉ được kéo dài **tối đa 8 phút** (tương đương 1 Phase cụ thể).
- **File điều hướng `PROGRESS.md`:** AI phải tạo file này ngay ở Phase 1 và liên tục cập nhật checklist sau mỗi hành động.
- **Dừng lại & Báo cáo:** Sau khi hoàn thành xong 1 Phase (hoặc khi đã làm gần 8 phút), AI **BẮT BUỘC PHẢI DỪNG LẠI**, xuất báo cáo tóm tắt tiến độ, và **chờ người dùng gửi lệnh xác nhận** (`"Tiếp tục"`, `"Làm tiếp"`) mới được làm Phase tiếp theo.

### 📋 4 Phase Chuẩn Hóa:

#### 🔹 PHASE 1: Khởi tạo, Đặc tả & Mục lục công việc (`PROGRESS.md`) (1 - 2 phút)
1. Tạo thư mục game mới.
2. Tạo file `PROGRESS.md` dựa theo `template/PROGRESS.md`: liệt kê chi tiết mục lục các việc cần làm từ tổng quát đến chi tiết (các file sẽ tạo, tính năng cụ thể).
3. Tạo file `package.json` và `.env.example`.
4. **DỪNG LẠI & BÁO CÁO:** Thông báo cho người dùng: *"Đã hoàn thành Phase 1 (Đặc tả & Mục lục PROGRESS.md). Xin lệnh 'Tiếp tục' để bắt đầu Phase 2 (Backend Node.js & Mock Admin)"*.

#### 🔹 PHASE 2: Xây dựng Backend & Giả lập Mock API (3 - 5 phút)
1. Viết `server.js` (Kết nối Socket.IO, TikTokLiveConnector, API TTS `/api/tts`, sự kiện mock).
2. Viết `public/admin.html` (Bảng giả lập comment, gift, like đầy đủ nút bấm để test độc lập).
3. Cập nhật `[x]` vào `PROGRESS.md`.
4. **DỪNG LẠI & BÁO CÁO:** Thông báo cho người dùng: *"Đã hoàn thành Phase 2 (Backend & Mock Simulator). Xin lệnh 'Tiếp tục' để bắt đầu Phase 3 (Frontend 9:16 & Hoạt ảnh)"*.

#### 🔹 PHASE 3: Thiết kế Giao diện 9:16 & Hoạt ảnh Frontend (5 - 7 phút)
1. Viết `public/index.html` (Khung nhìn chuẩn 1080x1920 dọc).
2. Viết `public/style.css` (Màu sắc neon, chữ to, hiệu ứng rung lắc/phát sáng).
3. Viết `public/game.js` (Xử lý Socket.IO, hoạt ảnh Canvas/DOM, âm thanh TTS, bảng xếp hạng).
4. Cập nhật `[x]` vào `PROGRESS.md`.
5. **DỪNG LẠI & BÁO CÁO:** Thông báo cho người dùng: *"Đã hoàn thành Phase 3 (Giao diện & Logic Game). Xin lệnh 'Tiếp tục' để bắt đầu Phase 4 (Runner Colab & Nghiệm thu)"*.

#### 🔹 PHASE 4: Tích hợp Dual-Mode Colab & Kiểm thử nghiệm thu (3 - 5 phút)
1. Tạo `run_colab.py` (Cloudflare Tunnel cho OBS Laptop).
2. Tạo `live_ngam_tiktok.py` (Xvfb + Chrome + FFmpeg RTMP phát ngầm).
3. Kiểm thử cú pháp server, đảm bảo không có file nào bị lỗi import.
4. Cập nhật hoàn tất `[x]` vào `PROGRESS.md`.
5. **HOÀN TẤT & BÀN GIAO:** Báo cáo toàn bộ project đã hoàn thành và hướng dẫn người dùng chạy thử.

---

## 7. HƯỚNG DẪN PROMPT MẪU CHO NGƯỜI DÙNG KHI GỌI GOOGLE ANTIGRAVITY

Để tránh bị timeout, người dùng hãy sử dụng chuỗi Prompt từng bước như sau:

### 💬 Prompt Bước 1: Khởi động dự án & Lập kế hoạch (Phase 1)
```text
Hãy đọc kỹ kiến trúc trong file SKILL.md của repo này.
Tôi muốn làm một Game TikTok Live mới có tên: [Tên Game của bạn].
Mô tả luật chơi:
- Giao diện: [Mô tả chủ đề, phong cách]
- Comment: [Luật khi comment]
- Quà tặng (Hoa hồng / Quà VIP): [Luật khi tặng quà]
- Thả tim: [Tác dụng khi thả tim]

TUÂN THỦ QUY TẮC CHỐNG TIMEOUT:
1. Hãy bắt đầu bằng PHASE 1: Tạo thư mục game, lập file PROGRESS.md chi tiết (mục lục các việc cần làm từ tổng quát đến cụ thể) và package.json.
2. Làm việc tối đa trong 8 phút. Sau khi xong Phase 1 hãy dừng lại, báo cáo tiến độ và CHỜ TÔI ĐỒNG Ý thì mới làm tiếp Phase 2.
```

### 💬 Prompt Bước 2, 3, 4: Phê duyệt làm tiếp
```text
Tốt lắm, tôi đồng ý. Hãy tiếp tục làm Phase tiếp theo theo đúng checklist trong PROGRESS.md. Làm xong phase này hãy dừng lại và báo cáo tiếp.
```
