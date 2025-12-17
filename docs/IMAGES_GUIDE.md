# CERNIS images guide

This document explains how to replace placeholder images with real assets.

## Current placeholders

| File | Size | Purpose | Where used |
|------|------|---------|------------|
| `static/logo-placeholder.svg` | 120x40 | Brand wordmark | Header, footer |
| `static/hero-placeholder.svg` | 500x400 | Hero section illustration | Home page |
| `static/service-cloud.svg` | 64x64 | Cloud services icon | Home, services pages |
| `static/service-data.svg` | 64x64 | Data services icon | Home, services pages |
| `static/service-dev.svg` | 64x64 | Development icon | Home, services pages |
| `static/favicon.svg` | 32x32 | Browser favicon | All pages |

## Recommended image specifications

### Logo

- **Format**: SVG preferred for crisp scaling, or PNG with 2x resolution
- **Dimensions**: 120px wide, 40px tall (or proportional)
- **Background**: Transparent
- **Variations**: Consider dark and light versions if needed

### Hero image

- **Format**: SVG for illustrations, or optimised WebP/PNG for photos
- **Dimensions**: Minimum 1000px wide for retina displays
- **Style**: Abstract, professional illustration or high-quality photography
- **Compression**: Aim for under 100KB

### Service icons

- **Format**: SVG strongly recommended
- **Dimensions**: 64x64 at 1x, provide 128x128 for retina
- **Style**: Consistent line weight and colour palette
- **Colours**: Use brand teal (#14B8A6) and navy (#0B1F3B)

### Favicon

- **Format**: SVG preferred for modern browsers
- **Fallback**: Also provide favicon.ico (32x32, 16x16)
- **Design**: Simple, recognisable at small sizes

## Adding real images

1. Place image files in `static/` directory
2. Update references in templates if filenames differ
3. Run `python build.py` to regenerate the site
4. Verify images appear correctly

## Image optimisation

Before adding images to the site:

1. **Compress**: Use tools like TinyPNG, Squoosh, or ImageOptim
2. **Resize**: Don't upload larger images than needed
3. **Format**: 
   - SVG for icons and illustrations
   - WebP for photographs (with PNG fallback)
   - PNG for images requiring transparency
4. **Alt text**: Ensure all images have descriptive alt attributes

## Case study images

For case study images, recommended specifications:

- **Dimensions**: 800x600 or similar 4:3 ratio
- **Format**: WebP or optimised JPEG
- **Content**: Project screenshots, diagrams, or relevant imagery
- **File size**: Under 200KB per image
