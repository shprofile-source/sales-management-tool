# 🔄 Chuyển đổi từ CSV sang Google Sheets

## 📌 Tài liệu hướng dẫn

| Tệp | Mục đích |
|-----|---------|
| **GOOGLE_SHEETS_QUICKSTART.md** | ⭐ **BẮT ĐẦU ĐÂY** - Hướng dẫn nhanh (10-15 phút) |
| **GOOGLE_SHEETS_SETUP.md** | Hướng dẫn chi tiết từng bước |
| **secrets_template.toml** | Template cấu hình Streamlit secrets |
| **app_google_sheets.py** | App đã cập nhật hỗ trợ Google Sheets |

---

## ⚡ Quy trình nhanh (Tóm tắt)

### 1️⃣ Cài đặt gspread
```bash
pip install gspread
```

### 2️⃣ Tạo Google Service Account & JSON Key
- Vào: https://console.cloud.google.com/
- Tạo Project → Kích hoạt Google Sheets API → Tạo Service Account → Tạo JSON Key
- **Chi tiết xem:** `GOOGLE_SHEETS_QUICKSTART.md` Bước 2

### 3️⃣ Lưu Credentials vào Streamlit Secrets
```bash
# Tạo thư mục nếu chưa có
mkdir -p ~/.streamlit

# Tạo/sửa file secrets.toml
nano ~/.streamlit/secrets.toml
```

Paste nội dung từ JSON vào, thêm `sheet_id` (xem template)

### 4️⃣ Tạo Google Sheet & Lấy Sheet ID
- Tạo sheet mới: https://sheets.google.com
- Rename tab thành: `Products`
- Thêm headers: `Tên hàng | Code | Phân loại | CBM | Packing | Giá | Ảnh`
- Lấy `SHEET_ID` từ URL: `https://docs.google.com/spreadsheets/d/SHEET_ID/edit`

### 5️⃣ Chia sẻ Sheet với Service Account
- Copy email từ JSON (`client_email`)
- Vào Google Sheet → Share → Paste email → Editor → Share

### 6️⃣ Cập nhật `sheet_id` trong `~/.streamlit/secrets.toml`

### 7️⃣ Chạy App
```bash
cd "/Users/sinhhungtruong/sale manager tool"
streamlit run app_google_sheets.py
```

---

## 🔍 So sánh CSV vs Google Sheets

| Tính năng | CSV (Cũ) | Google Sheets (Mới) |
|----------|---------|-------------------|
| 💾 Lưu trữ | Local file | Cloud (Google) |
| 🔄 Sync | Manual | Real-time |
| 🛡️ Backup | Manual | Tự động |
| 📱 Truy cập | Chỉ desktop | Mọi nơi |
| 👥 Chia sẻ | Khó | Dễ |
| ⚡ Tốc độ | Nhanh | Nhanh (có network) |
| 💰 Chi phí | Miễn phí | Miễn phí |

---

## ✅ Kiểm tra kết nối

Sau khi chạy app, bạn sẽ thấy:
- ✅ Thông báo: **"✅ Kết nối Google Sheets thành công!"** - OK
- ❌ Lỗi "Secrets not found" - Xem phần "Khắc phục sự cố"

---

## 📂 Cấu trúc file

```
/Users/sinhhungtruong/sale manager tool/
├── app.py                              (Original - CSV based)
├── app_google_sheets.py               (NEW - Google Sheets based)
├── GOOGLE_SHEETS_QUICKSTART.md        (Quick start guide)
├── GOOGLE_SHEETS_SETUP.md             (Chi tiết)
├── secrets_template.toml              (Template config)
├── images/                            (Ảnh hàng hóa)
└── data/                              (CSV cũ - optional)

~/.streamlit/
└── secrets.toml                       (Credentials của bạn)
```

---

## 🚨 Lưu ý bảo mật

⚠️ **KHÔNG BỎ LỠ!**

- ❌ Không public file `~/.streamlit/secrets.toml`
- ❌ Không commit `secrets.toml` vào Git
- ❌ Không share JSON file trên mạng công khai

✅ Nếu dùng Git, thêm:
```bash
echo "~/.streamlit/secrets.toml" >> .gitignore
```

---

## 🆘 Cần giúp?

1. **Lỗi ngay lúc start:** → Xem `GOOGLE_SHEETS_QUICKSTART.md` phần "Khắc phục sự cố"
2. **Chi tiết kỹ thuật:** → Xem `GOOGLE_SHEETS_SETUP.md`
3. **Template config:** → Xem `secrets_template.toml`

---

## 🎯 Tiếp theo

Sau khi thiết lập thành công:
1. ✅ Kiểm tra dữ liệu có hiện trên Google Sheet không
2. ✅ Thêm vài hàng hóa test
3. ✅ Kiểm tra xóa, sửa hoạt động bình thường
4. ✅ Xuất Excel để xác nhận

---

**Hãy bắt đầu với `GOOGLE_SHEETS_QUICKSTART.md` ngay! 🚀**
