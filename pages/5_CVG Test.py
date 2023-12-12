import streamlit as st
import requests

# Define your API key and headers
api_key = 'your_api_key_here'  # Replace with your actual API key
headers = {'Authorization': f'Bearer {api_key}'}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

# Streamlit app layout
st.set_page_config(layout="wide")

# App title
st.title('CV Generator 📃')

# LinkedIn profile URL input field
linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url')

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
        return extract_info(data)
    else:
        st.error(f"Failed to retrieve profile information: HTTP {response.status_code}")
        return {}

# Button to trigger the information retrieval
if st.button('Get your input via LinkedIn'):
    linkedin_data = retrieve_info(linkedin_profile_url)
else:
    linkedin_data = {}

# Define tabs
tab_titles = [
    "Consulting 🧮",
    "Finance 📈",
    "Corporate 🏢",
    "Start-Up 🚀",
    "IT 🖥",
    "Academic 📚"
]
tabs = st.tabs(tab_titles)

# Iterate over each tab and set up the corresponding input fields
for index, title in enumerate(tab_titles):
    with tabs[index]:
        st.header(f"{title} - Personal Information")
        # You can replace 'consulting' with the sector name as needed for different tabs
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key=f"{title}_name")
        address = st.text_input("Adresse", key=f"{title}_address")
        phone = st.text_input("Telefonnummer", key=f"{title}_phone")
        email = st.text_input("E-Mail", key=f"{title}_email")

        st.header(f"{title} - Education")
        # Add education input fields

        st.header(f"{title} - Professional Experience")
        # Add professional experience input fields

        st.header(f"{title} - Extracurricular Activities / Engagement")
        # Add extracurricular activities input fields

        st.header(f"{title} - Skills & Interest")
        # Add skills & interest input fields

        if st.button("CV Erstellen", key=f"{title}_create_cv"):
            # Add logic to create CV
            pass

# Remember to replace 'your_api_key_here' with your actual LinkedIn API key


    # Button zum Erstellen des CVs
    if st.button("CV Erstellen", key="unique_key_36"):
        try:
            with open('template_finance.tex', 'r', encoding='utf-8') as file:
                latex_template = file.read()

            try:
                # Formatierung des LaTeX-Templates
                latex_filled = latex_template.format(
                    name=name,
                    address=address,
                    phone=phone,
                    email=email,
                    university1=university1, 
                    locationus1=locationus1, 
                    majorus1=majorus1, 
                    timeus1=timeus1,
                    courses1=courses1, 
                    gpa1=gpa1, 
                    clubs1=clubs1,
                    university2=university2, 
                    locationus2=locationus2, 
                    majorus2=majorus2, 
                    timeus2=timeus2, 
                    courses2=courses2, 
                    gpa2=gpa2, 
                    clubs2=clubs2, 
                    experience1=experience1, 
                    locatione1=locatione1, 
                    position1=position1, 
                    timee1=timee1, 
                    task11=task11, 
                    task12=task12, 
                    task13=task13, 
                    experience2=experience2, 
                    locatione2=locatione2, 
                    position2=position2, 
                    timee2=timee2, 
                    task21=task21, 
                    task22=task22, 
                    task23=task23, 
                    experience3=experience3,
                    locatione3=locatione3, 
                    position3=position3, 
                    timee3=timee3, 
                    task31=task31, 
                    task32=task32, 
                    task33=task33, 
                    extracurricular1=extracurricular1, 
                    additionaleducation1=additionaleducation1, 
                    certificates1=certificates1, 
                    languages1=languages1,
                    computer1=computer1, 
                    interests1=interests1
                )

                # Anzeigen des gefüllten LaTeX-Codes auf der Streamlit-Oberfläche
                st.text_area("Gefüllter LaTeX-Code", latex_filled, height=300)

            except KeyError as key_err:
                st.error(f"Fehler bei der Formatierung: Unbekannter Platzhalter {key_err}")
            except Exception as format_err:
                st.error(f"Fehler bei der Formatierung: {format_err}")

        except FileNotFoundError:
            st.error("Die LaTeX-Vorlagendatei wurde nicht gefunden.")
        except Exception as e:
            st.error(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

