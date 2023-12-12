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

# Retrieve individual address components, defaulting to an empty string if not found
city = linkedin_data.get('city', '')
state = linkedin_data.get('state', '')
country = linkedin_data.get('country', '')

# Construct the address string, only including components that are present
address_components = [comp for comp in [city, state, country] if comp]  # List comprehension to filter out empty components
formatted_address = ', '.join(address_components)  # Join the components with a comma only if they are present

# Streamlit text input fields
name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key='name_key')
address = st.text_input("Adresse", value=formatted_address, key='address_key')
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

# Retrieve up to three experience entries from LinkedIn data if they exist
experience_entries = linkedin_data.get('experiences', [{} for _ in range(3)])

# If there are experience entries from LinkedIn, use them as default values, otherwise use empty strings
experience1 = experience_entries[0].get('company', '') if experience_entries else ''
locatione1 = experience_entries[0].get('location', '') if experience_entries else ''
position1 = experience_entries[0].get('title', '') if experience_entries else ''

experience2 = experience_entries[1].get('company', '') if len(experience_entries) > 1 else ''
locatione2 = experience_entries[1].get('location', '') if len(experience_entries) > 1 else ''
position2 = experience_entries[1].get('title', '') if len(experience_entries) > 1 else ''

experience3 = experience_entries[2].get('company', '') if len(experience_entries) > 2 else ''
locatione3 = experience_entries[2].get('location', '') if len(experience_entries) > 2 else ''
position3 = experience_entries[2].get('title', '') if len(experience_entries) > 2 else ''

# Text inputs for professional experience details with pre-populated or empty values
experience1 = st.text_input("Erfahrung 1", value=experience1, key="unique_key_131")
locatione1 = st.text_input("Standort Erfahrung 1", value=locatione1, key="unique_key_132")
position1 = st.text_input("Position 1", value=position1, key="unique_key_133")
timee1 = st.text_input("Zeitraum Erfahrung 1", key="unique_key_134")
task11 = st.text_area("Aufgaben 1", key='task11_19', height=100)
task12 = st.text_area("Aufgaben 2", key='task12_20', height=100)
task13 = st.text_area("Aufgaben 3", key='task13_21', height=100)

experience2 = st.text_input("Erfahrung 2", value=experience2, key="unique_key_135")
locatione2 = st.text_input("Standort Erfahrung 2", value=locatione2, key="unique_key_136")
position2 = st.text_input("Position 2", value=position2, key="unique_key_137")
timee2 = st.text_input("Zeitraum Erfahrung 2", key="unique_key_138")
task21 = st.text_area("Aufgaben 1", key='task21_22', height=100)
task22 = st.text_area("Aufgaben 2", key='task22_23', height=100)
task23 = st.text_area("Aufgaben 3", key='task23_24', height=100)

experience3 = st.text_input("Erfahrung 3", value=experience3, key="unique_key_139")
locatione3 = st.text_input("Standort Erfahrung 3", value=locatione3, key="unique_key_140")
position3 = st.text_input("Position 3", value=position3, key="unique_key_141")
timee3 = st.text_input("Zeitraum Erfahrung 3", key="unique_key_142")
task31 = st.text_area("Aufgaben 1", key='task31_25', height=100)
task32 = st.text_area("Aufgaben 2", key='task32_26', height=100)
task33 = st.text_area("Aufgaben 3", key='task33_27', height=100)

# Extracurricular Activities / Engagement Section
st.header("Extracurricular Activities / Engagement")

# Retrieve the volunteer work, certifications, languages, and interests from LinkedIn data if they exist
volunteer_work_entries = linkedin_data.get('volunteer_work', [])  # Assuming it's a list of dictionaries
certifications_entries = linkedin_data.get('certifications', [])  # Assuming it's a list of dictionaries
languages_entries = linkedin_data.get('languages', [''])  # Assuming it's a list of titles
interests_entries = linkedin_data.get('interests', [''])  # Assuming it's a list of titles

# Extract titles from volunteer work and certifications
volunteer_work_titles = [entry.get('title', '') for entry in volunteer_work_entries]
certifications_titles = [entry.get('name', '') for entry in certifications_entries]

# Combine the first three titles with a comma
volunteer_work_combined = ', '.join(volunteer_work_titles[0:3])
certifications_combined = ', '.join(certifications_titles[0:3])

# Text inputs for extracurricular activities details with pre-populated or empty values
extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten", value=volunteer_work_combined, key="extracurricular_1_key")
additionaleducation1 = st.text_input("Zusätzliche Bildung", key="additional_education_1_key")  # No specific API data, so left for manual input
certificates1 = st.text_input("Zertifikate und Errungenschaften", value=certifications_combined, key="certificates_1_key")

# Skills & Interest Section
st.header("Skills & Interest")

# Retrieve the computer skills entries from LinkedIn data if they exist
computer_skills_entries = linkedin_data.get('computer_skills', [''])  # Assuming it's a list of titles

# Join the first three entries for languages, interests, and computer skills with a comma
languages_combined = ', '.join(languages_entries[0:3])
interests_combined = ', '.join(interests_entries[0:3])
computer_skills_combined = ', '.join(computer_skills_entries[0:3])

# Text inputs for skills and interests details with pre-populated or empty values
languages1 = st.text_input("Sprachen", value=languages_combined, key="languages_1_key")
computer1 = st.text_input("Computerkenntnisse", value=computer_skills_combined, key="computer_skills_key")
interests1 = st.text_input("Interessen", value=interests_combined, key="interests_1_key")


# Button to create the CV
if st.button("Create CV", key='create_cv_button'):
    # Logic to create and display/download the CV
    pass

