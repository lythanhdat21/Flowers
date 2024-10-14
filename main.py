import streamlit as st
import streamlit.components.v1 as components
import requests

# Tải file HTML từ GitHub
url = "https://raw.githubusercontent.com/lythanhdat21/Flowers/refs/heads/main/index.html"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    components.html(html_content, height=300, scrolling=True)  # Sử dụng components.html
else:
    if response.status_code == 404:
        st.error("Không tìm thấy file HTML trên GitHub.")
    elif response.status_code == 403:
        st.error("Truy cập bị từ chối. Kiểm tra quyền truy cập tới file HTML.")
    else:
        st.error(f"Có lỗi xảy ra: {response.status_code}.")
