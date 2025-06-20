import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

def form_based_cover_letter():
    load_dotenv()
    api_key = os.getenv("GEMINI_KEY")
    if not api_key:
        st.error("❌ GEMINI_KEY not found in .env file. Please set it.")
        st.stop()

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    with st.form("cover_letter_form"):
        st.subheader("Form-Based Cover Letter")
        name = st.text_input("Your Name")
        job_title = st.text_input("Job Title")
        primary_skills = st.text_area("Primary Skills (comma-separated)", placeholder="e.g. Python, Django, REST APIs")
        experience = st.slider("Years of Experience", 0, 30, 3)
        client_job_post = st.text_area("Client's Job Post Description")
        relevant_projects = st.text_area("Relevant Projects (comma-separated)")
        client_name = st.text_input("Client Name")
        start_date = st.date_input("Start Date")
        deadline = st.date_input("Deadline")
        tone = st.selectbox("Preferred Tone", ["Formal", "Friendly", "Persuasive", "Confident"])
        submit = st.form_submit_button("Generate Cover Letter")

    if submit:
        data = {
            "name": name,
            "jobTitle": job_title,
            "primarySkills": [s.strip() for s in primary_skills.split(',')],
            "experience": experience,
            "clientJobPost": client_job_post,
            "relevantProjects": [p.strip() for p in relevant_projects.split(',')],
            "clientName": client_name,
            "startDate": str(start_date),
            "deadline": str(deadline),
            "tone": tone
        }
        clean_job_post = data['clientJobPost'].replace('\n', ' ')
        prompt = f"""
You are a skilled freelancer with expertise in writing cover letters that have helped secure jobs. Your task is to craft a compelling cover letter that persuades the client to contact the freelancer.

The letter should focus on results and solving the client’s goals, not just earning money.

Here is the candidate's information in JSON format:

{{
  "Name": "{data['name']}",
  "JobTitle": "{data['jobTitle']}",
  "PrimarySkills": {data['primarySkills']},
  "Experience": {data['experience']},
  "ClientJobPost": "{clean_job_post}",
  "RelevantProjects": {data['relevantProjects']},
  "ClientName": "{data['clientName']}",
  "StartDate": "{data['startDate']}",
  "Deadline": "{data['deadline']}",
  "Tone": "{data['tone']}"
}}

Write a personalized, professional cover letter based on this.
"""
        try:
            response = model.generate_content(prompt)
            st.success("Cover letter generated!")
            st.text_area("Your AI-Generated Cover Letter", response.text, height=350)
            st.download_button("Download Cover Letter", response.text, file_name="cover_letter.txt")
        except Exception as e:
            st.error(f"❌ Error: {e}")