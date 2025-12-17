# CERNIS Static Website (South Africa)

A professional B2B static website for CERNIS technology consultancy in South Africa, built with Python and Jinja2.

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

## Setting SITE_URL

The site uses a `SITE_URL` environment variable for generating absolute URLs in:
- Canonical links
- OpenGraph meta tags
- RSS feed links
- Sitemap URLs

**Default**: `https://cernis.co.za` (production domain)

**For local development**:
```bash
export SITE_URL="http://localhost:5000"
python build.py
```

**For staging/preview**:
```bash
export SITE_URL="https://staging.cernis.co.za"
python build.py
```

The environment variable takes precedence; if not set, it falls back to the production domain.

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
│   ├── blog/             # Blog post pages
│   ├── feed.xml          # RSS feed
│   ├── sitemap.xml       # XML sitemap for SEO
│   └── robots.txt        # Robots directive
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

### Adding blog posts

Add new posts to the `BLOG_POSTS` list in `site_config.py`:

```python
{
    "id": "unique-post-id",
    "title": "Your Post Title",
    "slug": "url-friendly-slug",
    "author": "Author Name",
    "date": "2025-12-15",  # YYYY-MM-DD format
    "summary": "Brief description for listings",
    "meta_description": "SEO description",
    "category": "Cloud",  # or "Data", "Technology"
    "read_time": "5 min read",
    "content": """<p>Your HTML content here...</p>""",
}
```

Run `python build.py` after adding posts to regenerate the site and RSS feed.

## Google Analytics / Ads Setup

To enable Google Analytics and Google Ads tracking:

1. Open `site_config.py`
2. Add your measurement ID:
   ```python
   SITE = {
       ...
       "google_analytics_id": "G-XXXXXXXXXX",  # Your GA4 ID
       "google_ads_id": "AW-XXXXXXXXX",  # Your Ads conversion ID
   }
   ```
3. Rebuild the site

## SEO Features

- XML sitemap at `/sitemap.xml`
- RSS feed at `/feed.xml`
- Structured data (JSON-LD) for organization and blog posts
- Open Graph and Twitter Card meta tags
- Canonical URLs
- Robots directives

## South African Localisation

This site is configured for South Africa:
- Domain: cernis.co.za
- Locale: en_ZA
- POPIA-compliant privacy notice
- South African legal jurisdiction in terms
- +27 phone format
- ZAR-aware content (e.g., currency considerations in cloud cost articles)

## Deployment

See `docs/DEPLOYMENT_GUIDE.md` for detailed deployment instructions.

### Quick Deploy Options

**Replit (Development)**
- The site auto-deploys when you publish from Replit

**Static Hosting (Production)**
1. Run `python build.py`
2. Upload the `output/` folder to:
   - AWS S3 + CloudFront
   - Netlify
   - Vercel
   - Any static host

## Technology

- **Templating**: Jinja2 (no Flask or other frameworks)
- **Styling**: Single CSS file with system fonts
- **JavaScript**: Minimal (mobile nav toggle only)
- **Hosting**: Designed for static website hosting

## Maintenance

- **Content updates**: Edit `site_config.py` and rebuild
- **Style changes**: Edit `static/style.css`
- **Template changes**: Edit files in `templates/`
- **New pages**: Add to `PAGES` dict in `build.py` and create template
