import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add base64 import
content = content.replace("import pandas as pd", "import base64\nimport pandas as pd")

# 2. Helper function for base64 image
helper_func = """
def get_image_html(img_val):
    if not pd.notna(img_val) or not str(img_val).strip():
        return "https://via.placeholder.com/300x200?text=No+Image"
    img_val = str(img_val).strip()
    if img_val.startswith("http"):
        return img_val
    else:
        path = Path(img_val)
        if path.exists():
            try:
                with open(path, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode()
                mime = "image/jpeg"
                if path.suffix.lower() == ".png":
                    mime = "image/png"
                elif path.suffix.lower() == ".webp":
                    mime = "image/webp"
                return f"data:{mime};base64,{encoded}"
            except:
                pass
        return "https://via.placeholder.com/300x200?text=Not+Found"

"""
content = content.replace("if \"logged_in\" not in st.session_state:", helper_func + "if \"logged_in\" not in st.session_state:")

# 3. Replace CSS block
old_css_start = 'st.markdown(\n    """\n    <style>'
old_css_end = '    </style>\n    """,\n    unsafe_allow_html=True,\n)'

new_css = '''st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        * {
            font-family: 'Inter', 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
        }

        .logo-container {
            text-align: center;
            padding: 2.5rem 0;
            background: linear-gradient(135deg, #4F46E5 0%, #312E81 100%);
            border-radius: 16px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.4);
        }

        .logo-text {
            font-size: 52px;
            font-weight: 800;
            letter-spacing: 2px;
            margin: 1rem 0 0.5rem 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .logo-tagline {
            font-size: 18px;
            font-style: italic;
            color: #FCD34D;
            font-weight: 600;
        }

        .header-info {
            background-color: #F8FAFC;
            padding: 1.2rem 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #4F46E5;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }

        .stButton>button {
            background-color: #4F46E5;
            color: white;
            border-radius: 8px;
            font-weight: 600;
            border: none;
            padding: 0.6rem 1.2rem;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #4338CA;
            color: white;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
            transform: translateY(-2px);
        }

        .stTextInput>div>div>input,
        .stSelectbox>div>div>div>select,
        .stTextArea>div>div>textarea {
            border-radius: 8px;
            border: 1px solid #CBD5E1;
            padding: 0.8rem;
            transition: all 0.2s ease;
        }

        .stTextInput>div>div>input:focus,
        .stSelectbox>div>div>div>select:focus,
        .stTextArea>div>div>textarea:focus {
            border: 2px solid #4F46E5;
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
        }

        .stFileUploader>div>div {
            border: 2px dashed #818CF8;
            border-radius: 12px;
            padding: 2rem;
            background-color: #EEF2FF;
            transition: all 0.3s ease;
        }

        h1, h2, h3, h4 {
            color: #1E293B;
            font-weight: 800;
        }

        .info-box {
            background-color: #FEF3C7;
            padding: 1.2rem;
            border-radius: 12px;
            border-left: 4px solid #F59E0B;
            margin-bottom: 1.5rem;
            color: #92400E;
            font-weight: 500;
        }
        
        /* Grid Card Hover Effects */
        [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 16px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
            background-color: white !important;
            border: 1px solid #E2E8F0 !important;
        }
        [data-testid="stVerticalBlockBorderWrapper"]:hover {
            transform: translateY(-5px) !important;
            box-shadow: 0 15px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1) !important;
            border-color: #818CF8 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)'''

# Regex replace CSS
content = re.sub(r'st\.markdown\(\s*"""\s*<style>.*?</style>\s*""",\s*unsafe_allow_html=True,\s*\)', new_css, content, flags=re.DOTALL)


