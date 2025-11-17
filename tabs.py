"""
TABS
Reusable UI components for the portfolio
"""

import streamlit as st
from datetime import datetime

def skill_chips(items):
    """Create tech stack chips/badges"""
    return "".join(f'<span class="skill-badge">{i}</span>' for i in items)

def profile_header(profile):
    """Render the profile header section - responsive for mobile"""
    st.markdown(f"""
        <div class="profile-header-container">
            <h1>{profile['name']} 🌿 </h1>
            <p class="profile-subtitle">
                <span class="profile-role">{profile['role']}</span>
                <span class="profile-location"> • {profile['location']}</span>
            </p>
            <p class="profile-tagline">{profile['tagline']}</p>
        </div>
    """, unsafe_allow_html=True)

def quick_stats(projects, education, awards, start_year=2023):
    """Render quick stats metrics - responsive layout"""
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        years_exp = datetime.now().year - start_year
        st.metric("**Years Experience**", value=f"{years_exp}+")
    with col2:
        st.metric("**Projects**", value=str(len(projects)))
    with col3:
        st.metric("**Degrees**", value=2)
    with col4:
        st.metric("**Awards**", value=str(len(awards)))

def sidebar_profile(profile):
    """Render sidebar profile section"""
    # Profile photo
    try:
        st.markdown('<div class="profile-container">', unsafe_allow_html=True)
        st.image("profile_photo.jpg", width=222)
        st.markdown('</div>', unsafe_allow_html=True)
    except:
        st.markdown(f"""
            <div class="profile-container">
                <div class="profile-placeholder">
                    {profile['name'][:2]}
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"<h2 class='sidebar-name'>{profile['name']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='sidebar-role'>{profile['role']}</p>", unsafe_allow_html=True)

def sidebar_contact(profile):
    """Render sidebar contact information - mobile optimized"""
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Contact")
    
    if profile.get('location'):
        col1, col2 = st.columns([1, 9])
        with col1:
            try:
                st.image("icons/location.png", width=20)
            except:
                st.markdown("📍")
        with col2:
            st.markdown(profile['location'])
    
    if profile.get('email'):
        col1, col2 = st.columns([1, 9])
        with col1:
            try:
                st.image("icons/email.png", width=20)
            except:
                st.markdown("✉️")
        with col2:
            st.markdown(f"[{profile['email']}](mailto:{profile['email']})")
    
    if profile.get('phone'):
        col1, col2 = st.columns([1, 9])
        with col1:
            try:
                st.image("icons/phone.png", width=20)
            except:
                st.markdown("📱")
        with col2:
            st.markdown(profile['phone'])
    
    if profile.get('github'):
        col1, col2 = st.columns([1, 9])
        with col1:
            try:
                st.image("icons/github.png", width=20)
            except:
                st.markdown("💻")
        with col2:
            st.markdown(f"[GitHub]({profile['github']})")
    
    if profile.get('linkedin'):
        col1, col2 = st.columns([1, 9])
        with col1:
            try:
                st.image("icons/linkedin.png", width=20)
            except:
                st.markdown("💼")
        with col2:
            st.markdown(f"[LinkedIn]({profile['linkedin']})")

def sidebar_filter(skills, experience, projects):
    """Render sidebar technology filter - mobile optimized"""
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("Filter")
    
    # Collect all technologies
    tech = set()
    for e in experience:
        tech.update(e.get("tech", []))
    for p in projects:
        tech.update(p.get("tech", []))
    for s in skills:
        tech.add(s['name'])
        for k in s.get("keywords", []):
            tech.add(k)
    
    all_tech = sorted(tech)
    selected = st.selectbox(
        "Select technology",
        options=["All Technologies"] + all_tech,
        label_visibility="collapsed"
    )
    
    if selected != "All Technologies":
        st.session_state['filters'] = {selected}
    else:
        st.session_state['filters'] = set()

def sidebar_download_resume():
    """Render download resume button"""
    st.markdown("<hr>", unsafe_allow_html=True)
    
    try:
        with open("CV_AudreyNguyen.pdf", "rb") as pdf_file:
            st.download_button(
                label="📥 Download Resume",
                data=pdf_file,
                file_name="CV_AudreyNguyen.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        st.button("📥 Download Resume", disabled=True, use_container_width=True)
        st.caption("Add CV_AudreyNguyen.pdf to enable")

def render_experience_card(exp):
    """Render an experience card - mobile responsive"""
    st.markdown(f"""
    <div class="experience-card">
        <h3>{exp['role']}</h3>
        <p class="company">{exp['company']}</p>
        <p class="period">{exp['period']} • {exp.get('location', '')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    for highlight in exp['highlights']:
        st.markdown(f"• {highlight}")
    
    st.markdown("<div style='margin-top: 0.75rem;'>" + skill_chips(exp.get('tech', [])) + "</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

def render_project_card(project):
    """Render a project card - mobile responsive"""
    # Try to show image first
    if project.get('image'):
        try:
            st.image(project['image'], use_container_width=True)
        except:
            pass
    
    st.markdown(f"""
    <div class="project-card">
        <h3>{project['name']}</h3>
        <p>{project['description']}</p>
        <div style='margin: 1rem 0;'>{skill_chips(project.get('tech', []))}</div>
        {'<a class="simple-btn" href="' + project['link'] + '" target="_blank">View Project →</a>' if project.get('link') else ''}
    </div>
    """, unsafe_allow_html=True)

def render_education_item(edu):
    """Render an education item - mobile responsive"""
    st.markdown(f"""
    <div class="education-item">
        <h3>{edu['degree']}</h3>
        <p class="education-school">{edu['school']}</p>
        <p class="education-period">{edu['period']} • {edu['location']}</p>
        {f"<p class='education-details'>{edu['details']}</p>" if edu.get('details') else ""}
    </div>
    """, unsafe_allow_html=True)

def render_award_item(award):
    """Render an award item - mobile responsive"""
    st.markdown(f"""
    <div class="award-item">
        <h3>🏆 {award['name']}</h3>
        <p class="award-organization">{award['organization']}</p>
        {f"<p class='award-details'>{award['details']}</p>" if award.get('details') else ""}
    </div>
    """, unsafe_allow_html=True)

def render_article_card(article):
    """Render an article card - mobile responsive"""
    st.markdown(f"""
    <div class="article-card">
        <h3>{article['title']}</h3>
        <p class="article-date">📅 {article['date']}</p>
        <p class="article-description">{article['description']}</p>
        {'<a class="simple-btn" href="' + article['link'] + '" target="_blank">Read Article →</a>' if article.get('link') else ''}
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Render footer section - mobile responsive"""
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="footer">
        <h3>Let's Connect</h3>
        <p class="footer-emoji">𓆝 𓆟 𓆞 𓆝 𓆟</p>
        <p class="footer-text">
            Interested in working together? Feel free to reach out.
        </p>
        <p class="footer-copyright">
            © 2025 Audrey Nguyen • Built with passion ✦
        </p>
    </div>
    """, unsafe_allow_html=True)