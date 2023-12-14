# Importing necessary libraries
import streamlit as st  # Streamlit library for creating web applications
import matplotlib.pyplot as plt  # Matplotlib for creating charts and plots
import numpy as np  # NumPy for numerical operations and array manipulations
import io  # IO module for handling in-memory file-like objects

# Setting up the Streamlit page with a specific title and layout
st.set_page_config(
    page_title="Industry Fit Assessment Tool",  # Title of the web page
    layout="wide",  # Layout of the page. 'wide' utilizes more screen space.
)

# Customizing the Streamlit app's background and text color using raw HTML and CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;  # Light grey background color
        color: #333333;  # Dark grey text color
    }
    </style>
    """,
    unsafe_allow_html=True,  # Allows HTML content. Use with caution as it can pose security risks.
)

# Function to create and display a radar chart
def plot_radar_chart(categories, scores, title, figure_size=(1.5, 1.5), dpi=2000, title_fontsize=4, label_distance=0.5):
    N = len(categories)  # Number of categories
    angles = [n / float(N) * 2 * np.pi for n in range(N)]  # Calculate angles for radar chart
    scores += scores[:1]  # Repeat the first score at the end to close the radar chart
    angles += angles[:1]  # Repeat the first angle to close the chart

    # Creating the figure and axis for the radar chart
    fig, ax = plt.subplots(subplot_kw={"polar": True}, figsize=figure_size, dpi=dpi)
    # Filling the radar chart with color
    ax.fill(angles, scores, color="green", alpha=0.7, linewidth=2, edgecolor="green")
    # Setting up category labels (x-ticks)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=3)  # Font size for category labels
    # Setting up score labels (y-ticks)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=4, color="gray")  # Font size and color for score labels

    ax.set_rlabel_position(label_distance)  # Setting radial label position

    plt.ylim(0, 100)  # Y-axis limits
    plt.title(title, fontsize=title_fontsize, weight="bold", color="#333333")  # Chart title

    # Customizing grid lines
    ax.xaxis.grid(color="gray", linestyle="--", linewidth=0.5)
    ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

    # Customize radial labels
    ax.tick_params(axis="y", colors="gray")
    ax.spines["polar"].set_visible(False)  # Hiding the polar spine

    # Saving the figure to a high-resolution image in memory
    img_data = io.BytesIO()
    fig.savefig(img_data, format="png", dpi=dpi, bbox_inches="tight")
    img_data.seek(0)  # Reset buffer to the start

    # Displaying the image in the Streamlit app
    st.image(img_data, width=700)

# Function to create and return a bar chart as an image
def plot_bar_chart(labels, values, title, figure_size=(8, 4), dpi=1500, label_fontsize=12, title_fontsize=14):
    fig, ax = plt.subplots(figsize=figure_size, dpi=dpi)  # Creating figure and axis
    ax.barh(labels, values, color='green')  # Creating horizontal bar chart
    ax.set_xlabel('Scores', fontsize=label_fontsize)  # X-axis label with fontsize
    ax.set_title(title, fontsize=title_fontsize)  # Chart title with fontsize

    # Customizing grid lines and labels
    ax.xaxis.grid(color="gray", linestyle="--", linewidth=0.5)
    ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

    plt.tight_layout()  # Adjust layout to fit all elements

    # Saving the figure to a high-resolution image in memory
    img_data = io.BytesIO()
    fig.savefig(img_data, format="png", dpi=dpi, bbox_inches="tight")
    img_data.seek(0)  # Reset buffer to the start

    return img_data

# Function to calculate total fit percentages for different industries
def calculate_total_fit(user_personality_scores, user_skill_scores, user_work_life_balance_scores, industry_scores):
    fit_percentages = {}  # Dictionary to store fit percentages for each industry
    for industry, (industry_personality, industry_skills, industry_work_life_balance) in industry_scores.items():
        # Calculate fit for personality, skills, and work-life balance
        personality_fit = 100 - np.sqrt(np.sum((np.array(user_personality_scores) - np.array(industry_personality)) ** 2))
        skill_fit = 100 - np.sqrt(np.sum((np.array(user_skill_scores) - np.array(industry_skills)) ** 2))
        work_life_balance_fit = 100 - np.sqrt(np.sum((np.array(user_work_life_balance_scores) - np.array(industry_work_life_balance)) ** 2))
        total_fit = (personality_fit + skill_fit + work_life_balance_fit) / 3  # Average of the three fits
        fit_percentages[industry] = max(0, total_fit)  # Ensure fit percentage is not negative
    return fit_percentages

# Function to calculate Big Five personality trait scores
def calculate_big_five_scores(responses):
    mapped_responses = [(response / 100) * 100 for response in responses]  # Mapping responses to a 0-100 scale
    # Calculating mean scores for each Big Five trait
    openness_score = np.mean(mapped_responses[0:2])
    conscientiousness_score = np.mean(mapped_responses[2:4])
    extraversion_score = np.mean(mapped_responses[4:6])
    agreeableness_score = np.mean(mapped_responses[6:8])
    neuroticism_score = np.mean(mapped_responses[8:10])
    # Returning a dictionary of trait scores
    return {
        "Openness": openness_score,
        "Conscientiousness": conscientiousness_score,
        "Extraversion": extraversion_score,
        "Agreeableness": agreeableness_score,
        "Neuroticism": neuroticism_score,
    }

# Function to collect responses from sliders
def get_responses_from_sliders(sliders):
    return [slider for slider in sliders]  # List comprehension to extract values from slider objects

# Main function defining the Streamlit app
def main():
    st.image('career.png', width=1000, use_column_width='true')  # Display header image
    # Displaying the title of the app
    st.title("Career Fit Assessment Tool\n Assessment of Industry Fit based on Big 5 Personality Traits, Skills, and Work-Life Balance")

    # Big Five Personality Questions
    personality_questions = [
        "I enjoy taking on new challenges and stepping outside my comfort zone.",
        "I often explore and appreciate new art, music, and creative works.",
        "I have a strong desire to learn new information and expand my knowledge.",
        "I am open to unconventional experiences and enjoy trying new things.",
        "I am organized and pay attention to detail in my work.",
        "I prefer planning and structure over spontaneity.",
        "I enjoy socializing and spending time with others.",
        "I feel energized when surrounded by people and social events.",
        "I tend to worry and feel anxious about various aspects of life.",
        "I find it difficult to relax and often feel tense."
    ]

    personality_sliders = []  # List to store slider widgets
    # Looping through personality questions to create sliders
    for index, question in enumerate(personality_questions):
        st.markdown(f"### {question}")  # Displaying the question as a subheading
        st.write("Rate your agreement on a scale from 1 to 100")  # Instruction for rating
        # Creating a slider for each question
        slider = st.slider("", 1, 100, 50, key=f"personality_slider_{index}")
        personality_sliders.append(slider)  # Adding the slider to the list

    # Similar blocks of code for skill and work-life balance assessments follow...
 # Skill Assessment Questions
    skill_questions = [
        "I excel at problem-solving and finding innovative solutions.",
        "I am skilled at critical thinking and analyzing complex issues.",
        "I have experience in leadership roles and can effectively manage teams.",
        "I am adept at clear and persuasive communication.",
        "I am known for my creativity and ability to think outside the box.",
    ]

    skill_sliders = []
    skill_labels = [
        "Problem Solving",
        "Critical Thinking",
        "Leadership",
        "Communication",
        "Creativity",
    ]
    for index, question in enumerate(skill_questions):
        st.markdown(f"### {question}")
        st.write("Rate your proficiency on a scale from 1 to 100")
        slider = st.slider("", 1, 100, 50, key=f"skill_slider_{index}")
        skill_sliders.append(slider)

    # Work-Life Balance Questions
    work_life_balance_questions = [
        "I am able to maintain a healthy work-life balance.",
        "I regularly take breaks and vacations to recharge.",
        "I can disconnect from work-related stress during personal time.",
        "I have time for hobbies and interests outside of work.",
        "I feel content with the amount of time I spend with family and friends.",
    ]

    work_life_balance_sliders = []
    for index, question in enumerate(work_life_balance_questions):
        st.markdown(f"### {question}")
        st.write("Rate the importance of this aspect on a scale from 1 to 100")
        slider = st.slider("", 1, 100, 50, key=f"work_life_balance_slider_{index}")
        work_life_balance_sliders.append(slider)

    if st.button("Submit"):  # Creating a submit button
        # Collecting responses from the sliders
        personality_responses = get_responses_from_sliders(personality_sliders)
        personality_scores = calculate_big_five_scores(personality_responses)
        skill_responses = get_responses_from_sliders(skill_sliders)
        work_life_balance_responses = get_responses_from_sliders(work_life_balance_sliders)


     # Defining industry scores for various aspects (big 5 Values, Skill Values, Work-life balance values)
        industry_scores = {
            "Finance": ([70, 90, 75, 65, 30], [80, 90, 50, 85, 70], [45, 25, 65, 90, 55]),
            "Corporate Job": ([65, 80, 50, 90, 50], [65, 60, 50, 75, 55], [95, 90, 90, 95, 85]),
            "Self-Employed (Entrepreneurship)": ([90, 95, 95, 70, 20], [95, 80, 90, 95, 85], [50, 40, 70, 60, 60]),
            "Tech Industry": ([50, 90, 55, 85, 30], [90, 90, 45, 75, 90], [70, 70, 75, 80, 70]),
            "Consulting": ([85, 90, 90, 90, 40], [95, 90, 40, 95, 85], [70, 55, 65, 60, 65]),
            "Academic Career": ([90, 90, 95, 70, 30], [70, 80, 90, 95, 75], [75, 60, 60, 70, 75])
        }

        # Calculating total fit percentages for each industry
        total_fit_percentages = calculate_total_fit(
        list(personality_scores.values()), skill_responses, work_life_balance_responses, industry_scores
        )

        # Displaying charts and results...
        # Display Radar Chart for Personality
        plot_radar_chart(
        list(personality_scores.keys()), list(personality_scores.values()), "Your Big Five Personality Traits"
        )
        # Display Skills Profile
       
        skills_profile_img = plot_bar_chart(skill_labels, skill_responses, "Skills Profile", label_fontsize=10, title_fontsize=12)
        st.image(skills_profile_img, width=700)

        # Display Work-Life Balance Profile
        
        average_work_life_balance = np.mean(work_life_balance_responses)
        st.write(f"Average Importance of Work-Life Balance: {average_work_life_balance:.2f} (out of 100)")

        # Visualize Importance of Work-Life Balance
        importance_values = [average_work_life_balance]
        importance_labels = ["Work-Life Balance"]

        # Use the modified plot_bar_chart function to get the image data
        importance_img_data = plot_bar_chart(importance_labels, importance_values, "Importance of Work-Life Balance", figure_size=(7, 1), dpi=1500, label_fontsize=6, title_fontsize=8)

        # Display the high-resolution image using st.image
        st.image(importance_img_data, width=700) 
        # Display Radar Chart for Industry Fit
       
        plot_radar_chart(list(industry_scores.keys()), list(total_fit_percentages.values()), "Industry Fit")
       
       
        # Loop to display total fit for each industry
        for industry, fit in total_fit_percentages.items():
            st.write(f"Total Fit for {industry}: {fit:.2f}%")

        recommended_industry = max(total_fit_percentages, key=total_fit_percentages.get)
        st.success(f"Recommended Industry: {recommended_industry}")
        # Call the main function when the script is executed
if __name__ == "__main__":
     main()
