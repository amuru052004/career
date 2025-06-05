# app.py

import openai
import streamlit as st

st.set_page_config(page_title="AI Career Counselor", layout="centered")
st.title("💼 AI Career Counselor")
st.write("Enter your skills, interests, and education to get career guidance.")

# Inputs
skills = st.text_input("Enter your skills (comma-separated):")
interests = st.text_input("Enter your interests:")
education = st.text_input("Enter your education background:")

# Get OpenAI key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_career_advice(skills, interests, education):
    prompt = f"""
    You are a career counselor AI. A user provided the following:

    Skills: {skills}
    Interests: {interests}
    Education: {education}

    Please return:
    1. A recommended career path.
    2. Missing skills the user should gain.
    3. A percentage match of their current profile with the suggested career.
    4. Advice and resources (like courses) to fill skill gaps.

    Format the result with clear bullet points and sections.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert AI career counselor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )
    return response['choices'][0]['message']['content']

if st.button("Get Career Advice"):
    if skills and interests and education:
        with st.spinner("Analyzing your profile..."):
            result = get_career_advice(skills, interests, education)
            st.markdown(result)
    else:
        st.warning("Please fill all the fields.")


