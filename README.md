# Career Compass Web Application

## Overview
Career Compass is a web application based on Streamlit that helps job seekers identify suitable industries for career progression, create tailored CVs and finds suitable job postings. The application has a user-friendly interface and integrates with the Nubela API, providing a comprehensive suite of tools for professional development.

## Homepage
- **Purpose:** This section provides an introduction to the purpose of the website, explains the process, and the industries covered by the web application.
  - **Main Title and Subheader:** Introducing the application and its primary purpose.
  - **Informational Section:** Detailed description of the application's functionalities, including CV generation and Industry Fit Assessment.

## Industry Fit Assessment Tool
- **Purpose:** Assists users in identifying industries that align with their personality traits and skills.
  - Comprehensive questionnaire evaluating personality, skills, and work-life balance preferences.
  - Advanced algorithms to match user profiles with suitable industries.
  - Visual representation of skills and personality traits through diagrams.

## CV Generator
- **Purpose:** Helps the user to create a CV in PDF format for job applications.
  - Offers an API to LinkedIn to retrieve profile information, expediting CV creation.
  - Tailors CVs to specific industries.
  - LaTeX code is provided, which must then be entered into the Overleaf editor to generate a PDF from it.

## Job Search
- **Purpose:** The platform assists users in discovering relevant job postings by inputting their preferences and industry.
  - List of job postings across various industries, including Consulting, Finance, Corporate, IT, Academic, and Startup sectors.
  - Inputs required: The job postings can be filtered based on country, employment type, experience level, job posting date, and flexibility.

## User Guide
- Begin at the homepage and follow the instructions provided.

## Technologies Used
- **Streamlit:** For building the web application.
- **Nubela-Jobs API:** For searching job postings on LinkedIn.
- **Nubela-People API:** To prefill the CV generator's inputs with LinkedIn data.
- **DALL·E 3:** For sourcing images.
