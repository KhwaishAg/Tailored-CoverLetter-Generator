import streamlit as st
  
def show_homepage():
    st.title("💼 Welcome to Smart AI Cover Letter Generator")

    # Custom CSS for fun, modern cards and sidebar
    st.markdown(
        """
        <style>
        .option-card {
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 0.7rem;
            background: linear-gradient(135deg, #e3f2fd 60%, #fffde7 100%);
            box-shadow: 0 4px 16px rgba(0,0,0,0.07);
            transition: transform 0.1s;
        }
        .option-card:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 32px rgba(25, 118, 210, 0.12);
        }
        .option-title {
            font-size: 1.3rem;
            font-weight: bold;
            color: #1976D2;
        }
        .option-desc {
            font-size: 1.05rem;
            color: #333;
            margin-bottom: 1rem;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown("### 🚀 What would you like to do today?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="option-card">', unsafe_allow_html=True)
        st.markdown('<span class="option-title">📝 Form-Based Cover Letter</span>', unsafe_allow_html=True)
        st.markdown(
            '<div class="option-desc">Manually enter your details<br>'
            'Fine-tune every field<br>'
            'Best for custom, detailed applications</div>',
            unsafe_allow_html=True
        )
        if st.button("✨ Go to Form-Based"):
            st.session_state['page'] = "Form-Based"
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="option-card">', unsafe_allow_html=True)
        st.markdown('<span class="option-title">📄 Resume-Based Cover Letter</span>', unsafe_allow_html=True)
        st.markdown(
            '<div class="option-desc">Upload your resume (PDF)<br>'
            'Let AI extract your info<br>'
            'Fastest way to get started</div>',
            unsafe_allow_html=True
        )
        if st.button("🚀 Go to Resume-Based"):
            st.session_state['page'] = "Resume-Based"
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(
        "<span style='font-size:1.1rem;'>Use the sidebar or the cards above to select your preferred method for generating a tailored cover letter.</span>",
        unsafe_allow_html=True
    )