# CERNIS Static Website (South Africa)

## Overview

A professional B2B static website for CERNIS technology consultancy in South Africa. Built with Python and Jinja2, designed for static hosting.

## Project Structure

```
├── build.py              # Static site generator script
├── site_config.py        # All site content and configuration
├── requirements.txt      # Python dependencies (Jinja2 only)
├── templates/            # Jinja2 templates
│   ├── base.html         # Base layout with SEO, analytics, structured data
│   ├── partials/         # Reusable components (nav, footer)
│   └── pages/            # Individual page templates including blog-post.html
├── static/               # CSS, JS, and images
│   ├── style.css         # Main stylesheet (includes blog styles)
│   ├── main.js           # Minimal JavaScript
│   └── *.svg             # Placeholder images
├── output/               # Generated static site
│   ├── blog/             # Generated blog post pages
│   ├── feed.xml          # RSS feed
│   ├── sitemap.xml       # XML sitemap
│   └── robots.txt        # Robots directive
└── docs/                 # Documentation
```

## Key Commands

- **Build site**: `python build.py`
- **Install dependencies**: `pip install -r requirements.txt`
- **Preview locally**: `cd output && python -m http.server 5000`

## How to Update Content

1. Edit `site_config.py` to change text, navigation, or metadata
2. Run `python build.py` to regenerate the site
3. The workflow automatically serves the output directory

### Adding Blog Posts

Add entries to `BLOG_POSTS` list in `site_config.py`:
```python
{
    "id": "unique-id",
    "title": "Post Title",
    "slug": "url-slug",
    "author": "CERNIS Team",
    "date": "2025-12-15",  # YYYY-MM-DD
    "summary": "Brief description",
    "meta_description": "SEO description",
    "category": "Cloud",
    "read_time": "5 min read",
    "content": """<p>HTML content...</p>""",
}
```

## Design System

### Colours
- Primary navy: #0B1F3B
- Accent teal: #14B8A6
- Text: #0F172A
- Background: #FFFFFF

### Typography
- System font stack
- Sentence case for all headings

### Language
- British English throughout (South African context)
- Professional B2B tone
- Focus on cost reduction and operational effectiveness

## Localisation

The site is configured for South Africa:
- Domain: cernis.co.za
- Locale: en_ZA
- Phone: +27 format
- POPIA-compliant privacy notice
- South African legal jurisdiction
- Content addressing SA-specific challenges (load shedding, rand volatility)

## SEO Features

- XML sitemap generation
- RSS feed for blog posts
- JSON-LD structured data (Organization, BlogPosting)
- Open Graph and Twitter Card meta tags
- Canonical URLs
- Google Analytics/Ads integration (configure in site_config.py)

## Google Analytics Setup

Add your tracking IDs in `site_config.py`:
```python
SITE = {
    ...
    "google_analytics_id": "G-XXXXXXXXXX",
    "google_ads_id": "AW-XXXXXXXXX",
}
```

## Recent Changes

- December 2025: South African localisation (domain, phone, address, POPIA compliance)
- December 2025: Added blog infrastructure with 3 SA-focused articles
- December 2025: Added RSS feed generation
- December 2025: Enhanced SEO with structured data and meta tags
- December 2025: Added Google Analytics/Ads integration support
- December 2025: Initial project setup with all pages and templates

## User Preferences

- British English spelling (South African variant)
- Sentence case headings
- No external CSS frameworks
- Minimal JavaScript
- POPIA-compliant data handling
