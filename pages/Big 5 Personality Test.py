import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from tkinter import ttk

# Set Streamlit theme to a colorful and attractive style
st.set_page_config(
    page_title="Career Fit Assessment Tool",
    page_icon="🌟",
    layout="wide",
)

# Customize the background color and text color
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
    
# Function to create radar charts
def plot_radar_chart(categories, scores, title, figure_size=(8, 8)):
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    scores += scores[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(subplot_kw={"polar": True}, figsize=figure_size)  # Set the figure size here
    ax.fill(angles, scores, color="skyblue", alpha=0.7, linewidth=2, edgecolor="blue")
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=10, color="gray")
    ax.set_rlabel_position(0)
    plt.ylim(0, 100)
    plt.title(title, fontsize=18, weight="bold", color="#333333")

    # Customize grid lines
    ax.xaxis.grid(color="gray", linestyle="--", linewidth=0.5)
    ax.yaxis.grid(color="gray", linestyle="--", linewidth=0.5)

    # Customize radial labels
    ax.tick_params(axis="y", colors="gray")
    ax.spines["polar"].set_visible(False)

    st.pyplot(fig)

# Function to calculate skill scores
def calculate_skill_scores(responses):
    mapped_responses = [((response - 1) / 4) * 100 for response in responses]
    return mapped_responses

# Function to calculate total fit percentages
def calculate_total_fit(user_personality_scores, user_skill_scores, industry_scores):
    fit_percentages = {}
    for industry, (industry_personality, industry_skills) in industry_scores.items():
        personality_fit = 100 - np.sqrt(np.sum((np.array(user_personality_scores) - np.array(industry_personality)) ** 2))
        skill_fit = 100 - np.sqrt(np.sum((np.array(user_skill_scores) - np.array(industry_skills)) ** 2))
        total_fit = (personality_fit + skill_fit) / 2
        fit_percentages[industry] = max(0, total_fit)
    return fit_percentages

# Function to calculate Big Five scores
def calculate_big_five_scores(responses):
    mapped_responses = [((response - 1) / 4) * 100 for response in responses]
    openness_score = np.mean(mapped_responses[0:5])
    conscientiousness_score = np.mean(mapped_responses[5:10])
    extraversion_score = np.mean(mapped_responses[10:15])
    agreeableness_score = np.mean(mapped_responses[15:20])
    neuroticism_score = np.mean(mapped_responses[20:25])
    return {
        "Openness": openness_score,
        "Conscientiousness": conscientiousness_score,
        "Extraversion": extraversion_score,
        "Agreeableness": agreeableness_score,
        "Neuroticism": neuroticism_score,
    }

# Function to get responses from sliders
def get_responses_from_sliders(sliders):
    return [slider for slider in sliders]

# Main function
def main():
    st.title("Career Fit Assessment Tool\n Assessment of Industry Fit based on Big 5 Personality Traits and Skillset")

    # Big Five Personality Questions
    personality_questions = [
        "I enjoy trying new things and exploring different experiences.",
        "I appreciate art, music, and creative expression.",
        "I am curious and eager to learn new information.",
        "I tend to think deeply and reflect on abstract ideas.",
        "I often seek out new and unconventional experiences.",
        "I am well-organized and pay attention to detail.",
        "I am diligent and always strive for excellence in my work.",
        "I prefer to plan things ahead of time rather than being spontaneous.",
        "I am a responsible and reliable person.",
        "I like to follow rules and stick to a routine.",
        "I enjoy socializing and spending time with others.",
        "I am outgoing and talkative in social situations.",
        "I feel energized when I'm around people.",
        "I enjoy being the center of attention at social gatherings.",
        "I prefer going out and being active over staying in.",
        "I am compassionate and empathetic towards others.",
        "I avoid conflicts and try to maintain harmony in my relationships.",
        "I am willing to help others even when it inconveniences me.",
        "I value cooperation and teamwork.",
        "I tend to forgive others easily and hold no grudges.",
        "I often worry about things and feel anxious.",
        "I am sensitive to criticism and easily get upset.",
        "I experience mood swings and emotional ups and downs.",
        "I find it challenging to relax and often feel tense.",
        "I tend to dwell on negative thoughts and events.",
    ]

    personality_sliders = []
    for index, question in enumerate(personality_questions):
        st.markdown(f"### {question}")
        st.write("Rate the fit on a scale from 1 to 5")
        slider = st.slider("", 1, 5, 3, key=f"personality_slider_{index}")
        personality_sliders.append(slider)

    # Skill Assessment Questions
    skill_questions = [
        "I am proficient in using technology and software relevant to my field.",
        "I have strong analytical and problem-solving skills.",
        "I can effectively lead a team and manage projects.",
        "I am skilled in communicating ideas clearly and persuasively.",
        "I am creative and can think outside the box.",
    ]

    skill_sliders = []
    for index, question in enumerate(skill_questions):
        st.markdown(f"### {question}")
        st.write("Rate the fit on a scale from 1 to 5")
        slider = st.slider("", 1, 5, 3, key=f"skill_slider_{index}")
        skill_sliders.append(slider)

    if st.button("Submit"):
        personality_responses = get_responses_from_sliders(personality_sliders)
        personality_scores = calculate_big_five_scores(personality_responses)

        skill_responses = get_responses_from_sliders(skill_sliders)
        skill_scores = calculate_skill_scores(skill_responses)

        industry_scores = {
            "Investment Banking": ([70, 85, 75, 60, 40], [80, 70, 90, 75, 60]),
            "Corporate Job (General)": ([60, 80, 65, 70, 45], [70, 80, 65, 70, 55]),
            "Self-Employed (Entrepreneurship)": ([85, 70, 70, 60, 35], [85, 60, 80, 65, 80]),
            "Computer Science (Tech Industry)": ([80, 85, 50, 50, 30], [90, 75, 55, 60, 70]),
            "Consulting": ([90, 85, 90, 85, 30], [75, 85, 80, 85, 65]),
        }
        total_fit_percentages = calculate_total_fit(
            list(personality_scores.values()), skill_scores, industry_scores
        )

        # Display Radar Charts and Fit Percentages
        plot_radar_chart(
            list(personality_scores.keys()), list(personality_scores.values()), "Your Big Five Personality Traits"
        )
        plot_radar_chart(list(industry_scores.keys()), list(total_fit_percentages.values()), "Industry Fit")

        for industry, fit in total_fit_percentages.items():
            st.write(f"Total Fit for {industry}: {fit:.2f}%")

        recommended_industry = max(total_fit_percentages, key=total_fit_percentages.get)
        st.success(f"Recommended Industry: {recommended_industry}")

if __name__ == "__main__":
    main()

