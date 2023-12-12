import streamlit as st
import requests

# Function to extract information from API response
def extract_info(jsondata):
    extracted_info = {
        'full_name': jsondata.get('full_name', ''),
        'city': jsondata.get('city', ''),
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
    # Define your API key and headers
    api_key = '_EIqMpWEbOnJLoQvNFz1CQ'  # Replace with your actual API key
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {'linkedin_profile_url': linkedin_profile_url}
    response = requests.get(api_endpoint, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        info = extract_info(data)
        return info
    else:
        st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
        return None

# Streamlit app layout
st.title("CV Generator 📃")
linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url')
if st.button('Retrieve LinkedIn Data'):
    linkedin_data = retrieve_info(linkedin_profile_url)

    if linkedin_data:
        # Personal Information Section
        st.header("Personal Information")
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name')
        address = st.text_input("Address", value=linkedin_data.get('city', ''), key='address')
        phone = st.text_input("Phone", key='phone')
        email = st.text_input("Email", key='email')

        # Education Section
        st.header("Education")
        for i, education in enumerate(linkedin_data.get('education', [])):
            with st.expander(f"Education {i+1}"):
                university = st.text_input(f"University/School {i+1}", value=education.get('school', ''), key=f'university_{i}')
                degree = st.text_input(f"Degree {i+1}", value=education.get('degree_name', ''), key=f'degree_{i}')
                field_of_study = st.text_input(f"Field of Study {i+1}", value=education.get('field_of_study', ''), key=f'field_of_study_{i}')
                gpa = st.text_input(f"GPA {i+1}", value=education.get('grade', ''), key=f'gpa_{i}')

        # Professional Experience Section
        st.header("Professional Experience")
        for j, experience in enumerate(linkedin_data.get('experiences', [])):
            with st.expander(f"Experience {j+1}"):
                company = st.text_input(f"Company {j+1}", value=experience.get('company', ''), key=f'company_{j}')
                position = st.text_input(f"Position {j+1}", value=experience.get('title', ''), key=f'position_{j}')
                location = st.text_input(f"Location {j+1}", value=experience.get('location', ''), key=f'location_{j}')
                description = st.text_area(f"Description {j+1}", key=f'description_{j}', height=150)

        # Extracurricular Activities Section
        st.header("Extracurricular Activities")
        activities = st.text_input("Extracurricular Activities", value=', '.join([work.get('title', '') for work in linkedin_data.get('volunteer_work', [])]), key='activities')

        # Additional Education Section
        st.header("Additional Education")
        certifications = st.text_input("Certificates and Achievements", value=', '.join([cert.get('name', '') for cert in linkedin_data.get('certifications', [])]), key='certifications')

        # Skills & Interest Section
        st.header("Skills & Interest")
        languages = st.text_input("Languages", value=', '.join(linkedin_data.get('languages', [])), key='languages')
        interests = st.text_input("Interests", value=', '.join(linkedin_data.get('interests', [])), key='interests')

        # CV Creation Button
        if st.button("Create CV"):
            # Here you would handle the CV creation logic
            pass
