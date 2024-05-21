import streamlit as st

st.title("Test streamlit")
st.header("Head")

st.file_uploader("Upload an image file")
st.text("Plain text section.")
st.selectbox("Select box", ["None", "Filter1", "Filter2"])