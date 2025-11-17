"""
Portfolio Website - Main Application
Multi-page portfolio for Audrey Nguyen
Built with Streamlit
"""

import streamlit as st
from data import PROFILE, SKILLS, EXPERIENCE, PROJECTS
from layout import apply_custom_styles
from tabs import (
    sidebar_profile,
    sidebar_contact,
    sidebar_filter,
    sidebar_download_resume
)

# Initialize session state
if "filters" not in st.session_state:
    st.session_state.filters = set()

# PAGE SETUP
st.set_page_config(
    page_title="Audrey Nguyen - Data Analytics Portfolio",
    page_icon="❀",
    layout="wide",
    menu_items={
        "Get help": None,
        "Report a bug": None,
        "About": "Data Analytics Portfolio by Audrey Nguyen. Built with Streamlit. Master of Business Analytics specializing in Power BI, Python, and ESG frameworks."
    }
)

# Apply custom styling
apply_custom_styles()

# Define navigation pages
pages = [
    st.Page(
        "page_about.py",
        title="About Me",
        icon="🌿",
        default=True
    ),
    st.Page(
        "page_experience.py",
        title="Experience",
        icon="❋˚"
    ),
    st.Page(
        "page_projects.py",
        title="Projects",
        icon="➤"
    ),
    st.Page(
        "page_skills.py",
        title="Skills",
        icon="⚡"
    ),
    st.Page(
        "page_education.py",
        title="Education",
        icon="🎓"
    ),
    st.Page(
        "page_articles.py",
        title="Articles",
        icon="✍️"
    ),
]

# Run navigation
page = st.navigation(pages)

# Sidebar content
with st.sidebar:
    sidebar_profile(PROFILE)
    sidebar_contact(PROFILE)
    sidebar_filter(SKILLS, EXPERIENCE, PROJECTS)
    sidebar_download_resume()

# Run the selected page
page.run()