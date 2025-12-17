# CERNIS project handover checklist

Use this checklist when handing over the project or resuming work after a break.

## Files to download

Before switching Replit accounts or ending a session:

- [ ] Download full project as ZIP (all source files)
- [ ] Download `output/` directory separately (ready for deployment)
- [ ] Export any environment variables (if applicable)

## Information to record

Keep a record of:

### AWS resources (after deployment)
- [ ] S3 bucket name
- [ ] S3 bucket region
- [ ] CloudFront distribution ID
- [ ] CloudFront domain name
- [ ] ACM certificate ARN

### DNS configuration
- [ ] DNS provider name
- [ ] Current DNS records for website
- [ ] Current DNS records for email

### Access credentials
- [ ] AWS IAM user or role for deployment
- [ ] DNS provider login
- [ ] Email provider admin access

## Resuming work

When returning to the project:

1. **Restore files**:
   - Upload the project ZIP to new Replit instance
   - Or clone from Git repository (if set up)

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify build**:
   ```bash
   python build.py
   ```

4. **Test locally**:
   ```bash
   cd output && python -m http.server 5000
   ```

5. **Check STATE.md** for current project status

## Making updates

1. Edit content in `site_config.py`
2. Modify templates in `templates/` if layout changes needed
3. Update styles in `static/style.css`
4. Run `python build.py`
5. Test locally
6. Deploy to S3:
   ```bash
   aws s3 sync output/ s3://your-bucket-name --delete
   ```
7. Invalidate CloudFront cache (if applicable):
   ```bash
   aws cloudfront create-invalidation --distribution-id YOUR_ID --paths "/*"
   ```

## Contact information

Project maintained by: [Add contact details]

## Version history

| Date | Version | Changes |
|------|---------|---------|
| December 2025 | 1.0.0 | Initial release |
