import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def resume_based_cover_letter():
    load_dotenv()
    api_key = os.getenv("GEMINI_KEY")
    if not api_key:
        st.error("❌ GEMINI_KEY not found in .env file. Please set it.")
        st.stop()

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    with st.form("resume_cover_letter_form"):
        st.subheader("Resume-Based Cover Letter")
        resume_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")
        job_description = st.text_area("Client's Job Post Description")
        tone = st.selectbox("Preferred Tone", ["Formal", "Friendly", "Persuasive", "Confident"])
        submit_resume = st.form_submit_button("Generate Cover Letter")

    if submit_resume:
        if resume_file is None or not job_description.strip():
            st.warning("Please upload your resume and fill in the job description.")
        else:
            try:
                pdf_reader = PdfReader(resume_file)
                resume_text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
                resume_text = resume_text[:3000]  # Limit for prompt size
                clean_job_post = job_description.replace('\n', ' ')
                prompt = f"""
You are a skilled freelancer with expertise in writing cover letters that have helped secure jobs. Your task is to craft a compelling cover letter that persuades the client to contact the freelancer.

The letter should focus on results and solving the client’s goals, not just earning money.

Here is the candidate's resume content (truncated if too long):

---RESUME---
{resume_text}
---END RESUME---

Here is the job description:
{clean_job_post}

Preferred Tone: {tone}

Write a personalized, professional cover letter based on this.
"""
                response = model.generate_content(prompt)
                st.success("Cover letter generated!")
                st.text_area("Your AI-Generated Cover Letter", response.text, height=350)
                st.download_button("Download Cover Letter", response.text, file_name="cover_letter.txt")
            except Exception as e:
                st.error(f"❌ Error: {e}")
