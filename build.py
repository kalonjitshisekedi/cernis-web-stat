#!/usr/bin/env python3
"""
CERNIS Static Site Generator
=============================
Renders Jinja2 templates to static HTML and copies assets to output directory.

Usage:
    python build.py

Output:
    - HTML files in output/
    - Static assets in output/static/
    - robots.txt and sitemap.xml in output/
"""

import os
import shutil
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, TemplateNotFound

# Import site configuration
import site_config

# Paths
BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / 'templates'
STATIC_DIR = BASE_DIR / 'static'
OUTPUT_DIR = BASE_DIR / 'output'

# Page definitions: template path -> output filename
PAGES = {
    'pages/home.html': 'index.html',
    'pages/services.html': 'services.html',
    'pages/about.html': 'about.html',
    'pages/how-we-work.html': 'how-we-work.html',
    'pages/case-studies.html': 'case-studies.html',
    'pages/insights.html': 'insights.html',
    'pages/contact.html': 'contact.html',
    'pages/privacy.html': 'privacy.html',
    'pages/terms.html': 'terms.html',
    'pages/404.html': '404.html',
}

# Page ID mapping for navigation highlighting
PAGE_IDS = {
    'index.html': 'home',
    'services.html': 'services',
    'about.html': 'about',
    'how-we-work.html': 'how-we-work',
    'case-studies.html': 'case-studies',
    'insights.html': 'insights',
    'contact.html': 'contact',
    'privacy.html': 'privacy',
    'terms.html': 'terms',
    '404.html': '404',
}


def clean_output():
    """Remove and recreate output directory."""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)
    print(f"  Cleaned {OUTPUT_DIR}")


def copy_static():
    """Copy static assets to output directory."""
    output_static = OUTPUT_DIR / 'static'
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, output_static)
        print(f"  Copied static assets to {output_static}")
    else:
        print(f"  Warning: Static directory not found at {STATIC_DIR}")


def get_page_config(page_id):
    """Get page-specific configuration from site_config."""
    page_map = {
        'home': 'home',
        'services': 'services',
        'about': 'about',
        'how-we-work': 'how_we_work',
        'case-studies': 'case_studies',
        'insights': 'insights',
        'contact': 'contact',
        'privacy': 'privacy',
        'terms': 'terms',
        '404': '404',
    }
    config_key = page_map.get(page_id, page_id)
    return site_config.PAGES.get(config_key, {})


def render_pages(env):
    """Render all page templates to HTML files."""
    for template_path, output_file in PAGES.items():
        try:
            template = env.get_template(template_path)
        except TemplateNotFound:
            print(f"  Error: Template not found: {template_path}")
            continue

        page_id = PAGE_IDS.get(output_file, output_file.replace('.html', ''))
        page_config = get_page_config(page_id)

        # Build context
        context = {
            'site': site_config.SITE,
            'contact': site_config.CONTACT,
            'nav_items': site_config.NAV_ITEMS,
            'footer_links': site_config.FOOTER_LINKS,
            'services': site_config.SERVICES,
            'process_steps': site_config.PROCESS_STEPS,
            'key_outcomes': site_config.KEY_OUTCOMES,
            'case_studies': site_config.CASE_STUDIES,
            'cta_section': site_config.CTA_SECTION,
            'page': page_config,
            'current_page': page_id,
            'current_year': datetime.now().year,
        }

        # Render and write
        html = template.render(**context)
        output_path = OUTPUT_DIR / output_file
        output_path.write_text(html, encoding='utf-8')
        print(f"  Generated {output_file}")


def generate_robots_txt():
    """Generate robots.txt file."""
    content = f"""User-agent: *
Allow: /

Sitemap: {site_config.SITE['url']}/sitemap.xml
"""
    (OUTPUT_DIR / 'robots.txt').write_text(content, encoding='utf-8')
    print("  Generated robots.txt")


def generate_sitemap():
    """Generate sitemap.xml file."""
    base_url = site_config.SITE['url']
    today = datetime.now().strftime('%Y-%m-%d')

    urls = []
    for output_file in PAGES.values():
        if output_file == '404.html':
            continue
        priority = '1.0' if output_file == 'index.html' else '0.8'
        urls.append(f"""  <url>
    <loc>{base_url}/{output_file}</loc>
    <lastmod>{today}</lastmod>
    <priority>{priority}</priority>
  </url>""")

    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>
"""
    (OUTPUT_DIR / 'sitemap.xml').write_text(sitemap, encoding='utf-8')
    print("  Generated sitemap.xml")


def main():
    """Main build process."""
    print("\nCERNIS Static Site Generator")
    print("=" * 40)

    # Validate templates directory
    if not TEMPLATES_DIR.exists():
        print(f"Error: Templates directory not found at {TEMPLATES_DIR}")
        return 1

    # Set up Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=True,
    )

    print("\n1. Cleaning output directory...")
    clean_output()

    print("\n2. Copying static assets...")
    copy_static()

    print("\n3. Rendering pages...")
    render_pages(env)

    print("\n4. Generating SEO files...")
    generate_robots_txt()
    generate_sitemap()

    print("\n" + "=" * 40)
    print("Build complete!")
    print(f"Output directory: {OUTPUT_DIR}")
    print("\nTo preview locally:")
    print(f"  cd {OUTPUT_DIR} && python -m http.server 5000")
    print("")

    return 0


if __name__ == '__main__':
    exit(main())
