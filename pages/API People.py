import streamlit as st
import requests
import json

# Function to extract info
def extract_info(jsondata):
    extracted_info = {
        'full_name': 'Not available',
        'city': 'Not available',
        'state': 'Not available',
        'country': 'Not available',
        'education': [],
        'occupation': 'Not available',
        'experiences': [],
        'volunteer_work': 'Not available',
        'certifications': 'Not available',
        'languages': 'Not available',
        'interests': 'Not available'
    }

    if "full_name" in jsondata:
        extracted_info["full_name"] = jsondata["full_name"]

    if "city" in jsondata:
        extracted_info["city"] = jsondata["city"]

    if "state" in jsondata:
        extracted_info["state"] = jsondata["state"]

    if "country" in jsondata:
        extracted_info["country"] = jsondata["country"]

    if "education" in jsondata:
        for educations in jsondata["education"]:
            extracted_info['education'].append({
                'school': educations.get("school", "Not available"),
                'degree_name': educations.get("degree_name", "Not available"),
                'field_of_study': educations.get("field_of_study", "Not available"),
                'grade': educations.get("grade", "Not available")
            })

    if "occupation" in jsondata:
        extracted_info["occupation"] = jsondata["occupation"]

    if "experiences" in jsondata:
        for experience in jsondata["experiences"]:
            extracted_info['experiences'].append({
                'title': experience.get("title", "Not available"),
                'company': experience.get("company", "Not available"),
                'location': experience.get("location", "Not available")
            })

    if "volunteer_work" in jsondata:
        extracted_info["volunteer_work"] = jsondata["volunteer_work"]

    if "certifications" in jsondata:
        extracted_info["certifications"] = jsondata["certifications"]

    if "languages" in jsondata:
        extracted_info["languages"] = jsondata["languages"]

    if "interests" in jsondata:
        extracted_info["interests"] = jsondata["interests"]

    return extracted_info

# Streamlit application starts here
st.title("LinkedIn Profile Scraper")

# Input from user
linkedin_url = st.text_input("Enter LinkedIn Profile URL", "")

if st.button("Fetch Profile Data"):
    if linkedin_url:
        # Call your API with the URL
        api_key = '_EIqMpWEbOnJLoQvNFz1CQ'
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            'linkedin_profile_url': linkedin_url,
            'use_cache': 'if-recent'
        }

        response = requests.get(api_endpoint, params=params, headers=headers)

        if response.status_code == 200:
            jsondata = response.json()
            extracted_info = extract_info(jsondata)

            # Display the extracted information
            st.write(extracted_info)
        else:
            st.error(f"Error: Unable to fetch data. Status code: {response.status_code}")
    else:
        st.error("Please enter a valid LinkedIn URL.")
