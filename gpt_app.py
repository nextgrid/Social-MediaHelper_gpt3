import welcomeMessage
import appTwitter
import streamlit as st

st.set_page_config(page_title="NewNative", page_icon="🟢", layout="centered")

# Pages as key-value pairs
PAGES = {
    "Dashboard": welcomeMessage,
    "Twitter": appTwitter,
    
    # "GPT-3 Sandbox": app3,
}

st.sidebar.title("Navigation:")

selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
