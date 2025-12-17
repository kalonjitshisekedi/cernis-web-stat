# Domain and email configuration notes

This document provides guidance on domain and email setup for the CERNIS website.

## Domain configuration

### DNS concepts

- **A record**: Points a domain to an IP address
- **AAAA record**: Points a domain to an IPv6 address
- **CNAME**: Points a domain to another domain (alias)
- **ALIAS/ANAME**: Like CNAME but works at the apex domain (Route 53 feature)

### Apex domain vs www

- **Apex domain**: `cernis.co.uk` (no subdomain)
- **www subdomain**: `www.cernis.co.uk`

For S3 static hosting with a custom domain:
- Apex domains require Route 53 ALIAS records or a DNS provider that supports ALIAS/ANAME
- www subdomain can use a standard CNAME record

### Recommended setup

1. **Primary domain**: `www.cernis.co.uk` (CloudFront distribution)
2. **Redirect**: `cernis.co.uk` → `www.cernis.co.uk`

Or:

1. **Primary domain**: `cernis.co.uk` (CloudFront distribution)
2. **Redirect**: `www.cernis.co.uk` → `cernis.co.uk`

### DNS records for CloudFront

```
Type    Name    Value
----    ----    -----
A       @       (ALIAS to CloudFront distribution)
CNAME   www     d1234567890.cloudfront.net
```

---

## Email configuration

**Important**: Email is separate from website hosting. The website uses S3/CloudFront, but email requires different DNS records and a mail provider.

### Choosing an email provider

Common options:
- **Microsoft 365**: Recommended for businesses using other Microsoft tools
- **Google Workspace**: Good alternative with strong spam filtering
- **Zoho Mail**: Cost-effective option for small teams
- **Proton Mail**: Privacy-focused option

### Required DNS records for email

Each provider will give you specific records, but typically:

1. **MX records**: Direct email to your provider's servers
2. **SPF record**: TXT record authorising servers to send email for your domain
3. **DKIM record**: TXT record for email authentication
4. **DMARC record**: TXT record specifying how to handle failed authentication

### Example records (Microsoft 365)

```
Type    Name        Value
----    ----        -----
MX      @           cernis-co-uk.mail.protection.outlook.com (Priority: 0)
TXT     @           v=spf1 include:spf.protection.outlook.com -all
CNAME   selector1._domainkey    selector1-cernis-co-uk._domainkey.cernis.onmicrosoft.com
CNAME   selector2._domainkey    selector2-cernis-co-uk._domainkey.cernis.onmicrosoft.com
TXT     _dmarc      v=DMARC1; p=quarantine; rua=mailto:dmarc@cernis.co.uk
```

### Example records (Google Workspace)

```
Type    Name        Value
----    ----        -----
MX      @           aspmx.l.google.com (Priority: 1)
MX      @           alt1.aspmx.l.google.com (Priority: 5)
MX      @           alt2.aspmx.l.google.com (Priority: 5)
TXT     @           v=spf1 include:_spf.google.com ~all
TXT     google._domainkey   (provided by Google)
TXT     _dmarc      v=DMARC1; p=quarantine; rua=mailto:dmarc@cernis.co.uk
```

---

## Setup order

1. **Purchase/configure domain** with your registrar
2. **Set up website hosting** (S3 + CloudFront)
3. **Configure website DNS** (A/ALIAS/CNAME for web)
4. **Set up email provider** (Microsoft 365/Google Workspace)
5. **Configure email DNS** (MX, SPF, DKIM, DMARC)
6. **Test email** delivery and authentication

---

## Verification tools

After configuration, verify your setup:

- **DNS propagation**: [dnschecker.org](https://dnschecker.org)
- **MX records**: [mxtoolbox.com](https://mxtoolbox.com)
- **SPF/DKIM/DMARC**: [mail-tester.com](https://mail-tester.com)
- **SSL certificate**: [ssllabs.com/ssltest](https://ssllabs.com/ssltest)

---

## Notes

- DNS changes can take up to 48 hours to propagate globally
- Always test email sending and receiving after setup
- Keep records of all DNS configurations for future reference
- Consider setting up monitoring for certificate expiry
