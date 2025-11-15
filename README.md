# Audrey's Data Analytics Portfolio

### 1. **Dark Theme with "Chill Coding Vibe" Color Palette**
- Primary Blue: `#4c748c`
- Accent Teal: `#8ce4e4`
- Light Mint: `#cdefe3`
- Dark Background: `#1a1d29`
- Card Background: `#242735`

### 2. **Enhanced Navigation**
- Emoji icons for each page (👋 Welcome, 🎯 Problem Statement, 📊 Dashboard, ✨ Credits, 👩‍💻 About Me)
- Smooth hover effects with color transitions
- Active page highlighting with gradient background
- Sliding animation on hover

### 3. **UI Improvements**
- Gradient text effects for headers
- Glassmorphism-style cards with hover animations
- Enhanced dashboard containers with glow effects
- Better visual hierarchy with the Inter font family
- Improved link styling and button designs

## Setup Instructions

### Option 1: Local Setup

1. **Install Streamlit** (if you haven't already):
   ```bash
   pip install streamlit
   ```

2. **Create the `.streamlit` folder** in your project directory:
   ```bash
   mkdir .streamlit
   ```

3. **Add the config file**:
   - Copy `config.toml` to the `.streamlit` folder

4. **Run the app**:
   ```bash
   streamlit run portfolio_app.py
   ```

### Option 2: Streamlit Cloud Deployment

1. **Push to GitHub**:
   - Create a new repository
   - Add `portfolio_app.py` and create a `.streamlit/config.toml` file with the provided config

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Select `portfolio_app.py` as the main file
   - Deploy!

## File Structure

```
your-portfolio/
├── portfolio_app.py          # Main application file
├── requirements.txt          # Dependencies
├── profile_photo.jpg         # Your profile photo (400x400px)
├── images/                   # Project cover images folder
│   ├── sdg7_cover.jpg       # SDG 7 project cover (1200x600px)
│   ├── retention_cover.jpg  # Student Retention cover (1200x600px)
│   ├── bike_sales_cover.jpg # Bike Sales cover (1200x600px)
│   └── dragonwagon_cover.jpg # DragonWagon cover (1200x600px)
└── .streamlit/
    └── config.toml          # Theme configuration
```

**Note:** If you don't have images yet, the app will display beautiful gradient placeholders!

## Navigation Pages

The navigation now uses a cleaner icon-based system:

- **👋 Welcome** - Home page (same as before)
- **👩‍💻 About Me** - About page
- **🎯 Power BI Dashboards** - Power BI projects
- **📊 Tableau Dashboards** - Tableau projects
- **✨ Articles & Writing** - Articles and technical writing

## Customization Tips

### Change Colors
Edit the CSS variables in the `<style>` section:
```css
:root {
    --primary-blue: #4c748c;
    --accent-teal: #8ce4e4;
    --light-mint: #cdefe3;
    /* ... */
}
```

### Add More Navigation Items
Update the `nav_options` dictionary:
```python
nav_options = {
    "👋 Welcome": "Home",
    "👩‍💻 About Me": "About Me",
    "🎯 Power BI Dashboards": "Power BI Dashboards",
    # Add your new page here
}
```

### Modify Hover Effects
Look for `transition` and `:hover` CSS rules to adjust animation speeds and effects.

## Features

✨ **Dark Mode** - Easy on the eyes with a professional dark theme
🎨 **Color Palette** - Cohesive "chill coding vibe" color scheme
🎯 **Enhanced Navigation** - Icon-based navigation with smooth animations
📊 **Interactive Cards** - Hover effects and glassmorphism design
🔗 **Responsive Links** - Styled with theme colors and hover states
⚡ **Performance** - Optimized CSS and efficient rendering

## Troubleshooting

**Theme not applying?**
- Make sure `config.toml` is in the `.streamlit` folder
- Restart the Streamlit server
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)

**Colors look different?**
- Check if your browser has dark mode extensions that might interfere
- Try viewing in an incognito/private window

**Navigation not working?**
- Ensure all page names in `nav_options` match the `if page == "..."` conditions

---

Built with ❤️ using Streamlit and the "chill coding vibe" color palett