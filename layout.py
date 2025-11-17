"""
LAYOUT
Contains all CSS styling for the portfolio with Anthropic-inspired light theme
"""


import streamlit as st


def apply_custom_styles():
    """Apply custom CSS styling to the Streamlit app"""
   
    st.markdown("""
    <style>
        /* Import Professional Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
       
        /* ==================== GLOBAL STYLES ==================== */
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }

        /* Apply cream background EVERYWHERE */
        .main, 
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewBlockContainer"] {
            background-color: #fdfdf8 !important;
        }

        /* Main content area - Clean cream background */
        .main {
            padding: 2rem 3rem;
        }
       
        /* ==================== SIDEBAR STYLING ==================== */
        [data-testid="stSidebar"] {
            background-color: #f0f0ec;
            padding: 2.0rem 1.0rem;
            border-right: 1px solid #E5E5E5;
        }
       
        [data-testid="stSidebar"] hr {
            border: none;
            border-top: 1px solid #E5E5E5;
            margin: 1rem 0;
        }
       
        /* Sidebar headings */
        [data-testid="stSidebar"] h1 {
            font-size: 1.9rem;
            font-weight: 700;
            color: #6c6b5f;
            margin-bottom: 0.5rem;
        }
       
        [data-testid="stSidebar"] h2 {
            font-size: 1.6rem;
            font-weight: 700;
            color: #3e3a2a;
            margin-bottom: 0rem;
        }
       
        [data-testid="stSidebar"] h3 {
            font-size: 0.9rem;
            font-weight: 700;
            color: #3e3a2a;
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
       
        /* Profile image container - Vertical with tight spacing */
        .profile-container {
            text-align: center;
            margin-bottom: 1rem;
        }


        .profile-container img {
            border-radius: 50%;
            border: 3px solid #E5E5E5;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            margin-bottom: 0.5rem;
        }


        /* Tighter spacing for name and title */
        [data-testid="stSidebar"] .profile-container + h2 {
            margin-top: 0.5rem !important;
            margin-bottom: 0.25rem !important;
            line-height: 1.2 !important;
        }


        [data-testid="stSidebar"] .profile-container + h2 + p {
            margin-top: 0 !important;
            margin-bottom: 0 !important;
            line-height: 1.2 !important;
        }
               
       
        /* Contact items in sidebar */
        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 0.75rem;
            padding: 0.75rem;
            background-color: #FFFFFF;
            border-radius: 8px;
            border: 1px solid #E5E5E5;
            transition: all 0.2s ease;
            color: #333333;
            font-size: 0.85rem;
        }
       
        .contact-item:hover {
            border-color: #CC785C;
            box-shadow: 0 2px 4px rgba(204, 120, 92, 0.1);
        }
       
        .contact-item img {
            margin-right: 3px;
            flex-shrink: 0;
        }
       
        /* ==================== SKILL BADGES ==================== */
        .skill-badge {
            display: inline-block;
            padding: 6px 14px;
            margin: 4px 4px 4px 0;
            background-color: #F5F5F5;
            color: #333333;
            border: 1px solid #E5E5E5;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            transition: all 0.2s;
        }
       
        .skill-badge:hover {
            background-color: #FFF5F2;
            border-color: #CC785C;
            color: #e6e6de;
        }
       
        /* ==================== PROJECT CARDS ==================== */
        .project-card {
            background: #FFFFFF;
            border: 1px solid #E5E5E5;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
            height: 100%;
        }
       
        .project-card:hover {
            border-color: #e6e6de;
            box-shadow: 0 4px 12px rgba(204, 120, 92, 0.12);
            transform: translateY(-2px);
        }
       
        .project-card h4 {
            color: #1A1A1A;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            line-height: 1.4;
        }
       
        .project-card p {
            color: #666666;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
       
        /* ==================== BUTTONS ==================== */
        .simple-btn {
            display: inline-block;
            padding: 10px 24px;
            background-color: #CC785C;
            color: #FFFFFF !important;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.2s ease;
            border: 2px solid #CC785C;
        }
       
        .simple-btn:hover {
            background-color: #B86A4F;
            border-color: #B86A4F;
            text-decoration: none;
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(204, 120, 92, 0.2);
        }
       
        /* ==================== EXPERIENCE CARDS ==================== */
        .experience-card {
            background: #FAFAFA;
            border-left: 3px solid #CC785C;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 4px;
        }
       
        .experience-card h3 {
            color: #1A1A1A;
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
       
        .experience-card .company {
            color: #333333;
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 0.25rem;
        }
       
        .experience-card .period {
            color: #666666;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
       
        /* ==================== HEADERS ==================== */
        h1, h2, h3 {
            color: #1A1A1A;
        }
       
        h1 {
            font-weight: 700;
        }
       
        h2 {
            font-weight: 600;
        }
       
        /* ==================== METRICS ==================== */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem;
            font-weight: 600;
            color: #a1b727;  /* Changed from #1A1A1A */
        }

        [data-testid="stMetricLabel"] {
            color: #1A1A1A;
            font-size: 1.2 rem;
            font-weight: 900;
        }
       
        /* ==================== NAVIGATION ==================== */
        /* Page navigation styling */
        [data-testid="stSidebarNav"] {
            background-color: #FAFAFA;
            padding: 1rem 0;
        }
       
        [data-testid="stSidebarNav"] ul {
            padding: 0;
        }
       
        [data-testid="stSidebarNav"] li {
            margin-bottom: 0.25rem;
        }
       
        [data-testid="stSidebarNav"] a {
            color: #333333;
            padding: 0.75rem 1rem;
            border-radius: 6px;
            transition: all 0.2s;
        }
       
        [data-testid="stSidebarNav"] a:hover {
            background-color: #FFF5F2;
            color: #CC785C;
        }
       
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background-color: #FFF5F2;
            color: #CC785C;
            font-weight: 600;
        }
       
        /* ==================== SECTION HEADERS ==================== */
        .section-header {
            color: #1A1A1A;
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #CC785C;
            display: inline-block;
        }
       
        /* ==================== EDUCATION & AWARDS ==================== */
        .education-item, .award-item {
            background: #fdfdf8;
            border: 1px solid #d5d4cc;
            padding: 1.25rem;
            margin-bottom: 1rem;
            border-radius: 8px;
            transition: all 0.2s;
        }
       
        .education-item:hover, .award-item:hover {
            border-color: #CC785C;
            box-shadow: 0 2px 8px rgba(204, 120, 92, 0.1);
        }
       
        .education-item h4, .award-item h4 {
            color: #1A1A1A;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
       
        .education-item p, .award-item p {
            color: #666666;
        }
       
        /* ==================== ARTICLE CARDS ==================== */
        .article-card {
            background: #fdfdf8;
            border: 1px solid #d5d4cc;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.2s;
        }
       
        .article-card:hover {
            border-color: #CC785C;
            box-shadow: 0 2px 8px rgba(204, 120, 92, 0.1);
        }
       
        .article-card h3 {
            color: #1A1A1A;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
       
        .article-card p {
            color: #666666;
        }
       
        /* ==================== FOOTER ==================== */
        .footer {
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            background-color: #ecebe3;
            border-top: 1px solid #d5d4cc;
            border-radius: 8px;
            color: #666666;
        }
       
        /* ==================== DOWNLOAD BUTTON ==================== */
        .stDownloadButton button {
            background-color: #e6e6de;
            color: #FFFFFF;
            font-weight: 600;
            border: #d5d4cc;
            border-radius: 6px;
            padding: 0.75rem 1rem;
            width: 100%;
            transition: all 0.2s ease;
        }
       
        .stDownloadButton button:hover {
            background-color: #B86A4F;
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(204, 120, 92, 0.2);
        }
       
        /* ==================== FORM ELEMENTS ==================== */
        /* Selectbox */
        [data-baseweb="select"] {
            background-color: #FFFFFF;
            border: 1px solid #E5E5E5;
        }
       
        /* Input fields */
        input, textarea {
            background-color: #FFFFFF !important;
            color: #1A1A1A !important;
            border: 1px solid #E5E5E5 !important;
        }
       
        /* ==================== STREAMLIT OVERRIDES ==================== */
        /* Hide Streamlit branding */
        #MainMenu {visibility: visible;}
        footer {visibility: hidden;}
       
        /* Style Streamlit menu to match cream background */
        [data-testid="stMainMenu"] {
            background-color: #fdfdf8 !important;
        }

        /* Style the menu button itself */
        [data-testid="stMainMenu"] button {
            background-color: #fdfdf8 !important;
            color: #333333 !important;
        }

        /* Style the dropdown menu when opened */
        [data-testid="stMainMenu"] > div {
            background-color: #fdfdf8 !important;
        }

        /* Header bar background */
        header[data-testid="stHeader"] {
            background-color: #fdfdf8 !important;
        }
                      
        /* Links */
        a {
            color: #CC785C;
            text-decoration: none;
            transition: all 0.2s;
        }
       
        a:hover {
            color: #B86A4F;
            text-decoration: underline;
        }
       
        /* General text color */
        p, li, span {
            color: #333333;
        }
       
        /* Streamlit default text color override */
        .stMarkdown {
            color: #333333;
        }
       
        /* ==================== DIVIDERS ==================== */
        hr {
            border: none;
            border-top: 1px solid #E5E5E5;
            margin: 2rem 0;
        }
       
        /* ==================== CODE BLOCKS ==================== */
        code {
            background-color: #ecebe3;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.9em;
            color: #CC785C;
        }
       
        /* ==================== LISTS ==================== */
        ul {
            color: #333333;
        }
       
        li {
            margin-bottom: 0.5rem;
            line-height: 1.6;
        }
       
        /* ==================== TABLES ==================== */
        table {
            border-collapse: collapse;
            width: 100%;
        }
       
        th {
            background-color: #fdfdf8;
            color: #1A1A1A;
            font-weight: 600;
            padding: 0.75rem;
            border: 1px solid #E5E5E5;
        }
       
        td {
            padding: 0.75rem;
            border: 1px solid #E5E5E5;
            color: #333333;
        }
       
        /* ==================== CONTAINERS ==================== */
        [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
            border: 1px solid #E5E5E5;
            border-radius: 8px;
            padding: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)

