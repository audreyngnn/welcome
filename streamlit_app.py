"""
Portfolio Website - Main Application
Multi-page portfolio for Audrey Nguyen
Built with Streamlit
"""

import streamlit as st
from data import PROFILE, SKILLS, EXPERIENCE, PROJECTS, EDUCATION, AWARDS, ARTICLES
from layout import apply_custom_styles
from tabs import (
    sidebar_profile,
    sidebar_contact,
    sidebar_filter,
    sidebar_download_resume,
    profile_header,
    quick_stats,
    render_footer,
    render_experience_card,
    render_project_card,
    render_education_item,
    render_award_item,
    render_article_card
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
        "About": "Data Analytics Portfolio by Audrey Nguyen. Master of Business Analytics specializing in Power BI, Python, and ESG frameworks."
    }
)

# Apply custom styling
apply_custom_styles()

# Mobile Profile Header (only visible on mobile devices)
# Using Streamlit's st.image for better compatibility
import base64
from pathlib import Path

def get_base64_image(image_path):
    """Convert image to base64 for mobile display"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Get base64 encoded image
img_base64 = get_base64_image("profile_photo.jpg")

if img_base64:
    st.markdown(f'''
        <div class="mobile-profile-container">
            <img src="data:image/jpeg;base64,{img_base64}" alt="Audrey Nguyen">
            <h2>Audrey Nguyen</h2>
            <p>Data Analyst | Sydney, Australia</p>
        </div>
    ''', unsafe_allow_html=True)
else:
    # Fallback if image doesn't load
    st.markdown('''
        <div class="mobile-profile-container">
            <h2>Audrey Nguyen</h2>
            <p>Data Analyst | Sydney, Australia</p>
        </div>
    ''', unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    sidebar_profile(PROFILE)
    sidebar_contact(PROFILE)
    sidebar_filter(SKILLS, EXPERIENCE, PROJECTS)
    sidebar_download_resume()

# Main content - Header
profile_header(PROFILE)
quick_stats(PROJECTS, EDUCATION, AWARDS)

st.markdown("<hr style='margin: 2rem 0; border: none; border-top: 1px solid #E5E5E5;'>", unsafe_allow_html=True)

# Horizontal tabs in main content
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 About Me",
    "💼 Experience", 
    "📊 Projects",
    "⚡ Skills",
    "🎓 Education",
    "✍️ Articles"
])

# TAB 1: About Me
with tab1:
    st.markdown('<p class="section-header">About Me</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1], gap="large")  # or "small", "medium"
    
    with col1:
        st.markdown("""
        I'm a data analyst with a Master of Business Analytics from Macquarie University, 
        specializing in business intelligence, data visualization, and ESG analysis. 
        
        With experience spanning financial analysis, data consulting, and operations management, 
        I bring a comprehensive analytical approach to solving complex business problems.
        """)
        
        st.markdown("##### What I Do")
        st.markdown("""
        - Build interactive Power BI dashboards for data-driven decision making
        - Conduct ESG analysis using UN SDG frameworks
        - Transform complex data into actionable insights
        - Design business intelligence solutions for stakeholders
        """)
    
    with col2:
        st.markdown("#### Core Strengths")
        strengths = [
            "Advanced Excel",
            "Advanced DAX & Data Modeling",
            "Statistical Analysis (Python & R)",
            "Financial Analysis",
            "Stakeholder Communication"
        ]
        for strength in strengths:
            st.markdown(f"• {strength}")

# TAB 2: Experience
with tab2:
    st.markdown('<p class="section-header">Professional Experience</p>', unsafe_allow_html=True)
    
    filters = st.session_state.get("filters", set())
    
    for exp in EXPERIENCE:
        if filters and not (filters & set(exp.get("tech", []))):
            continue
        render_experience_card(exp)

# TAB 3: Projects
with tab3:
    st.markdown('<p class="section-header">Featured Projects</p>', unsafe_allow_html=True)
    
    filters = st.session_state.get("filters", set())
    
    filtered_projects = []
    for p in PROJECTS:
        if filters and not (filters & set(p.get("tech", []))):
            continue
        filtered_projects.append(p)
    
    for i in range(0, len(filtered_projects), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(filtered_projects):
                p = filtered_projects[i + j]
                with col:
                    render_project_card(p)

# TAB 4: Skills
with tab4:
    from data import SKILLS
    
    st.markdown('<p class="section-header">Technical Skills</p>', unsafe_allow_html=True)
    
    st.markdown("### Business Intelligence & Visualization")
    bi_skills = [s for s in SKILLS if s['name'] in ['Power BI', 'Tableau']]
    for s in bi_skills:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown(f"**{s['name']}**")
            if s.get('keywords'):
                st.caption(", ".join(s['keywords']))
        with col2:
            st.progress(int(s.get("level", 0)) / 100)
    
    st.markdown("### Programming & Databases")
    prog_skills = [s for s in SKILLS if s['name'] in ['Python', 'R', 'PostgreSQL', 'SQL Server']]
    for s in prog_skills:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown(f"**{s['name']}**")
            if s.get('keywords'):
                st.caption(", ".join(s['keywords']))
        with col2:
            st.progress(int(s.get("level", 0)) / 100)
    
    st.markdown("### Data Tools")
    other_skills = [s for s in SKILLS if s['name'] in ['Excel']]
    for s in other_skills:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown(f"**{s['name']}**")
            if s.get('keywords'):
                st.caption(", ".join(s['keywords']))
        with col2:
            st.progress(int(s.get("level", 0)) / 100)

# TAB 5: Education
with tab5:
    st.markdown('<p class="section-header">Education</p>', unsafe_allow_html=True)
    
    for edu in EDUCATION:
        render_education_item(edu)
    
    if AWARDS:
        st.markdown('<p class="section-header" style="margin-top: 2rem;">Awards & Recognition</p>', unsafe_allow_html=True)
        for award in AWARDS:
            render_award_item(award)

# TAB 6: Articles
with tab6:
    st.markdown('<p class="section-header">Articles & Writing</p>', unsafe_allow_html=True)
    
    for article in ARTICLES:
        render_article_card(article)

# Footer
render_footer()