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
        padding: 2.0rem 0.5rem 2.0rem 1.0rem; /* Reduced right padding */
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
       
        /* Profile image container - Larger image */
        .profile-container {
            text-align: center;
            margin-bottom: 1rem;
        }

        .profile-container img {
            border-radius: 50%;
            border: 3px solid var(--border-color);
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            margin-bottom: 0.5rem;
            width: 200px !important;  /* Increased from default */
            height: 200px !important; /* Increased from default */
            object-fit: cover;
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

        /* ==================== SCROLLBAR STYLING ==================== */
        /* Sidebar scrollbar */
        [data-testid="stSidebar"] ::-webkit-scrollbar {
            width: 8px;
        }

        [data-testid="stSidebar"] ::-webkit-scrollbar-track {
            background: transparent;
            margin-right: 2px; /* Moves scrollbar closer to right edge */
        }

        [data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
            background: #c0c0c0;
            border-radius: 4px;
        }

        [data-testid="stSidebar"] ::-webkit-scrollbar-thumb:hover {
            background: #a0a0a0;
        }

        /* For Firefox */
        [data-testid="stSidebar"] {
            scrollbar-width: thin;
            scrollbar-color: #d2b891;
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
       
        /* ==================== PROFILE HEADER COMPONENTS ==================== */
        .profile-header-container h1 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }
       
        .profile-subtitle {
            font-size: 1.2rem;
            margin-bottom: 0.25rem;
        }
       
        .profile-role {
            color: var(--accent-green);
        }
       
        .profile-location {
            color: var(--text-secondary);
        }
       
        .profile-tagline {
            font-size: 1.0rem;
            color: var(--text-primary);
            margin-bottom: 2rem;
            line-height: 1.6;
        }
       
        /* ==================== SIDEBAR COMPONENTS ==================== */
        .sidebar-name {
            text-align: center;
            margin-top: 0.25rem;
            margin-bottom: 0.25rem;
            color: var(--text-primary);
        }
       
        .sidebar-role {
            text-align: center;
            color: var(--text-secondary);
            font-size: 1.2rem;
            margin-bottom: 0;
        }
       
        .profile-placeholder {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background-color: var(--bg-secondary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            color: var(--accent-primary);
            margin: 0 auto;
            border: 3px solid var(--border-color);
        }
       
        /* ==================== EDUCATION & AWARDS DETAIL CLASSES ==================== */
        .education-school {
            margin: 0 0 0.25rem 0;
            color: var(--text-secondary);
            font-weight: 500;
        }
       
        .education-period {
            margin: 0 0 0.5rem 0;
            color: var(--text-tertiary);
            font-size: 0.9rem;
        }
       
        .education-details {
            margin: 0;
            color: var(--text-secondary);
            font-style: italic;
        }
       
        .award-organization {
            margin: 0 0 0.25rem 0;
            color: var(--text-secondary);
            font-weight: 500;
        }
       
        .award-details {
            margin: 0;
            color: var(--text-tertiary);
        }
       
        /* ==================== ARTICLE CARD CLASSES ==================== */
        .article-date {
            margin: 0 0 1rem 0;
            color: var(--text-tertiary);
            font-size: 0.9rem;
        }
       
        .article-description {
            margin: 0 0 1rem 0;
            color: var(--text-secondary);
            line-height: 1.6;
        }
       
        /* ==================== FOOTER CLASSES ==================== */
        .footer h3 {
            color: var(--text-primary);
            margin-bottom: 0.75rem;
            font-weight: 600;
        }
       
        .footer-emoji {
            text-align: center;
            font-size: 1.2rem;
            margin: 0.5rem 0;
        }
       
        .footer-text {
            color: var(--text-tertiary);
            margin-bottom: 0.5rem;
        }
       
        .footer-copyright {
            color: var(--text-tertiary);
            font-size: 0.9rem;
            opacity: 0.7;
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

        /* Force menu icons to be dark in both themes */
        [data-testid="stMainMenu"] svg {
            color: #333333 !important;
            fill: #333333 !important;
        }

        [data-testid="stMainMenu"] button:hover svg {
            color: var(--accent-primary) !important;
            fill: var(--accent-primary) !important;
        }

        /* Target the three-dot menu specifically */
        header[data-testid="stHeader"] button svg {
            color: #333333 !important;
            fill: #333333 !important;
        }

        header[data-testid="stHeader"] button:hover svg {
            color: var(--accent-primary) !important;
            fill: var(--accent-primary) !important;
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
       
        /* Hide mobile profile container on desktop */
        .mobile-profile-container {
            display: none;
        }
       
        /* ==================== MOBILE RESPONSIVE STYLES ==================== */
        @media only screen and (max-width: 768px) {
            /* Main content padding */
            .main {
                padding: 1rem !important;
            }
           
            /* Profile header responsive */
            .profile-header-container h1 {
                font-size: 1.8rem !important;
            }
           
            .profile-subtitle {
                font-size: 1rem !important;
            }
           
            .profile-tagline {
                font-size: 0.9rem !important;
            }
           
            /* Sidebar adjustments */
            [data-testid="stSidebar"] {
                padding: 1.5rem 0.75rem !important;
            }
           
            [data-testid="stSidebar"] h1 {
                font-size: 1.5rem !important;
            }
           
            [data-testid="stSidebar"] h2 {
                font-size: 1.3rem !important;
            }
           
            [data-testid="stSidebar"] h3 {
                font-size: 0.8rem !important;
            }
           
            /* HIDE profile photo in sidebar on mobile */
            [data-testid="stSidebar"] .profile-container {
                display: none !important;
            }
           
            /* SHOW profile photo in main content on mobile */
            .main .mobile-profile-container {
                display: block !important;
                text-align: center;
                margin-bottom: 1.5rem;
                padding: 1rem;
                background-color: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: 12px;
            }
           
            .main .mobile-profile-container img {
                width: 120px !important;
                height: 120px !important;
                border-radius: 50%;
                border: 3px solid var(--border-color);
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                margin-bottom: 0.75rem;
                display: block;
                margin-left: auto;
                margin-right: auto;
            }
           
            .main .mobile-profile-container h2 {
                font-size: 1.5rem !important;
                font-weight: 700;
                color: var(--text-primary);
                margin-bottom: 0.25rem;
            }
           
            .main .mobile-profile-container p {
                font-size: 0.95rem !important;
                color: var(--text-secondary);
                margin-bottom: 0;
            }
           
            /* Footer responsive */
            .footer {
                padding: 1.5rem 1rem !important;
                margin-top: 2rem !important;
            }
           
            .footer h3 {
                font-size: 1.2rem !important;
            }
           
            .footer-emoji {
                font-size: 1rem !important;
            }
           
            .footer-text, .footer-copyright {
                font-size: 0.85rem !important;
            }
           
            /* Contact items - stack better on mobile */
            .contact-item {
                font-size: 0.8rem !important;
                padding: 0.6rem !important;
                margin-bottom: 0.5rem !important;
            }
           
            /* Headers */
            h1 {
                font-size: 1.8rem !important;
            }
           
            h2 {
                font-size: 1.5rem !important;
            }
           
            h3 {
                font-size: 1.2rem !important;
            }
           
            .section-header {
                font-size: 1.5rem !important;
            }
           
            /* Project cards */
            .project-card {
                padding: 1rem !important;
                margin-bottom: 1rem !important;
            }
           
            .project-card h4 {
                font-size: 1rem !important;
            }
           
            .project-card p {
                font-size: 0.9rem !important;
            }
           
            /* Skill badges - smaller on mobile */
            .skill-badge {
                padding: 4px 10px !important;
                margin: 3px 3px 3px 0 !important;
                font-size: 0.75rem !important;
            }
           
            /* Buttons */
            .simple-btn {
                padding: 8px 16px !important;
                font-size: 0.85rem !important;
                display: block !important;
                text-align: center !important;
                width: 100% !important;
                margin-bottom: 0.5rem !important;
            }
           
            .stDownloadButton button {
                padding: 0.6rem 0.8rem !important;
                font-size: 0.85rem !important;
            }
           
            /* Experience cards */
            .experience-card {
                padding: 1rem !important;
                margin-bottom: 1rem !important;
            }
           
            .experience-card h3 {
                font-size: 1.1rem !important;
            }
           
            .experience-card .company {
                font-size: 0.95rem !important;
            }
           
            .experience-card .period {
                font-size: 0.85rem !important;
            }
           
            /* Education and award items */
            .education-item, .award-item {
                padding: 1rem !important;
                margin-bottom: 0.75rem !important;
            }
           
            .education-item h4, .award-item h4 {
                font-size: 1rem !important;
            }
           
            .education-item p, .award-item p {
                font-size: 0.9rem !important;
            }
           
            /* Article cards */
            .article-card {
                padding: 1rem !important;
                margin-bottom: 1rem !important;
            }
           
            .article-card h3 {
                font-size: 1.1rem !important;
            }
           
            .article-card p {
                font-size: 0.9rem !important;
            }
           
            /* Metrics */
            [data-testid="stMetricValue"] {
                font-size: 1.5rem !important;
            }
           
            [data-testid="stMetricLabel"] {
                font-size: 0.95rem !important;
            }
           
            /* Footer */
            .footer {
                padding: 1.5rem 1rem !important;
                margin-top: 2rem !important;
            }
           
            /* Tables - make them scrollable on mobile */
            table {
                display: block;
                overflow-x: auto;
                white-space: nowrap;
            }
           
            th, td {
                padding: 0.5rem !important;
                font-size: 0.85rem !important;
            }
           
            /* Lists */
            li {
                font-size: 0.9rem !important;
                margin-bottom: 0.4rem !important;
            }
           
            /* General text */
            p, span {
                font-size: 0.9rem !important;
            }
           
            /* Containers */
            [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
                padding: 0.75rem !important;
            }
        }
       
        /* ==================== EXTRA SMALL MOBILE (< 480px) ==================== */
        @media only screen and (max-width: 480px) {
            /* Even more compact for very small screens */
            .main {
                padding: 0.75rem !important;
            }
           
            [data-testid="stSidebar"] {
                padding: 1rem 0.5rem !important;
            }
           
            .profile-container img {
                width: 120px !important;
                height: 120px !important;
            }
           
            /* Profile header extra small */
            .profile-header-container h1 {
                font-size: 1.5rem !important;
            }
           
            .profile-subtitle {
                font-size: 0.9rem !important;
            }
           
            .profile-tagline {
                font-size: 0.85rem !important;
            }
           
            h1 {
                font-size: 1.5rem !important;
            }
           
            h2 {
                font-size: 1.3rem !important;
            }
           
            .section-header {
                font-size: 1.3rem !important;
            }
           
            .project-card, .experience-card, .education-item, .award-item, .article-card {
                padding: 0.75rem !important;
            }
           
            .skill-badge {
                padding: 3px 8px !important;
                font-size: 0.7rem !important;
            }
           
            /* Footer extra small */
            .footer {
                padding: 1rem 0.75rem !important;
            }
           
            .footer h3 {
                font-size: 1.1rem !important;
            }
           
            .footer-emoji {
                font-size: 0.9rem !important;
            }
           
            .footer-text, .footer-copyright {
                font-size: 0.8rem !important;
            }
        }
       
        /* ==================== TABLET (769px - 1024px) ==================== */
        @media only screen and (min-width: 769px) and (max-width: 1024px) {
            .main {
                padding: 1.5rem 2rem !important;
            }
           
            .profile-container img {
                width: 180px !important;
                height: 180px !important;
            }
           
            .project-card {
                padding: 1.25rem !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)