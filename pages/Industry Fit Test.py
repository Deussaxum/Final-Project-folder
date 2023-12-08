import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

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
