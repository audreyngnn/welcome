import streamlit as st
from datetime import datetime

# PAGE SETUP
st.set_page_config(
    page_title="Audrey Nguyen - Data Analytics Portfolio",
    page_icon="📊",
    layout="wide",
    menu_items={
        "Get help": None,
        "Report a bug": None,
        "About": "A clean, single-file Streamlit portfolio"
    }
)

# -----------------------------------------------------------------------------
# DATA - UPDATE YOUR INFORMATION HERE
# -----------------------------------------------------------------------------

PROFILE = {
    "name": "Audrey Nguyen",
    "role": "Data Analyst",
    "tagline": "I build reliable, insightful data solutions with Power BI, Python, and ESG frameworks.",
    "location": "Sydney, Australia",
    "email": "audrey.tranguyen@gmail.com",
    "website": None,
    "github": "https://github.com/audreynguyen",
    "linkedin": "https://www.linkedin.com/in/audrey-nguyen",
    "phone": "0432 063 579"
}

# Each skill has an optional list of keywords; level is 0..100
SKILLS = [
    {"name": "Power BI", "level": 95, "keywords": ["DAX", "Data Modeling", "Microsoft Fabric", "Dashboards"]},
    {"name": "Python", "level": 85, "keywords": ["Data Analysis", "Automation", "2+ years"]},
    {"name": "R", "level": 80, "keywords": ["Statistical Analysis", "2+ years"]},
    {"name": "PostgreSQL", "level": 80, "keywords": ["Database Design", "SQL Queries", "2+ years"]},
    {"name": "Tableau", "level": 85, "keywords": ["Data Visualization", "Dashboards"]},
    {"name": "Excel", "level": 90, "keywords": ["Advanced Analytics", "Data Analysis"]},
    {"name": "SQL Server", "level": 80, "keywords": ["Database Management", "Queries"]},
]

EXPERIENCE = [
    {
        "role": "Data Analyst",
        "company": "Ptc. Consulting",
        "period": "Jun 2023 – Dec 2025",
        "location": "Sydney, NSW",
        "highlights": [
            "Accurate data collection on parking occupancy and turnover by conducting surveys across Sydney suburbs",
            "Data analysis by working with collected parking metrics, creating actionable insights for urban planning initiatives",
            "Achievement: Contributed to nine projects by delivering high-impact data records to city stakeholders",
        ],
        "tech": ["Data Analysis", "Urban Planning", "Survey Data"],
    },
    {
        "role": "Financial Analyst",
        "company": "Crawford and Company",
        "period": "Jan 2023 – Jul 2023",
        "location": "Sydney, NSW",
        "highlights": [
            "Involved in 134 financial loss claim assessments, including business interruption and stock loss policies",
            "Communicated with insured parties, insurers, and third-party representatives to gather case-specific data",
            "Validated claim information through detailed review of financial documentation and supporting evidence",
            "Presented data-driven financial analyses to support accurate claim assessment and settlement determination",
            "Generated reports detailing assessment processes, financial adjustments, and data-based recommendations for final settlement amounts",
            "Achievement: Generated $56,780 in company revenue by managing high-volume claims efficiently",
        ],
        "tech": ["Financial Analysis", "Data Analysis", "Excel"],
    },
    {
        "role": "Operations Manager",
        "company": "UAVS-NSW",
        "period": "Mar 2020 – Dec 2021",
        "location": "Sydney, NSW",
        "highlights": [
            "Collaborated with departments to analyze and restructure organizational workflows and procedures",
            "Collaborated with stakeholders to allocate personnel and resolve cross-team conflicts",
            "Identified training needs through performance data analysis",
            "Achievement: Doubled application volume and employee turnover reduced by 83% (vs. previous year)",
        ],
        "tech": ["Process Optimization", "Performance Analysis", "Data Analysis"],
    },
    {
        "role": "Mentor & Guest Speaker",
        "company": "RISE UP Competition (AVLD)",
        "period": "Jun 2022",
        "location": "Vietnam",
        "highlights": [
            "Presented research-driven analysis of sustainability challenges facing Vietnamese businesses, applying ESG (UN SDG) frameworks to assess environmental and social risks",
            "Mentored finalist team on developing blockchain solution for textile supply chain sustainability, evaluating ESG (UN SDG) materiality, impact measurement, and stakeholder transparency requirements",
            "Achievement: Strengthened leadership, communication, and coaching capabilities",
        ],
        "tech": ["ESG Analysis", "UN SDG", "Sustainability"],
    },
]

