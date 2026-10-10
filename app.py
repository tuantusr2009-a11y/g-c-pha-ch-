
import streamlit as st

st.set_page_config(
    page_title="Website của tôi",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Website đầu tiên của tôi")
st.write("Chào mừng bạn đến với website!")

ten = st.text_input("Nhập tên của bạn:")

if st.button("Gửi"):
    if ten:
        st.success(f"Xin chào {ten}!")
    else:
        st.warning("Bạn hãy nhập tên trước nhé!")

st.subheader("Giới thiệu")
st.write("Website này được xây dựng bằng Python và Streamlit.")

