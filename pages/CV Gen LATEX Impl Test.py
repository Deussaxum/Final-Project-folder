import streamlit as st
import requests
import subprocess

def build_latex_code(name, address, phone, email, university1, locationus1, majorus1, timeus1, courses1, gpa1, clubs1, university2, locationus2, majorus2, timeus2, courses2, gpa2, clubs2, experience1, locatione1, position1, timee1, task11, task12, task13, experience2, locatione2, position2, timee2, task21, task22, task23, experience3, locatione3, position3, timee3, task31, task32, task33, extracurricular1, additionaleducation1, certificates1, languages1, computer1, interests1):
    latex_code = fr"""
    % Hier kommt Ihr LaTeX-Code
    \documentclass[a4paper,8pt]{{article}}
    \usepackage{{parskip}}
    \usepackage{{hologo}}
    \usepackage{{fontspec}}
    \RequirePackage{{color}}
    \RequirePackage{{graphicx}}
    \usepackage[usenames,dvipsnames]{{xcolor}}
    \usepackage[scale=0.9, top=.4in, bottom=.4in]{{geometry}}
    \usepackage{{enumitem}}
    \usepackage{{tabularx}}
    \usepackage{{enumitem}}
    \newcolumntype{{C}}{{>{{\centering\arraybackslash}}X}}
    \usepackage{{supertabular}}
    \usepackage{{tabularx}}
    \newlength{{\fullcollw}}
    \setlength{{\fullcollw}}{{0.42\textwidth}}
    \usepackage{{titlesec}}             
    \usepackage{{multicol}}
    \usepackage{{multirow}}
    \titleformat{{\section}}{{\Large\scshape\raggedright}}{{}}{{0em}}{{}}[\titlerule]
    \titlespacing{{\section}}{{0pt}}{{2pt}}{{2pt}}
    \usepackage[style=authoryear,sorting=ynt, maxbibnames=2]{{biblatex}}
    \usepackage[unicode, draft=false]{{hyperref}}
    \color[HTML]{{110223}}
    \addbibresource{{citations.bib}}
    \setlength\bibitemsep{{1em}}
    \usepackage{{fontawesome5}}
    \usepackage[normalem]{{ulem}}
    \setmainfont{{Arial}}
    \begin{{document}}
    \pagestyle{{empty}}
    \begin{{tabularx}}{{\linewidth}}{{@{{}} C @{{}}}}
    \color[HTML]{{1C033C}} \Huge\textbf{{{name}}} \\[6pt]
    \textcolor[HTML]{{1C033C}} Address: {address} \\
    \textcolor[HTML]{{1C033C}} Mobile: {phone} \\
    \textcolor[HTML]{{1C033C}} Email: {email}
    \end{{tabularx}}
    \section{{EDUCATION}}
    \textbf{{{university1}}} \hfill \textbf{{{locationus1}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item {majorus1} \hfill \color[HTML]{{1C033C}} {timeus1}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item Courses: {courses1}
        \item GPA: {gpa1}
        \item {clubs1}
    \end{{itemize}}
    \textbf{{{university2}}} \hfill \textbf{{{locationus2}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item {majorus2} \hfill \color[HTML]{{1C033C}} {timeus2}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item Courses: {courses2}
        \item GPA: {gpa2}
        \item {clubs2}
    \end{{itemize}}
    \section{{PROFESSIONAL EXPERIENCE}}
    \textbf{{{experience1}}} \hfill \textbf{{{locatione1}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item \textit{{{position1}}} \hfill \color[HTML]{{1C033C}} {timee1}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {task11}
        \item {task12}
        \item {task13}
    \end{{itemize}}
    \textbf{{{experience2}}} \hfill \textbf{{{locatione2}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item \textit{{{position2}}} \hfill \color[HTML]{{1C033C}} {timee2}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {task21}
        \item {task22}
        \item {task23}
    \end{{itemize}}
    \textbf{{{experience3}}} \hfill \textbf{{{locatione3}}} \\[-3ex]
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item \textit{{{position3}}} \hfill \color[HTML]{{1C033C}} {timee3}
    \end{{itemize}}
    \begin{{itemize}}[label=$\circ$,itemsep=0.5ex,parsep=0.5ex]
        \item {task31}
        \item {task32}
        \item {task33}
    \end{{itemize}}
    \section{{EXTRACURRICULAR ACTIVITIES / ENGAGEMENT}}
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item Extracurricular: {extracurricular1}
        \item Additional Education: {additionaleducation1}
        \item Certificate & Achievements: {certificates1}
    \end{{itemize}}
    \section{{SKILLS /& INTEREST}}
    \begin{{itemize}}[label={{\large\textbullet}}, left=0pt, itemsep=0.5ex, parsep=0.5ex]
        \item Languages: {languages1}
        \item Computer: {computer1}
        \item Interests: {interests1}
    \end{{itemize}}
    \end{{document}}
    """
    return latex_code

