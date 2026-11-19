# HỆ THỐNG QUẢN LÝ & GIAO ĐỀ THI TỰ HỌC (PHIÊN BẢN 2026)

Hệ thống thi trắc nghiệm & tự luận online chạy trực tiếp 100% trên trình duyệt (GitHub Pages) dành riêng cho Giáo viên & Học sinh Việt Nam.

---

## 🎁 TẶNG KÈM TỆP ĐỀ THI MẪU CHUẨN BỘ GD&ĐT
Trong gói phân phối đã tích hợp sẵn tệp **`De_Thi_Mau_Chuan_BGD_2026.docx`**.
* **Trải nghiệm ngay trong 5 giây:** Thầy/Cô mở trang web `index.html`, vào mục **THƯ VIỆN** → bấm **TẠO ĐỀ THI** → bấm **📄 Nhập từ File Word (.docx)** và chọn tệp `De_Thi_Mau_Chuan_BGD_2026.docx`.
* Hệ thống sẽ tự động bóc tách đầy đủ **4 phần thi** (Phần I: Nhiều lựa chọn, Phần II: Đúng/Sai 4 ý, Phần III: Trả lời ngắn, Phần IV: Tự luận) cùng đáp án và lời giải chi tiết!

---

## 🚀 3 BƯỚC TRIỂN KHAI NHANH TRÊN GITHUB PAGES (HOÀN TOÀN MIỄN PHÍ)

1. **Tạo Repository mới trên GitHub**:
   - Truy cập: https://github.com
   - Bấm nút **New Repository**, đặt tên kho (ví dụ: `onthi2026` hoặc `kiemtra`).
   - Chọn chế độ **Public**.
2. **Tải lên các tệp tin này**:
   - `index.html` (Giao diện và toàn bộ hệ sinh thái thi tự học)
   - `cloud-config.json` (Cấu hình đồng bộ Firebase)
   - `database.rules.json` (Quy tắc bảo mật Firebase)
   - `.nojekyll` (Tệp cấu hình bắt buộc cho GitHub Pages)
   - `De_Thi_Mau_Chuan_BGD_2026.docx` (File Word mẫu để giáo viên/học sinh thử nghiệm)
   - `README.md`
3. **Bật GitHub Pages**:
   - Vào **Settings** → **Pages** → mục **Source** chọn `Deploy from a branch` → Branch `main` (hoặc `root`) → Bấm **Save**.
   - Sau 1–2 phút, bạn sẽ nhận được đường link dạng:
     👉 `https://<ten-tai-khoan>.github.io/<ten-repo>/`

---

## 🔥 THIẾT LẬP DATABASE FIREBASE RIÊNG (MIỄN PHÍ 100% - CHỈ MẤT 2 PHÚT)

Để học sinh nộp bài và đồng bộ điểm về máy giáo viên, thầy cô tạo một kho Firebase hoàn toàn miễn phí theo các bước:

1. **Tạo dự án Firebase**:
   - Truy cập: https://console.firebase.google.com/ bằng tài khoản Google (Gmail).
   - Bấm **Add project** (Tạo dự án) → Đặt tên (ví dụ: `onthi-thcs-2026`) → Bấm Tiếp tục cho đến khi hoàn tất.
2. **Kích hoạt Realtime Database**:
   - Ở cột menu bên trái, mục **Build** (Xây dựng) → chọn **Realtime Database** *(chú ý chọn Realtime Database, KHÔNG chọn Cloud Firestore)*.
   - Bấm **Create Database** (Tạo cơ sở dữ liệu).
   - Chọn vị trí máy chủ (Location): `Singapore (asia-southeast1)` để tốc độ tại Việt Nam nhanh nhất.
   - Chọn chế độ bắt đầu: **Start in test mode** → Bấm **Enable**.
3. **Cấu hình Quy tắc bảo mật (Rules)**:
   - Chuyển sang tab **Rules** (Quy tắc) ở phía trên.
   - Sao chép toàn bộ nội dung trong tệp `database.rules.json` và dán đè vào:
   ```json
   {
     "rules": {
       ".read": false,
       ".write": false,
       "t": {
         "$code": {
           ".read": "$code.length >= 16",
           ".write": "$code.length >= 16"
         }
       },
       "s": {
         "$code": {
           ".read": "$code.length >= 12",
           ".write": "$code.length >= 12"
         }
       }
     }
   }
   ```
   - Bấm **Publish** (Xuất bản).
4. **Lấy URL Database và dán vào phần mềm**:
   - Quay lại tab **Data** (Dữ liệu), sao chép đường dẫn URL của cơ sở dữ liệu.
     *Dạng: `https://<ten-du-an>-default-rtdb.asia-southeast1.firebasedatabase.app`*
   - **Cách 1 (Nhanh nhất):** Mở tệp `cloud-config.json`, điền URL vừa sao chép vào trường `"u"`:
     ```json
     {
       "u": "https://ten-du-an-default-rtdb.asia-southeast1.firebasedatabase.app",
       "p": "h2v8xsmcyut92yww"
     }
     ```
   - **Cách 2:** Mở trang web `index.html` trên máy tính → Bấm nút **☁️ ĐỒNG BỘ** ở góc màn hình → Dán URL vào ô số 1 và bấm **🔗 Kết nối & đồng bộ**.

---

## 🔑 THIẾT LẬP TÀI KHOẢN GIÁO VIÊN LẦN ĐẦU
- Khi mở trang web trên máy tính lần đầu tiên, hệ thống sẽ hiện hộp thoại yêu cầu:
  1. Nhập **Họ và tên giáo viên**.
  2. Tạo **Mật khẩu quản trị** (dùng để đăng nhập chấm thi, quản lý lớp, trộn đề).
- Mật khẩu được mã hóa an toàn bằng thuật toán SHA-256 (có muối bảo mật 8000 vòng) ngay tại trình duyệt của bạn.

---

## 🌟 CÁC TÍNH NĂNG VƯỢT TRỘI DÀNH CHO THẦY CÔ:
1. **Trộn đề thi chuẩn Bộ GD&ĐT**: Hỗ trợ đầy đủ Phần I (Trắc nghiệm), Phần II (Đúng/Sai), Phần III (Trả lời ngắn), Phần IV (Tự luận). Xuất nhiều mã đề ra file Word (.docx) kèm bảng đáp án và lời giải chi tiết.
2. **Nhận diện MathType & ChemDraw**: Nhập trực tiếp đề thi từ file Word giữ nguyên công thức toán MathType, hình hóa ChemDraw, bảng biểu, căn lề.
3. **Ngân hàng đề thi theo SGK mới**: Tích hợp danh mục bài học các bộ sách Kết nối tri thức, Cánh Diều, Chân trời cho tất cả các môn từ lớp 1 đến 12.
4. **Quản lý lớp học & Chấm tự luận bằng ảnh**: Học sinh làm tự luận trên giấy, chụp ảnh nộp; Thầy cô chấm điểm trực tiếp, chấm xong hệ thống tự xóa ảnh để tiết kiệm dung lượng.
5. **Chơi trực tiếp (Live Game)**: Thi đấu thời gian thực P2P (WebRTC/Firebase) với trò chơi ghép tranh Pixel Art 24x24 độc đáo.
6. **Đánh giá tiến bộ hàng tháng**: Tự động tổng hợp điểm, đánh giá mức độ tiến bộ/giảm sút vào ngày 30 hàng tháng và xuất file Excel.
