import streamlit as st
import requests

# Function to extract information from API response
def extract_info(jsondata):
    # Initialize default values for all fields
    extracted_info = {
        'full_name': jsondata.get('full_name', ''),
        'city': jsondata.get('city', ''),
        'state': jsondata.get('state', ''),
        'country': jsondata.get('country', ''),
        'education': jsondata.get('education', []),
        'experiences': jsondata.get('experiences', []),
        'volunteer_work': jsondata.get('volunteer_work', []),
        'certifications': jsondata.get('certifications', []),
        'languages': jsondata.get('languages', []),
        'interests': jsondata.get('interests', [])
    }
    return extracted_info

# Function to retrieve information
def retrieve_info(linkedin_profile_url):
    api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {'linkedin_profile_url': linkedin_profile_url}
    response = requests.get(api_endpoint, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return extract_info(data)
    else:
        st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
        return None

# Initialize linkedin_data as an empty dictionary
linkedin_data = {}

# Streamlit app layout
st.title("CV Generator 📃")
linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url')

if st.button('Retrieve LinkedIn Data'):
    linkedin_data = retrieve_info(linkedin_profile_url) or {}

# Use linkedin_data.get() for default values to avoid NameError
# Personal Information Section
st.header("Personal Information")
name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name')
address = st.text_input("Address", value=f"{linkedin_data.get('city', '')}, {linkedin_data.get('state', '')}, {linkedin_data.get('country', '')}", key='address')
phone = st.text_input("Phone", key='phone')
email = st.text_input("Email", key='email')

# Education Section
st.header("Education")
for i in range(2):  # Assuming up to 2 education entries
    with st.expander(f"Education {i+1}"):
        education = linkedin_data.get('education', [{}])[i] if i < len(linkin_data.get('education', [])) else {}
        university = st.text_input(f"University/School {i+1}", value=education.get('school', ''), key=f'university_{i}')
        degree = st.text_input(f"Degree {i+1}", value=education.get('degree_name', ''), key=f'degree_{i}')
        field_of_study = st.text_input(f"Field of Study {i+1}", value=education.get('field_of_study', ''), key=f'field_of_study_{i}')
        gpa = st.text_input(f"GPA {i+1}", value=education.get('grade', ''), key=f'gpa_{i}')

# Professional Experience Section
st.header("Professional Experience")
for j in range(3):  # Assuming up to 3 experiences
    with st.expander(f"Experience {j+1}"):
        experience = linkedin_data.get('experiences', [{}])[j] if j < len(linkedin_data.get('experiences', [])) else {}
        company = st.text_input(f"Company {j+1}", value=experience.get('company', ''), key=f'company_{j}')
        position = st.text_input(f"Position {j+1}", value=experience.get('title', ''), key=f'position_{j}')
        location = st.text_input(f"Location {j+1}", value=experience.get('location', ''), key=f'location_{j}')
        description = st.text_area(f"Description {j+1}", value=experience.get('description', ''), key=f'description_{j}', height=150)

# Extracurricular Activities Section
st.header("Extracurricular Activities / Engagement")
volunteer_works = ', '.join([work.get('title', '') for work in linkedin_data.get('volunteer_work', [])])
activities = st.text_input("Extracurricular Activities", value=volunteer_works, key='activities')

# Additional Education Section
st.header("Additional Education")
certifications = ', '.join([cert.get('name', '') for cert in linkedin_data.get('certifications', [])])
additional_education = st.text_input("Certificates and Achievements", value=certifications, key='additional_education')

# Skills & Interest Section
st.header("Skills & Interest")
languages = st.text_input("Languages", value=', '.join(linkedin_data.get('languages', [])), key='languages')
computer_skills = st.text_input("Computer Skills", key='computer_skills')
interests = st.text_input("Interests", value=', '.join(linkedin_data.get('interests', [])), key='interests')

# Button to create the CV
if st.button("Create CV"):
    # Logic to create and display/download the CV
    pass
