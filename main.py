import streamlit as st
import streamlit.components.v1 as components  # Nhập components module
import requests

# Tải file HTML từ GitHub
url = "https://raw.githubusercontent.com/lythanhdat21/Flowers/refs/heads/main/index.html"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    components.html(html_content, height=300, scrolling=True)  # Sử dụng components.html
else:
    st.error("Không thể tải file HTML từ GitHub.")
