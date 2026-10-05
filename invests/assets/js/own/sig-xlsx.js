/*
 * Azqato Invests: Excel and CSV files for the 9 Sig Calculator, with no
 * library (the site has no dependencies). An .xlsx file is a zip of XML parts.
 *
 *   SigXlsx.write(sheets)      -> Blob   sheets: [{ name, rows: [[cell]], widths? }]
 *                                        cell: string, number, null, or
 *                                        { v, fmt: "money"|"price"|"pct"|"shares"|"int"|"date", bold }
 *   SigXlsx.read(arrayBuffer)  -> Promise<[{ name, rows: [[value]] }]>
 *   SigXlsx.csv(rows)          -> string
 *   SigXlsx.parseCsv(text)     -> [[string]]
 *
 * Writing stores the parts uncompressed (any zip reader accepts that).
 * Reading inflates with the browser's own DecompressionStream.
 */
(function (root) {
  "use strict";

  /* ---------- zip ---------- */

  var CRC = (function () {
    var t = new Uint32Array(256);
    for (var n = 0; n < 256; n++) {
      var c = n;
      for (var k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
      t[n] = c >>> 0;
    }
    return t;
  })();

  function crc32(bytes) {
    var c = 0xffffffff;
    for (var i = 0; i < bytes.length; i++) c = CRC[(c ^ bytes[i]) & 0xff] ^ (c >>> 8);
    return (c ^ 0xffffffff) >>> 0;
  }

  function zip(files) {
    var enc = new TextEncoder();
    var parts = [], central = [], offset = 0;
    files.forEach(function (f) {
      var name = enc.encode(f.name);
      var data = typeof f.data === "string" ? enc.encode(f.data) : f.data;
      var crc = crc32(data);
      var head = new DataView(new ArrayBuffer(30));
      head.setUint32(0, 0x04034b50, true);
      head.setUint16(4, 20, true);
      head.setUint16(6, 0x0800, true); // UTF-8 names
      head.setUint16(8, 0, true);      // stored
      head.setUint32(14, crc, true);
      head.setUint32(18, data.length, true);
      head.setUint32(22, data.length, true);
      head.setUint16(26, name.length, true);
      parts.push(new Uint8Array(head.buffer), name, data);
      var cd = new DataView(new ArrayBuffer(46));
      cd.setUint32(0, 0x02014b50, true);
      cd.setUint16(4, 20, true);
      cd.setUint16(6, 20, true);
      cd.setUint16(8, 0x0800, true);
      cd.setUint32(16, crc, true);
      cd.setUint32(20, data.length, true);
      cd.setUint32(24, data.length, true);
      cd.setUint16(28, name.length, true);
      cd.setUint32(42, offset, true);
      central.push(new Uint8Array(cd.buffer), name);
      offset += 30 + name.length + data.length;
    });
    var size = central.reduce(function (s, p) { return s + p.length; }, 0);
    var end = new DataView(new ArrayBuffer(22));
    end.setUint32(0, 0x06054b50, true);
    end.setUint16(8, files.length, true);
    end.setUint16(10, files.length, true);
    end.setUint32(12, size, true);
    end.setUint32(16, offset, true);
    return new Blob(parts.concat(central, [new Uint8Array(end.buffer)]),
                    { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
  }

  function inflate(bytes) {
    if (typeof DecompressionStream === "undefined") {
      return Promise.reject(new Error("This browser can't open .xlsx files. Save the sheet as .csv and import that."));
    }
    var stream = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("deflate-raw"));
    return new Response(stream).arrayBuffer().then(function (b) { return new Uint8Array(b); });
  }

  function unzip(buffer) {
    var v = new DataView(buffer), u8 = new Uint8Array(buffer);
    var e = -1;
    for (var i = u8.length - 22; i >= Math.max(0, u8.length - 65557); i--) {
      if (v.getUint32(i, true) === 0x06054b50) { e = i; break; }
    }
    if (e < 0) return Promise.reject(new Error("This file isn't a valid .xlsx file."));
    var count = v.getUint16(e + 10, true), p = v.getUint32(e + 16, true);
    var dec = new TextDecoder(), jobs = [];
    for (var n = 0; n < count; n++) {
      var method = v.getUint16(p + 10, true);
      var csize = v.getUint32(p + 20, true);
      var nlen = v.getUint16(p + 28, true), xlen = v.getUint16(p + 30, true), clen = v.getUint16(p + 32, true);
      var local = v.getUint32(p + 42, true);
      var name = dec.decode(u8.subarray(p + 46, p + 46 + nlen));
      var start = local + 30 + v.getUint16(local + 26, true) + v.getUint16(local + 28, true);
      var data = u8.subarray(start, start + csize);
      jobs.push((function (name, method, data) {
        var got = method === 0 ? Promise.resolve(data) : method === 8 ? inflate(data)
          : Promise.reject(new Error("This .xlsx uses a compression the browser can't read."));
        return got.then(function (d) { return [name, dec.decode(d)]; });
      })(name, method, data));
      p += 46 + nlen + xlen + clen;
    }
    return Promise.all(jobs).then(function (pairs) {
      var out = {};
      pairs.forEach(function (x) { out[x[0]] = x[1]; });
      return out;
    });
  }

  /* ---------- writing ---------- */

  function xml(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;" }[c];
    }).replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, "");
  }

  // Style ids in styles.xml below.
  var STYLE = { money: 1, price: 2, pct: 3, shares: 4, int: 5, date: 6, bold: 7 };

  function colName(i) {
    var s = "";
    for (i++; i > 0; i = Math.floor((i - 1) / 26)) s = String.fromCharCode(65 + (i - 1) % 26) + s;
    return s;
  }

  function excelDate(iso) {
    var t = Date.parse(iso + "T00:00:00Z");
    return isFinite(t) ? t / 86400000 + 25569 : null;
  }

  function sheetXml(sheet) {
    var rows = sheet.rows.map(function (row, r) {
      var cells = row.map(function (cell, c) {
        if (cell === null || cell === undefined || cell === "") return "";
        var ref = colName(c) + (r + 1);
        var o = typeof cell === "object" ? cell : { v: cell };
        var s = o.bold ? STYLE.bold : o.fmt ? STYLE[o.fmt] : 0;
        var v = o.v;
        if (o.fmt === "date") v = excelDate(v);
        if (typeof v === "number" && isFinite(v)) return '<c r="' + ref + '"' + (s ? ' s="' + s + '"' : "") + "><v>" + v + "</v></c>";
        if (v === null || v === undefined) return "";
        return '<c r="' + ref + '" t="inlineStr"' + (s ? ' s="' + s + '"' : "") + "><is><t>" + xml(v) + "</t></is></c>";
      }).join("");
      return '<row r="' + (r + 1) + '">' + cells + "</row>";
    }).join("");
    var cols = sheet.widths ? "<cols>" + sheet.widths.map(function (w, i) {
      return '<col min="' + (i + 1) + '" max="' + (i + 1) + '" width="' + w + '" customWidth="1"/>';
    }).join("") + "</cols>" : "";
    var freeze = sheet.freeze ? '<sheetViews><sheetView workbookViewId="0"><pane xSplit="' + (sheet.freeze[0] || 0) +
      '" ySplit="' + (sheet.freeze[1] || 0) + '" topLeftCell="' + colName(sheet.freeze[0] || 0) + ((sheet.freeze[1] || 0) + 1) +
      '" activePane="bottomRight" state="frozen"/></sheetView></sheetViews>' : "";
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' +
      '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">' + freeze + cols +
      "<sheetData>" + rows + "</sheetData></worksheet>";
  }

  var STYLES = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' +
    '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">' +
    '<numFmts count="5"><numFmt numFmtId="164" formatCode="&quot;$&quot;#,##0;[Red]-&quot;$&quot;#,##0"/>' +
    '<numFmt numFmtId="165" formatCode="&quot;$&quot;#,##0.00"/><numFmt numFmtId="166" formatCode="0.00%"/>' +
    '<numFmt numFmtId="167" formatCode="#,##0.000"/><numFmt numFmtId="168" formatCode="yyyy-mm-dd"/></numFmts>' +
    '<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="11"/><name val="Calibri"/></font></fonts>' +
    '<fills count="2"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill></fills>' +
    '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>' +
    '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>' +
    '<cellXfs count="8"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>' +
    '<xf numFmtId="164" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>' +
    '<xf numFmtId="165" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>' +
    '<xf numFmtId="166" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>' +
    '<xf numFmtId="167" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>' +
    '<xf numFmtId="3" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>' +
    '<xf numFmtId="168" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>' +
    '<xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/></cellXfs>' +
    '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles></styleSheet>';

  function write(sheets) {
    var files = [
      { name: "[Content_Types].xml", data: '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' +
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">' +
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>' +
        '<Default Extension="xml" ContentType="application/xml"/>' +
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>' +
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>' +
        sheets.map(function (s, i) {
          return '<Override PartName="/xl/worksheets/sheet' + (i + 1) + '.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>';
        }).join("") + "</Types>" },
      { name: "_rels/.rels", data: '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' +
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' +
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>' },
      { name: "xl/workbook.xml", data: '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' +
        '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>' +
        sheets.map(function (s, i) {
          return '<sheet name="' + xml(s.name.slice(0, 31)) + '" sheetId="' + (i + 1) + '" r:id="rId' + (i + 1) + '"/>';
        }).join("") + "</sheets></workbook>" },
      { name: "xl/_rels/workbook.xml.rels", data: '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' +
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' +
        sheets.map(function (s, i) {
          return '<Relationship Id="rId' + (i + 1) + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet' + (i + 1) + '.xml"/>';
        }).join("") +
        '<Relationship Id="rId' + (sheets.length + 1) + '" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>' },
      { name: "xl/styles.xml", data: STYLES }
    ];
    sheets.forEach(function (s, i) { files.push({ name: "xl/worksheets/sheet" + (i + 1) + ".xml", data: sheetXml(s) }); });
    return zip(files);
  }

  /* ---------- reading ---------- */

  function parseXml(text) {
    return new DOMParser().parseFromString(text, "application/xml");
  }

  function kids(el, name) {
    return Array.prototype.filter.call(el.getElementsByTagName("*"), function (n) { return n.localName === name; });
  }

  function textOf(el) {
    return kids(el, "t").map(function (t) { return t.textContent; }).join("");
  }

  function colIndex(ref) {
    var m = /^([A-Z]+)/.exec(ref || ""), n = 0;
    if (!m) return -1;
    for (var i = 0; i < m[1].length; i++) n = n * 26 + m[1].charCodeAt(i) - 64;
    return n - 1;
  }

  function read(buffer) {
    return unzip(buffer).then(function (parts) {
      var wb = parts["xl/workbook.xml"];
      if (!wb) throw new Error("This file isn't an Excel workbook.");
      var strings = parts["xl/sharedStrings.xml"] ? kids(parseXml(parts["xl/sharedStrings.xml"]), "si").map(textOf) : [];
      var rels = {};
      if (parts["xl/_rels/workbook.xml.rels"]) {
        kids(parseXml(parts["xl/_rels/workbook.xml.rels"]), "Relationship").forEach(function (r) {
          var t = r.getAttribute("Target").replace(/^\/?xl\//, "").replace(/^\//, "");
          rels[r.getAttribute("Id")] = "xl/" + t;
        });
      }
      // Which number formats are dates, so serial numbers can be read as dates.
      var dateStyles = {};
      if (parts["xl/styles.xml"]) {
        var st = parseXml(parts["xl/styles.xml"]);
        var custom = {};
        kids(st, "numFmt").forEach(function (f) { custom[f.getAttribute("numFmtId")] = f.getAttribute("formatCode"); });
        var xfs = kids(st, "cellXfs")[0];
        if (xfs) {
          kids(xfs, "xf").forEach(function (xf, i) {
            var id = +xf.getAttribute("numFmtId");
            var code = custom[id] || "";
            if ((id >= 14 && id <= 22) || (id >= 45 && id <= 47) || /[dy]/i.test(code.replace(/\[[^\]]*\]|"[^"]*"/g, ""))) dateStyles[i] = true;
          });
        }
      }
      return kids(parseXml(wb), "sheet").map(function (sh) {
        var rid = sh.getAttributeNS("http://schemas.openxmlformats.org/officeDocument/2006/relationships", "id") || sh.getAttribute("r:id");
        var path = rels[rid];
        var rows = [];
        if (path && parts[path]) {
          kids(parseXml(parts[path]), "row").forEach(function (row) {
            var r = +row.getAttribute("r") - 1;
            var out = rows[r] = rows[r] || [];
            kids(row, "c").forEach(function (c) {
              var ci = colIndex(c.getAttribute("r"));
              if (ci < 0) ci = out.length;
              var t = c.getAttribute("t"), vEl = kids(c, "v")[0], v = vEl ? vEl.textContent : null;
              var val;
              if (t === "s") val = strings[+v];
              else if (t === "inlineStr") val = textOf(c);
              else if (t === "str" || t === "e") val = v;
              else if (t === "b") val = v === "1";
              else if (v !== null) {
                val = +v;
                if (dateStyles[+c.getAttribute("s")]) val = { date: val };
              }
              out[ci] = val;
            });
          });
        }
        for (var i = 0; i < rows.length; i++) rows[i] = rows[i] || [];
        return { name: sh.getAttribute("name"), rows: rows };
      });
    });
  }

  /* ---------- CSV ---------- */

  function csv(rows) {
    return rows.map(function (row) {
      return row.map(function (v) {
        if (v === null || v === undefined) return "";
        if (typeof v === "object") v = v.v;
        var s = String(v);
        return /[",\n\r]/.test(s) ? "\"" + s.replace(/"/g, "\"\"") + "\"" : s;
      }).join(",");
    }).join("\r\n") + "\r\n";
  }

  function parseCsv(text) {
    text = text.replace(/^﻿/, "");
    var sep = (text.split(/\r?\n/)[0].match(/;/g) || []).length > (text.split(/\r?\n/)[0].match(/,/g) || []).length ? ";" : ",";
    var rows = [], row = [], cell = "", q = false;
    for (var i = 0; i < text.length; i++) {
      var ch = text[i];
      if (q) {
        if (ch === "\"") {
          if (text[i + 1] === "\"") { cell += "\""; i++; } else q = false;
        } else cell += ch;
      } else if (ch === "\"") q = true;
      else if (ch === sep) { row.push(cell); cell = ""; }
      else if (ch === "\n" || ch === "\r") {
        if (ch === "\r" && text[i + 1] === "\n") i++;
        row.push(cell); rows.push(row); row = []; cell = "";
      } else cell += ch;
    }
    if (cell || row.length) { row.push(cell); rows.push(row); }
    return rows;
  }

  root.SigXlsx = { write: write, read: read, csv: csv, parseCsv: parseCsv, excelDate: excelDate };
})(window);
