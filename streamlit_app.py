import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Audrey - Data Analytics Portfolio',
    page_icon='📊',
    layout='wide'
)

# -----------------------------------------------------------------------------
# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .dashboard-container {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: #f9f9f9;
    }
    .article-card {
        border-left: 4px solid #1f77b4;
        padding-left: 1rem;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Sidebar Navigation

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Power BI Dashboards", "Tableau Dashboards", "Articles & Writing", "About Me"]
)

# -----------------------------------------------------------------------------
# Home Page

if page == "Home":
    st.markdown('<p class="main-header">Audrey Nguyen</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Master of Business Analytics | Data Analyst | ESG & Sustainability Analytics</p>', unsafe_allow_html=True)
    
    st.write("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Welcome! 👋
        
        I'm a data analyst with a Master of Business Analytics from Macquarie University, 
        specializing in business intelligence, data visualization, and ESG analysis. Previously, 
        I worked as a Financial Analyst at Crawford and Company and as a Data Analyst at Ptc. Consulting.
        
        This portfolio showcases my work in:
        - **Power BI**: Interactive dashboards for sustainability metrics and educational analytics
        - **Tableau**: Data visualizations for complex analytical insights
        - **ESG Analysis**: UN SDG frameworks and sustainability assessments
        - **Technical Writing**: Reflective articles on data analytics practices
        
        Feel free to explore my projects and get in touch!
        """)
    
    with col2:
        st.info("""
        **Quick Links**
        
        📧 audrey.tranguyen@gmail.com
        
        💼 [LinkedIn](https://www.linkedin.com/in/audrey-nguyen)
        
        🔗 [GitHub](https://github.com/audreynguyen)
        
        📍 Sydney, Australia
        """)
    
    st.write("---")
    
    # Featured Projects
    st.header("Featured Projects")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("⚡ Powering Tomorrow")
        st.write("Interactive Power BI dashboard tracking global progress on UN SDG 7 (Affordable and Clean Energy) from 2000-2022")
        st.caption("Power BI • Microsoft Fabric • UN SDG")
    
    with col2:
        st.subheader("🎓 University Student Retention")
        st.write("Comprehensive analytics dashboard analyzing student progression, retention, and transfer patterns for Macquarie University")
        st.caption("Power BI • DAX • Educational Analytics")
    
    with col3:
        st.subheader("🌾 DragonWagon")
        st.write("Mobile app connecting Vietnamese farmers with local buyers, promoting responsible supply chains (Top 5 Finalist - Engage in Asia)")
        st.caption("SDG 1 & 12 • Sustainability • Social Impact")

# -----------------------------------------------------------------------------
# Power BI Dashboards Page

elif page == "Power BI Dashboards":
    st.title("📊 Power BI Dashboards")
    st.write("Interactive business intelligence dashboards built with Power BI and advanced DAX measures")
    
    st.write("---")
    
    # Dashboard 1: Powering Tomorrow - SDG 7
    st.markdown('<div class="dashboard-container">', unsafe_allow_html=True)
    st.subheader("Powering Tomorrow: Tracking Global Progress on SDG 7 (2000–2022)")
    st.write("""
    **Project Overview:** An interactive Power BI dashboard visualizing global progress toward UN SDG 7 
    (Affordable and Clean Energy) from 2000–2022, highlighting trends in electricity access, clean cooking, 
    and renewable energy adoption.
    
    **Key Features:**
    - Global electricity access rates by region and country
    - Clean cooking fuel adoption trends
    - Renewable energy capacity and generation tracking
    - Progress indicators toward achieving SDG 7 targets
    - Time-series analysis showing 22 years of energy transition data
    
    **Data Sources:** UN SDG Database, World Bank Data
    
    **Tools & Techniques:** Power BI, Microsoft Fabric, Data Integration, ESG Framework
    
    **Read More:** [Medium Article - Beyond Technical Skills: What It Really Takes to Succeed as a Data Analyst](https://medium.com/@audrey.tranguyen)
    """)
    
    # Embed Power BI dashboard
    st.markdown("**Dashboard Preview:**")
    powerbi_embed_url = st.text_input(
        "Enter your Power BI embed URL (from Publish to web):",
        key="sdg7_dashboard",
        help="Go to your Power BI report > File > Embed report > Publish to web"
    )
    
    if powerbi_embed_url:
        st.components.v1.iframe(powerbi_embed_url, height=600, scrolling=True)
    else:
        st.info("👆 Paste your Power BI embed URL above to display the dashboard")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    
    # Dashboard 2: University Student Retention
    st.markdown('<div class="dashboard-container">', unsafe_allow_html=True)
    st.subheader("University Student Retention Analytics")
    st.write("""
    **Project Overview:** Comprehensive dashboard for Macquarie University's Business Intelligence and Reporting team 
    analyzing student progression, retention rates, and transfer patterns across programs.
    
    **Key Features:**
    - Student drop-out rate analysis by cohort and program
    - Year-over-year retention comparisons with cohort tracking
    - Transfer pattern tracking across different degree programs
    - Executive-level KPIs for University Executives, Course Directors, and Unit Convenors
    - Advanced DAX measures for calculating progression metrics
    
    **Stakeholders:** University Executives, Course Directors, Unit Convenors
    
    **Tools & Techniques:** Power BI, Advanced DAX, Complex Data Modeling, Educational Analytics
    """)
    
    powerbi_embed_url_2 = st.text_input(
        "Enter your Power BI embed URL:",
        key="retention_dashboard",
        help="Go to your Power BI report > File > Embed report > Publish to web"
    )
    
    if powerbi_embed_url_2:
        st.components.v1.iframe(powerbi_embed_url_2, height=600, scrolling=True)
    else:
        st.info("👆 Paste your Power BI embed URL above to display the dashboard")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add more dashboards as needed
    st.write("")
    st.info("💡 **Tip:** You can add more dashboards by duplicating the structure above")

# -----------------------------------------------------------------------------
# Tableau Dashboards Page

elif page == "Tableau Dashboards":
    st.title("📈 Tableau Dashboards")
    st.write("Data visualizations and analytical dashboards created with Tableau")
    
    st.write("---")
    
    st.markdown('<div class="dashboard-container">', unsafe_allow_html=True)
    st.subheader("Your Tableau Dashboard Title")
    st.write("""
    **Project Overview:** [Describe your Tableau project]
    
    **Key Features:**
    - Feature 1
    - Feature 2
    - Feature 3
    
    **Tools & Techniques:** Tableau, [Other tools]
    """)
    
    # Embed Tableau dashboard
    tableau_embed_url = st.text_input(
        "Enter your Tableau Public embed URL:",
        key="tableau_1",
        help="Share your Tableau Public visualization and copy the embed code URL"
    )
    
    if tableau_embed_url:
        st.components.v1.iframe(tableau_embed_url, height=800, scrolling=True)
    else:
        st.info("👆 Paste your Tableau Public embed URL above to display the dashboard")
    
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Articles & Writing Page

elif page == "Articles & Writing":
    st.title("📝 Articles & Technical Writing")
    st.write("Case studies, reports, and analytical articles")
    
    st.write("---")
    
    # Article 1
    st.markdown('<div class="article-card">', unsafe_allow_html=True)
    st.subheader("Beyond Technical Skills: What It Really Takes to Succeed as a Data Analyst")
    st.caption("Data Analytics Reflection | 2025")
    st.write("""
    A reflective article on 70 hours of data sourcing and 140 hours analyzing global energy poverty 
    through Power BI. The key lesson: domain expertise and stakeholder thinking matter more than perfect code.
    
    **Key Topics:** Data-driven decision-making, Problem-solving skills, Collaboration, Domain expertise, 
    Stakeholder management
    """)
    
    # Link to Medium article
    st.markdown("[📄 Read on Medium](https://medium.com/@audrey.tranguyen)")
    
    with st.expander("Read Summary"):
        st.write("""
        This article explores the often-overlooked "soft skills" that separate good data analysts 
        from great ones. Through the lens of my SDG 7 energy accessibility project, I discuss:
        
        - Why understanding the problem domain is crucial
        - How to think from your stakeholders' perspective
        - The importance of asking the right questions before diving into data
        - Balancing technical excellence with practical business impact
        - Learning to communicate insights effectively, not just build dashboards
        
        The reflection comes from real experience: spending over 200 hours on a single project taught me 
        that the value of analytics isn't in the code—it's in the insights that drive decisions.
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    
    # Article 2 - DragonWagon Project
    st.markdown('<div class="article-card">', unsafe_allow_html=True)
    st.subheader("DRAGONWAGON – Engage in Asia Competition")
    st.caption("Social Impact Project | Top 5 Finalist, University of Sydney | 2022")
    st.write("""
    Designed a mobile app to connect Vietnamese farmers with local buyers, promoting responsible supply chains 
    and addressing poverty through sustainable agriculture practices.
    
    **Key Topics:** UN SDG 1 (No Poverty), UN SDG 12 (Responsible Consumption and Production), 
    Supply Chain Sustainability, Social Impact, Agricultural Technology
    """)
    
    st.markdown("[📺 Watch Project Video on YouTube](https://www.youtube.com/watch?v=your-video-id)")
    
    with st.expander("Project Overview"):
        st.write("""
        **Challenge:** Vietnamese farmers struggle with market access and fair pricing, while urban consumers 
        lack transparency about food sources.
        
        **Solution:** DragonWagon is a mobile application that:
        - Directly connects farmers with local buyers, eliminating middlemen
        - Provides fair pricing mechanisms benefiting both producers and consumers
        - Promotes responsible and sustainable supply chains
        - Addresses SDG 1 by improving farmer livelihoods
        - Supports SDG 12 through responsible consumption patterns
        
        **Impact:** This project was recognized as a Top 5 Finalist in the prestigious Engage in Asia 
        Competition at the University of Sydney, competing against innovative solutions from across the region.
        
        **Skills Demonstrated:** ESG framework application, stakeholder analysis, social impact assessment, 
        sustainable business model design
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    
    # Add more articles
    st.info("💡 **Tip:** Add more articles by duplicating the structure above")

# -----------------------------------------------------------------------------
# About Me Page

elif page == "About Me":
    st.title("👩‍💻 About Me")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Background
        
        I'm a data analyst with a Master of Business Analytics from Macquarie University. 
        With experience spanning financial analysis, data consulting, and operations management, 
        I bring a comprehensive analytical approach to solving complex business problems.
        
        ### Professional Experience
        
        **Data Analyst** | Ptc. Consulting, Sydney (Jun 2023 – Dec 2025)
        - Conducted data collection and analysis on parking occupancy and turnover across Sydney suburbs
        - Created actionable insights for urban planning initiatives
        - Contributed to 9 projects delivering high-impact data records to city stakeholders
        
        **Financial Analyst** | Crawford and Company, Sydney (Jan 2023 – Jul 2023)
        - Managed 134 financial loss claim assessments including business interruption and stock loss policies
        - Delivered data-driven financial analyses for accurate claim assessment and settlement
        - Generated $56,780 in company revenue through efficient high-volume claims management
        
        **Operations Manager** | UAVS-NSW, Sydney (Mar 2020 – Dec 2021)
        - Analyzed and restructured organizational workflows through data-driven insights
        - Identified training needs through performance data analysis
        - Doubled application volume and reduced employee turnover by 83%
        
        **Mentor & Guest Speaker** | RISE UP Competition (AVLD), Vietnam (Jun 2022)
        - Presented research-driven ESG analysis for Vietnamese businesses using UN SDG frameworks
        - Mentored finalist team on blockchain solutions for textile supply chain sustainability
        
        ### Technical Skills
        
        **Programming & Databases:**
        - Python, R, PostgreSQL (2+ years experience)
        - SQL Server, Data Processing & ETL
        
        **Visualization & BI Tools:**
        - Power BI (Advanced DAX, Data Modeling, Microsoft Fabric)
        - Tableau (Interactive Dashboards)
        - Excel & MS Excel (Advanced Analytics)
        
        **Specializations:**
        - ESG & Sustainability Analytics (UN SDG Frameworks)
        - Business Intelligence & Reporting
        - Educational Analytics
        - Financial Analysis & Claim Assessment
        - Urban Planning Analytics
        
        **Core Competencies:**
        - Attention to Detail
        - Problem-Solving Skills
        - Communication Skills
        - AI Fluent
        
        ### Education
        
        **Master of Business Analytics**  
        Macquarie University, NSW (Feb 2024 – Dec 2025)
        
        **Master of Business Analytics**  
        University of Wollongong, NSW (Jun 2023 – Dec 2023)
        - Ranked 1st out of 149 students in Accounting and Financial Management
        - Ranked 2nd out of 100 students in Business Analytics for Economic and Market Environments
        
        **Bachelor of Commerce**  
        University of Sydney, NSW (Mar 2020 – Dec 2022)
        - Majors: Professional Accounting and Marketing
        
        ### Awards & Recognition
        
        **Vice-Chancellor's International Scholarship** | University of Sydney
        - Awarded based on academic excellence
        - First Vietnamese recipient of the scholarship
        
        **Top 5 Finalist** | Engage in Asia Competition, University of Sydney
        - Project: DragonWagon (Sustainable supply chain mobile app)
        """)
    
    with col2:
        st.markdown("""
        ### Connect With Me
        
        📧 **Email**  
        audrey.tranguyen@gmail.com
        
        📱 **Phone**  
        0432 063 579
        
        💼 **LinkedIn**  
        [linkedin.com/in/audrey-nguyen](https://www.linkedin.com/in/audrey-nguyen)
        
        🔗 **GitHub**  
        [github.com/audreynguyen](https://github.com/audreynguyen)
        
        📍 **Location**  
        Sydney, NSW, Australia
        """)
        
        st.write("---")
        
        st.markdown("""
        ### Areas of Interest
        
        - ESG & Sustainability Metrics
        - Data-driven Decision Making
        - Educational Analytics
        - UN Sustainable Development Goals
        - Business Intelligence & Reporting
        - Supply Chain Sustainability
        """)

# -----------------------------------------------------------------------------
# Footer

st.write("---")
st.caption("© 2025 Audrey Nguyen - Data Analytics Portfolio | Built with Streamlit")

