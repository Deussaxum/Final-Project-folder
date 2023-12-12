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

# If there are education entries from LinkedIn, use them as default values, otherwise use empty strings
university1 = education_entries[0].get('school', '') if education_entries else ''
locationus1 = education_entries[0].get('location', '') if education_entries else ''
majorus1 = education_entries[0].get('field_of_study', '') if education_entries else ''
gpa1 = education_entries[0].get('grade', '') if education_entries else ''

university2 = education_entries[1].get('school', '') if len(education_entries) > 1 else ''
locationus2 = education_entries[1].get('location', '') if len(education_entries) > 1 else ''
majorus2 = education_entries[1].get('field_of_study', '') if len(education_entries) > 1 else ''
gpa2 = education_entries[1].get('grade', '') if len(education_entries) > 1 else ''

# Text inputs for education details with pre-populated or empty values
university1 = st.text_input("Universität/Schule 1", value=university1, key="unique_key_5")
locationus1 = st.text_input("Standort 1", value=locationus1, key="unique_key_6")
majorus1 = st.text_input("Studiengang 1", value=majorus1, key="unique_key_7")
timeus1 = st.text_input("Zeitraum 1", key="unique_key_8")  # No LinkedIn data for the time period
courses1 = st.text_input("Kurse 1", key="unique_key_9")  # No LinkedIn data for courses
gpa1 = st.text_input("GPA 1", value=gpa1, key="unique_key_10")
clubs1 = st.text_input("Clubs/Aktivitäten 1", key="unique_key_11")  # No LinkedIn data for clubs/activities

university2 = st.text_input("Universität/Schule 2", value=university2, key="unique_key_12")
locationus2 = st.text_input("Standort 2", value=locationus2, key="unique_key_13")
majorus2 = st.text_input("Studiengang 2", value=majorus2, key="unique_key_14")
timeus2 = st.text_input("Zeitraum 2", key="unique_key_15")  # No LinkedIn data for the time period
courses2 = st.text_input("Kurse 2", key="unique_key_16")  # No LinkedIn data for courses
gpa2 = st.text_input("GPA 2", value=gpa2, key="unique_key_17")
clubs2 = st.text_input("Clubs/Aktivitäten 2", key="unique_key_18")  # No LinkedIn data for clubs/activities


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