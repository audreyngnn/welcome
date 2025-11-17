"""
About Page
Introduction and overview of skills and expertise
"""

import streamlit as st
from data import PROFILE, PROJECTS, EDUCATION, AWARDS
from tabs import profile_header, quick_stats, render_footer

# Page config is set in main app, so we don't need it here

# Header
profile_header(PROFILE)

# Quick Stats
quick_stats(PROJECTS, EDUCATION, AWARDS)

st.markdown("<hr style='margin: 2rem 0; border: none; border-top: 1px solid #E5E5E5;'>", unsafe_allow_html=True)

# About Me section
st.markdown('<p class="section-header">About Me</p>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    I'm a data analyst with a Master of Business Analytics from Macquarie University, 
    specializing in business intelligence, data visualization, and ESG analysis. 
    
    With experience spanning financial analysis, data consulting, and operations management, 
    I bring a comprehensive analytical approach to solving complex business problems.
    """)
    
    st.markdown("#### What I Do")
    st.markdown("""
    - Build interactive Power BI dashboards for data-driven decision making
    - Conduct ESG analysis using UN SDG frameworks
    - Transform complex data into actionable insights
    - Design business intelligence solutions for stakeholders
    """)

with col2:
    st.markdown("#### Core Strengths")
    strengths = [
        "Advanced Excel"
        "Advanced DAX & Data Modeling",
        "Statistical Analysis (Python & R)",
        "Financial Analysis",
        "Stakeholder Communication"
    ]
    for strength in strengths:
        st.markdown(f"• {strength}")

# Footer
render_footer()