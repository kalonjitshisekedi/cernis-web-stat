# CERNIS Deployment Guide

This guide explains how to deploy the CERNIS static website to production.

## Prerequisites

- Python 3.8+ installed
- Jinja2 package (`pip install -r requirements.txt`)
- Built site in `output/` directory
- For AWS: AWS CLI installed and configured

## Building for Production

1. Review and update `site_config.py`:
   - Verify domain is set to `https://www.cernis.co.za`
   - Add Google Analytics ID if using tracking
   - Update contact details with real information

2. Build the site:
   ```bash
   python build.py
   ```

3. Verify the `output/` directory contains:
   - All HTML pages
   - `static/` folder with CSS, JS, images
   - `blog/` folder with blog post pages
   - `sitemap.xml`
   - `robots.txt`
   - `feed.xml` (RSS)

---

## Deployment Options

### Option 1: Replit Deployment

If hosting on Replit:

1. The site is already configured to serve from the `output/` directory
2. Click "Publish" in Replit to deploy
3. Configure your custom domain (cernis.co.za) in Replit settings

### Option 2: AWS S3 Static Hosting (Simple)

Best for: Testing, internal sites, or when HTTPS is managed separately.

#### Step 1: Create S3 bucket

```bash
aws s3 mb s3://cernis-website --region af-south-1
```

#### Step 2: Configure bucket for static hosting

```bash
aws s3 website s3://cernis-website --index-document index.html --error-document 404.html
```

#### Step 3: Set bucket policy for public access

Create a file `bucket-policy.json`:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::cernis-website/*"
        }
    ]
}
```

Apply the policy:

```bash
aws s3api put-bucket-policy --bucket cernis-website --policy file://bucket-policy.json
```

#### Step 4: Upload site

```bash
aws s3 sync output/ s3://cernis-website --delete
```

### Option 3: AWS S3 + CloudFront with HTTPS (Recommended for Production)

Best for: Production sites requiring HTTPS and global performance.

#### Step 1: Create S3 bucket

```bash
aws s3 mb s3://cernis-website --region af-south-1
```

#### Step 2: Upload site

```bash
aws s3 sync output/ s3://cernis-website --delete
```

#### Step 3: Request SSL certificate in ACM

**Important**: Certificate must be in `us-east-1` region for CloudFront.

1. Go to AWS Certificate Manager in the AWS Console
2. Select **us-east-1 (N. Virginia)** region
3. Click "Request a certificate"
4. Choose "Request a public certificate"
5. Enter domain names:
   - `cernis.co.za`
   - `www.cernis.co.za`
6. Choose DNS validation
7. Add the CNAME records to your DNS provider
8. Wait for validation (can take up to 30 minutes)

#### Step 4: Create CloudFront distribution

1. Go to CloudFront in AWS Console
2. Click "Create distribution"
3. Configure:
   - **Origin domain**: Select your S3 bucket
   - **Origin access**: Origin access control settings (recommended)
   - **Viewer protocol policy**: Redirect HTTP to HTTPS
   - **Alternate domain names (CNAMEs)**: `cernis.co.za`, `www.cernis.co.za`
   - **Custom SSL certificate**: Select your ACM certificate
   - **Default root object**: `index.html`
4. Create the distribution

#### Step 5: Configure custom error pages

In CloudFront distribution settings:
1. Go to "Error pages" tab
2. Create custom error response:
   - HTTP error code: 403
   - Customise error response: Yes
   - Response page path: `/404.html`
   - HTTP response code: 404

#### Step 6: Configure DNS

Point your domain to CloudFront:
1. Create an A record (or ALIAS) pointing to the CloudFront distribution domain
2. For www subdomain, create a CNAME pointing to the CloudFront domain

### Option 4: Netlify

1. Connect your Git repository to Netlify
2. Set build command: `python build.py`
3. Set publish directory: `output`
4. Configure custom domain in Netlify dashboard

### Option 5: Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Create `vercel.json`:
   ```json
   {
     "buildCommand": "python build.py",
     "outputDirectory": "output"
   }
   ```
3. Deploy: `vercel --prod`

---

## Updating the Site

After making changes:

1. Rebuild the site:
   ```bash
   python build.py
   ```

2. Sync to S3:
   ```bash
   aws s3 sync output/ s3://cernis-website --delete
   ```

3. If using CloudFront, invalidate cache:
   ```bash
   aws cloudfront create-invalidation --distribution-id YOUR_DIST_ID --paths "/*"
   ```

---

## Post-Deployment Checklist

### Verify Core Functionality
- [ ] Homepage loads correctly
- [ ] All navigation links work
- [ ] Mobile responsive layout works
- [ ] Blog posts accessible via /blog/[slug].html

### Verify SEO
- [ ] `sitemap.xml` accessible at /sitemap.xml
- [ ] `robots.txt` accessible at /robots.txt
- [ ] RSS feed at /feed.xml is valid
- [ ] Open Graph tags render correctly (use Facebook Debugger)
- [ ] Structured data validates (use Google Rich Results Test)

### Verify Analytics (if configured)
- [ ] Google Analytics tracking code present in page source
- [ ] Real-time visitors showing in GA dashboard
- [ ] Google Ads conversion tracking working

### Verify SSL/Security
- [ ] HTTPS working on all pages
- [ ] HTTP redirects to HTTPS
- [ ] No mixed content warnings

---

## Common Issues

### Files not updating after deployment

- CloudFront caches files. Create an invalidation or wait for cache to expire.
- Browser may cache files. Clear cache or use incognito mode.

### 403 Forbidden errors

- Check bucket policy allows public read access
- For CloudFront, ensure Origin Access Control is configured correctly

### Custom domain not working

- DNS propagation can take up to 48 hours
- Verify CNAME/ALIAS records are correct
- Check certificate is validated

### RSS feed not validating

- Check XML syntax
- Ensure all special characters are escaped
- Validate at https://validator.w3.org/feed/

---

## Monitoring Recommendations

1. **Uptime**: Use UptimeRobot or similar for availability monitoring
2. **Analytics**: Google Analytics for traffic and behaviour
3. **Search Console**: Google Search Console for SEO health
4. **Performance**: Lighthouse audits or WebPageTest
