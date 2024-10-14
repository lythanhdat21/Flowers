import streamlit as st
import requests

# Tải nội dung HTML từ GitHub
url = "https://raw.githubusercontent.com/lythanhdat21/Flowers/refs/heads/main/index.html"
response = requests.get(url)

# Kiểm tra nếu tải thành công
if response.status_code == 200:
    html_content = response.text
    # Nhúng nội dung HTML vào Streamlit
    st.components.v1.html(html_content, height=600, scrolling=True)
else:
    st.error("Không thể tải file HTML từ GitHub.")
