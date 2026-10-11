# E-Ink 2.13" Web Studio (Serverless Web Serial)

Trình thiết kế và nạp dữ liệu trực tiếp cho màn hình E-Ink 2.13 inch (B/W & Red - 122x250) chạy hoàn toàn trên trình duyệt thông qua **Web Serial API** và **LZ4 WebAssembly**.

🌐 **Trải nghiệm trực tiếp:** [https://elink-111009.github.io/](https://elink-111009.github.io/)

---

### ✨ Tính năng nổi bật
- **Hoàn toàn Serverless:** Không cần cài Python hay server trung gian. Toàn bộ logic render Canvas, nén LZ4 và giao tiếp UART chạy ngay trong trình duyệt (Chrome, Edge, Opera).
- **Tốc độ cao:** Giao tiếp qua UART 921600 baud với CH340, nạp toàn màn hình chỉ mất 1-2 giây.
- **Thuật toán xử lý nét:**
  - Khử mờ và làm đậm viền (Pixel Edge Bold / Dilation).
  - Tự động khử răng cưa / rỗ khi thu nhỏ hình ảnh.
  - Tự động bỏ dấu tiếng Việt khi cần để hiển thị sắc nét nhất trên ma trận điểm E-Ink.
- **Hơn 12 mẫu template sẵn có:** Thẻ bé đi lạc, Bảng để bàn, Biển số điện thoại để xe ô tô, Menu mã QR, Thẻ nhân viên, Thông báo lịch làm việc,...
- **Công cụ tùy biến:** Tải ảnh từ máy tính, chèn mã QR, chèn Icon đa dạng, tùy chỉnh văn bản, xoay lật 90°/180°/270°.

---

### 🚀 Hướng dẫn sử dụng
1. Cắm mạch nạp USB-UART (CH340) kết nối với màn hình E-Ink 2.13".
2. Dùng trình duyệt **Google Chrome** hoặc **Microsoft Edge**, truy cập vào [https://elink-111009.github.io/](https://elink-111009.github.io/).
3. Bấm **"Kết nối COM"**, chọn đúng cổng COM của mạch nạp (CH340).
4. Thiết kế hoặc chọn template theo ý muốn, sau đó bấm **"Nạp màn hình (B/W + Đỏ)"**.
