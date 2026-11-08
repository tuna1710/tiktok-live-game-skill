# 🗺️ KẾ HOẠCH MỞ RỘNG KHO CÂU HỎI RUNG CHUÔNG VÀNG (265 -> 10.000 CÂU)

> **Mục tiêu:** Xây dựng bách khoa toàn thư tri thức tương tác đa dạng, hấp dẫn cho TikTok Live, tối ưu nhịp độ gameshow Đấu Trí Trạng Nguyên / Rung Chuông Vàng.
> **Khởi tạo:** 2026-11-07 | Cập nhật định kỳ sau mỗi đợt sinh câu hỏi.

---

## 📌 1. NGUYÊN TẮC VÀ QUY CHUẨN BIÊN SOẠN
- **Định dạng chuẩn:** Mỗi câu hỏi có đúng 4 lựa chọn `options`, chỉ số `correct` (0..3), `difficulty` (1: Dễ, 2: Trung bình, 3: Khó), và `explanation` súc tích (1-2 câu để MC AI đọc giải thích).
- **Phân bổ độ khó:**
  - Cấp 1 (Dễ): ~30% (Khuấy động không khí, giữ số lượng thí sinh trên sàn).
  - Cấp 2 (Trung bình): ~40% (Thử thách tư duy, phân hóa thí sinh).
  - Cấp 3 (Khó / Quyết định): ~30% (Phân định danh hiệu Trạng Nguyên / Rung Chuông Vàng).
- **Quy trình kiểm soát chất lượng (Auto-Pipeline):**
  1. Chuẩn hóa chuỗi văn bản (`normalize_text`) và loại bỏ trùng lặp qua SQLite `UNIQUE normalized`.
  2. Chạy `node scripts/manage_questions.js lint` kiểm tra 100% cú pháp.
  3. Đồng bộ hai chiều song song giữa SQLite `questions.db` và JSON modular `data/categories/*.json` & `data/questions.json`.

---

## 📚 2. CẤU TRÚC 6 CHỦ ĐỀ CHỦ ĐẠO
1. 💡 `do-vui-tri-tue`: Đố mẹo dân gian, đố chữ, tư duy logic hài hước, phản xạ nhanh cho TikTok Live.
2. 🏛️ `lich-su`: Lịch sử Việt Nam qua các triều đại (Hùng Vương, Lý, Trần, Lê, Nguyễn...), danh tướng anh hùng và lịch sử thế giới kinh điển.
3. 🗺️ `dia-ly`: Địa lý 63 tỉnh thành, danh lam thắng cảnh, di sản văn hóa, biển đảo quê hương, núi đèo, sông hồ.
4. 🔬 `khoa-hoc-tu-nhien`: Thiên văn học, vũ trụ, vật lý, hóa học, sinh học kỳ thú, cơ thể con người.
5. 📖 `van-hoc-nghe-thuat`: Ca dao tục ngữ, thành ngữ, cổ tích, tác phẩm văn học kinh điển, âm nhạc, nghệ thuật truyền thống.
6. 📱 `doi-song-cong-nghe`: Công nghệ thông tin, trí tuệ nhân tạo (AI), điện thoại thông minh, ẩm thực 3 miền, thể thao và đời sống hiện đại.

---

## 🚀 3. LỘ TRÌNH TRIỂN KHAI THEO CỘT MỐC (MILESTONES)

| Cột mốc | Mục tiêu số lượng | Quy mô bổ sung | Trạng thái | Đánh giá năng lực phát sóng |
|---|---|---|---|---|
| **Khởi đầu** | **265 câu** | Đợt 1 (+200 câu) | ✅ Hoàn thành | Đủ phát sóng thử nghiệm 1 buổi (10-15 ván). |
| **Cột mốc 1** | **500 câu** | Đợt 2 (+235 câu) | ✅ Hoàn thành | Đủ chơi liên tục 2-3 ngày không lo trùng lặp. |
| **Cột mốc 2** | **1.000 câu** | Đợt 3 (+232 câu) | ⏳ Đang tiến tới 1.000 (Hiện: 732 câu) | Đủ phát sóng 1 tuần liên tục (30-40 ván/ngày). |
| **Cột mốc 3** | **2.500 câu** | Đợt 4 (+1.500 câu) | 📅 Dự kiến | Bắt đầu phân nhánh chuyên đề sự kiện (Tết, Lịch sử, Học sinh). |
| **Cột mốc 4** | **5.000 câu** | Đợt 5 (+2.500 câu) | 📅 Dự kiến | Sẵn sàng cho live stream tự động 24/7 (Hands-free mode). |
| **Cột mốc 5** | **10.000 câu** | Đợt 6 (+5.000 câu) | 📅 Đích đến dài hạn | Kho bách khoa toàn thư tri thức khổng lồ trên TikTok Live. |

---

## 📝 4. NHẬT KÝ CHI TIẾT TỪNG ĐỢT (BATCH LOG)
- **Đợt 1 (2026-11-07):** Khởi tạo QuestionBank modular với 200 câu hỏi chuẩn hóa và nâng cấp lên 265 câu hỏi, phân loại theo 6 chủ đề, tích hợp SQLite `questions.db`.
- **Đợt 2 (2026-11-07):** ✅ Đã sinh mới thành công 235 câu hỏi chuẩn hóa, nạp và đồng bộ song song vào SQLite và JSON. Đã lint kiểm tra 100% đạt chuẩn, đưa ngân hàng câu hỏi chính thức cán mốc **500 câu**.
- **Đợt 3 (2026-11-07):** ✅ Đã sinh mới và tích hợp thêm 232 câu hỏi chuẩn hóa qua 6 chủ đề, nâng tổng ngân hàng câu hỏi lên **732 câu** (mỗi chủ đề đều vượt 100 câu). Lint kiểm định 100% không phát hiện lỗi.
