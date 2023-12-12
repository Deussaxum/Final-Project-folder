import streamlit as st

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
    import streamlit as st

    # Streamlit-Benutzeroberfläche
    st.title("Consulting 🧮")

    # API Anbindung
    st.button("Get your input via LinkedIn", key="unique_key_0")

    # Persönliche Informationen
    st.header("Personal Information")
    name = st.text_input("Name", key="unique_key_1")
    address = st.text_input("Adresse", key="unique_key_2")
    phone = st.text_input("Telefonnummer", key="unique_key_3")
    email = st.text_input("E-Mail", key="unique_key_4")

    # Education
    st.header("Education")
    university1 = st.text_input("Universität/Schule 1", key="unique_key_5")
    locationus1 = st.text_input("Standort 1", key="unique_key_6")
    majorus1 = st.text_input("Studiengang 1", key="unique_key_7")
    timeus1 = st.text_input("Zeitraum 1", key="unique_key_8")
    courses1 = st.text_input("Kurse 1", key="unique_key_9")
    gpa1 = st.text_input("GPA 1", key="unique_key_10")
    clubs1 = st.text_input("Clubs/Aktivitäten 1", key="unique_key_11")

    university2 = st.text_input("Universität/Schule 2", "", key="unique_key_12")
    locationus2 = st.text_input("Standort 2", "", key="unique_key_13")
    majorus2 = st.text_input("Studiengang 2", "", key="unique_key_14")
    timeus2 = st.text_input("Zeitraum 2", "", key="unique_key_15")
    courses2 = st.text_input("Kurse 2", "", key="unique_key_16")
    gpa2 = st.text_input("GPA 2", "", key="unique_key_17")
    clubs2 = st.text_input("Clubs/Aktivitäten 2", "", key="unique_key_18")

    # Professional Experience
    st.header("Professional Experience")
    experience1 = st.text_input("Erfahrung 1", key="unique_key_19")
    locatione1 = st.text_input("Standort Erfahrung 1", key="unique_key_20")
    position1 = st.text_input("Position 1", key="unique_key_21!")
    timee1 = st.text_input("Zeitraum Erfahrung 1", key="unique_key_22")
    task11 = st.text_area("Aufgaben 1", key='task11_1', height=100)
    task12 = st.text_area("Aufgaben 2", key='task12_2', height=100)
    task13 = st.text_area("Aufgaben 3", key='task13_3', height=100)

    experience2 = st.text_input("Erfahrung 2", "", key="unique_key_23")
    locatione2 = st.text_input("Standort Erfahrung 2", "", key="unique_key_24")
    position2 = st.text_input("Position 2", "", key="position_2_key")
    timee2 = st.text_input("Zeitraum Erfahrung 2", "", key="unique_key_25")
    task21 = st.text_area("Aufgaben 1", key='task21_4', height=100)
    task22 = st.text_area("Aufgaben 2", key='task22_5', height=100)
    task23 = st.text_area("Aufgaben 3", key='task23_6', height=100)

    experience3 = st.text_input("Erfahrung 3", "", key="unique_key_26")
    locatione3 = st.text_input("Standort Erfahrung 3", "", key="unique_key_27")
    position3 = st.text_input("Position 3", "", key="unique_key_28")
    timee3 = st.text_input("Zeitraum Erfahrung 3", "", key="unique_key_29")
    task31 = st.text_area("Aufgaben 1", key='task31_7', height=100)
    task32 = st.text_area("Aufgaben 2", key='task32_8', height=100)
    task33 = st.text_area("Aufgaben 3", key='task33_9', height=100)

    # Extracurricular Activities / Engagement
    st.header("Extracurricular Activities / Engagement")
    extracurricular1 = st.text_input("Extrakurrikulare Aktivitäten", key="unique_key_30")
    additionaleducation1 = st.text_input("Zusätzliche Bildung", key="unique_key_31")
    certificates1 = st.text_input("Zertifikate und Errungenschaften", key="unique_key_32")

    # Skills & Interest
    st.header("Skills & Interest")
    languages1 = st.text_input("Sprachen", key="unique_key_33")
    computer1 = st.text_input("Computerkenntnisse", key="unique_key_34")
    interests1 = st.text_input("Interesse   n", key="unique_key_35")

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

