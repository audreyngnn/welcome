"""
Articles Page
Published articles and writing samples
"""

import streamlit as st
from data import ARTICLES
from tabs import render_article_card, render_footer

st.markdown('<p class="section-header">Articles & Writing</p>', unsafe_allow_html=True)

for article in ARTICLES:
    render_article_card(article)

# Footer
render_footer()