PROJECTS = [
    {
        "name": "Powering Tomorrow: Tracking Global Progress on SDG 7 (2000–2022)",
        "description": "An interactive Power BI dashboard visualising global progress toward UN SDG 7 (Affordable and Clean Energy) from 2000–2022, highlighting trends in electricity access, clean cooking, and renewable energy adoption.",
        "tech": ["Power BI", "Microsoft Fabric", "UN SDG", "ESG Analysis"],
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNzQ1OGYxMDYtY2Y5ZS00ZDg0LTg5MTQtMjgyNGEzZTZhNjcxIiwidCI6IjgyYzUxNGMxLWE3MTctNDA4Ny1iZTA2LWQ0MGQyMDcwYWQ1MiJ9",
        "image": "images/sdg7_cover.jpg",
        "year": "2025"
    },
    {
        "name": "University Student Retention Analytics",
        "description": "Comprehensive dashboard for Macquarie University analyzing student progression, retention rates, and transfer patterns across programs with advanced DAX measures.",
        "tech": ["Power BI", "DAX", "Educational Analytics", "Data Modeling"],
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNGZhMjg0ODUtNjIyZC00OWRiLWFjNzctY2VkMzM2Y2EwZGMzIiwidCI6IjgyYzUxNGMxLWE3MTctNDA4Ny1iZTA2LWQ0MGQyMDcwYWQ1MiJ9",
        "image": "images/retention_cover.jpg",
        "year": "2024"
    },
    {
        "name": "BBE Bike Sales Dashboard",
        "description": "Sales analytics dashboard tracking bike sales performance, revenue metrics, and customer insights with interactive visualizations.",
        "tech": ["Power BI", "DAX", "Sales Analytics"],
        "link": "https://app.powerbi.com/view?r=eyJrIjoiM2I4MjE4MjEtOTc3MC00ZmU3LWJmYjctYjczZTc5YjdkMTc3IiwidCI6IjgyYzUxNGMxLWE3MTctNDA4Ny1iZTA2LWQ0MGQyMDcwYWQ1MiJ9",
        "image": "images/bike_sales_cover.jpg",
        "year": "2024"
    },
    {
        "name": "DRAGONWAGON – Engage in Asia",
        "description": "Designed a mobile app to connect Vietnamese farmers with local buyers, promoting responsible supply chains. Targeted SDGs 1 (No Poverty) and 12 (Responsible Consumption and Production). Top 5 Finalist at University of Sydney.",
        "tech": ["ESG", "UN SDG 1", "UN SDG 12", "Social Impact"],
        "link": "https://www.youtube.com/watch?v=your-video-id",
        "image": "images/dragonwagon_cover.jpg",
        "year": "2022"
    },
]

EDUCATION = [
    {
        "degree": "Master of Business Analytics",
        "school": "Macquarie University",
        "period": "Feb 2024 – Dec 2025",
        "location": "Sydney, NSW",
        "details": None
    },
    {
        "degree": "Master of Business Analytics",
        "school": "University of Wollongong",
        "period": "Jun 2023 – Dec 2023",
        "location": "Wollongong, NSW",
        "details": "Ranked 1st out of 149 students in Accounting and Financial Management. Ranked 2nd out of 100 students in Business Analytics."
    },
    {
        "degree": "Bachelor of Commerce (Accounting & Marketing)",
        "school": "University of Sydney",
        "period": "Mar 2020 – Dec 2022",
        "location": "Sydney, NSW",
        "details": "Vice-Chancellor's International Scholarship recipient - First Vietnamese student awarded."
    },
]

