"""
LAYOUT
Contains all CSS styling for the portfolio with Anthropic-inspired light theme
"""


import streamlit as st


def apply_custom_styles():
    """Apply custom CSS styling with light and dark theme support"""
   
    st.markdown("""
    <style>
        /* Import Professional Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
       
        /* ==================== LIGHT THEME (DEFAULT) ==================== */
        :root {
            --bg-primary: #fdfdf8;
            --bg-secondary: #f0f0ec;
            --bg-card: #FFFFFF;
            --bg-hover: #FFF5F2;
            --text-primary: #1A1A1A;
            --text-secondary: #333333;
            --text-tertiary: #666666;
            --accent-primary: #CC785C;
            --accent-secondary: #B86A4F;
            --accent-green: #3d5519;
            --accent-lime: #b1c92c;
            --border-color: #E5E5E5;
            --sidebar-bg: #f0f0ec;
        }
       
        /* ==================== DARK THEME ==================== */
        @media (prefers-color-scheme: dark) {
            :root {
                --bg-primary: #1a1a1a;
                --bg-secondary: #2d2d2d;
                --bg-card: #252525;
                --bg-hover: #3a3a3a;
                --text-primary: #e5e5e5;
                --text-secondary: #d0d0d0;
                --text-tertiary: #a0a0a0;
                --accent-primary: #e69580;
                --accent-secondary: #d4816d;
                --accent-green: #7a9b3a;
                --accent-lime: #c5d945;
                --border-color: #404040;
                --sidebar-bg: #2d2d2d;
            }
        }
       
        /* ==================== GLOBAL STYLES ==================== */
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }

        /* Apply background colors using variables */
        .main, 
        .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewBlockContainer"] {
            background-color: var(--bg-primary) !important;
        }

        .main {
            padding: 2rem 3rem;
        }
       
        /* ==================== SIDEBAR STYLING ==================== */
        [data-testid="stSidebar"] {
            background-color: var(--sidebar-bg);
            padding: 2.0rem 1.0rem;
            border-right: 1px solid var(--border-color);
        }
       
        [data-testid="stSidebar"] hr {
            border: none;
            border-top: 1px solid var(--border-color);
            margin: 1rem 0;
        }
       
        /* Sidebar headings */
        [data-testid="stSidebar"] h1 {
            font-size: 1.9rem;
            font-weight: 700;
            color: var(--text-tertiary);
            margin-bottom: 0.5rem;
        }
       
        [data-testid="stSidebar"] h2 {
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-secondary);
            margin-bottom: 0rem;
        }
       
        [data-testid="stSidebar"] h3 {
            font-size: 0.9rem;
            font-weight: 700;
            color: var(--text-secondary);
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
       
        /* Profile image container */
        .profile-container {
            text-align: center;
            margin-bottom: 1rem;
        }

        .profile-container img {
            border-radius: 50%;
            border: 3px solid var(--border-color);
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            margin-bottom: 0.5rem;
        }

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
            background-color: var(--bg-card);
            border-radius: 8px;
            border: 1px solid var(--border-color);
            transition: all 0.2s ease;
            color: var(--text-secondary);
            font-size: 0.85rem;
        }
       
        .contact-item:hover {
            border-color: var(--accent-primary);
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
            background-color: var(--bg-secondary);
            color: var(--text-secondary);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            transition: all 0.2s;
        }
       
        .skill-badge:hover {
            background-color: var(--bg-hover);
            border-color: var(--accent-primary);
            color: var(--accent-primary);
        }
       
        /* ==================== PROJECT CARDS ==================== */
        .project-card {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
            height: 100%;
        }
       
        .project-card:hover {
            border-color: var(--accent-primary);
            box-shadow: 0 4px 12px rgba(204, 120, 92, 0.12);
            transform: translateY(-2px);
        }
       
        .project-card h4 {
            color: var(--text-primary);
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            line-height: 1.4;
        }
       
        .project-card p {
            color: var(--text-tertiary);
            line-height: 1.6;
            margin-bottom: 1rem;
        }
       
        /* ==================== BUTTONS ==================== */
        .simple-btn {
            display: inline-block;
            padding: 10px 24px;
            background-color: var(--accent-primary);
            color: #FFFFFF !important;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.2s ease;
            border: 2px solid var(--accent-primary);
        }
       
        .simple-btn:hover {
            background-color: var(--accent-secondary);
            border-color: var(--accent-secondary);
            text-decoration: none;
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(204, 120, 92, 0.2);
        }
       
        /* ==================== EXPERIENCE CARDS ==================== */
        .experience-card {
            background: var(--bg-secondary);
            border-left: 3px solid var(--accent-primary);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 4px;
        }
       
        .experience-card h3 {
            color: var(--text-primary);
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
       
        .experience-card .company {
            color: var(--text-secondary);
            font-weight: 600;
            font-size: 1rem;
            margin-bottom: 0.25rem;
        }
       
        .experience-card .period {
            color: var(--text-tertiary);
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
       
        /* ==================== HEADERS ==================== */
        h1, h2, h3 {
            color: var(--text-primary);
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
            color: var(--accent-lime) !important;
        }
       
        [data-testid="stMetricLabel"] {
            color: var(--text-tertiary);
            font-size: 1.1rem;
            font-weight: 600;
        }
       
        /* ==================== HEADER & MENU STYLING ==================== */
        header[data-testid="stHeader"] {
            background-color: var(--bg-primary) !important;
        }

        [data-testid="stMainMenu"] {
            background-color: var(--bg-primary) !important;
        }

        [data-testid="stMainMenu"] button {
            background-color: transparent !important;
            color: var(--text-secondary) !important;
        }

        [data-testid="stMainMenu"] button:hover {
            background-color: var(--bg-secondary) !important;
            color: var(--accent-primary) !important;
        }
       
        /* ==================== NAVIGATION ==================== */
        [data-testid="stSidebarNav"] {
            background-color: var(--bg-secondary);
            padding: 1rem 0;
        }
       
        [data-testid="stSidebarNav"] a {
            color: var(--text-secondary);
            padding: 0.75rem 1rem;
            border-radius: 6px;
            transition: all 0.2s;
        }
       
        [data-testid="stSidebarNav"] a:hover {
            background-color: var(--bg-hover);
            color: var(--accent-primary);
        }
       
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background-color: var(--bg-hover);
            color: var(--accent-primary);
            font-weight: 600;
        }
       
        /* ==================== SECTION HEADERS ==================== */
        .section-header {
            color: var(--text-primary);
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--accent-primary);
            display: inline-block;
        }
       
        /* ==================== EDUCATION & AWARDS ==================== */
        .education-item, .award-item {
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            padding: 1.25rem;
            margin-bottom: 1rem;
            border-radius: 8px;
            transition: all 0.2s;
        }
       
        .education-item:hover, .award-item:hover {
            border-color: var(--accent-primary);
            box-shadow: 0 2px 8px rgba(204, 120, 92, 0.1);
        }
       
        .education-item h4, .award-item h4 {
            color: var(--text-primary);
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
       
        .education-item p, .award-item p {
            color: var(--text-tertiary);
        }
       
        /* ==================== ARTICLE CARDS ==================== */
        .article-card {
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.2s;
        }
       
        .article-card:hover {
            border-color: var(--accent-primary);
            box-shadow: 0 2px 8px rgba(204, 120, 92, 0.1);
        }
       
        .article-card h3 {
            color: var(--text-primary);
            font-weight: 600;
            margin-bottom: 0.5rem;
        }
       
        .article-card p {
            color: var(--text-tertiary);
        }
       
        /* ==================== FOOTER ==================== */
        .footer {
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            background-color: #ecebe3 !important;
            border-top: 1px solid var(--border-color);
            border-radius: 8px;
            color: var(--text-tertiary);
        }

        @media (prefers-color-scheme: dark) {
            .footer {
                background-color: #2a2a2a !important;
            }
        }
       
        /* ==================== DOWNLOAD BUTTON ==================== */
        .stDownloadButton button {
            background-color: var(--accent-primary);
            color: #FFFFFF;
            font-weight: 600;
            border: none;
            border-radius: 6px;
            padding: 0.75rem 1rem;
            width: 100%;
            transition: all 0.2s ease;
        }
       
        .stDownloadButton button:hover {
            background-color: var(--accent-secondary);
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(204, 120, 92, 0.2);
        }
       
        /* ==================== FORM ELEMENTS ==================== */
        [data-baseweb="select"] {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
        }
       
        input, textarea {
            background-color: var(--bg-card) !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
        }
       
        /* ==================== STREAMLIT OVERRIDES ==================== */
        footer {visibility: hidden;}
       
        /* Links */
        a {
            color: var(--accent-primary);
            text-decoration: none;
            transition: all 0.2s;
        }
       
        a:hover {
            color: var(--accent-secondary);
            text-decoration: underline;
        }
       
        /* General text color */
        p, li, span {
            color: var(--text-secondary);
        }
       
        .stMarkdown {
            color: var(--text-secondary);
        }
       
        /* ==================== DIVIDERS ==================== */
        hr {
            border: none;
            border-top: 1px solid var(--border-color);
            margin: 2rem 0;
        }
       
        /* ==================== CODE BLOCKS ==================== */
        code {
            background-color: var(--bg-secondary);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.9em;
            color: var(--accent-primary);
        }
       
        /* ==================== LISTS ==================== */
        ul {
            color: var(--text-secondary);
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
            background-color: var(--bg-secondary);
            color: var(--text-primary);
            font-weight: 600;
            padding: 0.75rem;
            border: 1px solid var(--border-color);
        }
       
        td {
            padding: 0.75rem;
            border: 1px solid var(--border-color);
            color: var(--text-secondary);
        }
       
        /* ==================== CONTAINERS ==================== */
        [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 1rem;
        }
    </style>
    """, unsafe_allow_html=True)