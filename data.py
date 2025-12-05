"""
Portfolio Data
All personal information, skills, experience, projects, and education data
"""

PROFILE = {
    "name": "Audrey Nguyen",
    "role": "Data Analyst",
    "tagline": "I generate accurate, meaningful business insights using Power BI, Python, and ESG frameworks to guide strategic decisions.",
    "location": "Sydney, Australia",
    "email": "audrey.tranguyen@gmail.com",
    "website": None,
    "github": "https://github.com/audreyngnn",
    "linkedin": "https://www.linkedin.com/in/audrey-tra-nguyen/",
    "phone": "0432 063 579"
}

SKILLS = [
    {"name": "Power BI", "level": 95, "keywords": ["DAX", "Data Modeling", "Microsoft Fabric", "Data Visualisation"]},
    {"name": "Tableau", "level": 85, "keywords": ["Data Visualization", "Data Visualisation"]},
    {"name": "Python", "level": 85, "keywords": ["Data Cleaning","Data Analysis", "Predictives"]},
    {"name": "R", "level": 80, "keywords": ["Data Cleaning", "Predictives", "Data Visualisation"]},
    {"name": "PostgreSQL", "level": 80, "keywords": ["Database Design", "SQL Queries"]},
    {"name": "Excel", "level": 90, "keywords": ["DAX", "Advanced Analytics", "Data Analysis", "Power Pivot"]},
    {"name": "SQL Server", "level": 80, "keywords": ["Database Management", "Queries", "ER Diagram"]},
]

EXPERIENCE = [
    {
        "role": "Student Research Assistant",
        "company": "Macquarie University",
        "period": "Jan 2025 – Oct 2025",
        "location": "Sydney, NSW",
        "description": "Analyzed how customers perceive virtual try-on technology and its impact on digital shopping behavior",
        "highlights": [
            "Analyzed engagement and conversion patterns in AR/VR virtual try-on environments to understand customer perceptions",
            "Researched VTO model advancements and realism to assess their impact on digital retail experiences",
            "Summarized findings into clear reports supporting product optimization and research direction"
        ],
        "achievement": None,
        "projects": None,
        "tech": ["Machine Learning", "AR/VR Analytics"],
        "domain": ["E-commerce Analytics", "Academic Research", "Virtual Try-On Technology"]
    },

    {
        "role": "Data Analyst",
        "company": "Ptc. Consulting",
        "period": "Jun 2023 – Dec 2024",
        "location": "Sydney, NSW",
        "description": "Delivered insights that informed nine urban planning and strategic infrastructure initiatives",
        "highlights": [
            "Collected and validated survey data, transforming raw datasets into data-informed recommendations",
            "Analyzed behavioral trends to identify patterns in customer movement, peak demand, and infrastructure use",
            "Produced concise reports for councils and business partners to support decision-making"
        ],
        "achievement": None,
        "projects": "Wollongong City Council Parking Strategy, Harbourside Car Park, Bonnyrigg Plaza, Deepwater Plaza, Landmark Building (St Leonards)",
        "tech": ["Advanced Excel", "Survey Data Analysis"],
        "domain": ["Urban Planning", "Infrastructure Analytics", "Stakeholder Communication"]
    },

    {
        "role": "Financial Analyst",
        "company": "Crawford and Company",
        "period": "Jan 2023 – Jun 2023",
        "location": "Sydney, NSW",
        "description": "Assessed 134 financial loss claims by analyzing operational patterns and key business performance drivers",
        "highlights": [
            "Collaborated cross-functionally with insurers, clients, and stakeholders to gather accurate case data",
            "Developed insight-driven analyses supporting fair and evidence-based business interruption settlements",
            "Produced detailed reports including methodology, financial modelling outcomes, and recommendations"
        ],
        "achievement": "Generated ~$56,780 in company revenue",
        "projects": "McDonald's (2022 flood interruption), Sydney Opera House (COVID-19 interruption)",
        "tech": ["Excel", "Financial Modeling"],
        "domain": ["Financial Analysis", "Forensic Accounting", "Claim Investigation", "Stakeholder Communication"]
    },

    {
        "role": "Operations Manager",
        "company": "UAVS-NSW",
        "period": "Mar 2020 – Dec 2021",
        "location": "Sydney, NSW",
        "description": "Led operational strategy and performance optimization across multiple concurrent projects",
        "highlights": [
            "Analyzed workflow, performance metrics, and operational bottlenecks to drive process optimization",
            "Coordinated cross-functional teams to ensure alignment and timely project execution",
            "Leveraged data insights to identify training needs and support capability-building initiatives"
        ],
        "achievement": "Doubled application volume and reduced employee turnover by 83%",
        "projects": None,
        "tech": ["Excel", "Process Analytics"],
        "domain": ["Process Optimization", "HR Analysis", "Project Management", "Stakeholder Communication"]
    },

    {
        "role": "Mentor & Guest Speaker",
        "company": "RISE UP Competition (AVLD)",
        "period": "Jun 2022",
        "location": "Vietnam",
        "description": None,
        "highlights": [
            "Delivered ESG/SDG research and market insights on sustainability risks impacting Vietnamese businesses",
            "Advised teams on blockchain-based transparency solutions, impact measurement, and strategic implementation"
        ],
        "achievement": "Strengthened leadership, analytical communication, and coaching capabilities",
        "projects": None,
        "tech": ["Blockchain"],
        "domain": ["ESG Analysis", "UN SDG", "Sustainability", "Stakeholder Communication"]
    },

{
        "role": "Marketing & Social Media Team",
        "company": "PTE MAGIC",
        "period": "Jun 2021 – Aug 2021",
        "location": "Sydney, NSW, Australia",
        "description": "Managed content performance and audience engagement across social media channels to optimize marketing effectiveness",
        "highlights": [
            "Managed content performance across company social media channels (Facebook page and group), monitoring engagement metrics to maintain optimal performance levels",
            "Analyzed audience engagement data to inform monthly content strategies, including posting frequency optimization and campaign effectiveness",
            "Collaborated with sales team to gather and analyze customer feedback data, translating insights into actionable content adjustments"
        ],
        "achievement": None,
        "projects": None,
        "tech": ["Social Media Analytics", "Content Strategy", "Excel"],
        "domain": ["Marketing Analytics", "Social Media Management"]
    },
    {
        "role": "Brand Management Team",
        "company": "Timex Group",
        "period": "Jan 2018 – Jun 2018",
        "location": "Toronto, ON, Canada",
        "description": "Supported digital catalog management and marketing campaign analysis using performance data and engagement metrics",
        "highlights": [
            "Managed digital product catalog updates and website content optimization based on performance data and user engagement metrics",
            "Monitored product launch performance and analyzed customer interaction data to inform content strategy",
            "Supported marketing campaign analysis by tracking key performance indicators and conversion metrics"
        ],
        "achievement": None,
        "projects": None,
        "tech": ["Web Analytics", "Performance Tracking", "Content Management"],
        "domain": ["Marketing Analytics", "E-commerce", "Brand Management"]
    }

]

