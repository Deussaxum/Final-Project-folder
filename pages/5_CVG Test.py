import streamlit as st
import requests

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
    # Define your API key and headers
    api_key = 'YOUR_API_KEY'  # Be sure to replace with your actual API key
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
        return {}

# Streamlit app layout
st.title("CV Generator 📃")
linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url')

tab_titles = [
    "Consulting 🧮",
    "Finance 📈",
    "Corporate 🏢",
    "Start-Up 🚀",
    "IT 🖥",
    "Academic 📚"
]

tabs = st.tabs(tab_titles)

for tab, title in zip(tabs, tab_titles):
    with tab:
        # Use the LinkedIn API data if available
        linkedin_data = {}
        if st.button(f'Get your input via LinkedIn for {title}', key=f'linkedin_button_{title}'):
            linkedin_data = retrieve_info(linkedin_profile_url)
        
        # Personal Information Section
        st.header("Personal Information")
        name = st.text_input("Name", value=linkedin_data.get('full_name', ''), key=f'name_{title}')
        address = st.text_input("Address", value=linkedin_data.get('city', ''), key=f'address_{title}')
        phone = st.text_input("Phone", key=f'phone_{title}')
        email = st.text_input("Email", key=f'email_{title}')

        # Education Section
        st.header("Education")
        university = st.text_input("University/School", key=f'university_{title}')
        degree = st.text_input("Degree", key=f'degree_{title}')
        field_of_study = st.text_input("Field of Study", key=f'field_of_study_{title}')
        start_year = st.text_input("Start Year", key=f'start_year_{title}')
        end_year = st.text_input("End Year", key=f'end_year_{title}')
        # Add more fields as needed, for example, GPA, courses, etc.

        # Professional Experience Section
        st.header("Professional Experience")
        company = st.text_input("Company", key=f'company_{title}')
        title = st.text_input("Title", key=f'title_{title}')
        start_date = st.text_input("Start Date", key=f'start_date_{title}')
        end_date = st.text_input("End Date", key=f'end_date_{title}')
        description = st.text_area("Description", key=f'description_{title}', height=150)
        # Add more fields or repeat this pattern for multiple experiences.

        # Extracurricular Activities / Engagement Section
        st.header("Extracurricular Activities / Engagement")
        activity = st.text_input("Activity", key=f'activity_{title}')
        role = st.text_input("Role", key=f'role_{title}')
        description = st.text_area("Description", key=f'activity_description_{title}', height=150)

        # Add other sections following the same pattern as above
        # ...
        # Here you would continue with 'Education', 'Professional Experience', etc.
        # Use `linkedin_data` to pre-fill the fields where applicable.

        # Finally, add the button to create the CV at the end of each tab
        if st.button(f"Create CV for {title}", key=f'create_cv_{title}'):
            # Your code to create the CV goes here
            # This could involve formatting the data into a LaTeX template
            # and then displaying or downloading the formatted CV
            pass

# You would continue the pattern above for other sections like 'Education', 'Professional Experience', etc.