CERTIFICATIONS = []

AWARDS = [
    {
        "name": "Vice-Chancellor's International Scholarship",
        "organization": "University of Sydney",
        "details": "Awarded based on academic excellence. 1st Vietnamese recipient of the scholarship."
    },
    {
        "name": "Top 5 Finalist - Engage in Asia Competition",
        "organization": "University of Sydney",
        "details": "Submitted project: DragonWagon"
    },
]

ARTICLES = [
    {
        "title": "Beyond Technical Skills: What It Really Takes to Succeed as a Data Analyst",
        "description": "An article where I reflect on 70 hours of data sourcing and 140 hours analyzing global energy poverty through Power BI. The lesson: domain expertise and stakeholder thinking matter more than perfect code. Topics covered: Data-driven decision-making, problem-solving skills, and collaboration.",
        "link": "https://medium.com/@audrey.tranguyen",
        "date": "2025"
    },
]

# -----------------------------------------------------------------------------
# STYLING
# -----------------------------------------------------------------------------

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    :root {
        --primary-blue: #4c748c;
        --accent-teal: #8ce4e4;
        --light-mint: #cdefe3;
        --dark-bg: #1a1d29;
        --card-bg: #242735;
        --sidebar-bg: #0e1117;
        --text-primary: #e8eaed;
        --text-secondary: #9aa0a6;
    }
    
    .stApp {
        background-color: var(--dark-bg);
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar - Dark Navy/Charcoal Background */
    [data-testid="stSidebar"] {
        background-color: var(--sidebar-bg) !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background-color: var(--sidebar-bg) !important;
    }
    
    /* Sidebar text colors */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] label {
        color: var(--text-primary) !important;
    }
    
    /* Sidebar links */
    [data-testid="stSidebar"] a {
        color: var(--accent-teal) !important;
    }
    
    [data-testid="stSidebar"] a:hover {
        color: var(--light-mint) !important;
    }
    
    /* Sidebar caption/small text */
    [data-testid="stSidebar"] .caption {
        color: var(--text-secondary) !important;
    }
    
    /* Sidebar multiselect */
    [data-testid="stSidebar"] .stMultiSelect {
        background-color: rgba(255, 255, 255, 0.05);
    }
    
    /* Sidebar selectbox (dropdown) */
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: var(--text-primary);
    }
    
    /* Download button styling */
    [data-testid="stSidebar"] .stDownloadButton > button {
        background-color: rgba(255, 255, 255, 0.1);
        color: var(--text-primary);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px;
        padding: 0.5rem 1rem;
        width: 100%;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    [data-testid="stSidebar"] .stDownloadButton > button:hover {
        background-color: rgba(255, 255, 255, 0.15);
        border-color: var(--accent-teal);
    }
    
    h1, h2, h3, h4, h5, h6, p, li, span, div, label {
        color: var(--text-primary) !important;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: var(--card-bg);
        border-radius: 8px;
        padding: 8px 16px;
        color: var(--text-secondary);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--accent-teal) 100%);
        color: white !important;
    }
    
    .project-card {
        background: var(--card-bg);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(140, 228, 228, 0.2);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        border-color: var(--accent-teal);
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(140, 228, 228, 0.15);
    }
    
    .skill-badge {
        display: inline-block;
        background: rgba(140, 228, 228, 0.1);
        color: var(--accent-teal);
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.85rem;
        margin: 4px;
        border: 1px solid rgba(140, 228, 228, 0.3);
    }
    
    .stMetric {
        background-color: var(--card-bg);
        padding: 1rem;
        border-radius: 8px;
    }
    
    .stProgress > div > div {
        background-color: var(--accent-teal);
    }
    
    a {
        color: var(--accent-teal) !important;
        text-decoration: none;
    }
    
    a:hover {
        color: var(--light-mint) !important;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def emoji_map(tech_name):
    """Map tech names to emojis"""
    emoji_dict = {
        'python': '🐍', 'power bi': '📊', 'tableau': '📈', 'sql': '🗄️',
        'excel': '📗', 'r': '📊', 'dax': '🧮', 'esg': '🌱',
        'pandas': '🐼', 'react': '⚛️', 'docker': '🐳'
    }
    return emoji_dict.get(tech_name.lower(), '🔹')

def chips(items):
    """Create tech stack chips/badges"""
    return "".join(f'<span class="skill-badge">{emoji_map(i)} {i}</span>' for i in items)

def collect_all_tech():
    """Collect unique technologies from experience and projects"""
    tech = set()
    for e in EXPERIENCE:
        tech.update(e.get("tech", []))
    for p in PROJECTS:
        tech.update(p.get("tech", []))
    for s in SKILLS:
        tech.add(s['name'])
        for k in s.get("keywords", []):
            tech.add(k)
    return sorted(tech)

# -----------------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------------

with st.sidebar:
    # Profile photo
    try:
        st.image("profile_photo.jpg", width=185)
    except:
        st.markdown(f"""
            <div style="width: 150px; height: 150px; border-radius: 50%; 
            background: linear-gradient(135deg, #4c748c 0%, #8ce4e4 100%); 
            display: flex; align-items: center; justify-content: center; 
            font-size: 3rem; color: white; margin: 0 auto;">
                {PROFILE['name'][:2]}
            </div>
        """, unsafe_allow_html=True)
    
    st.title(PROFILE['name'])
    st.write(PROFILE['role'])
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Contact info
    st.markdown("**CONTACT**")
    if PROFILE.get('email'):
        st.markdown(f"📧 [{PROFILE['email']}](mailto:{PROFILE['email']})")
    if PROFILE.get('github'):
        st.markdown(f"💻 [GitHub]({PROFILE['github']})")
    if PROFILE.get('linkedin'):
        st.markdown(f"💼 [LinkedIn]({PROFILE['linkedin']})")
    if PROFILE.get('location'):
        st.markdown(f"📍 {PROFILE['location']}")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Tech filter
    st.markdown("**Filters**")
    st.caption("Filter by tech")
    all_tech = collect_all_tech()
    selected = st.selectbox(
        "Filter by tech",
        options=["All"] + sorted(all_tech),
        label_visibility="collapsed"
    )
    if selected != "All":
        st.session_state['filters'] = {selected}
    else:
        st.session_state['filters'] = set()
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Download resume button
    try:
        with open("CV_AudreyNguyen.pdf", "rb") as pdf_file:
            st.download_button(
                label="Download resume",
                data=pdf_file,
                file_name="CV_AudreyNguyen.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        # If PDF not found, show a placeholder button
        st.button("Download resume", disabled=True, use_container_width=True)
        st.caption("📄 Add CV_AudreyNguyen_2025Nov15.pdf to enable")

# -----------------------------------------------------------------------------
# MAIN CONTENT
# -----------------------------------------------------------------------------

# Header
st.markdown(f"# {PROFILE['name']}")
st.markdown(f"**{PROFILE['role']}** · {PROFILE['location']}")
st.markdown(f"*{PROFILE['tagline']}*")

st.markdown("<hr>", unsafe_allow_html=True)

# Metrics
left, right = st.columns(2)
with left:
    st.markdown(f"📧 **{PROFILE['email']}**")
with right:
    col1, col2 = st.columns(2)
    with col1:
        years_exp = datetime.now().year - 2020  # Started in 2020
        st.metric("Years Experience", value=f"{years_exp}+")
    with col2:
        st.metric("Projects", value=str(len(PROJECTS)))

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TABS
# -----------------------------------------------------------------------------

about_tab, exp_tab, proj_tab, skills_tab, edu_tab, articles_tab = st.tabs([
    "📋 About",
    "💼 Experience",
    "🚀 Projects",
    "⚡ Skills",
    "🎓 Education",
    "📝 Articles"
])

# --- ABOUT TAB ---
with about_tab:
    st.subheader("About")
    st.write("""
    I'm a data analyst with a Master of Business Analytics from Macquarie University, 
    specializing in business intelligence, data visualization, and ESG analysis. 
    
    With experience spanning financial analysis, data consulting, and operations management, 
    I bring a comprehensive analytical approach to solving complex business problems.
    
    **What I Do:**
    - 📊 Build interactive Power BI dashboards for data-driven decision making
    - 🌱 Conduct ESG analysis using UN SDG frameworks
    - 📈 Transform complex data into actionable insights
    - 🎯 Design business intelligence solutions for stakeholders
    
    **Core Strengths:**
    - Advanced DAX and data modeling in Power BI
    - Statistical analysis and data processing with Python & R
    - Financial analysis and claims assessment
    - Stakeholder communication and requirement gathering
    """)

# --- EXPERIENCE TAB ---
with exp_tab:
    st.subheader("Experience")
    for e in EXPERIENCE:
        # Filter check
        if st.session_state.get("filters") and not (st.session_state["filters"] & set(e.get("tech", []))):
            continue
        
        with st.container():
            st.markdown(f"**{e['role']}** at **{e['company']}**")
            st.caption(f"{e['period']} · {e.get('location', '')}")
            
            for highlight in e['highlights']:
                st.write(f"• {highlight}")
            
            st.markdown(chips(e.get('tech', [])), unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

# --- PROJECTS TAB ---
with proj_tab:
    st.subheader("Projects")
    cols = st.columns(2)
    i = 0
    
    for p in PROJECTS:
        # Filter check
        if st.session_state.get("filters") and not (st.session_state["filters"] & set(p.get("tech", []))):
            continue
        
        with cols[i % 2]:
            st.markdown(f"""
            <div class="project-card">
                <h4 style='margin:6px 0'>{p['name']}</h4>
                <p style='margin:0 0 8px 0'>{p['description']}</p>
                <div style='margin:6px 0'>{chips(p.get('tech', []))}</div>
                {'<a class="pill-btn" href="' + p['link'] + '" target="_blank">View Project</a>' if p.get('link') else ''}
            </div>
            """, unsafe_allow_html=True)
            
            # Try to show image
            if p.get('image'):
                try:
                    st.image(p['image'], use_container_width=True)
                except:
                    pass
        
        i += 1

# --- SKILLS TAB ---
with skills_tab:
    st.subheader("Skills")
    for s in SKILLS:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(f"**{emoji_map(s['name'])} {s['name']}**")
            if s.get('keywords'):
                st.caption(", ".join(s['keywords']))
        with col2:
            st.progress(int(s.get("level", 0)) / 100)

# --- EDUCATION TAB ---
with edu_tab:
    st.subheader("Education")
    for edu in EDUCATION:
        st.markdown(f"**{edu['degree']}**")
        st.markdown(f"*{edu['school']}* · {edu['period']}")
        if edu.get('details'):
            st.caption(edu['details'])
        st.markdown("<br>", unsafe_allow_html=True)
    
    if AWARDS:
        st.subheader("Awards & Recognition")
        for award in AWARDS:
            st.markdown(f"🏆 **{award['name']}** - {award['organization']}")
            if award.get('details'):
                st.caption(award['details'])
            st.markdown("<br>", unsafe_allow_html=True)
    
    if CERTIFICATIONS:
        st.subheader("Certifications")
        for cert in CERTIFICATIONS:
            st.markdown(f"📜 **{cert['name']}** ({cert['year']})")

# --- ARTICLES TAB ---
with articles_tab:
    st.subheader("Articles & Writing")
    for article in ARTICLES:
        st.markdown(f"### {article['title']}")
        st.caption(article['date'])
        st.write(article['description'])
        if article.get('link'):
            st.markdown(f"[📄 Read Article]({article['link']})")
        st.markdown("<hr>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: center; color: #9aa0a6; font-size: 0.875rem;'>
    © 2025 Audrey Nguyen - Data Analytics Portfolio | Built with Streamlit
</p>
""", unsafe_allow_html=True)