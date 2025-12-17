# CERNIS Static Website

## Overview

A professional B2B static website for CERNIS technology consultancy, built with Python and Jinja2. The site is designed for deployment on AWS S3 with CloudFront CDN.

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
├── output/               # Generated static site
└── docs/                 # Documentation
```

## Key commands

- **Build site**: `python build.py`
- **Install dependencies**: `pip install -r requirements.txt`

## How to update content

1. Edit `site_config.py` to change text, navigation, or metadata
2. Run `python build.py` to regenerate the site
3. The workflow automatically serves the output directory

## Design system

### Colours
- Primary navy: #0B1F3B
- Accent teal: #14B8A6
- Text: #0F172A
- Background: #FFFFFF

### Typography
- System font stack
- Sentence case for all headings

### Language
- British English throughout
- Professional B2B tone
- Focus on cost reduction and operational effectiveness

## Recent changes

- December 2025: Initial project setup with all pages and templates

## User preferences

- British English spelling
- Sentence case headings
- No external CSS frameworks
- Minimal JavaScript
