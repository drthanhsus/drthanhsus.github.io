# -*- coding: utf-8 -*-
"""
Full Generator for E-Ink 2.13 Web Studio (250x128 Resolution, Web Serial & Web Bluetooth)
"""

LZ4_WASM_B64 = 'AGFzbQEAAAABHQVgAAF/YAF/AX9gA39/fwF/YAN/f38AYAJ/fwF/AwcGAAECAgQDBQMBAAEHWgUGbWVtb3J5AgAVZ2V0TGluZWFyTWVtb3J5T2Zmc2V0AAATbHo0QmxvY2tFbmNvZGVCb3VuZAABDmx6NEJsb2NrRW5jb2RlAAIObHo0QmxvY2tEZWNvZGUAAwq2CAYEAEEACx0AIABBgICA8AdLBEBBAA8LIAAgAEH/AW5qQRBqC+0DAQh/IAFBgICA8AdLBEBBAA8LIAFBDUkEQEEADwsgACEGIAAgAWoiCUF7aiIHQXlqIQogAiEBAkADQCAAIApPDQEgAC0AAEEIdCAALQABQRB0ciAALQACQRh0ciEDA0ACQCAAIAdLDQMgA0EIdiAALQADQRh0ciIDQbHz3fF5bEEQdkECdCIFKAIAIQQgBSAANgIAIAAgBGsiCEH//wNKDQAgA0H/AXEgBC0AAEcNACADQQh2Qf8BcSAELQABRw0AIANBEHZB/wFxIAQtAAJHDQAgA0EYdiAELQADRw0AIAAgBmshAyAAQQRqIQAgBEEEaiIFIQQCQANAIAAgB08NASAALQAAIAQtAABHDQEgAEEBaiEAIARBAWohBAwACwALIAIgA0EPIANBD0kbQQR0IAQgBWsiBUEPIAVBD0kbcjoAACACQQFqIQIgA0EPTgRAIAIgAxAEIQILIAIgBiADEAUgAiADaiICIAg6AAAgAiAIQQh2OgABIAJBAmohAiAFQQ9OBEAgAiAFEAQhAgsgACEGDAILIABBAWohAAwACwALAAsgAiABRgRAQQAPCyACIAkgBmsiA0EPIANBD0kbQQR0OgAAIAJBAWohAiADQQ9PBEAgAiADEAQhAgsgAiAGIAMQBSACIANqIAFrC+8BAQV/IAFFBEBBAA8LIAAiAyABaiEGIAIhBQJAA0AgAyAGTw0BIAMtAAAhASADQQFqIQMgAUEEdiIEBEAgBEEPRgRAA0AgAy0AACEAIANBAWohAyAAIARqIQQgAEH/AUYNAAsLIAUgAyAEEAUgBSAEaiEFIAQgA2oiAyAGRg0CCyAFIAMtAAAgAy0AAUEIdHJrIgcgBUYNASAHIAZJDQEgA0ECaiEDIAFBD3FBBGoiBEETRgRAA0AgAy0AACEAIANBAWohAyAAIARqIQQgAEH/AUYNAAsLIAUgByAEEAUgBCAFaiEFDAALAAsgBSACawszACABQQ9rIQEDQCAAIAFB/wEgAUH/AUkbOgAAIABBAWohACABQf8BayIBQQBODQALIAAL/AEAAkADQCACQQhJDQEgACABLQAAOgAAIAAgAS0AAToAASAAIAEtAAI6AAIgACABLQADOgADIAAgAS0ABDoABCAAIAEtAAU6AAUgACABLQAGOgAGIAAgAS0ABzoAByAAQQhqIQAgAUEIaiEBIAJBeGohAgwACwALIAJBBE8EQCAAIAEtAAA6AAAgACABLQABOgABIAAgAS0AAjoAAiAAIAEtAAM6AAMgAEEEaiEAIAFBBGohASACQXxqIQILIAJBAk8EQCAAIAEtAAA6AAAgACABLQABOgABIABBAmohACABQQJqIQEgAkF+aiECCyACBEAgACABLQAAOgAACws='

def hex_escape(s):
    return "".join(f"\\x{ord(c):02x}" for c in s)

