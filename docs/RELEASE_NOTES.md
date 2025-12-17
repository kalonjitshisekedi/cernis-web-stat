# CERNIS website release notes

## Version 1.0.0 - December 2025

Initial release of the CERNIS static website.

### Features included

#### Pages
- Home page with hero section, outcomes, and services overview
- Our services page with detailed service descriptions
- About us page with company story and values
- How we work page with process steps
- Case studies page with placeholder case studies
- Insights page (coming soon placeholder)
- Contact page with contact information
- Privacy notice
- Terms of use
- Custom 404 error page

#### Design and accessibility
- Responsive design (mobile, tablet, desktop)
- WCAG 2.1 AA compliant colour contrast
- Keyboard navigation support
- Skip to content link
- Focus states on all interactive elements
- Reduced motion support

#### SEO
- Unique titles and meta descriptions per page
- Open Graph meta tags
- Generated sitemap.xml
- Generated robots.txt
- Semantic HTML structure

#### Technical
- Python + Jinja2 static site generator
- Single CSS file with CSS custom properties
- Minimal JavaScript (mobile nav only)
- SVG placeholder images
- No external dependencies at runtime

### Placeholders to replace

Before going live, update these items:

1. **Contact details** (`site_config.py`):
   - Email address
   - Phone number
   - Physical address

2. **Images** (`static/`):
   - Logo (logo-placeholder.svg)
   - Hero image (hero-placeholder.svg)
   - Service icons (if desired)
   - Favicon

3. **Site URL** (`site_config.py`):
   - Update `SITE['url']` with actual domain

4. **Case studies**:
   - Replace placeholder content with real case studies
   - Add actual client logos or project images

5. **Insights page**:
   - Add articles when ready
   - Remove coming soon message

### How to update content

1. Edit `site_config.py` to change text, navigation, or metadata
2. Run `python build.py` to regenerate the site
3. Upload the `output/` directory to your hosting provider

### Known limitations

- No contact form (email link provided instead)
- No blog/insights functionality (placeholder only)
- No analytics integration (add manually if needed)
- Static site only (no dynamic features)

### Future enhancements

Consider adding:
- Functional contact form (via AWS Lambda or third-party service)
- Blog/insights with markdown support
- Analytics tracking
- Cookie consent banner (if required)
- Newsletter signup
