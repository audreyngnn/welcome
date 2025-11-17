"""
Education Page
Academic background and awards
"""

import streamlit as st
from data import EDUCATION, AWARDS
from tabs import render_education_item, render_award_item, render_footer

st.markdown('<p class="section-header">Education</p>', unsafe_allow_html=True)

for edu in EDUCATION:
    render_education_item(edu)

if AWARDS:
    st.markdown('<p class="section-header" style="margin-top: 2rem;">Awards & Recognition</p>', unsafe_allow_html=True)
    for award in AWARDS:
        render_award_item(award)

# Footer
render_footer()