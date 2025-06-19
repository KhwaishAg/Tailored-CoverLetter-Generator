import streamlit as st
from homepage import show_homepage
from form_based import form_based_cover_letter
from resume_based import resume_based_cover_letter

st.set_page_config(page_title="Smart Cover Letter Generator", page_icon="💼")

# Custom CSS for a modern, clean look
st.markdown(
    """
    <style>
    .main {background-color: #f8f9fa;}
    .stButton>button {background-color: #4CAF50; color: white; width: 100%; margin-bottom: 10px;}
    .stDownloadButton>button {background-color: #1976D2; color: white;}
    .sidebar-title {font-size: 1.3rem; font-weight: 600; margin-bottom: 1.5rem;}
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state['page'] = "Home"

st.sidebar.markdown('<div class="sidebar-title">🧭 Navigation</div>', unsafe_allow_html=True)

# Sidebar navigation with buttons (no radio or dropdown)
if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state['page'] = "Home"
if st.sidebar.button("📝 Form-Based", use_container_width=True):
    st.session_state['page'] = "Form-Based"
if st.sidebar.button("📄 Resume-Based", use_container_width=True):
    st.session_state['page'] = "Resume-Based"

# Main area
if st.session_state['page'] == "Home":
    show_homepage()
elif st.session_state['page'] == "Form-Based":
    form_based_cover_letter()
else:
    resume_based_cover_letter()