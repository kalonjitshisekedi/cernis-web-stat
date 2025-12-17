# CERNIS testing checklist

Use this checklist to validate the site before deployment.

## Build verification

- [ ] `python build.py` runs without errors
- [ ] All HTML files generated in `output/`
- [ ] Static assets copied to `output/static/`
- [ ] `robots.txt` generated
- [ ] `sitemap.xml` generated

## Pages

- [ ] Home page loads correctly
- [ ] Services page displays all three service pillars
- [ ] About page shows company values
- [ ] How we work page displays process steps
- [ ] Case studies page shows all case study cards
- [ ] Insights page shows coming soon message
- [ ] Contact page displays contact information
- [ ] Privacy notice page renders legal content
- [ ] Terms of use page renders legal content
- [ ] 404 page displays error message and link to home

## Navigation

- [ ] All navigation links work
- [ ] Current page is highlighted in navigation
- [ ] Mobile menu toggle works
- [ ] Skip to content link visible on keyboard focus
- [ ] Footer links work

## Responsive design

- [ ] Pages display correctly on mobile (320px)
- [ ] Pages display correctly on tablet (768px)
- [ ] Pages display correctly on desktop (1200px+)
- [ ] Navigation collapses on mobile
- [ ] Images scale appropriately
- [ ] Text remains readable at all sizes

## Accessibility

- [ ] All images have alt text
- [ ] Colour contrast meets WCAG 2.1 AA
- [ ] Focus states visible on interactive elements
- [ ] Keyboard navigation works throughout
- [ ] Skip link works correctly
- [ ] Headings follow logical hierarchy (h1 → h2 → h3)
- [ ] Forms have proper labels (when forms are added)

## Content

- [ ] All text is in British English
- [ ] All headings use sentence case
- [ ] No placeholder text visible (except intended placeholders)
- [ ] Contact details are accurate (or clearly marked as placeholders)
- [ ] Copyright year is current

## SEO

- [ ] Each page has unique title
- [ ] Each page has meta description
- [ ] Open Graph tags present
- [ ] Sitemap includes all public pages
- [ ] Sitemap excludes 404 page
- [ ] robots.txt allows crawling

## Performance

- [ ] CSS file loads
- [ ] JavaScript file loads
- [ ] Images load correctly
- [ ] Page load time acceptable (under 3 seconds on 3G)
- [ ] No console errors in browser

## Browser testing

Test in at least:

- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] iOS Safari
- [ ] Android Chrome

## Pre-deployment

- [ ] Update `site_config.SITE['url']` with actual domain
- [ ] Replace placeholder contact details
- [ ] Replace placeholder images with real assets
- [ ] Remove or update coming soon messages
- [ ] Final spell check
