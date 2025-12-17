# CERNIS design guide

This document captures the visual design system for the CERNIS website.

## Colour palette

| Role | Hex | Usage |
|------|-----|-------|
| Primary navy | `#0B1F3B` | Headers, buttons, primary actions |
| Navy hover | `#07162A` | Button hover states, dark accents |
| Accent teal | `#14B8A6` | CTAs, links, highlights |
| Accent teal dark | `#0F766E` | Hover states for teal elements |
| Text primary | `#0F172A` | Body text, headings |
| Text muted | `#475569` | Secondary text, captions |
| Background | `#FFFFFF` | Main background |
| Background subtle | `#F8FAFC` | Alternating sections, cards |
| Borders | `#E2E8F0` | Dividers, card borders |

## Typography

### Font stack

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

System fonts are used for optimal performance and consistent rendering across platforms.

### Scale

| Element | Size | Weight | Line height |
|---------|------|--------|-------------|
| H1 | 2.5rem (40px) | 700 | 1.2 |
| H2 | 2rem (32px) | 700 | 1.25 |
| H3 | 1.5rem (24px) | 600 | 1.3 |
| H4 | 1.25rem (20px) | 600 | 1.4 |
| Body | 1rem (16px) | 400 | 1.6 |
| Small | 0.875rem (14px) | 400 | 1.5 |

## Spacing

Use a consistent spacing scale based on 0.5rem (8px) increments:

- `0.5rem` (8px) - Tight spacing
- `1rem` (16px) - Default spacing
- `1.5rem` (24px) - Section padding
- `2rem` (32px) - Component gaps
- `3rem` (48px) - Section margins
- `4rem` (64px) - Large section breaks

## Components

### Buttons

**Primary button**
- Background: `#0B1F3B`
- Text: `#FFFFFF`
- Hover: `#07162A`
- Padding: `0.75rem 1.5rem`
- Border radius: `0.375rem`

**Secondary button**
- Background: transparent
- Border: `2px solid #0B1F3B`
- Text: `#0B1F3B`
- Hover: Background `#0B1F3B`, text `#FFFFFF`

**Accent button (CTA)**
- Background: `#14B8A6`
- Text: `#FFFFFF`
- Hover: `#0F766E`

### Cards

- Background: `#FFFFFF`
- Border: `1px solid #E2E8F0`
- Border radius: `0.5rem`
- Padding: `1.5rem`
- Shadow: `0 1px 3px rgba(0, 0, 0, 0.1)`

### Links

- Default: `#14B8A6`
- Hover: `#0F766E`
- Underline on hover

## Layout

### Container

- Max width: `1200px`
- Padding: `1rem` (mobile), `2rem` (desktop)
- Centred with `margin: 0 auto`

### Grid

- 12-column grid for complex layouts
- Flexbox for simpler component arrangements
- Gap: `2rem` between columns

### Breakpoints

| Name | Width | Usage |
|------|-------|-------|
| Mobile | < 640px | Single column, stacked layout |
| Tablet | 640px - 1024px | Two columns where appropriate |
| Desktop | > 1024px | Full multi-column layouts |

## Accessibility

### Contrast requirements

All text meets WCAG 2.1 AA requirements:
- Primary text (#0F172A) on white: 16.1:1
- Muted text (#475569) on white: 7.0:1
- White text on navy (#0B1F3B): 13.5:1
- White text on teal (#14B8A6): 3.0:1 (use for large text/icons only)

### Focus states

All interactive elements must have visible focus indicators:
- Outline: `2px solid #14B8A6`
- Outline offset: `2px`

### Motion

Respect `prefers-reduced-motion`:
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
}
```
