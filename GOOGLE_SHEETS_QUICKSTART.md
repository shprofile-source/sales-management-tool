# Google Sheets Integration - Quick Start

## 📋 Tổng quan

Hướng dẫn này giúp bạn chuyển từ lưu trữ CSV sang **Google Sheets** để dữ liệu được lưu trữ vĩnh viễn trên cloud.

---

## 🚀 Bước 1: Cài đặt gspread

```bash
pip install gspread
```

---

## 🔑 Bước 2: Tạo Google Service Account (5-10 phút)

### A. Vào Google Cloud Console

1. Truy cập: https://console.cloud.google.com/
2. Đăng nhập bằng tài khoản Google

### B. Tạo Project mới

1. Nhấp vào dropdown ở trên cùng (Select a Project)
2. Chọn **NEW PROJECT**
3. Nhập tên: `Streamlit Inventory`
4. Nhấp **CREATE**
5. Đợi 1-2 phút...

### C. Kích hoạt Google Sheets API

1. Tìm kiếm **"Google Sheets API"** ở thanh search
2. Nhấp vào **Google Sheets API**
3. Nhấp **ENABLE**

### D. Tạo Service Account

1. Vào menu bên trái → **APIs & Services** → **Credentials**
2. Nhấp **+ CREATE CREDENTIALS** → **Service Account**
3. Điền:
   - **Service account name**: `streamlit-bot`
   - **Service account ID**: *Tự động*
4. Nhấp **CREATE AND CONTINUE**
5. Bỏ qua các bước tiếp theo, nhấp **DONE**

### E. Tạo JSON Key

1. Từ danh sách Service Accounts, nhấp vào `streamlit-bot`
2. Đi tới tab **KEYS**
3. Nhấp **Add Key** → **Create new key**
4. Chọn **JSON**
5. Nhấp **CREATE**
6. File JSON sẽ tải xuống - **lưu ý nơi lưu file này**

---

## 📝 Bước 3: Lưu Credentials (Cách 1: Dễ nhất)

### Sử dụng Streamlit Secrets

1. Mở file JSON vừa tải xuống
2. Copy **toàn bộ nội dung**
3. Tạo/sửa file: `~/.streamlit/secrets.toml`

   **Trên macOS/Linux:**
   ```bash
   mkdir -p ~/.streamlit
   nano ~/.streamlit/secrets.toml
   ```

4. Paste nội dung từ JSON vào, sau đó thêm `sheet_id`:

   ```toml
   [gcp_service_account]
   type = "service_account"
   project_id = "your-project"
   private_key_id = "..."
   private_key = "..."
   client_email = "streamlit-bot@..."
   client_id = "..."
   auth_uri = "https://accounts.google.com/o/oauth2/auth"
   token_uri = "https://oauth2.googleapis.com/token"
   auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
   client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/..."

   # Thêm dòng này (sẽ fill sau)
   sheet_id = ""
   ```

5. Lưu file (Ctrl+O, Enter, Ctrl+X nếu dùng nano)

---

## 📊 Bước 4: Tạo Google Sheet

### A. Tạo Sheet mới

1. Đi tới: https://sheets.google.com
2. Tạo **New Spreadsheet** mới
3. Đặt tên: `Inventory Data`

### B. Tạo Sheet "Products"

1. Ở sheet "Sheet1", nhấp chuột phải → **Rename**
2. Đổi tên thành: `Products`
3. Thêm header (dòng 1):

   | Tên hàng | Code | Phân loại | CBM | Packing | Giá | Ảnh |
   |---------|------|---------|-----|---------|-----|-----|

4. **Không cần thêm dữ liệu**, app sẽ tự động thêm

### C. Lấy Sheet ID

1. URL sẽ như: `https://docs.google.com/spreadsheets/d/SHEET_ID/edit`
2. Copy phần `SHEET_ID` (chuỗi dài giữa `/d/` và `/edit`)
3. Ví dụ: `1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p`

---

## 👥 Bước 5: Chia sẻ Sheet với Service Account

1. Mở file JSON bạn tải xuống
2. Tìm dòng `"client_email"`, copy email đó
3. Ví dụ: `streamlit-bot@streamlit-inventory-xyz.iam.gserviceaccount.com`
4. Trong Google Sheet, nhấp **Share** (chia sẻ)
5. Paste email vào
6. Chọn quyền: **Editor**
7. Nhấp **Share**