# Initialize session state for LinkedIn data
if 'linkedin_data' not in st.session_state:
    st.session_state['linkedin_data'] = {}

st.title("CV Generator 📃")

tab_titles = [
    "Consulting 🧮",
    "Finance 📈",
    "Corporate 🏢",
    "Start-Up 🚀",
    "IT 🖥",
    "Academic 📚"
]

tabs=st.tabs(tab_titles)

with tabs[0]:

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
    linkedin_profile_url = st.text_input('Enter your LinkedIn profile URL', key='linkedin_url_key')

    if st.button('Retrieve LinkedIn Data', key='retrieve_data_button'):
            st.session_state['linkedin_data'] = retrieve_info(linkedin_profile_url) or {}

    # Personal Information Section
    st.header('Your CV, Your Story: Complete the Chapters')
    with st.expander("Personal Information", expanded=False):
        city = st.session_state['linkedin_data'].get('city', '')
        state = st.session_state['linkedin_data'].get('state', '')
        country = st.session_state['linkedin_data'].get('country', '')

        address_components = [comp for comp in [city, state, country] if comp]
        formatted_address = ', '.join(address_components)

        name = st.text_input("Name", value=st.session_state['linkedin_data'].get('full_name', ''), key='name_key')
        address = st.text_input("Address", value=formatted_address, key='address_key')
        phone = st.text_input("Phone Number", key='phone_key')
        email = st.text_input("E-Mail", key='email_key')

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

    with st.expander("Education", expanded=False):
        university1 = st.text_input("University/School 1", value=university1, key="unique_key_5")
        locationus1 = st.text_input("Location 1", value=locationus1, key="unique_key_6")
        majorus1 = st.text_input("Study Program 1", value=majorus1, key="unique_key_7")
        timeus1 = st.text_input("Time Frame 1", value=timeus1, key="unique_key_8")
        courses1 = st.text_input("Courses 1", key="unique_key_9")
        gpa1 = st.text_input("GPA 1", value=gpa1, key="unique_key_10")
        clubs1 = st.text_input("Clubs/Activities 1", key="unique_key_11")

        university2 = st.text_input("University/School 2", value=university2, key="unique_key_12")
        locationus2 = st.text_input("Location 2", value=locationus2, key="unique_key_13")
        majorus2 = st.text_input("Study Program 2", value=majorus2, key="unique_key_14")
        timeus2 = st.text_input("Time Frame 2", value=timeus2, key="unique_key_15")
        courses2 = st.text_input("Courses 2", key="unique_key_16")
        gpa2 = st.text_input("GPA 2", value=gpa2, key="unique_key_17")
        clubs2 = st.text_input("Clubs/Activities 2", key="unique_key_18")

    # Professional Experience Section
    def format_date(date_dict):
        """Formats a date dictionary into DD.MM.YYYY format."""
        if date_dict:
            day = date_dict.get('day', 1)  # Default to 1 if day is not available
            month = date_dict.get('month', 1)  # Default to 1 if month is not available
            year = date_dict.get('year', '')
            return f"{day:02d}.{month:02d}.{year}" if year else ''
        return ''

        # Retrieve experience entries from session state or initialize with defaults
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

    with st.expander("Professional Experience", expanded=False):
        experience1 = st.text_input("Company 1", value=experience1, key="unique_key_131")
        locatione1 = st.text_input("Location 1", value=locatione1, key="unique_key_132")
        position1 = st.text_input("Position 1", value=position1, key="unique_key_133")
        timee1 = st.text_input("Time Frame 1", value=timee1, key="unique_key_134")
        task11 = st.text_area("Tasks 1", key='task11_19', height=100)
        task12 = st.text_area("Tasks 2", key='task22_23', height=100)
        task13 = st.text_area("Tasks 3", key='task23_24', height=100)

        experience2 = st.text_input("Company 2", value=experience2, key="unique_key_135")
        locatione2 = st.text_input("Location 2", value=locatione2, key="unique_key_136")
        position2 = st.text_input("Position 2", value=position2, key="unique_key_137")
        timee2 = st.text_input("Time Frame 2", value=timee2, key="unique_key_138")
        task21 = st.text_area("Tasks 1", key='task21_22', height=100)
        task22 = st.text_area("Tasks 2", key='task22_23', height=100)
        task23 = st.text_area("Tasks 3", key='task23_24', height=100)

        experience3 = st.text_input("Company 3", value=experience3, key="unique_key_139")
        locatione3 = st.text_input("Location 3", value=locatione3, key="unique_key_140")
        position3 = st.text_input("Position 3", value=position3, key="unique_key_141")
        timee3 = st.text_input("Time Frame 3", value=timee3, key="unique_key_142")
        task31 = st.text_area("Tasks 1", key='task31_25', height=100)
        task32 = st.text_area("Tasks 2", key='task32_26', height=100)
        task33 = st.text_area("Tasks 3", key='task33_27', height=100)

    # Extracurricular Activities / Engagement Section
    with st.expander("Extracurricular Activities", expanded=False):
        volunteer_work_entries = st.session_state['linkedin_data'].get('volunteer_work', [])
        certifications_entries = st.session_state['linkedin_data'].get('certifications', [])
        languages_entries = st.session_state['linkedin_data'].get('languages', [''])
        interests_entries = st.session_state['linkedin_data'].get('interests', [''])

        volunteer_work_titles = [entry.get('title', '') for entry in volunteer_work_entries]
        certifications_titles = [entry.get('name', '') for entry in certifications_entries]

        volunteer_work_combined = ', '.join(volunteer_work_titles[0:3])
        certifications_combined = ', '.join(certifications_titles[0:3])

        extracurricular1 = st.text_input("Extracurricular Activities", value=volunteer_work_combined, key="extracurricular_1_key")
        additionaleducation1 = st.text_input("Additional Education", key="additional_education_1_key")
        certificates1 = st.text_input("Certificates and Awards", value=certifications_combined, key="certificates_1_key")

    # Skills & Interest Section
    # Wrap the Skills & Interest section in an expander
    with st.expander("Skills & Interest", expanded=False):
        computer_skills_entries = st.session_state['linkedin_data'].get('computer_skills', [''])

        languages_combined = ', '.join(languages_entries[0:3])
        interests_combined = ', '.join(interests_entries[0:3])
        computer_skills_combined = ', '.join(computer_skills_entries[0:3])

        languages1 = st.text_input("Languages", value=languages_combined, key="languages_1_key")
        computer1 = st.text_input("Computer Skills", value=computer_skills_combined, key="computer_skills_key")
        interests1 = st.text_input("Interests", value=interests_combined, key="interests_1_key")

    if st.button("Generate LaTeX"):
        latex_code = build_latex_code(name, address, phone, email, university1, locationus1, majorus1, timeus1, courses1, gpa1, clubs1, university2, locationus2, majorus2, timeus2, courses2, gpa2, clubs2, experience1, locatione1, position1, timee1, task11, task12, task13, experience2, locatione2, position2, timee2, task21, task22, task23, experience3, locatione3, position3, timee3, task31, task32, task33, extracurricular1, additionaleducation1, certificates1, languages1, computer1, interests1)
        st.text_area("Generated LaTeX Code:", latex_code, height=300)
        
        st.markdown("### How to Create a Pdf with this LaTeX Code")
        st.markdown("""
        - Copy the entire LaTeX code above.
        - Visit [Overleaf](https://www.overleaf.com/project) and create a new project.te that you will need to create a free account if you don't already have one.
        - In the project settings, set the compiler to either XeLaTeX or LuaTeX.
        - Paste the copied code on the left side of the Overleaf editor.
        - Compile the document to generate a PDF.
        - Download the PDF from Overleaf once it's compiled.
        """)