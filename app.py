import streamlit as st
from wizard import wizard_ui
from dashboard import dashboard_ui
from login import show_login

if "user" not in st.session_state:
    show_login()
    st.stop()
elif not st.session_state.get("wizard_complete", False):
    wizard_ui()
else:
    dashboard_ui()
