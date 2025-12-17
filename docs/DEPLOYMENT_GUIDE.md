# CERNIS deployment guide

This guide explains how to deploy the CERNIS static website to AWS S3 with CloudFront CDN.

## Prerequisites

- AWS account with appropriate permissions
- AWS CLI installed and configured
- Domain name (already owned)
- Built site in `output/` directory

## Option A: Simple S3 static hosting (HTTP only)

Best for: Testing, internal sites, or when HTTPS is not required.

### Step 1: Create S3 bucket

```bash
aws s3 mb s3://your-domain.com --region eu-west-2
```

### Step 2: Configure bucket for static hosting

```bash
aws s3 website s3://your-domain.com --index-document index.html --error-document 404.html
```

### Step 3: Set bucket policy for public access

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
            "Resource": "arn:aws:s3:::your-domain.com/*"
        }
    ]
}
```

Apply the policy:

```bash
aws s3api put-bucket-policy --bucket your-domain.com --policy file://bucket-policy.json
```

### Step 4: Upload site

```bash
aws s3 sync output/ s3://your-domain.com --delete
```

### Step 5: Configure DNS

Point your domain to the S3 website endpoint:
- **Endpoint format**: `your-domain.com.s3-website.eu-west-2.amazonaws.com`
- Create a CNAME record (for www) or use Route 53 alias (for apex domain)

---

## Option B: S3 + CloudFront with HTTPS (recommended)

Best for: Production sites requiring HTTPS and global performance.

### Step 1: Create S3 bucket

```bash
aws s3 mb s3://your-domain.com --region eu-west-2
```

Note: For CloudFront origin, you don't need to enable S3 static website hosting.

### Step 2: Upload site

```bash
aws s3 sync output/ s3://your-domain.com --delete
```

### Step 3: Request SSL certificate in ACM

**Important**: Certificate must be in `us-east-1` region for CloudFront.

1. Go to AWS Certificate Manager in the AWS Console
2. Select **us-east-1 (N. Virginia)** region
3. Click "Request a certificate"
4. Choose "Request a public certificate"
5. Enter domain names:
   - `your-domain.com`
   - `www.your-domain.com`
6. Choose DNS validation
7. Add the CNAME records to your DNS provider
8. Wait for validation (can take up to 30 minutes)

### Step 4: Create CloudFront distribution

1. Go to CloudFront in AWS Console
2. Click "Create distribution"
3. Configure:
   - **Origin domain**: Select your S3 bucket
   - **Origin access**: Origin access control settings (recommended)
   - **Viewer protocol policy**: Redirect HTTP to HTTPS
   - **Alternate domain names (CNAMEs)**: `your-domain.com`, `www.your-domain.com`
   - **Custom SSL certificate**: Select your ACM certificate
   - **Default root object**: `index.html`
4. Create the distribution

### Step 5: Update S3 bucket policy

CloudFront will provide a bucket policy to allow access. Apply it via:

```bash
aws s3api put-bucket-policy --bucket your-domain.com --policy file://cloudfront-policy.json
```

### Step 6: Configure custom error pages

In CloudFront distribution settings:
1. Go to "Error pages" tab
2. Create custom error response:
   - HTTP error code: 403
   - Customise error response: Yes
   - Response page path: `/404.html`
   - HTTP response code: 404

### Step 7: Configure DNS

Point your domain to CloudFront:
1. Create an A record (or ALIAS) pointing to the CloudFront distribution domain
2. For www subdomain, create a CNAME pointing to the CloudFront domain

---

## Updating the site

After making changes:

1. Rebuild the site:
   ```bash
   python build.py
   ```

2. Sync to S3:
   ```bash
   aws s3 sync output/ s3://your-domain.com --delete
   ```

3. If using CloudFront, invalidate cache:
   ```bash
   aws cloudfront create-invalidation --distribution-id YOUR_DIST_ID --paths "/*"
   ```

---

## Common issues

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

### MIME type issues

S3 usually handles MIME types correctly. If not, set content types during upload:

```bash
aws s3 sync output/ s3://your-domain.com --delete \
  --content-type "text/html" \
  --exclude "*" --include "*.html"
```

---

## Post-deployment checklist

- [ ] Site loads over HTTPS
- [ ] www and non-www both work
- [ ] All pages accessible
- [ ] Images and assets load
- [ ] 404 page displays for invalid URLs
- [ ] Contact details are correct
- [ ] Analytics configured (if applicable)
