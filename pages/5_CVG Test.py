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
        return {}

# Initialize linkedin_data as an empty dictionary to avoid NameError
linkedin_data = {}

# Streamlit app layout
st.title("CV Generator 📃")
linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url_key')

if st.button('Retrieve LinkedIn Data', key='retrieve_data_button'):
    linkedin_data = retrieve_info(linkedin_profile_url) or {}

# Personal Information Section
st.header("Persönliche Informationen")
name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name_key')
address = st.text_input("Adresse", value=f"{linkedin_data.get('city', '')}, {linkedin_data.get('state', '')}, {linkedin_data.get('country', '')}", key='address_key')
phone = st.text_input("Telefonnummer", key='phone_key')
email = st.text_input("E-Mail", key='email_key')

# Education Section
st.header("Education")
# Assuming the first two education entries in LinkedIn data (if they exist) are to be used
education_entries = linkedin_data.get('education', [{} for _ in range(2)])
for i in range(2):
    with st.expander(f"Education {i+1}"):
        education = education_entries[i]
        university = st.text_input(f"Universität/Schule {i+1}", value=education.get('school', ''), key=f'university_{i+1}_key')
        locationus = st.text_input(f"Standort {i+1}", value=education.get('location', ''), key=f'location_{i+1}_key')
        majorus = st.text_input(f"Studiengang {i+1}", value=education.get('field_of_study', ''), key=f'major_{i+1}_key')
        timeus = st.text_input(f"Zeitraum {i+1}", key=f'time_{i+1}_key')  # No LinkedIn data for the time period
        courses = st.text_input(f"Kurse {i+1}", key=f'courses_{i+1}_key')  # No LinkedIn data for courses
        gpa = st.text_input(f"GPA {i+1}", value=education.get('grade', ''), key=f'gpa_{i+1}_key')
        clubs = st.text_input(f"Clubs/Aktivitäten {i+1}", key=f'clubs_{i+1}_key')  # No LinkedIn data for clubs/activities

# Professional Experience Section
st.header("Professional Experience")
# Assuming the first three experience entries in LinkedIn data (if they exist) are to be used
experience_entries = linkedin_data.get('experiences', [{} for _ in range(3)])
for j in range(3):
    with st.expander(f"Experience {j+1}"):
        experience = experience_entries[j]
        company = st.text_input(f"Erfahrung {j+1}", value=experience.get('company', ''), key=f'company_{j+1}_key')
        locatione = st.text_input(f"Standort Erfahrung {j+1}", value=experience.get('location', ''), key=f'experience_location_{j+1}_key')
        position = st.text_input(f"Position {j+1}", value=experience.get('title', ''), key=f'position_{j+1}_key')
        timee = st.text_input(f"Zeitraum Erfahrung {j+1}", key=f'experience_time_{j+1}_key')
        # No LinkedIn data for tasks, so leaving them blank for user input
        task1 = st.text_area(f"Aufgaben {j+1} - 1", key=f'task_{j+1}_1_key', height=100)
        task2 = st.text_area(f"Aufgaben {j+1} - 2", key=f'task_{j+1}_2_key', height=100)
        task3 = st.text_area(f"Aufgaben {j+1} - 3", key=f'task_{j+1}_3_key', height=100)

# Extracurricular Activities / Engagement Section
st.header("Extracurricular Activities / Engagement")
extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten", key="extracurricular_1_key")
additionaleducation1 = st.text_input("Zusätzliche Bildung", key="additional_education_1_key")
certificates1 = st.text_input("Zertifikate und Errungenschaften", key="certificates_1_key")

# Skills & Interest Section
st.header("Skills & Interest")
languages1 = st.text_input("Sprachen", key="languages_1_key")
computer1 = st.text_input("Computerkenntnisse", key="computer_skills_key")
interests1 = st.text_input("Interessen", key="interests_1_key")

# Button to create the CV
if st.button("Create CV", key='create_cv_button'):
    # Logic to create and display/download the CV
    pass