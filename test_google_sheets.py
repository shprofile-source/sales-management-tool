#!/usr/bin/env python3
"""
Test script để kiểm tra kết nối Google Sheets
Chạy lệnh: python3 test_google_sheets.py
"""

import sys
from pathlib import Path

def test_gspread():
    """Kiểm tra gspread có được cài đặt không"""
    try:
        import gspread
        print("✅ gspread đã được cài đặt")
        return True
    except ImportError:
        print("❌ gspread chưa được cài đặt")
        print("   Chạy: pip install gspread")
        return False

def test_streamlit_secrets():
    """Kiểm tra ~/.streamlit/secrets.toml"""
    secrets_path = Path.home() / ".streamlit" / "secrets.toml"
    
    if not secrets_path.exists():
        print(f"❌ Không tìm thấy: {secrets_path}")
        print("   Hãy tạo file này với nội dung từ GOOGLE_SHEETS_QUICKSTART.md")
        return False
    
    print(f"✅ Tìm thấy: {secrets_path}")
    
    try:
        import toml
        config = toml.load(secrets_path)
        
        if "gcp_service_account" not in config:
            print("❌ [gcp_service_account] không tìm thấy trong secrets.toml")
            return False
        
        print("✅ [gcp_service_account] được tìm thấy")
        
        required_fields = ["type", "project_id", "private_key", "client_email"]
        for field in required_fields:
            if field not in config["gcp_service_account"]:
                print(f"❌ Thiếu field '{field}' trong [gcp_service_account]")
                return False
        
        print("✅ Tất cả các field bắt buộc đã tìm thấy")
        
        if "sheet_id" not in config:
            print("⚠️  Cảnh báo: sheet_id chưa được đặt (để trống)")
            return True
        
        if not config["sheet_id"] or config["sheet_id"].strip() == "":
            print("⚠️  Cảnh báo: sheet_id bị trống")
            return True
        
        print(f"✅ sheet_id được đặt: {config['sheet_id'][:20]}...")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi khi đọc secrets.toml: {e}")
        print("   Kiểm tra định dạng TOML có đúng không")
        return False

def test_google_auth():
    """Kiểm tra có thể xác thực với Google không"""
    try:
        import streamlit as st
        import gspread
        from google.oauth2.service_account import Credentials
        
        # Để lại không test vì cần streamlit secrets
        print("⏭️  Bỏ qua test xác thực (chạy streamlit run app_google_sheets.py để test đầy đủ)")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False

def main():
    print("\n" + "="*60)
    print("🔍 KIỂM TRA CẤU HÌNH GOOGLE SHEETS")
    print("="*60 + "\n")
    
    results = []
    
    print("1️⃣  Kiểm tra gspread...")
    results.append(test_gspread())
    print()
    
    print("2️⃣  Kiểm tra Streamlit Secrets...")
    results.append(test_streamlit_secrets())
    print()
    
    print("3️⃣  Kiểm tra xác thực...")
    results.append(test_google_auth())
    print()
    
    print("="*60)
    if all(results):
        print("✅ Tất cả kiểm tra đã qua!")
        print("\nChạy lệnh:")
        print("  streamlit run app_google_sheets.py")
    else:
        print("❌ Một số kiểm tra không qua, xem chi tiết ở trên")
        print("\n📖 Xem hướng dẫn: GOOGLE_SHEETS_QUICKSTART.md")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
