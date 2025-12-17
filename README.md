# CERNIS Static Website

A professional B2B static website for CERNIS technology consultancy, built with Python and Jinja2.

## Quick start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Build the site:
   ```bash
   python build.py
   ```

3. Preview locally:
   ```bash
   cd output && python -m http.server 5000
   ```

4. Open http://localhost:5000 in your browser.

## Project structure

```
├── build.py              # Static site generator script
├── site_config.py        # All site content and configuration
├── requirements.txt      # Python dependencies (Jinja2 only)
├── templates/            # Jinja2 templates
│   ├── base.html         # Base layout template
│   ├── partials/         # Reusable components (nav, footer)
│   └── pages/            # Individual page templates
├── static/               # CSS, JS, and images
│   ├── style.css         # Main stylesheet
│   ├── main.js           # Minimal JavaScript
│   └── *.svg             # Placeholder images
├── output/               # Generated static site (git-ignored)
└── docs/                 # Documentation
    ├── DESIGN_GUIDE.md
    ├── COPY_STYLE_GUIDE.md
    ├── IMAGES_GUIDE.md
    ├── TESTING_CHECKLIST.md
    ├── DEPLOYMENT_GUIDE.md
    ├── DOMAIN_AND_EMAIL_NOTES.md
    └── HANDOVER_CHECKLIST.md
```

## How to update content

1. Edit `site_config.py` to change text, navigation, or metadata
2. Run `python build.py` to regenerate the site
3. Upload the `output/` directory to your hosting provider

## Deployment

See `docs/DEPLOYMENT_GUIDE.md` for detailed AWS S3 + CloudFront deployment instructions.

## Technology

- **Templating**: Jinja2 (no Flask or other frameworks)
- **Styling**: Single CSS file with system fonts
- **JavaScript**: Minimal (mobile nav toggle only)
- **Hosting**: Designed for AWS S3 static website hosting with CloudFront CDN
