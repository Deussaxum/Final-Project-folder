import streamlit as st
import requests

# Function to extract information from API response
def extract_info(jsondata):
    extracted_info = {
        'full_name': jsondata.get('full_name', ''),
        'city': jsondata.get('city', ''),
        'experiences': jsondata.get('experiences', []),
        'education': jsondata.get('education', []),
        'languages': jsondata.get('languages', []),
        'interests': jsondata.get('interests', []),
        'certifications': jsondata.get('certifications', [])
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

# Streamlit app layout
st.title("CV Generator 📃")
linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url')

tab_titles = ["Consulting 🧮", "Finance 📈", "Corporate 🏢", "Start-Up 🚀", "IT 🖥", "Academic 📚"]
tabs = st.tabs(tab_titles)

for tab, title in zip(tabs, tab_titles):
    with tab:
        linkedin_data = {}
        if st.button(f'Get your input via LinkedIn for {title}', key=f'linkedin_button_{title}'):
            linkedin_data = retrieve_info(linkedin_profile_url) or {}

        # Personal Information Section
        st.header("Personal Information")
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key=f'name_{title}')
        address = st.text_input("Address", value=linkedin_data.get('city', ''), key=f'address_{title}')
        phone = st.text_input("Phone", key=f'phone_{title}')
        email = st.text_input("Email", key=f'email_{title}')

        # Education Section
        st.header("Education")
        for i in range(2):  # Assuming up to 2 education entries
            with st.expander(f"Education {i+1}"):
                university = st.text_input(f"University/School {i+1}", value=linkedin_data.get('education', [{}])[i].get('school', ''), key=f'university_{i}_{title}')
                degree = st.text_input(f"Degree {i+1}", value=linkedin_data.get('education', [{}])[i].get('degree_name', ''), key=f'degree_{i}_{title}')
                field_of_study = st.text_input(f"Field of Study {i+1}", value=linkedin_data.get('education', [{}])[i].get('field_of_study', ''), key=f'field_of_study_{i}_{title}')
                gpa = st.text_input(f"GPA {i+1}", value=linkedin_data.get('education', [{}])[i].get('grade', ''), key=f'gpa_{i}_{title}')

        # Professional Experience Section
        st.header("Professional Experience")
        for j in range(3):  # Assuming up to 3 experiences
            with st.expander(f"Experience {j+1}"):
                exp = linkedin_data.get('experiences', [{}])[j]
                company = st.text_input(f"Company {j+1}", value=exp.get('company', ''), key=f'company_{j}_{title}')
                position = st.text_input(f"Position {j+1}", value=exp.get('title', ''), key=f'position_{j}_{title}')
                location = st.text_input(f"Location {j+1}", value=exp.get('location', ''), key=f'location_{j}_{title}')
                # No field for duration in the API data

        # Extracurricular Activities Section
        st.header("Extracurricular Activities / Engagement")
        activities = st.text_input("Extracurricular Activities", value=', '.join([act.get('title', '') for act in linkedin_data.get('volunteer_work', [])]), key=f'activities_{title}')
        additional_education = st.text_input("Additional Education", key=f'additional_education_{title}')
        certificates = st.text_input("Certificates and Achievements", value=', '.join([cert.get('name', '') for cert in linkedin_data.get('certifications', [])]), key=f'certificates_{title}')

        # Skills & Interest Section
        st.header("Skills & Interest")
        languages = st.text_input("Languages", value=', '.join(linkedin_data.get('languages', [])), key=f'languages_{title}')
        computer_skills = st.text_input("Computer Skills", key=f'computer_skills_{title}')
        interests = st.text_input("Interests", value=', '.join(linkedin_data.get('interests', [])), key=f'interests_{title}')

        # Button to create the CV
        if st.button(f"Create CV for {title}", key=f'create_cv_{title}'):
            # Logic to create and display/download the CV
            pass