# Obfuscated Core Engine (Protected Hardware & WASM Codec)
def get_obfuscated_core_engine():
    h_b64 = LZ4_WASM_B64
    h_header = hex_escape("\r\nBBB,8000,")
    h_typ = hex_escape("\r\nTYP,\r\n")
    h_crlf = hex_escape("\r\n")

    code = f"""
// === PROTECTED HARDWARE ENGINE ===
(function(_0xglobal) {{
  var _0xwB64 = '{h_b64}';
  var _0xinst = null;

  async function _0xinitCodec() {{
    try {{
      var _0xbin = Uint8Array.from(atob(_0xwB64), function(_0xc) {{ return _0xc.charCodeAt(0); }});
      var _0xmod = await WebAssembly.instantiate(_0xbin);
      _0xinst = _0xmod.instance.exports;
      var _0xpages = _0xinst.memory.buffer.byteLength / 65536;
      if (_0xpages < 8) _0xinst.memory.grow(8 - _0xpages);
    }} catch (_0xe) {{
      console.error(_0xe);
    }}
  }}

  function _0xcompressRaw(_0xbuf) {{
    if (!_0xinst) throw new Error("Codec unitialized");
    var _0xmem = new Uint8Array(_0xinst.memory.buffer);
    _0xmem.fill(0, 0, 262144);
    var _0xin = 262144;
    var _0xout = _0xin + 16384;
    _0xmem.set(_0xbuf, _0xin);
    var _0xlen = _0xinst.lz4BlockEncode(_0xin, _0xbuf.length, _0xout);
    return new Uint8Array(_0xinst.memory.buffer, _0xout, _0xlen);
  }}

  function _0xextractBufferFromCanvas(_0xcvs, _0xallowRed) {{
    var _0xoff = document.createElement('canvas');
    _0xoff.width = 128;
    _0xoff.height = 250;
    var _0xctx = _0xoff.getContext('2d');
    _0xctx.fillStyle = '#FFFFFF';
    _0xctx.fillRect(0, 0, 128, 250);
    _0xctx.translate(128, 0);
    _0xctx.rotate(Math.PI / 2);
    _0xctx.drawImage(_0xcvs, 0, 0);

    var _0xdata = _0xctx.getImageData(0, 0, 128, 250).data;
    var _0xbw = new Uint8Array(4000);
    var _0xred = new Uint8Array(4000);

    for (var _0xy = 0; _0xy < 250; _0xy++) {{
      for (var _0xx = 0; _0xx < 128; _0xx++) {{
        var _0xi = (_0xy * 128 + _0xx) * 4;
        var _0xr = _0xdata[_0xi];
        var _0xg = _0xdata[_0xi + 1];
        var _0xb = _0xdata[_0xi + 2];

        var _0xisRed = (_0xallowRed === true) && (_0xr > 140 && _0xr > _0xg * 1.5 && _0xr > _0xb * 1.5);
        var _0xlum = 0.299 * _0xr + 0.587 * _0xg + 0.114 * _0xb;
        var _0xisW = _0xlum > 185;

        var _0xbi = _0xy * 16 + Math.floor(_0xx / 8);
        var _0xbit = 7 - (_0xx % 8);

        if (_0xisRed) {{
          _0xbw[_0xbi] |= (1 << _0xbit);  // White on BW plane
          _0xred[_0xbi] |= (1 << _0xbit); // Red on Red plane
        }} else if (_0xisW) {{
          _0xbw[_0xbi] |= (1 << _0xbit);  // White
        }} else {{
          // Black (0 on BW, 0 on Red)
        }}
      }}
    }}
    var _0xtotal = new Uint8Array(8000);
    _0xtotal.set(_0xbw, 0);
    _0xtotal.set(_0xred, 4000);
    return _0xtotal;
  }}

  var _0xport = null;

  async function _0xopenPort(_0xbaud) {{
    if (!('serial' in navigator)) return false;
    _0xport = await navigator.serial.requestPort();
    await _0xport.open({{ baudRate: _0xbaud, dataBits: 8, stopBits: 1, parity: 'none' }});
    return true;
  }}

  async function _0xclosePort() {{
    if (_0xport) {{
      await _0xport.close();
      _0xport = null;
    }}
  }}

  async function _0xpingHW() {{
    if (!_0xport || !_0xport.writable) return false;
    var _0xw = _0xport.writable.getWriter();
    var _0xenc = new TextEncoder();
    await _0xw.write(_0xenc.encode("{h_typ}"));
    _0xw.releaseLock();

    var _0xr = _0xport.readable.getReader();
    var _0xdec = new TextDecoder();
    var _0xres = "";
    var _0xto = setTimeout(function() {{
      try {{ _0xr.cancel(); }} catch (_0xe) {{}}
    }}, 1500);

    try {{
      while (true) {{
        var _0xchunk = await _0xr.read();
        if (_0xchunk.done) break;
        _0xres += _0xdec.decode(_0xchunk.value);
        if (_0xres.includes('\\n')) break;
      }}
    }} catch (_0xe) {{}} finally {{
      clearTimeout(_0xto);
      _0xr.releaseLock();
    }}
    return (_0xres && _0xres.length > 0);
  }}

  async function _0xtransmitData(_0xraw8000) {{
    if (!_0xport || !_0xport.writable) throw new Error("Chua ket noi thiet bi");
    var _0xcomp = _0xcompressRaw(_0xraw8000);
    var _0xenc = new TextEncoder();
    var _0xhdr = _0xenc.encode("{h_header}" + _0xcomp.length + ",1,");
    var _0xtail = _0xenc.encode("{h_crlf}");

    var _0xw = _0xport.writable.getWriter();
    try {{
      await _0xw.write(_0xhdr);
      await _0xw.write(_0xcomp);
      await new Promise(function(_0xr) {{ setTimeout(_0xr, 10); }});
      await _0xw.write(_0xtail);
    }} finally {{
      _0xw.releaseLock();
    }}
  }}

  async function _0xclearScreenHW() {{
    if (!_0xport || !_0xport.writable) throw new Error("Chua ket noi thiet bi");
    var _0xwBuf = new Uint8Array(8000);
    _0xwBuf.fill(0xFF, 0, 4000);
    _0xwBuf.fill(0x00, 4000, 8000);
    await _0xtransmitData(_0xwBuf);
  }}

  // === WEB BLUETOOTH API SUPPORT ===
  var _0xbleDevice = null;
  var _0xbleServer = null;
  var _0xbleChar = null;

  async function _0xopenBle() {{
    if (!('bluetooth' in navigator)) {{
      throw new Error("Trinh duyet khong ho tro Web Bluetooth. Vui long dung Google Chrome hoac Microsoft Edge.");
    }}
    _0xbleDevice = await navigator.bluetooth.requestDevice({{
      acceptAllDevices: true,
      optionalServices: [
        '0000ffe0-0000-1000-8000-00805f9b34fb',
        '00001800-0000-1000-8000-00805f9b34fb',
        '0000180a-0000-1000-8000-00805f9b34fb'
      ]
    }});
    _0xbleServer = await _0xbleDevice.gatt.connect();
    var _0xservices = await _0xbleServer.getPrimaryServices();
    if (_0xservices && _0xservices.length > 0) {{
      for (var _0xsi = 0; _0xsi < _0xservices.length; _0xsi++) {{
        try {{
          var _0xchars = await _0xservices[_0xsi].getCharacteristics();
          for (var _0xci = 0; _0xci < _0xchars.length; _0xci++) {{
            if (_0xchars[_0xci].properties.write || _0xchars[_0xci].properties.writeWithoutResponse) {{
              _0xbleChar = _0xchars[_0xci];
              break;
            }}
          }}
        }} catch (_0xce) {{}}
        if (_0xbleChar) break;
      }}
    }}
    return (_0xbleDevice.name || "EINK-TAG");
  }}

  async function _0xcloseBle() {{
    if (_0xbleDevice && _0xbleDevice.gatt && _0xbleDevice.gatt.connected) {{
      _0xbleDevice.gatt.disconnect();
    }}
    _0xbleDevice = null;
    _0xbleServer = null;
    _0xbleChar = null;
  }}

  async function _0xtransmitBleData(_0xbuf, _0xonProgress) {{
    if (!_0xbleChar) throw new Error("Chua ket noi Bluetooth toi thiet bi");
    var _0xchunkSize = 240;
    var _0xtotal = _0xbuf.length;
    for (var _0xoffset = 0; _0xoffset < _0xtotal; _0xoffset += _0xchunkSize) {{
      var _0xchunk = _0xbuf.slice(_0xoffset, _0xoffset + _0xchunkSize);
      if (_0xbleChar.properties.writeWithoutResponse) {{
        await _0xbleChar.writeValueWithoutResponse(_0xchunk);
      }} else {{
        await _0xbleChar.writeValue(_0xchunk);
      }}
      if (_0xonProgress) _0xonProgress(Math.min(_0xoffset + _0xchunkSize, _0xtotal), _0xtotal);
      await new Promise(function(_0xr) {{ setTimeout(_0xr, 15); }});
    }}
  }}

  _0xglobal.__epdHW = {{
    init: _0xinitCodec,
    open: _0xopenPort,
    close: _0xclosePort,
    ping: _0xpingHW,
    openBle: _0xopenBle,
    closeBle: _0xcloseBle,
    sendBle: _0xtransmitBleData,
    extract: _0xextractBufferFromCanvas,
    send: _0xtransmitData,
    clear: _0xclearScreenHW,
    isReady: function() {{ return (_0xport !== null && _0xport.writable !== null); }},
    isBleReady: function() {{ return (_0xbleChar !== null); }}
  }};
}})(window);
"""
    return code
