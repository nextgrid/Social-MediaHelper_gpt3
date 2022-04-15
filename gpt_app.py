import app1
import app2
import streamlit as st

st.set_page_config(page_title="NewNative", page_icon="🟢", layout="centered")

# Pages as key-value pairs
PAGES = {
    "Dashboard": app1,
    "Summarization": app2,
    # "GPT-3 Sandbox": app3,
}

st.sidebar.title("Navigation:")

selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
