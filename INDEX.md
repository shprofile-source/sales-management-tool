# 📑 Tài liệu Google Sheets Integration - Mục lục

## 🎯 Bắt đầu từ đây

### 1. **QUICK_COMMANDS.txt** ⭐ (Khởi đầu nhanh)
   - Danh sách các lệnh cần chạy
   - Nhanh nhất để setup (2-3 phút scan lại)

### 2. **GOOGLE_SHEETS_QUICKSTART.md** ⭐⭐ (Hướng dẫn chính)
   - 7 bước chi tiết để setup
   - Có ảnh chỉ dẫn từng bước
   - Khắc phục sự cố
   - **Bắt buộc đọc trước khi bắt đầu**

### 3. **GOOGLE_SHEETS_SETUP.md** (Chi tiết kỹ thuật)
   - Hướng dẫn chi tiết từng bước
   - Thích hợp cho những ai cần hiểu sâu
   - Tất cả các option kỹ thuật

### 4. **README_GOOGLE_SHEETS.md** (Tóm tắt tổng quan)
   - So sánh CSV vs Google Sheets
   - Cấu trúc file
   - Lưu ý bảo mật
   - Câu hỏi thường gặp

---

## 📂 Các tệp chính

### App Files (Ứng dụng)
- **app.py** - Phiên bản cũ (CSV based)
- **app_google_sheets.py** - Phiên bản mới (Google Sheets based) ✨

### Configuration
- **secrets_template.toml** - Template cho `~/.streamlit/secrets.toml`
- **requirements.txt** - Danh sách package cần cài

### Testing & Verification
- **test_google_sheets.py** - Script kiểm tra kết nối
  ```bash
  python3 test_google_sheets.py
  ```

---

## 🚀 Quy trình setup (Tóm tắt)

```
1. pip install gspread
2. Tạo Google Cloud Project
3. Tạo Service Account & JSON Key
4. Cấu hình ~/.streamlit/secrets.toml
5. Tạo Google Sheet
6. Chia sẻ Sheet với Service Account
7. Chạy: streamlit run app_google_sheets.py
```

**Chi tiết đầy đủ:** → Xem `GOOGLE_SHEETS_QUICKSTART.md`

---

## 🔄 Migration từ CSV

### CSV cũ (app.py)
- ✅ Vẫn hoạt động bình thường
- 📁 Dữ liệu lưu tại: `data/database.csv`
- ⚡ Nhanh nhất nhưng chỉ local

### Google Sheets (app_google_sheets.py)
- ✅ Dữ liệu trên Cloud
- 🔄 Real-time sync
- 📱 Truy cập từ mọi nơi
- 🛡️ Tự động backup
- ⚠️ Cần setup ban đầu

**Chọn cái nào?**
- Nếu dùng một mình: CSV là OK
- Nếu team nhiều người / cần cloud: **Google Sheets**

---

## ⚡ Kiểm tra nhanh

```bash
# 1. Kiểm tra cấu hình
cd "/Users/sinhhungtruong/sale manager tool"
python3 test_google_sheets.py

# 2. Chạy app
streamlit run app_google_sheets.py

# 3. Nếu thấy "✅ Kết nối Google Sheets thành công!" = OK ✅
```

---

## 🆘 Gặp vấn đề?

| Vấn đề | Giải pháp |
|--------|----------|
| ❌ ModuleNotFoundError: gspread | `pip install gspread` |
| ❌ Secrets not found | Kiểm tra `~/.streamlit/secrets.toml` |
| ❌ Access denied | Chia sẻ Google Sheet với email từ JSON |
| ❌ Worksheet not found | Kiểm tra sheet name có phải "Products" không |
| ❌ Khác | Chạy `python3 test_google_sheets.py` để chẩn đoán |

**Chi tiết:** → Xem `GOOGLE_SHEETS_QUICKSTART.md` phần "Khắc phục sự cố"

---

## 📌 Lưu ý bảo mật

⚠️ **QUAN TRỌNG**

- ❌ Không commit `secrets.toml` vào Git
- ❌ Không chia sẻ JSON file công khai
- ✅ Thêm vào `.gitignore`:
  ```
  ~/.streamlit/secrets.toml
  google_creds.json
  ```

---

## 📊 So sánh nhanh

| Tính năng | CSV | Google Sheets |
|----------|-----|--------------|
| Cloud storage | ❌ | ✅ |
| Real-time sync | ❌ | ✅ |
| Auto backup | ❌ | ✅ |
| Truy cập từ mọi nơi | ❌ | ✅ |
| Chia sẻ dễ dàng | ❌ | ✅ |
| Setup phức tạp | ❌ | ✅ |
| Tốc độ | ⚡⚡⚡ | ⚡⚡ |

---

## 📞 Support

Nếu cần thêm giúp đỡ:
1. Chạy `python3 test_google_sheets.py` để chẩn đoán
2. Xem error message chi tiết
3. Đọc lại phần "Khắc phục sự cố" trong các hướng dẫn

---

## ✅ Checklist hoàn thành

- [ ] Cài đặt gspread: `pip install gspread`
- [ ] Tạo Google Cloud Project
- [ ] Tạo Service Account & JSON Key
- [ ] Cấu hình `~/.streamlit/secrets.toml`
- [ ] Tạo Google Sheet mới
- [ ] Lấy Sheet ID
- [ ] Chia sẻ Sheet với Service Account
- [ ] Cập nhật `sheet_id` trong `secrets.toml`
- [ ] Chạy: `python3 test_google_sheets.py` ✅
- [ ] Chạy: `streamlit run app_google_sheets.py` ✅
- [ ] Test nhập hàng → Check Google Sheet ✅

---

**🎉 Hoàn tất setup! Dữ liệu giờ đã an toàn trên Google Sheets.**

---

## 📚 Thứ tự đọc khuyên cáo

1. ✅ **QUICK_COMMANDS.txt** - Scan nhanh (2 phút)
2. ✅ **GOOGLE_SHEETS_QUICKSTART.md** - Làm theo (20 phút)
3. ✅ **test_google_sheets.py** - Kiểm tra (1 phút)
4. ✅ **streamlit run app_google_sheets.py** - Chạy (ngay lập tức)

---

**Bắt đầu tại đây: → GOOGLE_SHEETS_QUICKSTART.md 🚀**
