# BÍ KÍP TẠO FIRMWARE BLE & MỞ KHÓA MÀN HÌNH E-INK 2.13"

Tài liệu ghi nhớ toàn bộ thông tin và quy trình để ngày mai tiếp tục thực hiện mà không cần cấu hình lại từ đầu.

---

## 1. TRẠNG THÁI HIỆN TẠI (ĐÃ HOÀN THÀNH)

1. **Phần cứng màn hình:**
   - Model: E-Ink 2.13 inch DKE (`DKE_213_BW`), phân giải chuẩn phần cứng: **250 × 122 pixel**.
   - Đã xử lý triệt để lỗi lệch 6 pixel viền trên (đưa về chuẩn active area 250×122).
   - Đã tinh chỉnh ngưỡng tương phản độ sáng `Threshold = 145`: Chữ hiển thị sắc nét, thanh mảnh, không bị răng cưa hay vỡ chữ.

2. **Web Tool:**
   - Link online: [https://drthanhsus.github.io/](https://drthanhsus.github.io/)
   - Đã tích hợp đầy đủ cả **Web Serial (USB qua COM13)** và **Web Bluetooth (BLE)**.

3. **Simplicity Studio 6 (Đang cài đặt):**
   - Đang tiến hành cài đặt: Gói **`Simplicity SDK 2026.6.1`** (bản nâng cấp mới nhất của Gecko SDK, tích hợp sẵn toàn bộ Bluetooth LE stack cho dòng chip EFR32).

---

## 2. QUY TRÌNH TIẾP TỤC VÀO NGÀY MAI (CHỈ 3 BƯỚC)

Sau khi máy tính hoàn tất tải `Simplicity SDK 2026.6.1`:

### Bước 1: Tạo dự án Bluetooth - SoC Empty
1. Mở Simplicity Studio 6.
2. Tại màn hình **Home** hoặc thẻ **Devices**:
   - Chọn bo mạch / chip: **`EFR32BG22 Explorer Kit Board (BRD4108A)`** hoặc gõ Part: **`EFR32BG22C224F512IM`**.
   - Vào thẻ **EXAMPLE PROJECTS & DEMOS**.
3. Lúc này danh sách sẽ hiển thị đầy đủ các project mẫu.
4. Chọn project: **`Bluetooth - SoC Empty`** ➔ Nhấn **Create** ➔ Đặt tên (vd: `Eink_BLE`) ➔ **Finish**.

---

### Bước 2: Ghép mã nguồn Driver E-Ink (Đã chuẩn bị sẵn)
Các file mã nguồn C trong thư mục `d:\DỰ ÁN\pkgera\`:
- [epd_dke213.h](file:///d:/DỰ%20ÁN/pkgera/epd_dke213.h): Định nghĩa các chân điều khiển SPI & GPIO (CS A6, DC C3, RST C4, BUSY C5).
- [epd_dke213.c](file:///d:/DỰ%20ÁN/pkgera/epd_dke213.c): Driver xuất ảnh lên tấm kính 2.13" E-Ink.
- [app_ble_epd.c](file:///d:/DỰ%20ÁN/pkgera/app_ble_epd.c): Khởi tạo Bluetooth LE, phát quảng cáo tên `EINK-TAG`, nhận mảng 4000 byte ảnh qua không dây và gọi driver cập nhật màn hình.

**Thao tác:**
1. Kéo 2 file `epd_dke213.h` và `epd_dke213.c` thả vào thư mục dự án trong Simplicity Studio.
2. Mở file `app.c` có sẵn của dự án, dán đè toàn bộ nội dung từ file `app_ble_epd.c` vào rồi nhấn `Ctrl + S`.

---

### Bước 3: Biên dịch & Nạp 1 chạm
1. Nhấn nút **`Ctrl + B`** (hoặc biểu tượng cái búa 🔨) để biên dịch.
2. Simplicity Studio sẽ tự động sinh ra file nhị phân OTA: **`application.gbl`**.
3. Copy file `application.gbl` mới vào thư mục [qr_ota_v4/](file:///d:/DỰ%20ÁN/pkgera/qr_ota_v4).
4. Bấm đúp vào file [nang_cap_fw.bat](file:///d:/DỰ%20ÁN/pkgera/nang_cap_fw.bat) để nạp thẳng vào chip qua COM13.
5. Màn hình sẽ phát Bluetooth `EINK-TAG`. Anh có thể kết nối từ điện thoại hoặc bấm nút "KẾT NỐI BLUETOOTH" trên web [https://drthanhsus.github.io/](https://drthanhsus.github.io/)!

---

*Lưu trữ tại `d:\DỰ ÁN\pkgera\HUONG_DAN_TAO_FIRMWARE_BLE.md` - Sẵn sàng cho phiên làm việc tiếp theo.*
