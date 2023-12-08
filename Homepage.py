import streamlit as st


st.set_page_config(
    page_title="Career Compass 🧭",
)


header_image_url = "https://cdn.thenudge.com/wp-content/uploads/2022/09/skyline.png"
st.image(header_image_url)

st.title("The Career Compass CV Generator")
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
st.info("4. Insert your data by easily importing it from LinkedIn to streamline your CV creation process!")

st.subheader("What is the Industry Fit Assessment?")

st.info("""
    The Industry Fit Assessment serves as a valuable tool to guide you in determining the ideal industry for your job applications. It operates through a comprehensive questionnaire designed to assess various facets of your personality, skills, and expectations regarding work-life balance. The process involves completing a thoughtfully curated set of questions that delve into different dimensions of your character.

    Once you've provided your responses, the test leverages advanced algorithms to analyze and compare your answers against a diverse array of industries. The ultimate goal is to pinpoint the sector that aligns most closely with your unique combination of personality traits and skills, ensuring a tailored career fit.

    The results are presented in a visually accessible format, utilizing diagrams to illustrate your skills and personality traits. Here you can see some examples for such diagrams: 
""")

  

st.subheader("Industry Overview")

image_url_1 = "https://media.gq-magazin.de/photos/5f684a5c1744746f33a1c573/1:1/w_1248,h_1248,c_limit/leonardo-dicaprio-el-lobo-de-wall-street.jpg"
image_url_2 = "https://media.gq-magazin.de/photos/5f684a5c1744746f33a1c573/1:1/w_1248,h_1248,c_limit/leonardo-dicaprio-el-lobo-de-wall-street.jpg"
image_url_3 = "https://media.gq-magazin.de/photos/5f684a5c1744746f33a1c573/1:1/w_1248,h_1248,c_limit/leonardo-dicaprio-el-lobo-de-wall-street.jpg"
image_url_4 = "https://media.gq-magazin.de/photos/5f684a5c1744746f33a1c573/1:1/w_1248,h_1248,c_limit/leonardo-dicaprio-el-lobo-de-wall-street.jpg"
image_url_5 = "https://media.gq-magazin.de/photos/5f684a5c1744746f33a1c573/1:1/w_1248,h_1248,c_limit/leonardo-dicaprio-el-lobo-de-wall-street.jpg"
image_url_6 = "https://media.gq-magazin.de/photos/5f684a5c1744746f33a1c573/1:1/w_1248,h_1248,c_limit/leonardo-dicaprio-el-lobo-de-wall-street.jpg"


col1, col2 = st.columns(2)

# Box 1
with col1:
    st.subheader("Consulting 🛫")
    st.image(image_url_1)
    st.write("As a consultant, you provide expert advice to organizations, helping them improve performance, operations, and profitability. Your role involves analyzing situations, identifying problems, and presenting comprehensive solutions to meet client needs.")

# Box 2
with col2:
    st.subheader("Finance 📈")
    st.image(image_url_2)
    st.write("In Finance you offer financial advice, prepare lending agreements, and ensure accurate corporate records. Your role involves working with corporations of various sizes, providing services like credit, treasury, financing, and commercial analysis to meet their financial needs.")

# Box 3
with col1:
    st.subheader("Corporate 🏢")
    st.image(image_url_3)
    st.write("In Corporate, you work within an organization with opportunities for career advancement, beeing resposible for a variety of roles including account management, providing financial advice, or ensuring accurate records to contribute to the companys business goals.")

# Box 4
with col2:
    st.subheader("Start-Up 🚀")
    st.image(image_url_4)
    st.write("In a startup, you typically wear multiple hats, taking on various responsibilities that can range from strategic planning to hands-on execution. Your role may involve setting direction, creating culture, and driving growth, all while adapting to the fast-paced and ever-changing startup environment.")

 # Box 5
with col1:
    st.subheader("IT 💻")
    st.image(image_url_4)
    st.write("As an IT professional, you manage and store data using computers, software, databases, networks, and servers, and your role may include writing programs, maintaining networks, analyzing systems, and providing technical support.") 

 # Box 6
with col2:
    st.subheader("Academic 📚")
    st.image(image_url_4)
    st.write("Working in Academia involves teaching, guiding students through lectures and seminars, and conducts research to contribute to their field of expertise. You often participate in academic service such as serving on committees and reviewing scholarly work.")
st.write("   ")
st.write("   ")
st.write("   ")
st.write("   ")
st.write("   ")
st.write("   ")





