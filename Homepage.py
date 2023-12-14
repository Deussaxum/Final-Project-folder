# Import the Streamlit library
import streamlit as st  

# Set page configuration, including the page title displayed in the browser tab
st.set_page_config(
    page_title="Career Compass 🧭",  
)

# Variable assignment: Define the file path for the header image
header_image_url = "CareerCompassHeader.jpeg"

# Display the header image
st.image(header_image_url)  


st.title("The Career Compass")  #Display the main title
st.subheader("Creating your own CV has never been easier!")  #Display a subheader

# Display information using the 'info' function about the Career Compass CV Generator - the info function generates a box around the text. In this case, the info function adresses several lines in order to create a big box.
st.info("""
    Struggling with frequent rejections despite possessing valuable experience and skills? Look no further – the Career Compass CV Generator is here to solve this challenge by crafting a tailored CV that accurately showcases your capabilities. In just under 10 minutes, our user-friendly platform, enhanced by the LinkedIn API, will generate the perfect CV for you.

    Our solution doesn't stop at optimizing your CV; we understand that identifying the right places to apply is equally crucial. Introducing the Industry Fit Assessment. By analyzing your personality traits and skills, we will identify the industry you would fit in the best. This empowers you to apply strategically, increasing your chances of landing a position that aligns with your abilities and professional goals.

    Don't let rejection letters deter you – let the Career Compass CV Generator and the Industry Fit Assessment be your allies in navigating the competitive job market. Take control of your career journey with confidence and precision.
""") 


st.subheader("HOW IT WORKS")  #Display a subheader
st.info("1. Determine which industry suits you best by completing our Industry Fit Assessment.")
st.info("2. Choose the industry you want your CV to be tailored to by going to the CV Generator and choosing the right industry.")
st.info("3. If you already know which industry to apply for, you can directly go to the CV Generator and choose the corresponding industry without completing the Assessment.")
st.info("4. In case you have a LinkedIn account, use our LinkedIn tool to retrieve your profile information to accelerate the generation of your CV.")
# Display information about how the system works, using info function - in this case line by line, creating 4 boxes.


st.subheader("What is the Industry Fit Assessment?")  #Display a subheader

st.info("""
    The Industry Fit Assessment serves as a valuable tool to guide you in determining the ideal industry for your job applications. It operates through a comprehensive questionnaire designed to assess various facets of your personality, skills, and expectations regarding work-life balance. The process involves completing a thoughtfully curated set of questions that delve into different dimensions of your character.

    Once you've provided your responses, the test leverages advanced algorithms to analyze and compare your answers against a diverse array of industries. The ultimate goal is to pinpoint the sector that aligns most closely with your unique combination of personality traits and skills, ensuring a tailored career fit.

    The results are presented in a visually accessible format, utilizing diagrams to illustrate your skills and personality traits. Here you can see some examples for such diagrams: 
""")  #Display information about the Industry Fit Assessment

# Define URLs for various diagram images and display them in a two-column layout
# Variable assignment: Define the file path for the Example Diagramms
diagramm_image_url1 = "Example_Diagramm1.png"
diagramm_image_url2 = "Example_Diagramm2.jpg"
diagramm_image_url3 = "Example_Diagramm3.png"
diagramm_image_url4 = "Example_Diagramm4.png"
col1, col2 = st.columns(2)  #Create two columns for displaying images

# Box 1
with col1:
    st.image(diagramm_image_url1)  #Display the first example diagram in the first column in the first row 

# Box 2
with col2:
    st.image(diagramm_image_url2)  #Display the second example diagram in the second column in the first row
 
# Box 3
with col1:
    st.image(diagramm_image_url3)  #Display the third example diagram in the first column in the second row

# Box 4
with col2:
    st.image(diagramm_image_url4)  #Display the fourth example diagram in the second column in the second row 


st.subheader("Industry Overview")  #Display a subheader

#Variable assignment: Define file paths for images related to different industries
header_image_url1 = "Consulting.Picture.jpeg"
header_image_url2 = "Finance.Picture.jpeg"
header_image_url3 = "Corporate.Picture.jpeg"
header_image_url4 = "IT.Picture.jpeg"
header_image_url5 = "Academic.Picture.jpeg"
header_image_url6 = "Startup.Picture.jpeg"
header_image_url7 = "Law.Picture.jpeg"

# Create two columns for displaying industry information in the industry boxes
col1, col2 = st.columns(2)  

# Define content for each box, including subheaders, images, and descriptions
# Box 1
with col1: #In column 1 row 1 
    st.subheader("Consulting 🛫")  #Display a subheader for Consulting
    st.image(header_image_url1)  #Display an image related to Consulting
    st.write("As a consultant, you provide expert advice to organizations, helping them improve performance, operations, and profitability. Your role involves analyzing situations, identifying problems, and presenting comprehensive solutions to meet client needs.")
    #Display text related to Consulting

# Box 2
with col2: #In column 2 row 1 
    st.subheader("Finance 📈")  #Display a subheader for Finance
    st.image(header_image_url2)  #Display an image related to Finance
    st.write("In Finance you offer financial advice, prepare lending agreements, and ensure accurate corporate records. Your role involves working with corporations of various sizes, providing services like credit, treasury, financing, and commercial analysis to meet their financial needs.")
    #Display text related to Finance

# Box 3
with col1: #In column 1 row 2
    st.subheader("Corporate 🏢")  #Display a subheader for Corporate
    st.image(header_image_url3)  #Display an image related to Corporate
    st.write("In Corporate, you work within an organization with opportunities for career advancement, being responsible for a variety of roles including account management, providing financial advice, or ensuring accurate records to contribute to the company's business goals.")
    #Display text related to Corporate

# Box 4
with col2: #In column 2 row 2 
    st.subheader("IT 💻")  #Display a subheader for IT
    st.image(header_image_url4) #Display an image related to IT
    st.write("As an IT professional, you manage and store data using computers, software, databases, networks, and servers. Your role may include writing programs, maintaining networks, analyzing systems, and providing technical support for customers.") 
    #Display text related to IT
    
# Box 5
with col1: #In column 1 row 3
    st.subheader("Academic 📚")#Display a subheader for Academic
    st.image(header_image_url5) #Display an image realted to Academic
    st.write("Working in Academia involves teaching, guiding students through lectures and seminars, and conducts research to contribute to their field of expertise. You often participate in academic service such as serving on committees and reviewing scholarly work.")
    #Display text relasted to Academic
# Box 6
with col2: #In column 2 row 3
    st.subheader("Start-Up 🚀")#Display a subheader for Start-Up
    st.image(header_image_url6)#Display an image related to Start-Up
    st.write("In a startup, you typically wear multiple hats, taking on various responsibilities that can range from strategic planning to hands-on execution. Your role may involve setting direction, creating culture, and driving growth, all while adapting to the fast-paced and ever-changing startup environment.")
    #Display text related to Start-Up
# Box 7
with col1: #In column 1 row 4
    st.subheader("Law 👨🏼‍⚖️")#Display a subheader for LaW
    st.image(header_image_url7) #Display an image related to Law
    st.write("As a lawyer, you will undertake a diverse range of tasks and responsibilities, with a primary focus on defending your clients. Various specialized areas within the legal field offer opportunities for practice, and one illustrative example is tax law.")
    #Display text related to Law

# Display a message in the sidebar
st.sidebar.success("Please select a page Above.")