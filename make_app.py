# -*- coding: utf-8 -*-
"""
Python script to generate complete clean HTML file
(Default Black/White, Optional Red Accent Toggle)
"""
from build_clean_app import get_obfuscated_core_engine

def generate_html():
    core_engine = get_obfuscated_core_engine()

    html = f'''<!DOCTYPE html>
<html lang="vi" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>E-Ink 2.13" Web Studio</title>
  <!-- Polyfill -->
  <script>
    if (!window.crypto) window.crypto = {{}};
    if (!window.crypto.randomUUID) {{
      window.crypto.randomUUID = function() {{
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {{
          var r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
          return v.toString(16);
        }});
      }};
    }}
  </script>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- QRCode.js & JsBarcode -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/jsbarcode@3.11.5/dist/JsBarcode.all.min.js"></script>
  <!-- Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          }}
        }}
      }}
    }}
  </script>
  <style>
    .pixelated {{
      image-rendering: -moz-crisp-edges;
      image-rendering: -webkit-crisp-edges;
      image-rendering: pixelated;
      image-rendering: crisp-edges;
    }}
    .eink-bezel {{
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
      border: 12px solid #18181b;
      border-radius: 12px;
    }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen font-sans antialiased flex flex-col">

  <!-- TOP HEADER -->
  <header class="bg-slate-900 border-b border-slate-800 px-6 py-3.5 sticky top-0 z-50 shadow-md">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-4">
      <div class="flex items-center space-x-3">
        <div class="w-9 h-9 rounded-lg bg-blue-600 flex items-center justify-center font-bold text-white shadow-lg shadow-blue-500/30">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
        </div>
        <div>
          <h1 class="font-extrabold text-lg tracking-tight text-white flex items-center gap-2">
            E-INK 2.13" WEB STUDIO
            <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Bản Trực Tuyến</span>
          </h1>
          <p class="text-xs text-slate-400">Trình thiết kế và nạp dữ liệu màn hình E-Ink 2.13 inch trực tiếp</p>
        </div>
      </div>

      <!-- CONNECTION BAR -->
      <div class="flex items-center flex-wrap gap-2.5 bg-slate-950 px-3.5 py-1.5 rounded-xl border border-slate-800">
        <!-- USB Serial -->
        <button id="connectSerialBtn" class="flex items-center gap-1.5 text-xs font-semibold bg-blue-600 hover:bg-blue-500 text-white px-3 py-1.5 rounded-lg transition shadow-sm">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          <span id="connectBtnText">Cổng USB (CH340)</span>
        </button>

        <button id="disconnectBtn" title="Ngắt kết nối USB" class="text-xs font-medium bg-rose-900/40 hover:bg-rose-800 text-rose-300 px-2 py-1.5 rounded-lg transition border border-rose-800/50 hidden">
          Ngắt USB
        </button>

        <div class="h-4 w-px bg-slate-800 hidden sm:block"></div>

        <!-- Web Bluetooth BLE -->
        <button id="connectBleBtn" class="flex items-center gap-1.5 text-xs font-semibold bg-indigo-600 hover:bg-indigo-500 text-white px-3 py-1.5 rounded-lg transition shadow-sm">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18l4-4-4-4m0 8V6l-4 4 4 4"></path></svg>
          <span id="connectBleBtnText">Bluetooth (BLE)</span>
        </button>

        <button id="disconnectBleBtn" title="Ngắt kết nối Bluetooth" class="text-xs font-medium bg-rose-900/40 hover:bg-rose-800 text-rose-300 px-2 py-1.5 rounded-lg transition border border-rose-800/50 hidden">
          Ngắt BLE
        </button>

        <div class="h-4 w-px bg-slate-800 hidden sm:block"></div>

        <div class="flex items-center gap-1.5">
          <span class="text-xs font-medium text-slate-400">Baud:</span>
          <select id="baudSelect" class="bg-slate-900 border border-slate-700 text-xs rounded-lg px-2 py-1.5 text-white font-mono">
            <option value="921600" selected>921600</option>
            <option value="115200">115200</option>
            <option value="230400">230400</option>
          </select>
        </div>

        <button id="pingBtn" class="flex items-center gap-1.5 text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 px-2.5 py-1.5 rounded-lg transition border border-slate-700">
          <span id="pingDot" class="w-2 h-2 rounded-full bg-slate-500"></span>
          <span>Kiểm Tra</span>
        </button>
      </div>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main class="max-w-7xl mx-auto p-4 sm:p-6 flex-1 w-full grid grid-cols-1 lg:grid-cols-12 gap-6">

    <!-- LEFT PANEL: CONTROLS & TEMPLATES (7 cols) -->
    <div class="lg:col-span-7 flex flex-col gap-5">

      <!-- MODE NAVIGATION TABS -->
      <div class="flex bg-slate-900 p-1.5 rounded-xl border border-slate-800 shadow-sm">
        <button id="tabTemplateBtn" class="flex-1 py-2 text-xs sm:text-sm font-semibold rounded-lg transition flex items-center justify-center gap-2 bg-blue-600 text-white shadow">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z"></path></svg>
          Mẫu Thiết Kế Sẵn Có (22 Mẫu)
        </button>
        <button id="tabCustomImageBtn" class="flex-1 py-2 text-xs sm:text-sm font-semibold rounded-lg transition flex items-center justify-center gap-2 text-slate-400 hover:text-white">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
          Nạp Ảnh Tự Do (Từ Máy Tính)
        </button>
      </div>

      <!-- SECTION 1: TEMPLATE STUDIO CONTROLS -->
      <div id="templateSection" class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-sm flex flex-col gap-4">
        <div>
          <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Chọn Mẫu Thiết Kế:</label>
          <select id="templateSelector" class="w-full bg-slate-950 border border-slate-700 rounded-xl px-3.5 py-2.5 text-sm text-white font-medium focus:ring-2 focus:ring-blue-500 focus:outline-none">
            <optgroup label="MẪU THIẾT KẾ ĐẶC SẮC (BỐ CỤC 2 CỘT, KHUNG ẢNH)">
              <option value="floral_card" selected>1. Thiệp Chúc Mừng & Tri Ân (Khung viền trang trí cổ điển)</option>
              <option value="side_avatar_id">2. Thẻ Nhân Viên Chân Dung (Ảnh thẻ 3x4 bên trái, thông tin bên phải)</option>
              <option value="menu_dish">3. Thực Đơn Món Ăn & Đồ Uống (Ảnh món bên trái, giá và mô tả bên phải)</option>
              <option value="pet_id_cute">4. Thẻ Thú Cưng (Khung ảnh bé cưng, thông tin liên hệ khi thất lạc)</option>
              <option value="sale_voucher">5. Phiếu Giảm Giá & Voucher (Khung ưu đãi, mã giảm giá, hạn sử dụng)</option>
              <option value="botanical_plant">6. Bảng Cây Cảnh & Sinh Thái (Hình ảnh chậu cây, chế độ chăm sóc)</option>
              <option value="art_exhibit">7. Bảng Trưng Bày Tác Phẩm (Hình tác phẩm nghệ thuật, tác giả, giá)</option>
              <option value="hotel_welcome">8. Bảng Chào Đón Khách VIP (Biểu tượng sang trọng, tên khách, số phòng)</option>
              <option value="quote_floral">9. Châm Ngôn & Lời Nhắc Việc (Trang trí nghệ thuật, câu danh ngôn)</option>
              <option value="vip_member_club">10. Thẻ Hội Viên VIP (Khung viền cao cấp, mã thẻ, hạng hội viên)</option>
            </optgroup>
            <optgroup label="MẪU THIẾT KẾ TIỆN ÍCH CƠ BẢN">
              <option value="kid_tag">11. Thẻ Học Sinh / Trẻ Em (Thông tin gia đình và số điện thoại)</option>
              <option value="car_parking">12. Thẻ Đỗ Xe Ô Tô (Số điện thoại dời xe lịch sự)</option>
              <option value="desk_nameplate">13. Biển Chức Danh Để Bàn (Công ty, họ tên, chức vụ, phòng ban)</option>
              <option value="badge">14. Thẻ Tên & Hotline (Dải banner đen nổi bật)</option>
              <option value="esl_price">15. Thẻ Giá Siêu Thị ESL (Giá bán kèm mã vạch Barcode)</option>
              <option value="bank_qr">16. Mã QR Thanh Toán Ngân Hàng (Mã QR chuyển khoản, số tài khoản)</option>
              <option value="table_order">17. Biển Số Bàn & Gọi Món QR (Số bàn lớn kèm mã QR xem menu)</option>
              <option value="meeting_status">18. Bảng Trạng Thái Cuộc Họp (Đang họp, vắng mặt, giờ quay lại)</option>
              <option value="wifi_share">19. Chia Sẻ Mạng Wifi (Mã QR quét nhanh kèm mật khẩu)</option>
              <option value="desk_clock">20. Đồng Hồ Để Bàn & Thời Tiết (Giờ lớn, ngày tháng, nhiệt độ)</option>
              <option value="todo_list">21. Danh Sách Việc Cần Làm (To-Do List ghi nhớ công việc)</option>
              <option value="custom_free">22. Tùy Biến Tự Do (Tiêu đề trên và 3 dòng thông tin)</option>
            </optgroup>
          </select>
        </div>

        <!-- COLOR MODE SELECTION BAR (DEFAULT BLACK & WHITE) -->
        <div class="flex flex-wrap items-center justify-between gap-2 bg-slate-950/80 px-3.5 py-2.5 rounded-xl border border-slate-800">
          <div class="flex flex-col">
            <span class="text-xs font-semibold text-slate-200">Chế độ hiển thị màn hình:</span>
            <span class="text-[10px] text-slate-400">Mặc định Trắng/Đen (Bảo toàn 100% nét chữ trên màn hình đơn sắc)</span>
          </div>
          <label class="flex items-center gap-2 cursor-pointer text-xs text-rose-400 hover:text-rose-300 font-medium bg-rose-950/30 px-2.5 py-1 rounded-lg border border-rose-900/40">
            <input type="checkbox" id="enableRedAccentCheckbox" class="rounded bg-slate-800 border-slate-700 text-rose-600 focus:ring-rose-500">
            <span>Bật màu đỏ (Chỉ dành cho màn 3 màu)</span>
          </label>
        </div>

        <hr class="border-slate-800">

        <!-- DYNAMIC INPUT FIELDS CONTAINER -->
        <div id="dynamicInputs" class="flex flex-col gap-3.5">
          <!-- Injected via JavaScript -->
        </div>
      </div>

      <!-- SECTION 2: CUSTOM IMAGE CONTROLS -->
      <div id="customImageSection" class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-sm flex flex-col gap-4 hidden">
        <div>
          <label class="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Tải Ảnh Lên (Hỗ trợ định dạng PNG, JPG, BMP):</label>
          <div id="dropZone" class="border-2 border-dashed border-slate-700 hover:border-blue-500 rounded-xl p-6 text-center cursor-pointer bg-slate-950 transition">
            <input type="file" id="imageFileInput" accept="image/*" class="hidden">
            <svg class="w-10 h-10 text-slate-500 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path></svg>
            <p class="text-sm font-medium text-slate-300">Kéo thả ảnh vào đây hoặc <span class="text-blue-400 underline">Chọn tệp</span></p>
            <p class="text-xs text-slate-500 mt-1">Ảnh sẽ tự động co giãn tối ưu chuẩn 250×122 pixel</p>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Kiểu Cắt (Fit Mode):</label>
            <select id="fitModeSelect" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-xs text-white">
              <option value="cover" selected>Cover (Lấp đầy toàn màn hình)</option>
              <option value="contain">Contain (Giữ nguyên tỉ lệ ảnh)</option>
              <option value="stretch">Stretch (Kéo giãn vừa khung)</option>
            </select>
          </div>

          <div>
            <div class="flex justify-between items-center mb-1">
              <label class="text-xs font-semibold text-slate-400">Độ Ngưỡng Tương Phản (Threshold):</label>
              <span id="thresholdVal" class="text-xs font-mono text-blue-400">185</span>
            </div>
            <input type="range" id="thresholdSlider" min="10" max="245" value="185" class="w-full accent-blue-500">
            <p class="text-[10px] text-slate-500 mt-0.5">Mặc định 185: Giữ nét chữ mảnh, khử đốm đen</p>
          </div>
        </div>

        <div class="flex flex-wrap gap-4 pt-1">
          <label class="flex items-center gap-2 cursor-pointer text-xs text-slate-300">
            <input type="checkbox" id="invertCheck" class="rounded bg-slate-800 border-slate-700 text-blue-600 focus:ring-blue-500">
            <span>Đảo ngược màu sắc (Nền đen chữ trắng)</span>
          </label>
        </div>
      </div>

      <!-- LOG CONSOLE -->
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-sm flex flex-col gap-2">
        <div class="flex items-center justify-between">
          <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            Nhật Ký Hoạt Động
          </span>
          <button id="clearLogBtn" class="text-[11px] text-slate-500 hover:text-slate-300">Xóa nhật ký</button>
        </div>
        <div id="logOutput" class="bg-slate-950 rounded-xl p-3 h-28 overflow-y-auto font-mono text-xs text-slate-300 border border-slate-800/60 space-y-1">
          <div><span class="text-blue-400">[Hệ thống]</span> Sẵn sàng. Vui lòng bấm "Chọn Cổng USB" để bắt đầu kết nối.</div>
        </div>
      </div>

    </div>

    <!-- RIGHT PANEL: WYSIWYG PREVIEW & FLASH ACTIONS (5 cols) -->
    <div class="lg:col-span-5 flex flex-col gap-5">

      <!-- PREVIEW CARD -->
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-sm flex flex-col items-center">
        <div class="w-full flex items-center justify-between mb-4">
          <div class="flex items-center gap-2">
            <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Xem Trước Trực Quan</span>
            <span class="text-[10px] bg-slate-800 text-slate-300 font-mono px-2 py-0.5 rounded-md">250×122 px</span>
          </div>
          <span class="text-xs text-emerald-400 font-medium flex items-center gap-1">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
            Chuẩn Xác 100%
          </span>
        </div>

        <!-- E-INK SCREEN FRAME BEZEL -->
        <div class="eink-bezel p-1.5 bg-zinc-900 w-full max-w-[440px] flex items-center justify-center">
          <div class="bg-white overflow-hidden rounded-[2px] w-full relative flex items-center justify-center border border-zinc-700" style="aspect-ratio: 250 / 122;">
            <canvas id="previewCanvas" width="250" height="122" class="w-full h-full pixelated bg-white block" style="aspect-ratio: 250 / 122;"></canvas>
          </div>
        </div>

        <p class="text-[11px] text-slate-500 text-center mt-3">
          Hiển thị chuẩn xác từng điểm ảnh trên màn hình E-Ink 2.13 inch.
        </p>
      </div>

      <!-- PRIMARY ACTION BUTTONS -->
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-sm flex flex-col gap-3">
        <!-- NẠP VÀO MÀN HÌNH -->
        <button id="pushBtn" class="w-full py-4 rounded-xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-500 hover:from-blue-500 hover:to-indigo-500 text-white font-bold text-base shadow-lg shadow-blue-500/25 transition flex items-center justify-center gap-2 group disabled:opacity-50 disabled:cursor-not-allowed">
          <svg class="w-5 h-5 group-hover:scale-110 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
          <span id="pushBtnText">NẠP VÀO MÀN HÌNH NGAY</span>
        </button>

        <div class="grid grid-cols-2 gap-3">
          <!-- LÀM SẠCH MÀN HÌNH -->
          <button id="clearBtn" class="py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition flex items-center justify-center gap-1.5">
            <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
            Xóa / Làm Trắng Màn
          </button>

          <!-- TẢI ẢNH VỀ MÁY -->
          <button id="downloadBtn" class="py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition flex items-center justify-center gap-1.5">
            <svg class="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            Tải Ảnh PNG Về Máy
          </button>
        </div>
      </div>

    </div>

  </main>

  <!-- HIDDEN HELPERS -->
  <div class="hidden">
    <div id="qrCodeContainer"></div>
    <svg id="barcodeSvg"></svg>
  </div>

  <!-- SCRIPT -->
  <script>
{core_engine}

// === APPLICATION UI & CANVAS CONTROLLER ===
(function() {{
  const canvas = document.getElementById('previewCanvas');
  const ctx = canvas.getContext('2d', {{ willReadFrequently: true }});

  let currentMode = 'template';
  let currentTemplate = 'floral_card';
  let uploadedImageObj = null;
  let templateCustomImgObj = null;

  function isRedMode() {{
    return document.getElementById('enableRedAccentCheckbox')?.checked ?? false;
  }}

  function getAccentColor() {{
    return isRedMode() ? '#EF4444' : '#000000';
  }}

  function addLog(msg, type = 'info') {{
    const box = document.getElementById('logOutput');
    if (!box) return;
    const time = new Date().toLocaleTimeString();
    let colorClass = 'text-slate-300';
    if (type === 'success') colorClass = 'text-emerald-400 font-semibold';
    if (type === 'error') colorClass = 'text-rose-400 font-semibold';
    if (type === 'warning') colorClass = 'text-amber-400';

    const line = document.createElement('div');
    line.className = colorClass;
    line.innerHTML = `<span class="text-slate-500 font-mono">[${{time}}]</span> ${{msg}}`;
    box.appendChild(line);
    box.scrollTop = box.scrollHeight;
  }}

  async function connectSerial() {{
    if (!('serial' in navigator)) {{
      alert("Trình duyệt của bạn không hỗ trợ Web Serial API.\\nVui lòng sử dụng Google Chrome hoặc Microsoft Edge trên máy tính.");
      addLog("Trình duyệt không hỗ trợ Web Serial API. Vui lòng sử dụng Chrome hoặc Edge.", "error");
      return;
    }}
    try {{
      const baudRate = parseInt(document.getElementById('baudSelect').value);
      addLog("Đang mở hộp thoại chọn cổng USB...");
      const ok = await window.__epdHW.open(baudRate);
      if (ok) {{
        document.getElementById('connectBtnText').textContent = "Đã Kết Nối";
        document.getElementById('connectSerialBtn').className = "flex items-center gap-1.5 text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white px-3.5 py-1.5 rounded-lg transition shadow-sm";
        document.getElementById('pingDot').className = "w-2 h-2 rounded-full bg-emerald-400 animate-ping";
        document.getElementById('disconnectBtn').classList.remove('hidden');
        addLog("Đã kết nối thiết bị thành công qua cổng Serial.", "success");
      }}
    }} catch (err) {{
      if (err.name !== 'NotFoundError') {{
        addLog("Lỗi mở cổng kết nối: " + err.message, "error");
      }} else {{
        addLog("Người dùng đã hủy thao tác chọn cổng USB.", "warning");
      }}
    }}
  }}

  async function disconnectSerial() {{
    try {{
      await window.__epdHW.close();
      document.getElementById('connectBtnText').textContent = "Cổng USB (CH340)";
      document.getElementById('connectSerialBtn').className = "flex items-center gap-1.5 text-xs font-semibold bg-blue-600 hover:bg-blue-500 text-white px-3.5 py-1.5 rounded-lg transition shadow-sm";
      document.getElementById('pingDot').className = "w-2 h-2 rounded-full bg-slate-500";
      document.getElementById('disconnectBtn').classList.add('hidden');
      addLog("Đã ngắt kết nối cổng USB Serial.");
    }} catch (e) {{
      console.error(e);
    }}
  }}

  async function connectBle() {{
    if (!('bluetooth' in navigator)) {{
      alert("Trình duyệt của bạn không hỗ trợ Web Bluetooth API.\\nVui lòng sử dụng Google Chrome hoặc Microsoft Edge.");
      addLog("Trình duyệt không hỗ trợ Web Bluetooth API.", "error");
      return;
    }}
    try {{
      addLog("Đang mở hộp thoại quét Bluetooth (BLE)...");
      const devName = await window.__epdHW.openBle();
      document.getElementById('connectBleBtnText').textContent = "BLE: " + devName;
      document.getElementById('connectBleBtn').className = "flex items-center gap-1.5 text-xs font-semibold bg-emerald-600 hover:bg-emerald-500 text-white px-3.5 py-1.5 rounded-lg transition shadow-sm";
      document.getElementById('disconnectBleBtn').classList.remove('hidden');
      addLog("Đã kết nối Bluetooth thành công tới " + devName, "success");
    }} catch (err) {{
      if (err.name !== 'NotFoundError') {{
        addLog("Lỗi kết nối Bluetooth: " + err.message, "error");
      }} else {{
        addLog("Người dùng đã hủy chọn thiết bị Bluetooth.", "warning");
      }}
    }}
  }}

  async function disconnectBle() {{
    try {{
      await window.__epdHW.closeBle();
      document.getElementById('connectBleBtnText').textContent = "Bluetooth (BLE)";
      document.getElementById('connectBleBtn').className = "flex items-center gap-1.5 text-xs font-semibold bg-indigo-600 hover:bg-indigo-500 text-white px-3.5 py-1.5 rounded-lg transition shadow-sm";
      document.getElementById('disconnectBleBtn').classList.add('hidden');
      addLog("Đã ngắt kết nối Bluetooth BLE.");
    }} catch (e) {{
      console.error(e);
    }}
  }}

  async function pingDevice() {{
    if (!window.__epdHW.isReady()) {{
      addLog("Chưa kết nối cổng USB. Vui lòng bấm 'Cổng USB' trước.", "warning");
      alert("Vui lòng chọn và kết nối cổng USB trước.");
      return;
    }}

    addLog("Đang kiểm tra kết nối thiết bị...");
    try {{
      const ok = await window.__epdHW.ping();
      if (ok) {{
        addLog("Thiết bị phản hồi tốt, kết nối thành công.", "success");
        alert("Kết nối thiết bị thành công. Màn hình đã sẵn sàng.");
      }} else {{
        addLog("Thiết bị không phản hồi. Vui lòng kiểm tra lại cáp kết nối.", "warning");
      }}
    }} catch (e) {{
      addLog("Lỗi kiểm tra: " + e.message, "error");
    }}
  }}

  async function pushToScreen() {{
    const isSerial = window.__epdHW.isReady();
    const isBle = window.__epdHW.isBleReady();

    if (!isSerial && !isBle) {{
      await connectSerial();
      if (!window.__epdHW.isReady() && !window.__epdHW.isBleReady()) return;
    }}

    const pushBtn = document.getElementById('pushBtn');
    const pushBtnText = document.getElementById('pushBtnText');
    pushBtn.disabled = true;
    pushBtnText.textContent = "ĐANG XỬ LÝ VÀ NẠP...";

    try {{
      addLog("Đang xử lý dữ liệu hình ảnh chuẩn 250×122 pixel...");
      const raw8000 = window.__epdHW.extract(canvas, isRedMode());

      if (window.__epdHW.isBleReady()) {{
        addLog("Đang nạp không dây qua Bluetooth BLE...");
        await window.__epdHW.sendBle(raw8000, function(curr, tot) {{
          var pct = Math.round((curr * 100) / tot);
          pushBtnText.textContent = "ĐANG TRUYỀN BLE " + pct + "%...";
        }});
        addLog("Nạp qua Bluetooth BLE thành công! Màn hình đang quét nội dung mới.", "success");
        alert("Nạp qua Bluetooth thành công! Màn hình đang cập nhật.");
      }} else {{
        addLog("Đang nạp qua cổng USB Serial...");
        await window.__epdHW.send(raw8000);
        addLog("Nạp thành công qua USB. Màn hình đang hiển thị nội dung mới.", "success");
        alert("Nạp thành công qua USB. Màn hình đang hiển thị nội dung mới.");
      }}
    }} catch (err) {{
      addLog("Lỗi nạp màn hình: " + err.message, "error");
      alert("Lỗi: " + err.message);
    }} finally {{
      pushBtn.disabled = false;
      pushBtnText.textContent = "NẠP VÀO MÀN HÌNH NGAY";
    }}
  }}

  async function clearScreen() {{
    if (!window.__epdHW.isReady()) {{
      await connectSerial();
      if (!window.__epdHW.isReady()) return;
    }}
    if (!confirm("Bạn có chắc chắn muốn làm trắng hoàn toàn màn hình?")) return;

    try {{
      await window.__epdHW.clear();
      addLog("Đã gửi lệnh xóa trắng màn hình thành công.", "success");
    }} catch (e) {{
      addLog("Lỗi xóa màn: " + e.message, "error");
    }}
  }}

  function removeVietnameseTones(str) {{
    if (!str) return '';
    return str
      .normalize('NFD')
      .replace(/[\\u0300-\\u036f]/g, '')
      .replace(/đ/g, 'd')
      .replace(/Đ/g, 'D');
  }}

  // === VECTOR DRAWING HELPERS ===
  function drawFloralCorners(x, y, w, h, color = '#000000') {{
    ctx.save();
    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.lineWidth = 1.2;

    const corners = [
      {{ cx: x + 6, cy: y + 6, sx: 1, sy: 1 }},
      {{ cx: x + w - 6, cy: y + 6, sx: -1, sy: 1 }},
      {{ cx: x + 6, cy: y + h - 6, sx: 1, sy: -1 }},
      {{ cx: x + w - 6, cy: y + h - 6, sx: -1, sy: -1 }}
    ];

    corners.forEach(c => {{
      ctx.save();
      ctx.translate(c.cx, c.cy);
      ctx.scale(c.sx, c.sy);

      ctx.beginPath();
      ctx.moveTo(0, 16);
      ctx.quadraticCurveTo(0, 0, 16, 0);
      ctx.stroke();

      ctx.beginPath();
      ctx.ellipse(3, 8, 3, 1.5, Math.PI / 4, 0, Math.PI * 2);
      ctx.fill();

      ctx.beginPath();
      ctx.ellipse(8, 3, 3, 1.5, -Math.PI / 4, 0, Math.PI * 2);
      ctx.fill();

      ctx.beginPath();
      ctx.arc(0, 0, 1.8, 0, Math.PI * 2);
      ctx.fill();

      ctx.restore();
    }});
    ctx.restore();
  }}

  function drawRose(cx, cy, r = 12, color = '#000000') {{
    ctx.save();
    const isRed = (color !== '#000000');
    ctx.fillStyle = color;
    ctx.strokeStyle = isRed ? '#000000' : '#FFFFFF';
    ctx.lineWidth = isRed ? 1 : 1.5;

    for (let i = 0; i < 5; i++) {{
      const angle = (i * Math.PI * 2) / 5;
      const px = cx + Math.cos(angle) * (r * 0.6);
      const py = cy + Math.sin(angle) * (r * 0.6);
      ctx.beginPath();
      ctx.arc(px, py, r * 0.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
    }}
    ctx.fillStyle = isRed ? '#991B1B' : '#000000';
    ctx.beginPath();
    ctx.arc(cx, cy, r * 0.35, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#000000';
    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.ellipse(cx - r * 0.9, cy + r * 0.5, r * 0.4, r * 0.2, -Math.PI / 6, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    ctx.beginPath();
    ctx.ellipse(cx + r * 0.9, cy + r * 0.5, r * 0.4, r * 0.2, Math.PI / 6, 0, Math.PI * 2);
    ctx.fill();
    ctx.stroke();
    ctx.restore();
  }}

  function drawPawPrint(cx, cy, r = 10, color = '#000000') {{
    ctx.save();
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.ellipse(cx, cy + r * 0.2, r * 0.6, r * 0.45, 0, 0, Math.PI * 2);
    ctx.fill();
    const toeAngles = [-0.6, -0.2, 0.2, 0.6];
    toeAngles.forEach(ang => {{
      const tx = cx + Math.sin(ang) * (r * 0.85);
      const ty = cy - Math.cos(ang) * (r * 0.7);
      ctx.beginPath();
      ctx.ellipse(tx, ty, r * 0.22, r * 0.3, ang, 0, Math.PI * 2);
      ctx.fill();
    }});
    ctx.restore();
  }}

  function drawCrown(cx, cy, w = 24, h = 16, color = '#000000') {{
    ctx.save();
    ctx.fillStyle = color;
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;

    ctx.beginPath();
    ctx.moveTo(cx - w / 2, cy + h / 2);
    ctx.lineTo(cx - w / 2, cy - h / 3);
    ctx.lineTo(cx - w / 4, cy);
    ctx.lineTo(cx, cy - h / 2);
    ctx.lineTo(cx + w / 4, cy);
    ctx.lineTo(cx + w / 2, cy - h / 3);
    ctx.lineTo(cx + w / 2, cy + h / 2);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#FFFFFF';
    [-w/2, 0, w/2].forEach(ox => {{
      ctx.beginPath();
      ctx.arc(cx + ox, cy - h/2 + (ox === 0 ? 0 : h/6), 1.5, 0, Math.PI * 2);
      ctx.fill();
    }});
    ctx.restore();
  }}

  function drawMonsteraLeaf(cx, cy, size = 18, color = '#000000') {{
    ctx.save();
    ctx.fillStyle = color;
    ctx.strokeStyle = color;
    ctx.lineWidth = 1;

    ctx.beginPath();
    ctx.ellipse(cx, cy, size * 0.6, size * 0.9, 0, 0, Math.PI * 2);
    ctx.fill();

    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(cx, cy - size * 0.8);
    ctx.lineTo(cx, cy + size * 0.9);
    ctx.stroke();

    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 2;
    for (let i = -2; i <= 2; i++) {{
      if (i === 0) continue;
      const vy = cy + i * (size * 0.3);
      ctx.beginPath();
      ctx.moveTo(cx, vy);
      ctx.lineTo(cx + (i > 0 ? 1 : -1) * (size * 0.55), vy - 3);
      ctx.stroke();
    }}
    ctx.restore();
  }}

  function drawCoffeeCup(cx, cy, color = '#000000') {{
    ctx.save();
    ctx.fillStyle = color;
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;

    ctx.beginPath();
    ctx.moveTo(cx - 10, cy - 6);
    ctx.lineTo(cx + 10, cy - 6);
    ctx.lineTo(cx + 8, cy + 8);
    ctx.lineTo(cx - 8, cy + 8);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(cx + 11, cy, 4, -Math.PI / 2, Math.PI / 2);
    ctx.stroke();

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    [-4, 0, 4].forEach(ox => {{
      ctx.beginPath();
      ctx.moveTo(cx + ox, cy - 9);
      ctx.quadraticCurveTo(cx + ox + 2, cy - 12, cx + ox, cy - 15);
      ctx.stroke();
    }});
    ctx.restore();
  }}

  function drawTemplateImage(targetImg, dx, dy, dw, dh, threshold = 185) {{
    if (!targetImg) return false;
    try {{
      const offC = document.createElement('canvas');
      offC.width = dw;
      offC.height = dh;
      const offX = offC.getContext('2d');
      offX.fillStyle = '#FFFFFF';
      offX.fillRect(0, 0, dw, dh);

      const rImg = targetImg.width / targetImg.height;
      const rBox = dw / dh;
      let sx = 0, sy = 0, sw = dw, sh = dh;
      if (rImg > rBox) {{
        sw = dh * rImg;
        sx = (dw - sw) / 2;
      }} else {{
        sh = dw / rImg;
        sy = (dh - sh) / 2;
      }}
      offX.drawImage(targetImg, sx, sy, sw, sh);

      const idata = offX.getImageData(0, 0, dw, dh);
      const d = idata.data;
      for (let i = 0; i < d.length; i += 4) {{
        const luma = 0.299 * d[i] + 0.587 * d[i+1] + 0.114 * d[i+2];
        const val = luma > threshold ? 255 : 0;
        d[i] = val;
        d[i+1] = val;
        d[i+2] = val;
      }}
      offX.putImageData(idata, 0, 0);
      ctx.drawImage(offC, dx, dy);
      return true;
    }} catch(e) {{
      return false;
    }}
  }}

  function wrapText(text, x, y, maxWidth, lineHeight) {{
    const words = text.split(' ');
    let line = '';
    let curY = y;
    for (let n = 0; n < words.length; n++) {{
      const testLine = line + words[n] + ' ';
      const metrics = ctx.measureText(testLine);
      if (metrics.width > maxWidth && n > 0) {{
        ctx.fillText(line, x, curY);
        line = words[n] + ' ';
        curY += lineHeight;
        if (curY > 115) break;
      }} else {{
        line = testLine;
      }}
    }}
    if (curY <= 115) ctx.fillText(line, x, curY);
  }}

  // === TEMPLATE RENDERING ===
  function renderCanvas() {{
    ctx.fillStyle = '#FFFFFF';
    ctx.fillRect(0, 0, 250, 122);

    if (currentMode === 'custom_image') {{
      renderCustomImage();
      return;
    }}

    switch (currentTemplate) {{
      case 'floral_card': renderFloralCardTemplate(); break;
      case 'side_avatar_id': renderSideAvatarIdTemplate(); break;
      case 'menu_dish': renderMenuDishTemplate(); break;
      case 'pet_id_cute': renderPetIdCuteTemplate(); break;
      case 'sale_voucher': renderSaleVoucherTemplate(); break;
      case 'botanical_plant': renderBotanicalPlantTemplate(); break;
      case 'art_exhibit': renderArtExhibitTemplate(); break;
      case 'hotel_welcome': renderHotelWelcomeTemplate(); break;
      case 'quote_floral': renderQuoteFloralTemplate(); break;
      case 'vip_member_club': renderVipMemberClubTemplate(); break;

      case 'kid_tag': renderKidTagTemplate(); break;
      case 'car_parking': renderCarParkingTemplate(); break;
      case 'desk_nameplate': renderDeskNameplateTemplate(); break;
      case 'badge': renderBadgeTemplate(); break;
      case 'esl_price': renderEslPriceTemplate(); break;
      case 'bank_qr': renderBankQrTemplate(); break;
      case 'table_order': renderTableOrderTemplate(); break;
      case 'meeting_status': renderMeetingStatusTemplate(); break;
      case 'wifi_share': renderWifiTemplate(); break;
      case 'desk_clock': renderDeskClockTemplate(); break;
      case 'todo_list': renderTodoListTemplate(); break;
      case 'custom_free': renderCustomFreeTemplate(); break;
    }}
  }}

  // 1. Thiệp Chúc Mừng & Tri Ân
  function renderFloralCardTemplate() {{
    const title = document.getElementById('flTitle')?.value || 'CHÚC MỪNG SINH NHẬT';
    const msg = document.getElementById('flMsg')?.value || 'Chúc bạn luôn vui vẻ, hạnh phúc và thành công rực rỡ trong cuộc sống!';
    const sender = document.getElementById('flSender')?.value || 'Từ: Người bạn thân thiết';
    const accent = getAccentColor();

    drawFloralCorners(2, 2, 246, 118, accent);
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(6, 6, 238, 110);

    const hasImg = drawTemplateImage(templateCustomImgObj, 14, 18, 64, 86);
    if (!hasImg) {{
      drawRose(46, 52, 22, accent);
      drawRose(32, 74, 14, accent);
      drawRose(60, 74, 14, '#000000');
    }}

    ctx.beginPath();
    ctx.moveTo(86, 14);
    ctx.lineTo(86, 108);
    ctx.stroke();

    ctx.fillStyle = accent;
    ctx.font = 'bold 13px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(title.toUpperCase(), 94, 14);

    ctx.fillStyle = '#000000';
    ctx.font = '11px Arial, sans-serif';
    wrapText(msg, 94, 38, 142, 16);

    ctx.fillStyle = accent;
    ctx.font = 'bold italic 11px Arial, sans-serif';
    ctx.fillText(sender, 94, 94);
  }}

  // 2. Thẻ Nhân Viên Chân Dung
  function renderSideAvatarIdTemplate() {{
    const comp = document.getElementById('avCompany')?.value || 'CÔNG TY CỔ PHẦN CÔNG NGHỆ';
    const name = document.getElementById('avName')?.value || 'LƯƠNG QUANG THANH';
    const role = document.getElementById('avRole')?.value || 'GIÁM ĐỐC KỸ THUẬT';
    const idCode = document.getElementById('avId')?.value || 'Mã NV: NV-8888';
    const phone = document.getElementById('avPhone')?.value || '0989.146.951';
    const accent = getAccentColor();

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(2, 2, 246, 118);

    ctx.fillStyle = '#F4F4F5';
    ctx.fillRect(10, 14, 68, 94);
    ctx.strokeStyle = accent;
    ctx.lineWidth = 2;
    ctx.strokeRect(10, 14, 68, 94);

    const hasImg = drawTemplateImage(templateCustomImgObj, 10, 14, 68, 94);
    if (!hasImg) {{
      ctx.fillStyle = '#000000';
      ctx.beginPath();
      ctx.arc(44, 46, 18, 0, Math.PI * 2);
      ctx.fill();
      ctx.beginPath();
      ctx.ellipse(44, 92, 26, 20, 0, Math.PI, 0);
      ctx.fill();
    }}

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 10px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(comp.toUpperCase(), 88, 14);

    ctx.fillStyle = accent;
    ctx.font = 'bold 15px Arial, sans-serif';
    ctx.fillText(name.toUpperCase(), 88, 30);

    ctx.fillStyle = accent;
    ctx.fillRect(88, 52, 148, 20);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 11px Arial, sans-serif';
    ctx.fillText(role.toUpperCase(), 94, 56);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 11px Arial, sans-serif';
    ctx.fillText(idCode, 88, 80);
    ctx.font = 'bold 12px "Arial Narrow", Arial, sans-serif';
    ctx.fillText('Hotline: ' + phone, 88, 96);
  }}

  // 3. Thực Đơn Món Ăn & Đồ Uống
  function renderMenuDishTemplate() {{
    const dish = document.getElementById('mnDish')?.value || 'TRÀ SEN VÀNG KEM CHEESE';
    const price = document.getElementById('mnPrice')?.value || '45.000đ';
    const desc = document.getElementById('mnDesc')?.value || 'Hạt sen bùi béo kết hợp cốt trà thanh mát và lớp màng sữa thơm ngậy.';
    const accent = getAccentColor();

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(2, 2, 246, 118);

    ctx.strokeStyle = accent;
    ctx.lineWidth = 1.5;
    ctx.strokeRect(10, 14, 72, 94);
    const hasImg = drawTemplateImage(templateCustomImgObj, 10, 14, 72, 94);
    if (!hasImg) {{
      drawCoffeeCup(46, 55, accent);
      ctx.fillStyle = '#000000';
      ctx.font = 'bold 10px Arial, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('SPECIAL', 46, 92);
    }}

    ctx.fillStyle = accent;
    ctx.font = 'bold 13px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(dish.toUpperCase().slice(0, 22), 90, 14);

    ctx.fillStyle = accent;
    ctx.font = '12px Arial, sans-serif';
    ctx.fillText('★★★★★', 90, 32);

    ctx.fillStyle = '#000000';
    ctx.fillRect(164, 30, 74, 22);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 13px "Arial Narrow", Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(price, 201, 34);

    ctx.fillStyle = '#000000';
    ctx.font = '10px Arial, sans-serif';
    ctx.textAlign = 'left';
    wrapText(desc, 90, 60, 148, 15);
  }}

  // 4. Thẻ Thú Cưng
  function renderPetIdCuteTemplate() {{
    const name = document.getElementById('ptName')?.value || 'BƠ BÉ BỎNG';
    const breed = document.getElementById('ptBreed')?.value || 'Corgi Vàng Trắng • 1 Tuổi';
    const phone = document.getElementById('ptPhone')?.value || '0989.146.951';
    const note = document.getElementById('ptNote')?.value || 'Nếu em bị lạc, xin vui lòng gọi cho bố mẹ em nhé!';
    const accent = getAccentColor();

    drawPawPrint(18, 18, 8, accent);
    drawPawPrint(232, 18, 8, '#000000');
    drawPawPrint(18, 104, 8, '#000000');
    drawPawPrint(232, 104, 8, accent);

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(4, 4, 242, 114);

    ctx.save();
    ctx.beginPath();
    ctx.arc(52, 61, 36, 0, Math.PI * 2);
    ctx.strokeStyle = accent;
    ctx.lineWidth = 2.5;
    ctx.stroke();

    const hasImg = drawTemplateImage(templateCustomImgObj, 16, 25, 72, 72);
    if (!hasImg) {{
      drawPawPrint(52, 61, 20, accent);
    }}
    ctx.restore();

    ctx.fillStyle = accent;
    ctx.font = 'bold 18px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(name.toUpperCase(), 98, 14);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 11px Arial, sans-serif';
    ctx.fillText(breed, 98, 38);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 16px "Arial Narrow", Impact, Arial, sans-serif';
    ctx.fillText('Số ĐT: ' + phone, 98, 56);

    ctx.font = 'italic 10px Arial, sans-serif';
    wrapText(note, 98, 80, 138, 14);
  }}

  // 5. Phiếu Giảm Giá & Voucher
  function renderSaleVoucherTemplate() {{
    const saleVal = document.getElementById('scValue')?.value || '-50%';
    const title = document.getElementById('scTitle')?.value || 'PHIẾU GIẢM GIÁ ĐẶC BIỆT';
    const code = document.getElementById('scCode')?.value || 'VIP50K-2026';
    const exp = document.getElementById('scExp')?.value || 'Hạn dùng: 31/12/2026 • Áp dụng toàn hệ thống';
    const accent = getAccentColor();

    ctx.fillStyle = accent;
    ctx.fillRect(0, 0, 250, 24);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 12px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('CHƯƠNG TRÌNH ƯU ĐÃI ĐẶC BIỆT', 125, 12);

    ctx.fillStyle = accent;
    ctx.fillRect(8, 32, 76, 80);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 28px "Arial Narrow", Impact, Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(saleVal, 46, 64);
    ctx.font = 'bold 11px Arial, sans-serif';
    ctx.fillText('ƯU ĐÃI', 46, 92);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 12px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(title, 94, 32);

    ctx.save();
    ctx.setLineDash([4, 2]);
    ctx.strokeStyle = accent;
    ctx.lineWidth = 1.5;
    ctx.strokeRect(94, 52, 146, 28);
    ctx.restore();

    ctx.fillStyle = accent;
    ctx.font = 'bold 15px "JetBrains Mono", Courier, monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('MÃ: ' + code, 167, 66);

    ctx.fillStyle = '#000000';
    ctx.font = '10px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText(exp, 94, 94);

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(1, 1, 248, 120);
  }}

  // 6. Bảng Cây Cảnh & Sinh Thái
  function renderBotanicalPlantTemplate() {{
    const vnName = document.getElementById('btVnName')?.value || 'TRẦU BÀ LÁ XẺ (MONSTERA)';
    const sciName = document.getElementById('btSciName')?.value || 'Monstera Deliciosa';
    const water = document.getElementById('btWater')?.value || 'Tưới nước: 2 lần/tuần (Độ ẩm cao)';
    const light = document.getElementById('btLight')?.value || 'Ánh sáng: Khuếch tán, bóng râm';
    const accent = getAccentColor();

    drawFloralCorners(2, 2, 246, 118, '#000000');
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(4, 4, 242, 114);

    ctx.strokeStyle = accent;
    ctx.lineWidth = 1.5;
    ctx.strokeRect(10, 14, 70, 94);

    const hasImg = drawTemplateImage(templateCustomImgObj, 10, 14, 70, 94);
    if (!hasImg) {{
      drawMonsteraLeaf(45, 61, 30, '#000000');
    }}

    ctx.fillStyle = accent;
    ctx.font = 'bold 12px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(vnName.toUpperCase().slice(0, 24), 88, 14);

    ctx.fillStyle = '#000000';
    ctx.font = 'italic 11px "Times New Roman", serif';
    ctx.fillText(sciName, 88, 32);

    ctx.beginPath();
    ctx.moveTo(88, 50);
    ctx.lineTo(236, 50);
    ctx.stroke();

    ctx.font = 'bold 11px Arial, sans-serif';
    ctx.fillText(water, 88, 62);
    ctx.fillText(light, 88, 80);

    ctx.fillStyle = accent;
    ctx.font = 'italic 10px Arial, sans-serif';
    ctx.fillText('Chăm sóc cây bằng sự yêu thương', 88, 98);
  }}

  // 7. Bảng Trưng Bày Tác Phẩm
  function renderArtExhibitTemplate() {{
    const artName = document.getElementById('arTitle')?.value || 'HOÀNG HÔN TRÊN SÔNG';
    const artist = document.getElementById('arArtist')?.value || 'Họa sĩ: Trần Minh Đức';
    const material = document.getElementById('arMat')?.value || 'Sơn dầu trên toan • 2026';
    const price = document.getElementById('arPrice')?.value || 'Giá niêm yết: 15.000.000 VNĐ';
    const accent = getAccentColor();

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(3, 3, 244, 116);

    ctx.strokeStyle = accent;
    ctx.lineWidth = 2;
    ctx.strokeRect(10, 12, 76, 98);

    const hasImg = drawTemplateImage(templateCustomImgObj, 10, 12, 76, 98);
    if (!hasImg) {{
      ctx.fillStyle = '#000000';
      ctx.font = 'bold 10px Arial, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('TÁC PHẨM', 48, 62);
    }}

    ctx.fillStyle = accent;
    ctx.font = 'bold 15px "Times New Roman", Georgia, serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(artName.toUpperCase(), 96, 16);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 12px Arial, sans-serif';
    ctx.fillText(artist, 96, 40);

    ctx.font = '11px Arial, sans-serif';
    ctx.fillText(material, 96, 62);

    ctx.beginPath();
    ctx.moveTo(96, 80);
    ctx.lineTo(236, 80);
    ctx.stroke();

    ctx.fillStyle = accent;
    ctx.font = 'bold 13px Arial, sans-serif';
    ctx.fillText(price, 96, 90);
  }}

  // 8. Bảng Chào Đón Khách VIP
  function renderHotelWelcomeTemplate() {{
    const hotel = document.getElementById('hwHotel')?.value || 'THE RIVANA LUXURY RESIDENCE';
    const guest = document.getElementById('hwGuest')?.value || 'ÔNG LƯƠNG QUANG THANH';
    const room = document.getElementById('hwRoom')?.value || 'PHÒNG 802 (DELUXE)';
    const hotline = document.getElementById('hwHotline')?.value || 'Lễ tân 24/7: 0989.146.951';
    const accent = getAccentColor();

    drawFloralCorners(2, 2, 246, 118, accent);
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(6, 6, 238, 110);

    drawCrown(125, 20, 26, 16, accent);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 10px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    ctx.fillText(hotel.toUpperCase(), 125, 34);

    ctx.fillStyle = accent;
    ctx.font = 'bold 16px "Times New Roman", Arial, sans-serif';
    ctx.fillText('CHÀO ĐÓN QUÝ KHÁCH', 125, 48);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 15px Arial, sans-serif';
    ctx.fillText(guest.toUpperCase(), 125, 68);

    ctx.fillStyle = accent;
    ctx.fillRect(40, 88, 170, 18);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 11px Arial, sans-serif';
    ctx.textBaseline = 'middle';
    ctx.fillText(room + ' • ' + hotline, 125, 97);
  }}

  // 9. Châm Ngôn & Lời Nhắc Việc
  function renderQuoteFloralTemplate() {{
    const quote = document.getElementById('qtText')?.value || 'HÃY LUÔN MỈM CƯỜI, ĐIỀU KỲ DIỆU SẼ ĐẾN VỚI BẠN!';
    const author = document.getElementById('qtAuthor')?.value || '— Chúc bạn một ngày tốt lành —';
    const dateStr = document.getElementById('qtDate')?.value || 'Ngày 12/10/2026';
    const accent = getAccentColor();

    drawFloralCorners(2, 2, 246, 118, accent);
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(5, 5, 240, 112);

    drawRose(38, 61, 24, accent);

    ctx.fillStyle = accent;
    ctx.font = 'bold 24px "Times New Roman", serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText('“', 72, 14);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 12px Arial, sans-serif';
    wrapText(quote, 82, 22, 154, 18);

    ctx.fillStyle = accent;
    ctx.font = 'italic 11px Arial, sans-serif';
    ctx.fillText(author, 82, 80);

    ctx.fillStyle = '#000000';
    ctx.font = '10px Arial, sans-serif';
    ctx.fillText(dateStr, 82, 98);
  }}

  // 10. Thẻ Hội Viên VIP
  function renderVipMemberClubTemplate() {{
    const club = document.getElementById('rcClub')?.value || 'ELITE DIAMOND CLUB';
    const name = document.getElementById('rcName')?.value || 'LƯƠNG QUANG THANH';
    const cardId = document.getElementById('rcId')?.value || 'SỐ THẺ: 8888-9999-111009';
    const exp = document.getElementById('rcExp')?.value || 'HẠN THẺ: 12/2030';
    const accent = getAccentColor();

    ctx.strokeStyle = accent;
    ctx.lineWidth = 2;
    ctx.strokeRect(3, 3, 244, 116);
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(6, 6, 238, 110);

    ctx.strokeStyle = accent;
    ctx.lineWidth = 1.5;
    ctx.strokeRect(12, 14, 68, 94);
    const hasImg = drawTemplateImage(templateCustomImgObj, 12, 14, 68, 94);
    if (!hasImg) {{
      drawCrown(46, 45, 30, 20, accent);
      ctx.fillStyle = '#000000';
      ctx.font = 'bold 10px Arial, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('HỘI VIÊN VIP', 46, 85);
    }}

    ctx.fillStyle = accent;
    ctx.font = 'bold 12px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText('👑 ' + club.toUpperCase(), 90, 16);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 15px Arial, sans-serif';
    ctx.fillText(name.toUpperCase(), 90, 36);

    ctx.fillStyle = accent;
    ctx.fillRect(90, 56, 144, 20);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 11px Arial, sans-serif';
    ctx.fillText('HỘI VIÊN KIM CƯƠNG', 98, 60);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 11px "JetBrains Mono", Courier, monospace';
    ctx.fillText(cardId, 90, 84);
    ctx.font = '10px Arial, sans-serif';
    ctx.fillText(exp, 90, 98);
  }}

  // 11. Thẻ Học Sinh / Trẻ Em (Chuẩn Full Height)
  function renderKidTagTemplate() {{
    let name = document.getElementById('kidNameInput')?.value || 'LƯƠNG Ý NHI';
    let hCol1 = document.getElementById('kidCol1Header')?.value || 'BA/MẸ';
    let hCol2 = document.getElementById('kidCol2Header')?.value || 'SỐ ĐIỆN THOẠI';
    let parent1 = document.getElementById('kidParent1')?.value || 'LƯƠNG QUANG THANH';
    let phone1 = document.getElementById('kidPhone1')?.value || '0989.146.951';
    let parent2 = document.getElementById('kidParent2')?.value || 'LÊ THỊ THU HƯƠNG';
    let phone2 = document.getElementById('kidPhone2')?.value || '096.3350.567';
    let address = document.getElementById('kidAddress')?.value || 'CHUNG CƯ THE RIVANA - QL13 - HCM';
    const noAccent = document.getElementById('kidNoAccentInput')?.checked ?? false;
    const superBold = document.getElementById('kidBoldFontInput')?.checked ?? true;

    if (noAccent) {{
      name = removeVietnameseTones(name);
      hCol1 = removeVietnameseTones(hCol1);
      hCol2 = removeVietnameseTones(hCol2);
      parent1 = removeVietnameseTones(parent1);
      parent2 = removeVietnameseTones(parent2);
      address = removeVietnameseTones(address);
    }}

    function drawBold(text, x, y, font, align = 'center') {{
      ctx.font = font;
      ctx.textAlign = align;
      ctx.textBaseline = 'middle';
      ctx.fillStyle = '#000000';
      ctx.fillText(text, x, y);
      if (superBold) {{
        ctx.fillText(text, x + 0.35, y);
        ctx.fillText(text, x, y + 0.35);
      }}
    }}

    drawBold(name.toUpperCase(), 125, 12, 'bold 16px Arial, sans-serif');

    const tblX = 4, tblY = 23, tblW = 242, tblH = 74, rowH = 24.66, colSplitX = 138;
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 2;
    ctx.strokeRect(tblX, tblY, tblW, tblH);

    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(tblX, tblY + rowH);
    ctx.lineTo(tblX + tblW, tblY + rowH);
    ctx.moveTo(tblX, tblY + rowH * 2);
    ctx.lineTo(tblX + tblW, tblY + rowH * 2);
    ctx.moveTo(colSplitX, tblY);
    ctx.lineTo(colSplitX, tblY + tblH);
    ctx.stroke();

    drawBold(hCol1.toUpperCase(), tblX + 6, tblY + rowH * 0.5, 'bold 11px Arial, sans-serif', 'left');
    drawBold(hCol2.toUpperCase(), colSplitX + 6, tblY + rowH * 0.5, 'bold 11px Arial, sans-serif', 'left');
    drawBold(parent1.toUpperCase(), tblX + 6, tblY + rowH * 1.5, 'bold 11px Arial, sans-serif', 'left');
    drawBold(phone1, colSplitX + 6, tblY + rowH * 1.5, 'bold 13px "Arial Narrow", Arial, sans-serif', 'left');
    drawBold(parent2.toUpperCase(), tblX + 6, tblY + rowH * 2.5, 'bold 11px Arial, sans-serif', 'left');
    drawBold(phone2, colSplitX + 6, tblY + rowH * 2.5, 'bold 13px "Arial Narrow", Arial, sans-serif', 'left');

    drawBold(address.toUpperCase(), 125, 110, 'bold 11px Arial, sans-serif', 'center');
  }}

  // 12. Thẻ Đỗ Xe Ô Tô
  function renderCarParkingTemplate() {{
    const msg = document.getElementById('carMsgInput')?.value || 'LÀM PHIỀN GỌI KHI CẦN DỜI XE';
    const phone = document.getElementById('carPhoneInput')?.value || '0989.146.951';
    const note = document.getElementById('carNoteInput')?.value || 'CẢM ƠN BẠN ĐÃ THÔNG CẢM!';
    const hasBorder = document.getElementById('carBorderInput')?.checked ?? true;

    if (hasBorder) {{
      ctx.strokeStyle = '#000000';
      ctx.lineWidth = 1;
      ctx.strokeRect(3, 3, 244, 116);
      ctx.strokeRect(6, 6, 238, 110);
    }}
    ctx.fillStyle = '#000000';
    ctx.fillRect(10, 10, 230, 24);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 11px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(msg.toUpperCase(), 125, 22);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 36px "Arial Narrow", Impact, Arial, sans-serif';
    ctx.fillText(phone, 125, 66);

    ctx.font = 'italic 11px Arial, sans-serif';
    ctx.fillText(note, 125, 99);
  }}

  // 13. Biển Chức Danh Để Bàn
  function renderDeskNameplateTemplate() {{
    const company = document.getElementById('npCompany')?.value || 'CÔNG TY CỔ PHẦN CÔNG NGHỆ ABC';
    const name = document.getElementById('npName')?.value || 'NGUYỄN VĂN THANH';
    const title = document.getElementById('npTitle')?.value || 'TRƯỞNG PHÒNG KỸ THUẬT';
    const contact = document.getElementById('npContact')?.value || 'Phòng 402 • Hotline: 0989.146.951';

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(3, 3, 244, 116);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 10px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(company.toUpperCase(), 125, 17);

    ctx.beginPath();
    ctx.moveTo(25, 27);
    ctx.lineTo(225, 27);
    ctx.stroke();

    ctx.font = 'bold 21px Arial, sans-serif';
    ctx.fillText(name.toUpperCase(), 125, 51);

    ctx.fillStyle = '#000000';
    ctx.fillRect(20, 69, 210, 20);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 11px Arial, sans-serif';
    ctx.fillText(title.toUpperCase(), 125, 79);

    ctx.fillStyle = '#000000';
    ctx.font = '10px Arial, sans-serif';
    ctx.fillText(contact, 125, 103);
  }}

  // 14. Thẻ Tên & Hotline
  function renderBadgeTemplate() {{
    const bannerText = document.getElementById('badgeBannerInput')?.value || 'MR THANH - 111009';
    const phoneText = document.getElementById('badgePhoneInput')?.value || '0989.146.951';
    const bannerHeight = parseInt(document.getElementById('badgeBannerHInput')?.value || '42');
    const hasBorder = document.getElementById('badgeBorderInput')?.checked ?? false;

    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, 250, bannerHeight);

    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 18px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(bannerText, 125, bannerHeight / 2);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 36px "Arial Narrow", Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(phoneText, 125, bannerHeight + (122 - bannerHeight) / 2);

    if (hasBorder) {{
      ctx.strokeStyle = '#000000';
      ctx.lineWidth = 1;
      ctx.strokeRect(1, 1, 248, 120);
    }}
  }}

  // 15. Thẻ Giá Siêu Thị ESL
  function renderEslPriceTemplate() {{
    const name = document.getElementById('eslNameInput')?.value || 'NƯỚC NGỌT COCA-COLA';
    const unit = document.getElementById('eslUnitInput')?.value || 'Chai 390ml';
    const oldPrice = document.getElementById('eslOldPriceInput')?.value || '12.000đ';
    const newPrice = document.getElementById('eslNewPriceInput')?.value || '10.000đ';
    const barcodeCode = document.getElementById('eslBarcodeInput')?.value || '893456789012';

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(1, 1, 248, 120);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 13px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.fillText(name.slice(0, 32), 6, 6);

    ctx.font = '11px Arial, sans-serif';
    ctx.fillText(unit, 6, 23);

    if (oldPrice) {{
      ctx.font = '11px Arial, sans-serif';
      ctx.fillText('Gốc: ' + oldPrice, 6, 38);
      const w = ctx.measureText('Gốc: ' + oldPrice).width;
      ctx.beginPath();
      ctx.moveTo(6, 43);
      ctx.lineTo(6 + w, 43);
      ctx.stroke();
    }}

    ctx.font = 'bold 34px "Arial Narrow", Impact, Arial, sans-serif';
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    ctx.fillText(newPrice, 244, 38);

    ctx.beginPath();
    ctx.moveTo(1, 58);
    ctx.lineTo(249, 58);
    ctx.stroke();

    drawBarcode(barcodeCode, 6, 66, 170, 38);

    ctx.font = 'bold 10px Arial, sans-serif';
    ctx.textAlign = 'right';
    ctx.textBaseline = 'middle';
    ctx.fillText('SKU: ' + barcodeCode.slice(-6), 244, 76);
    ctx.fillText('GIẢM GIÁ SỐC', 244, 92);
  }}

  function drawBarcode(text, x, y, width, height) {{
    try {{
      const svg = document.getElementById('barcodeSvg');
      JsBarcode(svg, text, {{ format: "CODE128", width: 1, height: height, displayValue: false, margin: 0 }});
      const xml = new XMLSerializer().serializeToString(svg);
      const img = new Image();
      img.src = 'data:image/svg+xml;base64,' + btoa(xml);
      img.onload = () => {{ ctx.drawImage(img, x, y, width, height); }};
    }} catch (e) {{
      ctx.fillStyle = '#000000';
      for (let i = 0; i < 40; i++) {{
        if (i % 2 === 0 || i % 5 === 0) ctx.fillRect(x + i * 3.5, y, 2, height);
      }}
    }}
  }}

  // 16. Mã QR Thanh Toán Ngân Hàng
  function renderBankQrTemplate() {{
    const qrData = document.getElementById('bankQrDataInput')?.value || '0989146951';
    const bankName = document.getElementById('bankNameInput')?.value || 'MB BANK';
    const accNum = document.getElementById('bankAccInput')?.value || '0989.146.951';
    const accHolder = document.getElementById('bankHolderInput')?.value || 'TRẦN VĂN THANH';

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(1, 1, 248, 120);

    const qrDiv = document.getElementById('qrCodeContainer');
    qrDiv.innerHTML = '';
    try {{
      new QRCode(qrDiv, {{ text: qrData, width: 104, height: 104, colorDark: "#000000", colorLight: "#ffffff", correctLevel: QRCode.CorrectLevel.M }});
      setTimeout(() => {{
        const qrImg = qrDiv.querySelector('img');
        if (qrImg && qrImg.src) {{
          const img = new Image();
          img.src = qrImg.src;
          img.onload = () => {{ ctx.drawImage(img, 9, 9, 104, 104); }};
        }}
      }}, 50);
    }} catch (e) {{}}

    ctx.beginPath();
    ctx.moveTo(122, 1);
    ctx.lineTo(122, 121);
    ctx.stroke();

    ctx.fillStyle = '#000000';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.font = 'bold 13px Arial, sans-serif';
    ctx.fillText(bankName, 129, 12);
    ctx.font = '10px Arial, sans-serif';
    ctx.fillText('Số tài khoản:', 129, 32);
    ctx.font = 'bold 15px "Arial Narrow", Arial, sans-serif';
    ctx.fillText(accNum, 129, 46);
    ctx.font = '10px Arial, sans-serif';
    ctx.fillText('Chủ tài khoản:', 129, 68);
    ctx.font = 'bold 12px Arial, sans-serif';
    ctx.fillText(accHolder.toUpperCase(), 129, 82);
    ctx.font = 'italic 10px Arial, sans-serif';
    ctx.fillText('Quét để chuyển khoản', 129, 102);
  }}

  // 17. Biển Số Bàn & Gọi Món QR
  function renderTableOrderTemplate() {{
    const shopName = document.getElementById('tbShopName')?.value || 'THE COFFEE HOUSE';
    const tableNum = document.getElementById('tbNumber')?.value || '08';
    const qrData = document.getElementById('tbQrData')?.value || 'https://order.menu/table/08';
    const note = document.getElementById('tbNote')?.value || 'QUÉT QR XEM MENU VÀ GỌI MÓN';

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(2, 2, 246, 118);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 14px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('BÀN', 55, 30);
    ctx.font = 'bold 54px "Arial Narrow", Impact, Arial, sans-serif';
    ctx.fillText(tableNum, 55, 75);

    ctx.beginPath();
    ctx.moveTo(110, 8);
    ctx.lineTo(110, 114);
    ctx.stroke();

    ctx.font = 'bold 12px Arial, sans-serif';
    ctx.fillText(shopName.toUpperCase(), 180, 20);

    const qrDiv = document.getElementById('qrCodeContainer');
    qrDiv.innerHTML = '';
    try {{
      new QRCode(qrDiv, {{ text: qrData, width: 72, height: 72, colorDark: "#000000", colorLight: "#ffffff", correctLevel: QRCode.CorrectLevel.M }});
      setTimeout(() => {{
        const qrImg = qrDiv.querySelector('img');
        if (qrImg && qrImg.src) {{
          const img = new Image();
          img.src = qrImg.src;
          img.onload = () => {{ ctx.drawImage(img, 144, 32, 72, 72); }};
        }}
      }}, 50);
    }} catch (e) {{}}

    ctx.font = '9px Arial, sans-serif';
    ctx.fillText(note, 180, 110);
  }}

  // 18. Bảng Trạng Thái Cuộc Họp
  function renderMeetingStatusTemplate() {{
    const mainStatus = document.getElementById('statusMainInput')?.value || 'ĐANG HỌP (BUSY)';
    const subStatus = document.getElementById('statusSubInput')?.value || 'Vui lòng không làm phiền';
    const returnTime = document.getElementById('statusReturnInput')?.value || 'Dự kiến xong: 15h30';
    const contact = document.getElementById('statusContactInput')?.value || 'Khẩn cấp gọi: 0989.146.951';

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 2;
    ctx.strokeRect(3, 3, 244, 116);
    ctx.lineWidth = 1;

    ctx.fillStyle = '#000000';
    ctx.fillRect(8, 8, 234, 44);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 18px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(mainStatus.toUpperCase(), 125, 30);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 13px Arial, sans-serif';
    ctx.fillText(subStatus, 125, 68);
    ctx.font = '11px Arial, sans-serif';
    ctx.fillText(returnTime, 125, 88);
    ctx.font = 'italic 10px Arial, sans-serif';
    ctx.fillText(contact, 125, 106);
  }}

  // 19. Chia Sẻ Mạng Wifi
  function renderWifiTemplate() {{
    const ssid = document.getElementById('wifiSsidInput')?.value || 'KHACH_HANG_VIP';
    const pass = document.getElementById('wifiPassInput')?.value || '88889999';
    const note = document.getElementById('wifiNoteInput')?.value || 'QUÉT QR ĐỂ KẾT NỐI WIFI';

    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, 250, 26);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 13px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(note, 125, 13);

    const wifiString = `WIFI:T:WPA;S:${{ssid}};P:${{pass}};;`;
    const qrDiv = document.getElementById('qrCodeContainer');
    qrDiv.innerHTML = '';
    try {{
      new QRCode(qrDiv, {{ text: wifiString, width: 86, height: 86, colorDark: "#000000", colorLight: "#ffffff", correctLevel: QRCode.CorrectLevel.M }});
      setTimeout(() => {{
        const qrImg = qrDiv.querySelector('img');
        if (qrImg && qrImg.src) {{
          const img = new Image();
          img.src = qrImg.src;
          img.onload = () => {{ ctx.drawImage(img, 8, 31, 86, 86); }};
        }}
      }}, 50);
    }} catch (e) {{}}

    ctx.fillStyle = '#000000';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'top';
    ctx.font = '11px Arial, sans-serif';
    ctx.fillText('Tên Wifi (SSID):', 104, 36);
    ctx.font = 'bold 14px Arial, sans-serif';
    ctx.fillText(ssid, 104, 52);
    ctx.font = '11px Arial, sans-serif';
    ctx.fillText('Mật khẩu:', 104, 76);
    ctx.font = 'bold 16px "Arial Narrow", Arial, sans-serif';
    ctx.fillText(pass, 104, 92);
  }}

  // 20. Đồng Hồ Để Bàn & Thời Tiết
  function renderDeskClockTemplate() {{
    const timeStr = document.getElementById('clockTimeInput')?.value || '14:49';
    const dateStr = document.getElementById('clockDateInput')?.value || 'Thứ Hai, 12/10/2026';
    const temp = document.getElementById('clockTempInput')?.value || '28°C';
    const humi = document.getElementById('clockHumiInput')?.value || '65%';

    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.strokeRect(1, 1, 248, 120);

    ctx.fillStyle = '#000000';
    ctx.font = 'bold 64px "Arial Narrow", Impact, Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(timeStr, 125, 45);

    ctx.beginPath();
    ctx.moveTo(10, 84);
    ctx.lineTo(240, 84);
    ctx.stroke();

    ctx.font = 'bold 12px Arial, sans-serif';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'middle';
    ctx.fillText(dateStr, 12, 102);

    ctx.textAlign = 'right';
    ctx.fillText(`Nhiệt độ: ${{temp}} | Độ ẩm: ${{humi}}`, 238, 102);
  }}

  // 21. Danh Sách Việc Cần Làm
  function renderTodoListTemplate() {{
    const title = document.getElementById('todoTitleInput')?.value || 'MỤC TIÊU HÔM NAY';
    const task1 = document.getElementById('todoTask1Input')?.value || 'Hoàn thành nạp E-Ink 2.13 inch';
    const task2 = document.getElementById('todoTask2Input')?.value || 'Kiểm tra hiển thị chữ tiếng Việt sắc nét';
    const task3 = document.getElementById('todoTask3Input')?.value || 'Bàn giao và tận hưởng dự án!';

    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, 250, 26);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 13px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(title, 125, 13);

    ctx.fillStyle = '#000000';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'middle';
    ctx.font = '12px Arial, sans-serif';

    const tasks = [task1, task2, task3];
    tasks.forEach((t, i) => {{
      const y = 46 + i * 26;
      ctx.strokeRect(10, y - 6, 12, 12);
      if (i === 0) {{
        ctx.beginPath();
        ctx.moveTo(12, y);
        ctx.lineTo(15, y + 3);
        ctx.lineTo(20, y - 4);
        ctx.lineWidth = 1.5;
        ctx.stroke();
        ctx.lineWidth = 1;
      }}
      ctx.fillText(t.slice(0, 32), 30, y);
    }});
  }}

  // 22. Tùy Biến Tự Do
  function renderCustomFreeTemplate() {{
    const topTitle = document.getElementById('freeTitleInput')?.value || 'THÔNG BÁO QUAN TRỌNG';
    const line1 = document.getElementById('freeLine1Input')?.value || 'Khu vực làm việc chuyên viên';
    const line2 = document.getElementById('freeLine2Input')?.value || 'Vui lòng không làm phiền';
    const line3 = document.getElementById('freeLine3Input')?.value || 'Liên hệ quản lý khi cần hỗ trợ';

    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, 250, 28);
    ctx.fillStyle = '#FFFFFF';
    ctx.font = 'bold 13px Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(topTitle, 125, 14);

    ctx.fillStyle = '#000000';
    ctx.font = '13px Arial, sans-serif';
    ctx.fillText(line1, 125, 50);
    ctx.font = 'bold 14px Arial, sans-serif';
    ctx.fillText(line2, 125, 75);
    ctx.font = '11px Arial, sans-serif';
    ctx.fillText(line3, 125, 100);

    ctx.strokeRect(1, 1, 248, 120);
  }}

  // === CUSTOM IMAGE PROCESSOR ===
  function renderCustomImage() {{
    if (!uploadedImageObj) {{
      ctx.fillStyle = '#f8fafc';
      ctx.fillRect(0, 0, 250, 122);
      ctx.fillStyle = '#64748b';
      ctx.font = '13px Arial, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('Chưa tải ảnh lên. Hãy chọn ảnh ở cột bên trái.', 125, 61);
      return;
    }}

    const img = new Image();
    img.onload = () => {{
      const threshold = parseInt(document.getElementById('thresholdSlider').value);
      const invert = document.getElementById('invertCheck').checked;
      const fit = document.getElementById('fitModeSelect').value;

      const targetW = 250, targetH = 122;
      let drawW = targetW, drawH = targetH, drawX = 0, drawY = 0;

      const ratio = img.width / img.height;
      const targetRatio = targetW / targetH;
      if (fit === 'contain') {{
        if (ratio > targetRatio) {{
          drawW = targetW; drawH = targetW / ratio; drawY = (targetH - drawH) / 2;
        }} else {{
          drawH = targetH; drawW = targetH * ratio; drawX = (targetW - drawW) / 2;
        }}
      }} else if (fit === 'cover') {{
        if (ratio > targetRatio) {{
          drawH = targetH; drawW = targetH * ratio; drawX = (targetW - drawW) / 2;
        }} else {{
          drawW = targetW; drawH = targetW / ratio; drawY = (targetH - drawH) / 2;
        }}
      }}

      ctx.fillStyle = '#FFFFFF';
      ctx.fillRect(0, 0, targetW, targetH);
      ctx.drawImage(img, drawX, drawY, drawW, drawH);

      const imgData = ctx.getImageData(0, 0, targetW, targetH);
      const data = imgData.data;

      for (let i = 0; i < data.length; i += 4) {{
        const luma = 0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];
        let val = luma > threshold ? 255 : 0;
        if (invert) val = 255 - val;
        data[i] = val;
        data[i + 1] = val;
        data[i + 2] = val;
        data[i + 3] = 255;
      }}
      ctx.putImageData(imgData, 0, 0);
    }};
    img.src = uploadedImageObj;
  }}

  // === DYNAMIC TEMPLATE INPUT GENERATOR ===
  function updateTemplateInputs() {{
    const sel = document.getElementById('templateSelector').value;
    currentTemplate = sel;
    const container = document.getElementById('dynamicInputs');

    const uploadSnippet = `
      <div class="bg-slate-950/60 p-2.5 rounded-xl border border-slate-800">
        <label class="block text-xs font-semibold text-slate-300 mb-1 flex items-center justify-between">
          <span>Tải ảnh riêng vào khung hình (Tùy chọn):</span>
          <span class="text-[10px] text-blue-400">Tự động co giãn sắc nét</span>
        </label>
        <input type="file" id="templateCustomImgUpload" accept="image/*" class="w-full text-xs text-slate-400 file:mr-2 file:py-1 file:px-2.5 file:rounded-lg file:border-0 file:text-xs file:font-semibold file:bg-blue-600 file:text-white hover:file:bg-blue-500 cursor-pointer">
      </div>
    `;

    let html = '';
    if (sel === 'floral_card') {{
      html = `
        ${{uploadSnippet}}
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tiêu Đề:</label>
          <input type="text" id="flTitle" value="CHÚC MỪNG SINH NHẬT" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Nội Dung Lời Chúc:</label>
          <textarea id="flMsg" rows="2" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">Chúc bạn luôn vui vẻ, hạnh phúc và thành công rực rỡ trong cuộc sống!</textarea>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Người Gửi (Chữ Ký):</label>
          <input type="text" id="flSender" value="Từ: Người bạn thân thiết" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
      `;
    }} else if (sel === 'side_avatar_id') {{
      html = `
        ${{uploadSnippet}}
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Đơn Vị / Công Ty:</label>
          <input type="text" id="avCompany" value="CÔNG TY CỔ PHẦN CÔNG NGHỆ" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Họ Và Tên (Chữ To):</label>
          <input type="text" id="avName" value="LƯƠNG QUANG THANH" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Chức Danh / Vị Trí:</label>
          <input type="text" id="avRole" value="GIÁM ĐỐC KỸ THUẬT" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Mã Nhân Viên:</label>
            <input type="text" id="avId" value="Mã NV: NV-8888" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Hotline Liên Hệ:</label>
            <input type="text" id="avPhone" value="0989.146.951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-mono">
          </div>
        </div>
      `;
    }} else if (sel === 'menu_dish') {{
      html = `
        ${{uploadSnippet}}
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Món Ăn / Đồ Uống:</label>
          <input type="text" id="mnDish" value="TRÀ SEN VÀNG KEM CHEESE" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Giá Tiền:</label>
          <input type="text" id="mnPrice" value="45.000đ" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-sm text-white font-bold text-amber-400">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Mô Tả / Thành Phần Món:</label>
          <textarea id="mnDesc" rows="2" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">Hạt sen bùi béo kết hợp cốt trà thanh mát và lớp màng sữa thơm ngậy.</textarea>
        </div>
      `;
    }} else if (sel === 'pet_id_cute') {{
      html = `
        ${{uploadSnippet}}
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Bé Cưng:</label>
          <input type="text" id="ptName" value="BƠ BÉ BỎNG" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Giống Loài & Tuổi:</label>
            <input type="text" id="ptBreed" value="Corgi Vàng Trắng • 1 Tuổi" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Số ĐT Bố Mẹ:</label>
            <input type="text" id="ptPhone" value="0989.146.951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-mono font-bold">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Lời Nhắn Khi Đi Lạc:</label>
          <input type="text" id="ptNote" value="Nếu em bị lạc, xin vui lòng gọi cho bố mẹ em nhé!" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
      `;
    }} else if (sel === 'sale_voucher') {{
      html = `
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Mức Giảm Giá (Chữ Lớn):</label>
            <input type="text" id="scValue" value="-50%" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold text-rose-400">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Mã Ưu Đãi (Coupon Code):</label>
            <input type="text" id="scCode" value="VIP50K-2026" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-mono font-bold">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tiêu Đề Chương Trình:</label>
          <input type="text" id="scTitle" value="PHIẾU GIẢM GIÁ ĐẶC BIỆT" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white font-bold">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Hạn Sử Dụng & Điều Kiện:</label>
          <input type="text" id="scExp" value="Hạn dùng: 31/12/2026 • Áp dụng toàn hệ thống" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
      `;
    }} else if (sel === 'botanical_plant') {{
      html = `
        ${{uploadSnippet}}
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Tiếng Việt:</label>
          <input type="text" id="btVnName" value="TRẦU BÀ LÁ XẺ (MONSTERA)" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Khoa Học (Latinh):</label>
          <input type="text" id="btSciName" value="Monstera Deliciosa" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white italic">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Chế Độ Tưới Nước:</label>
            <input type="text" id="btWater" value="Tưới nước: 2 lần/tuần (Độ ẩm cao)" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Nhu Cầu Ánh Sáng:</label>
            <input type="text" id="btLight" value="Ánh sáng: Khuếch tán, bóng râm" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
        </div>
      `;
    }} else if (sel === 'art_exhibit') {{
      html = `
        ${{uploadSnippet}}
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Tác Phẩm Nghệ Thuật:</label>
          <input type="text" id="arTitle" value="HOÀNG HÔN TRÊN SÔNG" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Tác Giả (Họa Sĩ):</label>
            <input type="text" id="arArtist" value="Họa sĩ: Trần Minh Đức" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Chất Liệu & Năm:</label>
            <input type="text" id="arMat" value="Sơn dầu trên toan • 2026" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Giá Bán / Niêm Yết:</label>
          <input type="text" id="arPrice" value="Giá niêm yết: 15.000.000 VNĐ" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white font-semibold">
        </div>
      `;
    }} else if (sel === 'hotel_welcome') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Khách Sạn / Cơ Sở:</label>
          <input type="text" id="hwHotel" value="THE RIVANA LUXURY RESIDENCE" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Khách Hàng VIP:</label>
          <input type="text" id="hwGuest" value="ÔNG LƯƠNG QUANG THANH" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Số Phòng:</label>
            <input type="text" id="hwRoom" value="PHÒNG 802 (DELUXE)" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-bold">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Hotline Lễ Tân:</label>
            <input type="text" id="hwHotline" value="Lễ tân 24/7: 0989.146.951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
        </div>
      `;
    }} else if (sel === 'quote_floral') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Câu Châm Ngôn / Lời Hay Ý Đẹp:</label>
          <textarea id="qtText" rows="2" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white font-bold">HÃY LUÔN MỈM CƯỜI, ĐIỀU KỲ DIỆU SẼ ĐẾN VỚI BẠN!</textarea>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Tác Giả / Lời Nhắn:</label>
            <input type="text" id="qtAuthor" value="— Chúc bạn một ngày tốt lành —" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Ngày Tháng:</label>
            <input type="text" id="qtDate" value="Ngày 12/10/2026" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
        </div>
      `;
    }} else if (sel === 'vip_member_club') {{
      html = `
        ${{uploadSnippet}}
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Câu Lạc Bộ / Hệ Thống:</label>
          <input type="text" id="rcClub" value="ELITE DIAMOND CLUB" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white font-bold">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Họ Tên Hội Viên:</label>
          <input type="text" id="rcName" value="LƯƠNG QUANG THANH" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Số Thẻ Hội Viên:</label>
            <input type="text" id="rcId" value="SỐ THẺ: 8888-9999-111009" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-mono">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Hạn Sử Dụng Thẻ:</label>
            <input type="text" id="rcExp" value="HẠN THẺ: 12/2030" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
        </div>
      `;
    }} else if (sel === 'kid_tag') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Họ Và Tên Học Sinh / Trẻ Em:</label>
          <input type="text" id="kidNameInput" value="LƯƠNG Ý NHI" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold focus:ring-2 focus:ring-blue-500">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Tiêu Đề Cột 1:</label>
            <input type="text" id="kidCol1Header" value="BA/MẸ" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-semibold">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Tiêu Đề Cột 2:</label>
            <input type="text" id="kidCol2Header" value="SỐ ĐIỆN THOẠI" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-semibold">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Người Giám Hộ 1:</label>
            <input type="text" id="kidParent1" value="LƯƠNG QUANG THANH" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Số Điện Thoại 1:</label>
            <input type="text" id="kidPhone1" value="0989.146.951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-mono font-bold">
          </div>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Người Giám Hộ 2:</label>
            <input type="text" id="kidParent2" value="LÊ THỊ THU HƯƠNG" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Số Điện Thoại 2:</label>
            <input type="text" id="kidPhone2" value="096.3350.567" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-mono font-bold">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Địa Chỉ Nhà / Lớp Học:</label>
          <input type="text" id="kidAddress" value="CHUNG CƯ THE RIVANA - QL13 - HCM" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white font-medium">
        </div>
        <div class="flex flex-col gap-2 pt-1 border-t border-slate-800/80">
          <label class="flex items-center gap-2 cursor-pointer text-xs text-blue-400">
            <input type="checkbox" id="kidBoldFontInput" checked class="rounded bg-slate-800 border-slate-700 text-blue-600 focus:ring-blue-500">
            <span class="font-medium">Chế độ nét siêu đậm (Super Bold)</span>
          </label>
          <label class="flex items-center gap-2 cursor-pointer text-xs text-slate-300">
            <input type="checkbox" id="kidNoAccentInput" class="rounded bg-slate-800 border-slate-700 text-blue-600 focus:ring-blue-500">
            <span>Chữ không dấu (Tối ưu độ sắc nét viền)</span>
          </label>
        </div>
      `;
    }} else if (sel === 'car_parking') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Lời Nhắn Trên (Banner):</label>
          <input type="text" id="carMsgInput" value="LÀM PHIỀN GỌI KHI CẦN DỜI XE" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Số Điện Thoại Liên Hệ:</label>
          <input type="text" id="carPhoneInput" value="0989.146.951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-mono font-bold">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Lời Cảm Ơn Phía Dưới:</label>
          <input type="text" id="carNoteInput" value="CẢM ƠN BẠN ĐÃ THÔNG CẢM!" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div class="flex items-center pt-1">
          <label class="flex items-center gap-2 cursor-pointer text-xs text-slate-300">
            <input type="checkbox" id="carBorderInput" checked class="rounded bg-slate-800 border-slate-700 text-blue-600">
            <span>Khung viền đôi lịch sự</span>
          </label>
        </div>
      `;
    }} else if (sel === 'desk_nameplate') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Công Ty / Đơn Vị:</label>
          <input type="text" id="npCompany" value="CÔNG TY CỔ PHẦN CÔNG NGHỆ ABC" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Họ Và Tên:</label>
          <input type="text" id="npName" value="NGUYỄN VĂN THANH" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Chức Danh / Vị Trí:</label>
          <input type="text" id="npTitle" value="TRƯỞNG PHÒNG KỸ THUẬT" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Phòng Ban / Liên Hệ:</label>
          <input type="text" id="npContact" value="Phòng 402 • Hotline: 0989.146.951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
      `;
    }} else if (sel === 'badge') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tiêu Đề Banner Trên:</label>
          <input type="text" id="badgeBannerInput" value="MR THANH - 111009" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Số Điện Thoại:</label>
          <input type="text" id="badgePhoneInput" value="0989.146.951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-mono">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Chiều Cao Banner (px):</label>
            <input type="number" id="badgeBannerHInput" value="42" min="30" max="60" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
          </div>
          <div class="flex items-center pt-5">
            <label class="flex items-center gap-2 cursor-pointer text-xs text-slate-300">
              <input type="checkbox" id="badgeBorderInput" class="rounded bg-slate-800 border-slate-700 text-blue-600">
              <span>Khung viền ngoài</span>
            </label>
          </div>
        </div>
      `;
    }} else if (sel === 'esl_price') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Sản Phẩm:</label>
          <input type="text" id="eslNameInput" value="NƯỚC NGỌT COCA-COLA" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white">
        </div>
        <div class="grid grid-cols-3 gap-2">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Quy Cách:</label>
            <input type="text" id="eslUnitInput" value="Chai 390ml" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Giá Cũ (Gốc):</label>
            <input type="text" id="eslOldPriceInput" value="12.000đ" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Giá Khuyến Mãi:</label>
            <input type="text" id="eslNewPriceInput" value="10.000đ" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white font-bold text-amber-400">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Mã Vạch Barcode (Code128):</label>
          <input type="text" id="eslBarcodeInput" value="893456789012" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white font-mono">
        </div>
      `;
    }} else if (sel === 'bank_qr') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Dữ Liệu Mã QR (Link hoặc STK):</label>
          <input type="text" id="bankQrDataInput" value="0989146951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Ngân Hàng:</label>
            <input type="text" id="bankNameInput" value="MB BANK" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Số Tài Khoản:</label>
            <input type="text" id="bankAccInput" value="0989.146.951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white font-mono">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Chủ Tài Khoản:</label>
          <input type="text" id="bankHolderInput" value="TRẦN VĂN THANH" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
      `;
    }} else if (sel === 'table_order') {{
      html = `
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Số Bàn:</label>
            <input type="text" id="tbNumber" value="08" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Cơ Sở / Quán:</label>
            <input type="text" id="tbShopName" value="THE COFFEE HOUSE" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white">
          </div>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Đường Dẫn Menu QR:</label>
          <input type="text" id="tbQrData" value="https://order.menu/table/08" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Lời Nhắc Khách Hàng:</label>
          <input type="text" id="tbNote" value="QUÉT QR XEM MENU VÀ GỌI MÓN" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
      `;
    }} else if (sel === 'meeting_status') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Trạng Thái Chính:</label>
          <input type="text" id="statusMainInput" value="ĐANG HỌP (BUSY)" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-white font-bold">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Nội Dung Chi Tiết:</label>
          <input type="text" id="statusSubInput" value="Vui lòng không làm phiền" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Thời Gian Kết Thúc Dự Kiến:</label>
            <input type="text" id="statusReturnInput" value="Dự kiến xong: 15h30" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Số ĐT Liên Hệ Khẩn Cấp:</label>
            <input type="text" id="statusContactInput" value="Khẩn cấp gọi: 0989.146.951" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-white">
          </div>
        </div>
      `;
    }} else if (sel === 'wifi_share') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tiêu Đề Hướng Dẫn:</label>
          <input type="text" id="wifiNoteInput" value="QUÉT QR ĐỂ KẾT NỐI WIFI" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Tên Mạng Wifi (SSID):</label>
            <input type="text" id="wifiSsidInput" value="KHACH_HANG_VIP" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Mật Khẩu Mạng:</label>
            <input type="text" id="wifiPassInput" value="88889999" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white font-mono">
          </div>
        </div>
      `;
    }} else if (sel === 'desk_clock') {{
      html = `
        <div class="flex items-center gap-2">
          <div class="flex-1">
            <label class="block text-xs font-semibold text-slate-400 mb-1">Giờ Phút:</label>
            <input type="text" id="clockTimeInput" value="14:49" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-sm text-white font-mono">
          </div>
          <button id="setNowBtn" class="mt-5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-300">Lấy giờ hệ thống</button>
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Ngày Tháng:</label>
          <input type="text" id="clockDateInput" value="Thứ Hai, 12/10/2026" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Nhiệt Độ:</label>
            <input type="text" id="clockTempInput" value="28°C" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-1">Độ Ẩm:</label>
            <input type="text" id="clockHumiInput" value="65%" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
          </div>
        </div>
      `;
    }} else if (sel === 'todo_list') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tiêu Đề Danh Sách:</label>
          <input type="text" id="todoTitleInput" value="MỤC TIÊU HÔM NAY" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Công Việc 1:</label>
          <input type="text" id="todoTask1Input" value="Hoàn thành nạp E-Ink 2.13 inch" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Công Việc 2:</label>
          <input type="text" id="todoTask2Input" value="Kiểm tra hiển thị chữ tiếng Việt sắc nét" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Công Việc 3:</label>
          <input type="text" id="todoTask3Input" value="Bàn giao và tận hưởng dự án!" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
      `;
    }} else if (sel === 'custom_free') {{
      html = `
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Tiêu Đề Banner:</label>
          <input type="text" id="freeTitleInput" value="THÔNG BÁO QUAN TRỌNG" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Dòng 1:</label>
          <input type="text" id="freeLine1Input" value="Khu vực làm việc chuyên viên" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Dòng 2:</label>
          <input type="text" id="freeLine2Input" value="Vui lòng không làm phiền" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
        <div>
          <label class="block text-xs font-semibold text-slate-400 mb-1">Dòng 3:</label>
          <input type="text" id="freeLine3Input" value="Liên hệ quản lý khi cần hỗ trợ" class="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
        </div>
      `;
    }}

    container.innerHTML = html;

    container.querySelectorAll('input, textarea').forEach(input => {{
      input.addEventListener('input', renderCanvas);
      input.addEventListener('change', renderCanvas);
    }});

    const setNowBtn = document.getElementById('setNowBtn');
    if (setNowBtn) {{
      setNowBtn.addEventListener('click', () => {{
        const now = new Date();
        const hh = String(now.getHours()).padStart(2, '0');
        const mm = String(now.getMinutes()).padStart(2, '0');
        document.getElementById('clockTimeInput').value = `${{hh}}:${{mm}}`;
        renderCanvas();
      }});
    }}

    const tImgInput = document.getElementById('templateCustomImgUpload');
    if (tImgInput) {{
      tImgInput.addEventListener('change', (e) => {{
        if (e.target.files.length > 0) {{
          const file = e.target.files[0];
          const reader = new FileReader();
          reader.onload = (re) => {{
            const im = new Image();
            im.onload = () => {{
              templateCustomImgObj = im;
              renderCanvas();
            }};
            im.src = re.target.result;
          }};
          reader.readAsDataURL(file);
        }}
      }});
    }}

    renderCanvas();
  }}

  function handleFile(file) {{
    if (!file || !file.type.startsWith('image/')) {{
      alert('Vui lòng chọn tệp hình ảnh hợp lệ.');
      return;
    }}
    const reader = new FileReader();
    reader.onload = (e) => {{
      uploadedImageObj = e.target.result;
      addLog(`Đã tải hình ảnh lên: ${{file.name}}`);
      renderCustomImage();
    }};
    reader.readAsDataURL(file);
  }}

  document.addEventListener('DOMContentLoaded', () => {{
    window.__epdHW.init();

    document.getElementById('connectSerialBtn').addEventListener('click', connectSerial);
    document.getElementById('disconnectBtn').addEventListener('click', disconnectSerial);
    document.getElementById('connectBleBtn').addEventListener('click', connectBle);
    document.getElementById('disconnectBleBtn').addEventListener('click', disconnectBle);
    document.getElementById('pingBtn').addEventListener('click', pingDevice);
    document.getElementById('pushBtn').addEventListener('click', pushToScreen);
    document.getElementById('clearBtn').addEventListener('click', clearScreen);
    document.getElementById('templateSelector').addEventListener('change', updateTemplateInputs);
    document.getElementById('enableRedAccentCheckbox').addEventListener('change', renderCanvas);

    document.getElementById('downloadBtn').addEventListener('click', () => {{
      const a = document.createElement('a');
      a.download = 'eink_preview_250x122.png';
      a.href = canvas.toDataURL('image/png');
      a.click();
    }});

    document.getElementById('clearLogBtn').addEventListener('click', () => {{
      document.getElementById('logOutput').innerHTML = '';
    }});

    const tabTemplate = document.getElementById('tabTemplateBtn');
    const tabCustom = document.getElementById('tabCustomImageBtn');
    const sectionTemplate = document.getElementById('templateSection');
    const sectionCustom = document.getElementById('customImageSection');

    tabTemplate.addEventListener('click', () => {{
      currentMode = 'template';
      tabTemplate.className = 'flex-1 py-2 text-xs sm:text-sm font-semibold rounded-lg transition flex items-center justify-center gap-2 bg-blue-600 text-white shadow';
      tabCustom.className = 'flex-1 py-2 text-xs sm:text-sm font-semibold rounded-lg transition flex items-center justify-center gap-2 text-slate-400 hover:text-white';
      sectionTemplate.classList.remove('hidden');
      sectionCustom.classList.add('hidden');
      renderCanvas();
    }});

    tabCustom.addEventListener('click', () => {{
      currentMode = 'custom_image';
      tabCustom.className = 'flex-1 py-2 text-xs sm:text-sm font-semibold rounded-lg transition flex items-center justify-center gap-2 bg-blue-600 text-white shadow';
      tabTemplate.className = 'flex-1 py-2 text-xs sm:text-sm font-semibold rounded-lg transition flex items-center justify-center gap-2 text-slate-400 hover:text-white';
      sectionCustom.classList.remove('hidden');
      sectionTemplate.classList.add('hidden');
      renderCanvas();
    }});

    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('imageFileInput');
    dropZone.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', (e) => {{
      if (e.target.files.length > 0) handleFile(e.target.files[0]);
    }});
    dropZone.addEventListener('dragover', (e) => {{
      e.preventDefault();
      dropZone.classList.add('border-blue-500', 'bg-blue-950/20');
    }});
    dropZone.addEventListener('dragleave', () => {{
      dropZone.classList.remove('border-blue-500', 'bg-blue-950/20');
    }});
    dropZone.addEventListener('drop', (e) => {{
      e.preventDefault();
      dropZone.classList.remove('border-blue-500', 'bg-blue-950/20');
      if (e.dataTransfer.files.length > 0) handleFile(e.dataTransfer.files[0]);
    }});

    const thresholdSlider = document.getElementById('thresholdSlider');
    thresholdSlider.addEventListener('input', (e) => {{
      document.getElementById('thresholdVal').textContent = e.target.value;
      renderCanvas();
    }});
    document.getElementById('fitModeSelect').addEventListener('change', renderCanvas);
    document.getElementById('invertCheck').addEventListener('change', renderCanvas);

    updateTemplateInputs();
  }});
}})();
  </script>
</body>
</html>
'''
    return html

if __name__ == '__main__':
    content = generate_html()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done! index.html generated with size:", len(content))