---

## ⚙️ Bước 6: Cập nhật Streamlit Secrets

1. Mở lại `~/.streamlit/secrets.toml`
2. Thay đổi dòng `sheet_id`:

   ```toml
   sheet_id = "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p"
   ```

   (Dùng Sheet ID bạn copy ở bước trên)

3. Lưu file

---

## 🚀 Bước 7: Chạy App

```bash
cd "/Users/sinhhungtruong/sale manager tool"
streamlit run app_google_sheets.py
```

### Kết quả mong đợi:

- ✅ Thấy thông báo: **"✅ Kết nối Google Sheets thành công!"**
- ✅ Khi nhập hàng, dữ liệu sẽ hiển thị trên Google Sheet
- ✅ Tất cả các chức năng (edit, delete, export) vẫn hoạt động bình thường

---

## 🐛 Khắc phục sự cố

### Lỗi: "Secrets not found" hoặc "sheet_id not found"

**Nguyên nhân:** Secrets chưa được cấu hình đúng
**Cách sửa:**
- Kiểm tra file `~/.streamlit/secrets.toml` tồn tại không
- Kiểm tra định dạng TOML có đúng không (không dư/thiếu dấu ngoặc)
- Restart Streamlit: `Ctrl+C` rồi chạy lại

### Lỗi: "Access denied" hoặc "Permission denied"

**Nguyên nhân:** Google Sheet chưa được chia sẻ với Service Account
**Cách sửa:**
- Kiểm tra email `client_email` từ JSON có trùng khớp không
- Chắc chắn đã chia sẻ Sheet với **Editor** quyền
- Thử refresh browser

### Lỗi: "Worksheet 'Products' not found"

**Nguyên nhân:** Sheet chưa có tab "Products"
**Cách sửa:**
- Mở Google Sheet
- Kiểm tra tên tab (phải là `Products`, không phải `Sheet1`)
- Nếu cần, rename sheet và cấu hình lại

### Lỗi: "ModuleNotFoundError: No module named 'gspread'"

**Nguyên nhân:** Chưa cài gspread
**Cách sửa:**
```bash
pip install gspread
```

---

## 📁 File Cấu hình

- **Credentials:** `~/.streamlit/secrets.toml`
- **App:** `app_google_sheets.py`
- **Template:** `secrets_template.toml`
- **Hướng dẫn chi tiết:** `GOOGLE_SHEETS_SETUP.md`

---

## 📌 Lợi ích của Google Sheets

✅ **Cloud Storage** - Dữ liệu an toàn trên Google servers  
✅ **Real-time Sync** - Cập nhật tức thời từ bất kỳ đâu  
✅ **Auto Backup** - Google tự động backup  
✅ **Dễ chia sẻ** - Có thể xem trực tiếp trên sheet  
✅ **Lịch sử** - Google Sheets giữ lịch sử chỉnh sửa  
✅ **Multi-device** - Truy cập từ desktop, mobile, tablet  

---

## ❓ Câu hỏi thường gặp

**Q: Sẽ mất dữ liệu khi chuyển từ CSV sang Google Sheets?**  
A: Không. Bạn có thể giữ file CSV cũ. App sẽ tự động sử dụng Google Sheets nếu được cấu hình.

**Q: Có thể dùng cả CSV lẫn Google Sheets không?**  
A: Có. App hỗ trợ fallback. Nếu Google Sheets không khả dụng, sẽ tự động dùng CSV.

**Q: Tôi có thể xem dữ liệu trực tiếp trên Google Sheet không?**  
A: Có! Mọi dữ liệu nhập trong app sẽ hiển thị trực tiếp trên Google Sheet.

**Q: Chi phí là bao nhiêu?**  
A: Google Sheets API miễn phí (miễn là nằm trong quota hợp lý). Service Account cũng miễn phí.

**Q: Tôi cần phải lo lắng về bảo mật không?**  
A: Nên. Hãy:
- Không share file `secrets.toml` công khai
- Thêm vào `.gitignore` nếu dùng Git
- Chỉ chia sẻ Google Sheet với những người cần quyền truy cập

---

**Chúc bạn thành công! 🎉**
