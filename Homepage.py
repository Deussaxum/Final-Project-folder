import streamlit as st


st.set_page_config(
    page_title="Career Compass 🧭",
)


header_image_url = "CareerCompassHeader.jpeg"
st.image(header_image_url)

st.title("The Career Compass")
st.subheader("Creating your own CV has never been easier!")

st.info("""
    Struggling with frequent rejections despite possessing valuable experience and skills? Look no further – the Career Compass CV Generator is here to solve this challenge by crafting a tailored CV that accurately showcases your capabilities. In just under 10 minutes, our user-friendly platform, enhanced by the LinkedIn API, will generate the perfect CV for you.

    Our solution doesn't stop at optimizing your CV; we understand that identifying the right places to apply is equally crucial. Introducing the Industry Fit Assessment. By analyzing your personality traits and skills, we will identify the industry you would fit in the best. This empowers you to apply strategically, increasing your chances of landing a position that aligns with your abilities and professional goals.

    Don't let rejection letters deter you – let the Career Compass CV Generator and the Industry Fit Assessment be your allies in navigating the competitive job market. Take control of your career journey with confidence and precision.
""")

st.subheader("HOW IT WORKS")
st.info("1. Determine which industry suits you best by taking our test based on the Industry Fit Assessment.")
st.info("2. Choose the industry you want your CV to be tailored to by going to the CV Generator and choosing the industry.")
st.info("3. If you already know which industry to apply for, you can directly go to the CV Generator and choose the corresponding industry.")
st.info("4. In case you are having a LinkedIn account, use our LinkedIn tool to retrieve your profile information to accelerate the generation of your CV.")

st.subheader("What is the Industry Fit Assessment?")

st.info("""
    The Industry Fit Assessment serves as a valuable tool to guide you in determining the ideal industry for your job applications. It operates through a comprehensive questionnaire designed to assess various facets of your personality, skills, and expectations regarding work-life balance. The process involves completing a thoughtfully curated set of questions that delve into different dimensions of your character.

    Once you've provided your responses, the test leverages advanced algorithms to analyze and compare your answers against a diverse array of industries. The ultimate goal is to pinpoint the sector that aligns most closely with your unique combination of personality traits and skills, ensuring a tailored career fit.

    The results are presented in a visually accessible format, utilizing diagrams to illustrate your skills and personality traits. Here you can see some examples for such diagrams: 
""")

diagramm_image_url1 = "Example_Diagramm1.png"
diagramm_image_url2 = "Example_Diagramm2.jpg"
diagramm_image_url3 = "Example_Diagramm3.png"
diagramm_image_url4 = "Example_Diagramm4.png"
col1, col2 = st.columns(2)

# Box 1
with col1:
    
    st.image(diagramm_image_url1)
  

# Box 2
with col2:
   
    st.image(diagramm_image_url2)
   

# Box 3
with col1:
  
    st.image(diagramm_image_url3)
    

# Box 4
with col2:
   
    st.image(diagramm_image_url4)

st.subheader("Industry Overview")
#defintion of the file paths for the pictures below    
  
header_image_url1 = "Consulting.Picture.jpeg"
header_image_url2 = "Finance.Picture.jpeg"
header_image_url3 = "Corporate.Picture.jpeg"
header_image_url4 = "IT.Picture.jpeg"
header_image_url5 = "Academic.Picture.jpeg"
header_image_url6 = "Startup.Picture.jpeg"
header_image_url7 = "Law.Picture.jpeg"

#creation of the two columns for the different boxes
col1, col2 = st.columns(2)

# Box 1
with col1:
    st.subheader("Consulting 🛫")
    st.image(header_image_url1)
    st.write("As a consultant, you provide expert advice to organizations, helping them improve performance, operations, and profitability. Your role involves analyzing situations, identifying problems, and presenting comprehensive solutions to meet client needs.")

# Box 2
with col2:
    st.subheader("Finance 📈")
    st.image(header_image_url2)
    st.write("In Finance you offer financial advice, prepare lending agreements, and ensure accurate corporate records. Your role involves working with corporations of various sizes, providing services like credit, treasury, financing, and commercial analysis to meet their financial needs.")

# Box 3
with col1:
    st.subheader("Corporate 🏢")
    st.image(header_image_url3)
    st.write("In Corporate, you work within an organization with opportunities for career advancement, being responsible for a variety of roles including account management, providing financial advice, or ensuring accurate records to contribute to the company's business goals.")

# Box 4
with col2:
    st.subheader("IT 💻")
    st.image(header_image_url4)
    st.write("As an IT professional, you manage and store data using computers, software, databases, networks, and servers. Your role may include writing programs, maintaining networks, analyzing systems, and providing technical support for customers.") 

# Box 5
with col1:
    st.subheader("Academic 📚")
    st.image(header_image_url5)
    st.write("Working in Academia involves teaching, guiding students through lectures and seminars, and conducts research to contribute to their field of expertise. You often participate in academic service such as serving on committees and reviewing scholarly work.")

# Box 6
with col2:
    st.subheader("Start-Up 🚀")
    st.image(header_image_url6)
    st.write("In a startup, you typically wear multiple hats, taking on various responsibilities that can range from strategic planning to hands-on execution. Your role may involve setting direction, creating culture, and driving growth, all while adapting to the fast-paced and ever-changing startup environment.")

# Box 7
with col1:
    st.subheader("Law 👨🏼‍⚖️")
    st.image(header_image_url7)
    st.write("As a lawyer, you will undertake a diverse range of tasks and responsibilities, with a primary focus on defending your clients. Various specialized areas within the legal field offer opportunities for practice, and one illustrative example is tax law.")

st.sidebar.success("Please select a page Above.")
