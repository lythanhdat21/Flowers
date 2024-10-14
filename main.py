import streamlit as st

# Tải nội dung HTML từ GitHub
url = "https://raw.githubusercontent.com/lythanhdat21/Flowers/refs/heads/main/index.html"
# Nhúng file HTML qua iframe
st.markdown(
    f'<iframe src="{html_url}" width="800" height="600" frameborder="0"></iframe>',
    unsafe_allow_html=True,
)
