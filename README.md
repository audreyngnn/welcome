# Audrey Nguyen - Data Analytics Portfolio

A portfolio website built with Streamlit featuring an Anthropic-inspired light theme and multi-page navigation.

## 🎨 Design Features

- **Anthropic-inspired Light Theme**: Clean, professional design with subtle colors
- **Multi-page Navigation**: Separate pages for different content sections
- **Responsive Layout**: Adapts to different screen sizes
- **Interactive Filtering**: Filter projects and experience by technology
- **Modern Typography**: Inter font family for clean, readable text

## 📁 Project Structure

```
portfolio/
├── streamlit_app.py          # Main application with navigation
├── portfolio_data.py          # All portfolio data (profile, skills, experience, etc.)
├── portfolio_styles.py        # CSS styling with Anthropic-inspired theme
├── portfolio_components.py    # Reusable UI components
├── page_about.py             # About/Home page
├── page_experience.py        # Professional experience page
├── page_projects.py          # Featured projects page
├── page_skills.py            # Technical skills page
├── page_education.py         # Education and awards page
├── page_articles.py          # Articles and writing page
├── CV_AudreyNguyen.pdf       # Resume PDF (optional)
├── profile_photo.jpg         # Profile photo (optional)
└── images/                   # Project images folder
    ├── sdg7_cover.jpg
    ├── retention_cover.jpg
    ├── bike_sales_cover.jpg
    └── dragonwagon_cover.jpg
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install streamlit
```

### Running Locally

```bash
streamlit run streamlit_app.py
```

### Deployment to Streamlit Cloud

1. Push all files to GitHub repository
2. Connect to Streamlit Cloud
3. Deploy from your repository

## 🎨 Color Palette

The Anthropic-inspired light theme uses:

- **Primary Accent**: #CC785C (Warm terracotta)
- **Background**: #FFFFFF (Pure white)
- **Secondary Background**: #FAFAFA (Light gray)
- **Text Primary**: #1A1A1A (Almost black)
- **Text Secondary**: #666666 (Medium gray)
- **Borders**: #E5E5E5 (Light border)

## 📝 Customization Guide

### Update Your Information

Edit `portfolio_data.py`:

```python
PROFILE = {
    "name": "Your Name",
    "role": "Your Role",
    # ... update other fields
}
```

### Add New Projects

Add to `PROJECTS` list in `portfolio_data.py`:

```python
{
    "name": "Project Name",
    "description": "Project description",
    "tech": ["Tech1", "Tech2"],
    "link": "https://project-link.com",
    "image": "images/project.jpg",
    "year": "2025"
}
```

### Modify Colors

Edit `portfolio_styles.py` and update the color variables:

```css
/* Change primary accent color */
background-color: #CC785C; /* Replace with your color */
```

### Add New Pages

1. Create new page file: `page_newpage.py`
2. Add to navigation in `streamlit_app.py`:

```python
st.Page(
    "page_newpage.py",
    title="New Page",
    icon="🆕"
)
```

## 📦 Required Files

### Essential Files
- `streamlit_app.py` - Main application (required)
- `portfolio_data.py` - Your data (required)
- `portfolio_styles.py` - Styling (required)
- `portfolio_components.py` - UI components (required)
- All `page_*.py` files (required)

### Optional Files
- `CV_AudreyNguyen.pdf` - Resume download
- `profile_photo.jpg` - Profile picture
- `images/` folder - Project screenshots
- `icons/` folder - Custom contact icons

## 🔧 Features

### Technology Filtering
- Sidebar filter automatically collects all technologies
- Filter projects and experience by selected technology
- Real-time filtering without page reload

### Responsive Design
- Adapts to mobile, tablet, and desktop screens
- Clean card-based layout
- Optimized for readability

### Performance
- Modular code structure for easy maintenance
- Reusable components reduce code duplication
- Efficient state management

## 📸 Adding Images

Place images in appropriate folders:

```
images/
├── sdg7_cover.jpg
├── retention_cover.jpg
└── bike_sales_cover.jpg

icons/
├── email.png
├── location.png
├── github.png
└── linkedin.png
```

## 🎯 Key Improvements Over Previous Version

1. **Multi-page Navigation**: Cleaner organization vs. tabs
2. **Light Theme**: More professional, easier to read
3. **Modular Structure**: Better code organization
4. **Reusable Components**: Easier to maintain and update
5. **Better Performance**: Faster load times with separated pages
6. **Enhanced UX**: Cleaner navigation and filtering

## 💡 Tips

- Update `portfolio_data.py` regularly with new projects
- Keep images optimized (<500KB) for faster loading
- Use consistent naming for technology tags for better filtering
- Test on mobile devices before deployment
- Keep resume PDF up to date

## 🐛 Troubleshooting

**Images not showing?**
- Check file paths are correct
- Ensure images are in correct folders
- Use try/except blocks for optional images

**Filter not working?**
- Check technology names match exactly in SKILLS, EXPERIENCE, and PROJECTS
- Case-sensitive matching

**Styling issues?**
- Clear browser cache
- Check CSS syntax in `portfolio_styles.py`
- Verify class names match in HTML and CSS

## 📄 License

This portfolio template is free to use and modify for personal use.

## 👤 Contact

Audrey Nguyen
- Email: audrey.tranguyen@gmail.com
- LinkedIn: [linkedin.com/in/audrey-tra-nguyen](https://www.linkedin.com/in/audrey-tra-nguyen/)
- GitHub: [github.com/audreyngnn](https://github.com/audreyngnn)

---

Built with ❤️ using Streamlit