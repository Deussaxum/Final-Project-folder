with tabs[3]:

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
    linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url_key_4')

    if st.button('Retrieve LinkedIn Data', key='retrieve_data_button_4'):
        linkedin_data = retrieve_info(linkedin_profile_url) or {}

    # Personal Information Section
    st.header("Your CV, Your Story: Complete the Chapters")

    # Retrieve individual address components, defaulting to an empty string if not found
    with st.expander("Personal Information", expanded=False):  # 'expanded=True' means the section will be expanded by default
        city = st.session_state['linkedin_data'].get('city', '')
        state = st.session_state['linkedin_data'].get('state', '')
        country = st.session_state['linkedin_data'].get('country', '')

        address_components = [comp for comp in [city, state, country] if comp]
        formatted_address = ', '.join(address_components)

        name = st.text_input("Name", value=st.session_state['linkedin_data'].get('full_name', ''), key='name_key_4')
        address = st.text_input("Address", value=formatted_address, key='address_key_4')
        phone = st.text_input("Phone Number", key='phone_key_4')
        email = st.text_input("E-Mail", key='email_key_4')

    # Education Section
    # Assuming the first two education entries in LinkedIn data (if they exist) are to be used
    education_entries = st.session_state['linkedin_data'].get('education', [{} for _ in range(2)])

    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # If there are education entries from LinkedIn, use them as default values, otherwise use empty strings
    university1 = education_entries[0].get('school', '') if education_entries else ''
    locationus1 = education_entries[0].get('location', '') if education_entries else ''
    majorus1 = education_entries[0].get('field_of_study', '') if education_entries else ''
    gpa1 = education_entries[0].get('grade', '') if education_entries else ''
    starts_at1 = format_date(education_entries[0].get('starts_at')) if education_entries else ''
    ends_at1 = format_date(education_entries[0].get('ends_at')) if education_entries else ''
    timeus1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    university2 = education_entries[1].get('school', '') if len(education_entries) > 1 else ''
    locationus2 = education_entries[1].get('location', '') if len(education_entries) > 1 else ''
    majorus2 = education_entries[1].get('field_of_study', '') if len(education_entries) > 1 else ''
    gpa2 = education_entries[1].get('grade', '') if len(education_entries) > 1 else ''
    starts_at2 = format_date(education_entries[1].get('starts_at')) if len(education_entries) > 1 else ''
    ends_at2 = format_date(education_entries[1].get('ends_at')) if len(education_entries) > 1 else ''
    timeus2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    with st.expander("Education", expanded=False):  # 'expanded=True' means the section will be expanded by default
        university1 = st.text_input("University/School 1", value=university1, key="unique_key_196")
        locationus1 = st.text_input("Location 1", value=locationus1, key="unique_key_197")
        majorus1 = st.text_input("Study Program 1", value=majorus1, key="unique_key_198")
        timeus1 = st.text_input("Time Frame 1", value=timeus1, key="unique_key_199")
        courses1 = st.text_input("Courses 1", key="unique_key_200")
        gpa1 = st.text_input("GPA 1", value=gpa1, key="unique_key_201")
        clubs1 = st.text_input("Clubs/Activities 1", key="unique_key_202")

        university2 = st.text_input("University/School 2", value=university2, key="unique_key_203")
        locationus2 = st.text_input("Location 2", value=locationus2, key="unique_key_204")
        majorus2 = st.text_input("Study Program 2", value=majorus2, key="unique_key_205")
        timeus2 = st.text_input("Time Frame 2", value=timeus2, key="unique_key_206")
        courses2 = st.text_input("Courses 2", key="unique_key_207")
        gpa2 = st.text_input("GPA 2", value=gpa2, key="unique_key_208")
        clubs2 = st.text_input("Clubs/Activities 2", key="unique_key_209")

    # Professional Experience Section
    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

    # Retrieve up to three experience entries from LinkedIn data if they exist
    experience_entries = st.session_state['linkedin_data'].get('experiences', [{} for _ in range(3)])

    # If there are experience entries from LinkedIn, use them as default values, otherwise use empty strings
    experience1 = experience_entries[0].get('company', '') if experience_entries else ''
    locatione1 = experience_entries[0].get('location', '') if experience_entries else ''
    position1 = experience_entries[0].get('title', '') if experience_entries else ''
    starts_at1 = format_date(experience_entries[0].get('starts_at')) if experience_entries else ''
    ends_at1 = format_date(experience_entries[0].get('ends_at')) if experience_entries else ''
    timee1 = f"{starts_at1} - {ends_at1}" if ends_at1 else starts_at1

    experience2 = experience_entries[1].get('company', '') if len(experience_entries) > 1 else ''
    locatione2 = experience_entries[1].get('location', '') if len(experience_entries) > 1 else ''
    position2 = experience_entries[1].get('title', '') if len(experience_entries) > 1 else ''
    starts_at2 = format_date(experience_entries[1].get('starts_at')) if len(experience_entries) > 1 else ''
    ends_at2 = format_date(experience_entries[1].get('ends_at')) if len(experience_entries) > 1 else ''
    timee2 = f"{starts_at2} - {ends_at2}" if ends_at2 else starts_at2

    experience3 = experience_entries[2].get('company', '') if len(experience_entries) > 2 else ''
    locatione3 = experience_entries[2].get('location', '') if len(experience_entries) > 2 else ''
    position3 = experience_entries[2].get('title', '') if len(experience_entries) > 2 else ''
    starts_at3 = format_date(experience_entries[2].get('starts_at')) if len(experience_entries) > 2 else ''
    ends_at3 = format_date(experience_entries[2].get('ends_at')) if len(experience_entries) > 2 else ''
    timee3 = f"{starts_at3} - {ends_at3}" if ends_at3 else starts_at3

    with st.expander("Professional Experience", expanded=False):  # 'expanded=True' means the section will be expanded by default
        experience1 = st.text_input("Company 1", value=experience1, key="unique_key_210")
        locatione1 = st.text_input("Location 1", value=locatione1, key="unique_key_211")
        position1 = st.text_input("Position 1", value=position1, key="unique_key_212")
        timee1 = st.text_input("Time Frame 1", value=timee1, key="unique_key_213")
        task11 = st.text_area("Tasks 1", key='task11_46', height=100)
        task12 = st.text_area("Tasks 2", key='task12_47', height=100)

        experience2 = st.text_input("Company 2", value=experience2, key="unique_key_214")
        locatione2 = st.text_input("Location 2", value=locatione2, key="unique_key_215")
        position2 = st.text_input("Position 2", value=position2, key="unique_key_216")
        timee2 = st.text_input("Time Frame 2", value=timee2, key="unique_key_217")
        task21 = st.text_area("Tasks 1", key='task21_49', height=100)
        task22 = st.text_area("Tasks 2", key='task22_50', height=100)

    # Extracurricular Activities / Engagement Section
    with st.expander("Extracurricular Activities", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the volunteer work, certifications, languages, and interests from LinkedIn data if they exist
        volunteer_work_entries = st.session_state['linkedin_data'].get('volunteer_work', [])
        certifications_entries = st.session_state['linkedin_data'].get('certifications', [])
        languages_entries = st.session_state['linkedin_data'].get('languages', [''])
        interests_entries = st.session_state['linkedin_data'].get('interests', [''])

        # Extract titles from volunteer work and certifications
        volunteer_work_titles = [entry.get('title', '') for entry in volunteer_work_entries]
        certifications_titles = [entry.get('name', '') for entry in certifications_entries]

        # Combine the first three titles with a comma
        volunteer_work_combined = ', '.join(volunteer_work_titles[0:3])
        certifications_combined = ', '.join(certifications_titles[0:3])

        extracurricular1 = st.text_input("Extracurricular Activities", value=volunteer_work_combined, key="extracurricular_4_key")
        additionaleducation1 = st.text_input("Additional Education", key="additional_education_4_key")  # No specific API data, so left for manual input
        certificates1 = st.text_input("Certificates and Awards", value=certifications_combined, key="certificates_4_key")

    # Projects Section
    with st.expander("Projects", expanded=False):  # 'expanded=True' means the section will be expanded by default
        projectname1 = st.text_input("Project Name 1", key="project_1")
        elocation1 = st.text_input("Location 1", key="project_location_1")
        ereason1 = st.text_input("Reason for the Project 1", key="project_reason_1")
        timeen1 = st.text_input("Time Frame 1", key="project_time_1")
        taske11 = st.text_area("Tasks 1", key="project_task_11", height=100)
        taske12 = st.text_area("Tasks 2", key='project_task_12', height=100)

        projectname2 = st.text_input("Project Name 2", key="project_2")
        elocation2 = st.text_input("Location 2", key="project_location_2")
        ereason2 = st.text_input("Reason for the Project 2", key="project_reason_2")
        timeen2 = st.text_input("Time Frame 2", key="project_time_2")
        taske21 = st.text_area("Tasks 1", key="project_task_21", height=100)
        taske22 = st.text_area("Tasks 2", key='project_task_22', height=100)

    # Skills & Interest Section
    # Wrap the Skills & Interest section in an expander
    with st.expander("Skills & Interest", expanded=False):  # 'expanded=True' means the section will be expanded by default
        # Retrieve the computer skills entries from LinkedIn data if they exist
        computer_skills_entries = st.session_state['linkedin_data'].get('computer_skills', [''])

        # Join the first three entries for languages, interests, and computer skills with a comma
        languages_combined = ', '.join(languages_entries[0:3])
        interests_combined = ', '.join(interests_entries[0:3])
        computer_skills_combined = ', '.join(computer_skills_entries[0:3])

        languages1 = st.text_input("Languages", value=languages_combined, key="languages_4_key")
        computer1 = st.text_input("Computer Skills", value=computer_skills_combined, key="computer_skills_key_4")
        interests1 = st.text_input("Interests", value=interests_combined, key="interests_4_key")

    

    if st.button("Generate LaTeX", key='generate_latex_button_tab4'):
        latex_code = build_latex_code(name, address, phone, email, university1, locationus1, majorus1, timeus1, courses1, gpa1, clubs1, university2, locationus2, majorus2, timeus2, courses2, gpa2, clubs2, experience1, locatione1, position1, timee1, task11, task12, experience2, locatione2, position2, timee2, task21, task22, extracurricular1, additionaleducation1, certificates1, languages1, projectname1,projectname2, elocation1, ereason1, timeen1, taske11, taske12, elocation2, timeen2, taske21, taske22, computer1, interests1, ereason2)
        st.text_area("Generated LaTeX Code:", latex_code, height=300, key="a")
        
        st.markdown("### How to Create a Pdf with this LaTeX Code")
        st.markdown("""
        - Copy the entire LaTeX code above.
        - Visit [Overleaf](https://www.overleaf.com/project) and create a new project.te that you will need to create a free account if you don't already have one.
        - In the project settings, set the compiler to either XeLaTeX or LuaTeX.
        - Paste the copied code on the left side of the Overleaf editor.
        - Compile the document to generate a PDF.
        - Download the PDF from Overleaf once it's compiled.
        """)