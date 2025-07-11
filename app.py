# app.py
import streamlit as st
import pandas as pd
from matching import JobResumeMatcher

# Initialize the matcher
matcher = JobResumeMatcher()

# Load data
@st.cache_data
def load_data():
    jobs = pd.read_csv('data/job_descriptions.csv')
    resumes = pd.read_csv('data/resumes.csv')
    return jobs, resumes

jobs, resumes = load_data()

# Title
st.title("AI Job Description Matching System")
st.write("Match candidate resumes with job descriptions using advanced AI")

# Sidebar filters
st.sidebar.header("Filters")
job_title_filter = st.sidebar.selectbox("Filter by Job Title", ['All'] + list(jobs['title'].unique()))
exp_level_filter = st.sidebar.selectbox("Filter by Experience Level", ['All'] + list(jobs['experience_level'].unique()))

# Apply filters
filtered_jobs = jobs.copy()
if job_title_filter != 'All':
    filtered_jobs = filtered_jobs[filtered_jobs['title'] == job_title_filter]
if exp_level_filter != 'All':
    filtered_jobs = filtered_jobs[filtered_jobs['experience_level'] == exp_level_filter]

# Display filtered jobs
st.header("Available Job Positions")
st.dataframe(filtered_jobs[['title', 'experience_level', 'required_skills']])

# Select a job to match
selected_job_id = st.selectbox(
    "Select a job to find matching candidates",
    filtered_jobs['job_id']
)

selected_job = filtered_jobs[filtered_jobs['job_id'] == selected_job_id].iloc[0]

# Display selected job details
st.subheader(f"Selected Job: {selected_job['title']}")
st.write(f"**Experience Level:** {selected_job['experience_level']}")
st.write("**Required Skills:**")
st.write(selected_job['required_skills'])
st.write("**Job Description:**")
st.write(selected_job['description'])

if st.button("Find Matching Candidates"):
    with st.spinner('Calculating matches using AI...'):
        results = matcher.get_matched_results(jobs, resumes, job_id=selected_job_id)
        
        st.subheader("Top Matching Candidates")
        for i, match in enumerate(results['matches']):
            st.write(f"### Match #{i+1} - Score: {match['match_score']:.2f}")
            st.write(f"**Name:** {match['candidate_name']}")
            st.write(f"**Experience:** {match['experience_years']} years")
            st.write(f"**Education:** {match['education']}")
            st.write("**Skills:**")
            st.write(match['skills'])
            st.write("---")

# Optional: Show all data
if st.checkbox("Show raw data"):
    st.subheader("Job Descriptions Data")
    st.dataframe(jobs)
    st.subheader("Resumes Data")
    st.dataframe(resumes)