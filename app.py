import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

JOB_TITLES = [
    "data scientist", "data analyst", "machine learning engineer",
    "software engineer", "backend developer", "frontend developer",
    "full stack developer", "devops engineer", "cloud engineer",
    "product manager", "project manager", "business analyst",
    "cybersecurity analyst", "network engineer", "ai engineer",
    "python developer", "java developer", "react developer",
    "data engineer", "mobile developer"
]

st.title("UK Salary Estimator")
st.write("Live data from the UK job market.")

search = st.text_input("Search job title", "")

filtered = [j for j in JOB_TITLES if search.lower() in j] if search else JOB_TITLES

job_title = st.selectbox("Select job title", filtered)

location = st.selectbox("Location", ["london", "manchester", "birmingham", "edinburgh", "bristol", "leeds", "liverpool"])

experience = st.slider("Years of experience", 0, 20, 2)

if st.button("Estimate Salary"):
    with st.spinner("Fetching live data..."):
        url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "what": job_title,
            "where": location,
            "results_per_page": 20
        }
        response = requests.get(url, params=params)
        data = response.json()

        salaries = [job["salary_max"] for job in data["results"] if "salary_max" in job]

        if salaries:
            avg = sum(salaries) / len(salaries)

            if experience < 2:
                adjusted = avg * 0.75
                level = "Junior"
            elif experience < 5:
                adjusted = avg * 0.90
                level = "Mid-level"
            elif experience < 10:
                adjusted = avg
                level = "Senior"
            else:
                adjusted = avg * 1.20
                level = "Lead/Principal"

            st.success(f"Estimated salary for {level} {job_title} in {location}: £{adjusted:,.0f}")
            st.write(f"Based on {len(salaries)} live listings — experience level: {level}")
        else:
            st.warning("No salary data found, try a different job title or location.")