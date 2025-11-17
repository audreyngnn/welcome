"""
Experience Page
Professional work history and achievements
"""

import streamlit as st
from data import EXPERIENCE
from tabs import render_experience_card, render_footer

st.markdown('<p class="section-header">Professional Experience</p>', unsafe_allow_html=True)

# Filter by technology if filter is set
filters = st.session_state.get("filters", set())

for exp in EXPERIENCE:
    # Filter check
    if filters and not (filters & set(exp.get("tech", []))):
        continue
    
    render_experience_card(exp)

# Footer
render_footer()