# 4. Replace List Tab logic completely
# We find the start of `with list_tab:` and replace to the end
list_tab_start = 'with list_tab:\n    st.markdown("### 📋 Danh sách hàng hóa")'
list_tab_idx = content.find(list_tab_start)
if list_tab_idx != -1:
    new_list_tab = '''with list_tab:
    st.markdown("### 📋 Danh sách hàng hóa")
    df = load_data()
    if df.empty:
        st.info("ℹ️ Chưa có mặt hàng nào. Vui lòng thêm hàng hóa nếu bạn là Thu mua.")
    else:
        selected_rows = []
        if is_purchasing:
            edit_code = st.session_state.get("edit_code", "")
            if edit_code:
                edit_df = df[df["Code"].astype(str) == edit_code]
                if not edit_df.empty:
                    row = edit_df.iloc[0]
                    st.markdown("---")
                    st.markdown(f"### ✏️ Chỉnh sửa hàng hóa: {row['Tên hàng']} ({row['Code']})")
                    with st.form("edit_form", clear_on_submit=False):
                        col1, col2 = st.columns(2)
                        edit_name = col1.text_input("📦 Tên hàng", value=row["Tên hàng"])
                        edit_category = col2.selectbox(
                            "📂 Phân loại",
                            options=categories_list() + ["Nhập mới..."],
                            index=0 if row["Phân loại"] in categories_list() else len(categories_list()),
                        )
                        if edit_category == "Nhập mới...":
                            edit_category = col1.text_input("📝 Phân loại mới", value=row["Phân loại"])
                        edit_cbm = col1.text_input("📏 CBM", value=row["CBM"])
                        edit_packing = col2.text_input("📦 Packing", value=row["Packing"])
                        edit_price = col1.text_input("💰 Giá", value=row["Giá"])
                        edit_image = col2.file_uploader("📸 Cập nhật ảnh (không bắt buộc)", type=["jpg", "jpeg", "png", "webp"])

                        save_edit = st.form_submit_button("✅ Cập nhật")
                        cancel_edit = st.form_submit_button("❌ Hủy")
                        if save_edit:
                            success, message = update_product(edit_code, edit_name, edit_category, edit_cbm, edit_packing, edit_price, edit_image if edit_image else None)
                            if success:
                                st.success(message)
                                st.session_state["edit_code"] = ""
                                st.rerun()
                            else:
                                st.error(message)
                        if cancel_edit:
                            st.session_state["edit_code"] = ""
                            st.rerun()
                else:
                    st.session_state["edit_code"] = ""

        # --- SMART FILTERING TOP BAR ---
        st.markdown("---")
        with st.container():
            filter_cols = st.columns([1.5, 2])
            with filter_cols[0]:
                search_q = st.text_input("🔍 Tìm kiếm (Tên / Code)", key="search_q")
            with filter_cols[1]:
                cats = categories_list()
                selected_cats = st.multiselect("📂 Phân loại", options=cats, key="cat_q")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.spinner("Đang tải danh sách..."):
            filtered_df = df.copy()
            if search_q:
                q = search_q.lower()
                filtered_df = filtered_df[
                    filtered_df["Tên hàng"].astype(str).str.lower().str.contains(q) |
                    filtered_df["Code"].astype(str).str.lower().str.contains(q)
                ]
            if selected_cats:
                filtered_df = filtered_df[filtered_df["Phân loại"].isin(selected_cats)]

            if filtered_df.empty:
                st.info("ℹ️ Không có mặt hàng nào khớp với tìm kiếm của bạn.")
            else:
                items_per_page = 20
                total_pages = (len(filtered_df) + items_per_page - 1) // items_per_page
                
                # Check pagination bounds
                current_page_key = "current_page_purchasing" if is_purchasing else "current_page_sale"
                if st.session_state[current_page_key] >= total_pages:
                    st.session_state[current_page_key] = max(0, total_pages - 1)
                
                start_idx = st.session_state[current_page_key] * items_per_page
                end_idx = start_idx + items_per_page
                df_page = filtered_df.iloc[start_idx:end_idx]
                
                # --- GRID LAYOUT ---
                cols_per_row = 4
                for i in range(0, len(df_page), cols_per_row):
                    grid_cols = st.columns(cols_per_row)
                    for j in range(cols_per_row):
                        if i + j < len(df_page):
                            row = df_page.iloc[i + j]
                            with grid_cols[j]:
                                with st.container(border=True):
                                    img_src = get_image_html(row["Ảnh"])
                                    st.markdown(f\'\'\'
                                    <div style="text-align: center;">
                                        <img src="{img_src}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px; margin-bottom: 10px;">
                                    </div>
                                    <div style="padding: 5px;">
                                        <h4 style="margin: 0; color: #1E293B; font-size: 1.1rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{row['Tên hàng']}">{row['Tên hàng']}</h4>
                                        <p style="margin: 5px 0 0 0; color: #64748B; font-size: 0.9rem;">🏷️ <b>Code:</b> {row['Code']}</p>
                                        <p style="margin: 2px 0 0 0; color: #64748B; font-size: 0.9rem;">📂 {row['Phân loại']}</p>
                                        <p style="margin: 5px 0 10px 0; color: #4F46E5; font-weight: 700; font-size: 1.1rem;">💰 {row['Giá']}</p>
                                    </div>
                                    \'\'\', unsafe_allow_html=True)
                                    
                                    selected = st.checkbox("✅ Chọn", key=f"select_{row['Code']}")
                                    if selected:
                                        selected_rows.append(row)
                                        
                                    if is_purchasing:
                                        action_cols = st.columns(2)
                                        if action_cols[0].button("✏️", key=f"edit_{row['Code']}", use_container_width=True):
                                            st.session_state["edit_code"] = str(row["Code"])
                                            st.rerun()
                                        if action_cols[1].button("🗑️", key=f"delete_{row['Code']}", use_container_width=True):
                                            success, message = delete_product(str(row["Code"]))
                                            if success:
                                                st.success(message)
                                            else:
                                                st.error(message)
                                            st.rerun()

                # Pagination UI
                st.markdown("<br>", unsafe_allow_html=True)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    if st.button("⬅️ Trang trước", use_container_width=True, disabled=st.session_state[current_page_key] == 0):
                        st.session_state[current_page_key] -= 1
                        st.rerun()
                with col2:
                    st.markdown(f"<div style='text-align: center; padding: 0.5rem; background: #EEF2FF; border-radius: 8px; color: #4F46E5; font-weight: 600;'>Trang {st.session_state[current_page_key] + 1} / {total_pages}</div>", unsafe_allow_html=True)
                with col3:
                    if st.button("Trang sau ➡️", use_container_width=True, disabled=st.session_state[current_page_key] >= total_pages - 1):
                        st.session_state[current_page_key] += 1
                        st.rerun()

        # Excel Export Bottom
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📊 Xuất Excel PO", use_container_width=True):
                if not selected_rows:
                    st.warning("⚠️ Vui lòng chọn ít nhất một mặt hàng trước khi xuất Excel.")
                else:
                    result_df = pd.DataFrame(selected_rows)
                    buffer = create_excel(result_df)
                    file_name = f"PO_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
                    st.download_button(
                        label="📥 Tải file Excel",
                        data=buffer,
                        file_name=file_name,
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True,
                    )
'''
    content = content[:list_tab_idx] + new_list_tab

with open('app_new.py', 'w', encoding='utf-8') as f:
    f.write(content)