PROJECTS = [
    {
        "name": "UN SDG 7: A Global Energy Story (2000–2022)",
        "description": "An interactive Power BI dashboard visualising global progress toward UN SDG 7 (Affordable and Clean Energy) from 2000–2022, highlighting trends in electricity access, clean cooking, and renewable energy adoption.",
        "tech": ["Power BI", "DAX", "Microsoft Fabric", "Data Modelling", "Data Cleaning"],
        "domain": ["ESG Analysis", "UN SDG"],
        "link": "https://app.powerbi.com/view?r=eyJrIjoiMGIwODZiNmEtN2FmNS00OTMwLWE2MDYtZTZiYzA0NDE2ODhhIiwidCI6IjgyYzUxNGMxLWE3MTctNDA4Ny1iZTA2LWQ0MGQyMDcwYWQ1MiJ9",
        "image": "images/sdg7_cover.jpg",
        "year": "2025"
    },
    {
        "name": "HR Operations Process Optimization",
        "description": "Process optimization framework documenting agile-style information flow, feedback loops, task delegation, and reporting workflows. Resulted in doubled applications and 83% reduction in turnover at UAVS-NSW.",
        "tech": ["Process Mapping", "Diagrams.net", "Excel", "Organizational Design"],
        "domain": ["HR Analytics", "Operations"],
        "link": "https://github.com/yourusername/hr-process-optimization",
        "image": "images/hr_process_cover.jpg",
        "year": "2021"
    },
    {
        "name": "University Student Retention Analytics",
        "description": "Comprehensive dashboard for Macquarie University analyzing student progression, retention rates, and transfer patterns across programs with advanced DAX measures.",
        "tech": ["Power BI", "DAX", "Data Modelling", "Data Cleaning"],
        "domain": ["Educational Analytics", "Retention Analytics"],
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNGZhMjg0ODUtNjIyZC00OWRiLWFjNzctY2VkMzM2Y2EwZGMzIiwidCI6IjgyYzUxNGMxLWE3MTctNDA4Ny1iZTA2LWQ0MGQyMDcwYWQ1MiJ9",
        "image": "images/retention_cover.jpg",
        "year": "2024"
    },
    {
        "name": "Australian Road Death Analysis (2010-2024)",
        "description": "Analyzed Australian road fatalities (2010-2024) using three R visualizations to identify temporal patterns, high-risk demographics, and policy effectiveness toward the 2030 target.",
        "tech": ["R", "Data Visualization", "Data Analysis"],
        "domain": ["Risk Analytics", "Public Policy"],
        "link": "https://github.com/audreyngnn/R-Project-1",
        "image": "images/road_cover.jpg",
        "year": "2024"
    },
    {
        "name": "Global Earthquake Risk Analysis",
        "description": "This analysis transforms earthquake data into actionable emergency management strategies. Here's what the data tells us and what we should do about it.",
        "tech": ["Tableau", "Data Visualization", "Risk Analysis"],
        "domain": ["Risk Analytics", "Emergency Management"],
        "link": "https://github.com/audreyngnn/Tableau-Project-1",
        "image": "images/earthquake_cover.jpg",
        "year": "2024"
    },
    {
        "name": "Predictive Analytics: AirBnb Pricing in Melbourne",
        "description": "This project focuses on building a machine learning model to predict the price of Airbnb listings in Melbourne based on property and host features. The model was trained on historical data and applied to unseen listings, with the aim of achieving high predictive accuracy.",
        "tech": ["Python", "Machine Learning", "Feature Engineering", "Predictive Modeling"],
        "domain": ["Predictive Analytics", "Price Analytics", "Real Estate"],
        "link": "https://github.com/audreyngnn/Python-Project-1",
        "image": "images/airbnb.jpg",
        "year": "2024"
    },
    {
        "name": "Furniture E-Commerce Sales Analytics",
        "description": "This project demonstrates advanced SQL Server capabilities through comprehensive analysis of furniture e-commerce sales data, focusing on business intelligence insights critical for data-driven decision-making in the furniture retail industry.",
        "tech": ["SQL Server", "Data Analysis", "Business Intelligence"],
        "domain": ["E-Commerce Analytics", "Sales Analytics", "Retail"],
        "link": "https://github.com/audreyngnn/SQL-Project-1",
        "image": "images/sql_furniture.jpg",
        "year": "2024"
    },
    {
        "name": "Global Internet Usage Data - E-Commerce Opportunity",
        "description": "This project applies SQL-based data cleaning and analysis to global internet penetration data to uncover e-commerce market opportunities. The goal is to transform raw World Bank/ITU data into a reliable, business-ready dataset for strategic decision-making.",
        "tech": ["SQL", "Data Cleaning", "Market Analysis"],
        "domain": ["E-Commerce Analytics", "Market Research", "Data Quality"],
        "link": "https://github.com/audreyngnn/SQL-Project-2",
        "image": "images/sql_internet.jpg",
        "year": "2024"
    },
    {
        "name": "ProApp SQL Database Project",
        "description": "This project demonstrates how I applied SQL and analytics thinking to solve real business problems for ProApp, a startup revolutionizing the service industry by connecting customers seeking personal services, tradespeople offering their skills, and suppliers providing materials and equipment.",
        "tech": ["SQL", "Database Design", "Business Analytics"],
        "domain": ["Database Management", "Startup Analytics", "Service Industry"],
        "link": "https://github.com/audreyngnn/SQL-Project-3",
        "image": "images/sql_proapp.jpg",
        "year": "2024"
    },
    {
        "name": "DRAGONWAGON – Engage in Asia",
        "description": "Designed a mobile app to connect Vietnamese farmers with local buyers, promoting responsible supply chains. Targeted SDGs 1 (No Poverty) and 12 (Responsible Consumption and Production). Top 5 Finalist at University of Sydney.",
        "tech": ["Blockchain", "Mobile App Design", "UX"],
        "domain": ["ESG Analysis", "UN SDG", "Supply Chain"],
        "link": "https://www.youtube.com/watch?v=your-video-id",
        "image": "images/dragonwagon_cover.jpg",
        "year": "2022"
    }
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