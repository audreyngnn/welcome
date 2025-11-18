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
        "role": "Research Assistant",
        "company": "Macquarie University",
        "period": "Jan 2025 – Jun 2025",
        "location": "Sydney, NSW",
        "highlights": [
            "Analyzed user engagement metrics for virtual try-on technology in e-commerce environments",
            "Conducted data-driven research on digital customer experience, measuring conversion rates and user interaction with AR/VR features",
        ],
        "tech": ["Machine Learning"],
        "domain": ["E-commerce Analytics", "Academic Research", "User Engagement Metrics"]
    },

    {
        "role": "Data Analyst",
        "company": "Ptc. Consulting",
        "period": "Jun 2023 – Dec 2024",
        "location": "Sydney, NSW",
        "highlights": [
            "Accurate data collection on parking occupancy and turnover by conducting surveys across Sydney suburbs",
            "Data analysis by working with collected parking metrics, creating actionable insights for urban planning initiatives",
            "Achievement: Contributed to nine projects by delivering high-impact data records to city stakeholders",
        ],
        "tech": ["Excel"],
        "domain": ["Urban Planning", "Survey Data", "Parking Analytics", "Stakeholder Communication"],
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
        "tech": ["Excel"],
        "domain": ["Financial Analysis", "Forensic Accounting", "Claim Investigation", "Stakeholder Communication"],
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
        "tech": ["Excel"],
        "domain": ["Process Optimization", "Performance Analysis", "Project Management", "Stakeholder Communication"]
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
        "tech": ["Blockchain"],
        "domain": ["ESG Analysis", "UN SDG", "Sustainability", "Stakeholder Communication"]
    },
]

PROJECTS = [
    {
        "name": "Powering Tomorrow: Tracking Global Progress on SDG 7 (2000–2022)",
        "description": "An interactive Power BI dashboard visualising global progress toward UN SDG 7 (Affordable and Clean Energy) from 2000–2022, highlighting trends in electricity access, clean cooking, and renewable energy adoption.",
        "tech": ["Power BI", "DAX", "Microsoft Fabric", "Data Modelling", "Data Cleaning"],
        "domain": ["ESG Analysis", "UN SDG"],
        "link": "https://app.powerbi.com/view?r=eyJrIjoiNzQ1OGYxMDYtY2Y5ZS00ZDg0LTg5MTQtMjgyNGEzZTZhNjcxIiwidCI6IjgyYzUxNGMxLWE3MTctNDA4Ny1iZTA2LWQ0MGQyMDcwYWQ1MiJ9",
        "image": "images/sdg7_cover.jpg",
        "year": "2025"
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
        "name": "Bike Sales Dashboard",
        "description": "Sales analytics dashboard tracking bike sales performance, revenue metrics, and customer insights with interactive visualizations.",
        "tech": ["Power BI", "DAX", "Data Modelling", "Data Cleaning"],
        "domain": ["Sales Analytics", "Retail Analysis"],
        "link": "https://app.powerbi.com/view?r=eyJrIjoiM2I4MjE4MjEtOTc3MC00ZmU3LWJmYjctYjczZTc5YjdkMTc3IiwidCI6IjgyYzUxNGMxLWE3MTctNDA4Ny1iZTA2LWQ0MGQyMDcwYWQ1MiJ9",
        "image": "images/bike_sales_cover.jpg",
        "year": "2024"
    },
    {
        "name": "DRAGONWAGON – Engage in Asia",
        "description": "Designed a mobile app to connect Vietnamese farmers with local buyers, promoting responsible supply chains. Targeted SDGs 1 (No Poverty) and 12 (Responsible Consumption and Production). Top 5 Finalist at University of Sydney.",
        "tech": ["Blockchain"],
        "domain": ["ESG Analysis", "UN SDG", "E-Commerce Analysis"],
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