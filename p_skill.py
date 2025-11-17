"""
Skills Page
Technical skills and proficiency levels
"""

import streamlit as st
from data import SKILLS
from tabs import render_footer

st.markdown('<p class="section-header">Technical Skills</p>', unsafe_allow_html=True)

# Group skills by category
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

# Footer
render_footer()