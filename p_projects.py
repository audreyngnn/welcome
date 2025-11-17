"""
Projects Page
Featured portfolio projects and case studies
"""

import streamlit as st
from data import PROJECTS
from tabs import render_project_card, render_footer

st.markdown('<p class="section-header">Featured Projects</p>', unsafe_allow_html=True)

# Filter by technology if filter is set
filters = st.session_state.get("filters", set())

# Filter projects
filtered_projects = []
for p in PROJECTS:
    if filters and not (filters & set(p.get("tech", []))):
        continue
    filtered_projects.append(p)

# Display in 2 columns
for i in range(0, len(filtered_projects), 2):
    cols = st.columns(2)
    for j, col in enumerate(cols):
        if i + j < len(filtered_projects):
            p = filtered_projects[i + j]
            with col:
                render_project_card(p)

# Footer
render_footer()