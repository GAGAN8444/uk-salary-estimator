import streamlit as st

st.title("UK Salary Estimator")
st.write("Tell me about your job and I'll estimate your salary.")

job_title = st.text_input("Job title")
experience = st.slider("Years of experience", 0, 20, 2)
location = st.selectbox("Location", ["London", "Manchester", "Birmingham", "Edinburgh"])

if st.button("Estimate"):
    st.write(f"Estimating salary for a {job_title} in {location} with {experience} years experience...")
    st.success("Model coming soon — but the UI works!")