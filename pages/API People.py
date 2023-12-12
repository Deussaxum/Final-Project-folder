import streamlit as st
import requests

# Define your API key and headers
api_key = '_EIqMpWEbOnJLoQvNFz1CQ'  # Be sure to replace with your actual API key
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

# Streamlit app layout
st.set_page_config(layout="wide")  # Set the page layout to wide

# Create columns for the header and the LinkedIn logo
header_col, logo_col = st.columns([0.9, 0.1])

# Use the first column to display the app title
with header_col:
    st.title('CV Generator 📃')

# Use the second column to display the LinkedIn logo
with logo_col:
    linkedin_logo_url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png'
    st.image(linkedin_logo_url, width=50)

# Function to extract information from API response
def extract_info(jsondata):
    extracted_info = {
        'full_name': jsondata.get('full_name', ''),
        'city': jsondata.get('city', ''),
        'experiences': jsondata.get('experiences', [])
    }
    return extracted_info

# Function to retrieve information
def retrieve_info(linkedin_profile_url):
    params = {'linkedin_profile_url': linkedin_profile_url}
    response = requests.get(api_endpoint, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        info = extract_info(data)
        return info
    else:
        st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
        return {}

linkedin_data = {}
linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url')
if st.button('Get your input via LinkedIn', key='linkedin_button'):
    linkedin_data = retrieve_info(linkedin_profile_url)

# CV Generator tabs
tab_titles = [
    "Consulting 🧮",
    "Finance 📈",
    "Corporate 🏢",
    "Start-Up 🚀",
    "IT 🖥",
    "Academic 📚"
]
tabs = st.tabs(tab_titles)

# Assuming the structure for each tab is the same, I will show the code for the first tab "Consulting"
with tabs[0]:
    st.header("Personal Information")
    name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key="consulting_name")
    address = st.text_input("Adresse", key="consulting_address")
    phone = st.text_input("Telefonnummer", key="consulting_phone")
    email = st.text_input("E-Mail", key="consulting_email")

    st.header("Education")
    university1 = st.text_input("Universität/Schule 1", key="consulting_university1")
    locationus1 = st.text_input("Standort 1", key="consulting_locationus1")
    majorus1 = st.text_input("Studiengang 1", key="consulting_majorus1")
    timeus1 = st.text_input("Zeitraum 1", key="consulting_timeus1")
    # ... repeat for all education inputs

    st.header("Professional Experience")
    # Experience 1
    if linkedin_data and linkedin_data.get('experiences'):
        exp1 = linkedin_data['experiences'][0] if len(linkedin_data['experiences']) > 0 else {}
        experience1 = st.text_input("Erfahrung 1", value=exp1.get('company', ''), key="consulting_experience1")
        position1 = st.text_input("Position 1", value=exp1.get('title', ''), key="consulting_position1")
        # ... and so on for time, tasks, etc., and for other experiences

    st.header("Skills & Interest")
    languages1 = st.text_input("Sprachen", key="consulting_languages1")
    computer1 = st.text_input("Computerkenntnisse", key="consulting_computer1")
    interests1 = st.text_input("Interessen", key="consulting_interests1")
    # ... repeat for all other skills and interests inputs

    if st.button("CV Erstellen", key="consulting_create_cv"):
        # Logic to create CV using the provided information
        pass

# Repeat the same structure for other tabs ("Finance", "Corporate", etc.) with relevant key changes

# Ensure to define the logic to create the CV (where the 'pass' statement is) and any additional functionality as needed.
