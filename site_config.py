"""
CERNIS Static Website Configuration
====================================
Single source of truth for all site content, metadata, and navigation.
Edit this file to update website content, then run `python build.py`.
"""

# Site metadata
SITE = {
    "name": "CERNIS",
    "tagline": "Technology solutions that reduce costs and drive effectiveness",
    "description": "CERNIS helps organisations reduce technology costs and operate more effectively through integrated cloud, data and software solutions.",
    "url": "https://www.cernis.co.uk",  # Update with actual domain
    "locale": "en_GB",
    "twitter": "@cernis",  # Placeholder - update or remove
}

# Contact details (placeholders - update with real information)
CONTACT = {
    "email": "hello@cernis.co.uk",
    "phone": "+44 (0) 20 XXXX XXXX",
    "address": {
        "line1": "123 Business Street",
        "line2": "London",
        "postcode": "EC1A 1AA",
        "country": "United Kingdom",
    },
}

# Navigation (main menu)
NAV_ITEMS = [
    {"label": "Home", "url": "index.html", "id": "home"},
    {"label": "Our services", "url": "services.html", "id": "services"},
    {"label": "About us", "url": "about.html", "id": "about"},
    {"label": "How we work", "url": "how-we-work.html", "id": "how-we-work"},
    {"label": "Case studies", "url": "case-studies.html", "id": "case-studies"},
    {"label": "Insights", "url": "insights.html", "id": "insights"},
    {"label": "Contact", "url": "contact.html", "id": "contact"},
]

# Footer links
FOOTER_LINKS = {
    "company": [
        {"label": "About us", "url": "about.html"},
        {"label": "How we work", "url": "how-we-work.html"},
        {"label": "Case studies", "url": "case-studies.html"},
        {"label": "Insights", "url": "insights.html"},
        {"label": "Contact", "url": "contact.html"},
    ],
    "services": [
        {"label": "Cloud infrastructure", "url": "services.html#cloud"},
        {"label": "Data science", "url": "services.html#data"},
        {"label": "Custom development", "url": "services.html#development"},
    ],
    "legal": [
        {"label": "Privacy notice", "url": "privacy.html"},
        {"label": "Terms of use", "url": "terms.html"},
    ],
}

# Service pillars
SERVICES = [
    {
        "id": "cloud",
        "title": "Cloud infrastructure and management",
        "icon": "static/service-cloud.svg",
        "summary": "Optimise your cloud spend and operations with expert Azure and AWS solutions.",
        "description": """
            We help organisations build, migrate, and manage cloud infrastructure that 
            delivers genuine cost savings while improving reliability and security.
        """,
        "features": [
            "Azure and Microsoft ecosystem: Azure, Microsoft 365, SharePoint, Copilot integration",
            "AWS solutions for scalable, compute-heavy workloads",
            "Security, compliance, and multi-cloud governance",
            "Cloud cost optimisation and FinOps",
            "Infrastructure as code and automation",
        ],
        "outcomes": [
            "Reduced cloud spend through right-sizing and optimisation",
            "Improved security posture and compliance",
            "Faster deployment and reduced operational overhead",
        ],
    },
    {
        "id": "data",
        "title": "Data science and engineering",
        "icon": "static/service-data.svg",
        "summary": "Transform raw data into actionable insights that drive better decisions.",
        "description": """
            From data pipelines to predictive models, we help you unlock the value 
            in your data while maintaining governance and quality.
        """,
        "features": [
            "Data pipelines and engineering",
            "Analytics dashboards and reporting",
            "Machine learning and predictive modelling",
            "Data governance and quality frameworks",
            "Business intelligence strategy",
        ],
        "outcomes": [
            "Faster, data-driven decision making",
            "Automated reporting and reduced manual effort",
            "Predictive insights for proactive operations",
        ],
    },
    {
        "id": "development",
        "title": "Custom full-stack development",
        "icon": "static/service-dev.svg",
        "summary": "Purpose-built applications that integrate seamlessly with your technology stack.",
        "description": """
            We design and build web and mobile applications that solve specific 
            business problems, integrating with your existing cloud and data platforms.
        """,
        "features": [
            "Web and mobile application development",
            "System integration across cloud and data platforms",
            "API design and implementation",
            "Legacy system modernisation",
            "User experience design",
        ],
        "outcomes": [
            "Streamlined processes and reduced manual work",
            "Improved user satisfaction and adoption",
            "Seamless data flow across systems",
        ],
    },
]

# How we work - process steps
PROCESS_STEPS = [
    {
        "number": "01",
        "title": "Understand",
        "description": "We start by listening. Understanding your challenges, goals, and constraints ensures we focus on what matters most to your organisation.",
    },
    {
        "number": "02",
        "title": "Design",
        "description": "We design solutions that balance technical excellence with practical constraints. Every recommendation is grounded in real-world feasibility.",
    },
    {
        "number": "03",
        "title": "Deliver",
        "description": "We implement incrementally, delivering value early and often. You see progress continuously, not just at the end.",
    },
    {
        "number": "04",
        "title": "Support",
        "description": "We stay engaged after go-live. Whether you need ongoing support or knowledge transfer, we ensure lasting success.",
    },
]

# Key outcomes (used on home and throughout)
KEY_OUTCOMES = [
    {
        "title": "Reduce costs",
        "description": "Optimise cloud spend, automate manual processes, and eliminate waste through smart technology choices.",
    },
    {
        "title": "Improve effectiveness",
        "description": "Enable faster decisions, streamline operations, and build reliability into your technology foundation.",
    },
    {
        "title": "Accelerate delivery",
        "description": "Ship faster with modern development practices, proven architectures, and experienced delivery teams.",
    },
]

# Case studies (placeholders)
CASE_STUDIES = [
    {
        "id": "case-study-1",
        "title": "Cloud cost reduction for financial services firm",
        "client": "Confidential",
        "industry": "Financial services",
        "summary": "Reduced annual cloud spend by 40% while improving performance and reliability.",
        "challenge": "A growing financial services firm faced escalating cloud costs with limited visibility into resource utilisation.",
        "solution": "We implemented comprehensive cloud cost management, right-sizing resources and optimising reserved capacity.",
        "results": [
            "40% reduction in annual cloud spend",
            "Improved performance through architecture optimisation",
            "Automated cost monitoring and alerting",
        ],
        "image": "static/hero-placeholder.svg",
    },
    {
        "id": "case-study-2",
        "title": "Data platform modernisation for healthcare provider",
        "client": "Confidential",
        "industry": "Healthcare",
        "summary": "Unified disparate data sources into a modern analytics platform, enabling real-time insights.",
        "challenge": "Legacy systems and siloed data prevented meaningful analysis and slowed decision-making.",
        "solution": "We designed and built a cloud-native data platform with automated pipelines and self-service analytics.",
        "results": [
            "Real-time visibility across operations",
            "90% reduction in report generation time",
            "Foundation for predictive analytics",
        ],
        "image": "static/hero-placeholder.svg",
    },
    {
        "id": "case-study-3",
        "title": "Custom application for logistics company",
        "client": "Confidential",
        "industry": "Logistics",
        "summary": "Built a purpose-designed operations platform that replaced multiple legacy systems.",
        "challenge": "Manual processes and disconnected systems created inefficiency and errors.",
        "solution": "We developed an integrated web application connecting warehouse, transport, and customer systems.",
        "results": [
            "50% reduction in order processing time",
            "Eliminated manual data entry errors",
            "Improved customer satisfaction scores",
        ],
        "image": "static/hero-placeholder.svg",
    },
]

# Page-specific metadata
PAGES = {
    "home": {
        "title": "CERNIS | Technology solutions for cost reduction and operational effectiveness",
        "meta_description": "CERNIS helps organisations reduce technology costs and operate more effectively through integrated cloud, data and software solutions.",
        "og_title": "CERNIS - Technology consultancy",
        "og_description": "Reduce costs and improve effectiveness with expert cloud, data and software solutions.",
        "hero_headline": "Technology that delivers results",
        "hero_subheadline": "We help organisations reduce costs and operate more effectively through integrated cloud, data and software solutions.",
        "hero_cta": "Start a conversation",
        "hero_cta_url": "contact.html",
    },
    "services": {
        "title": "Our services | CERNIS",
        "meta_description": "Expert cloud infrastructure, data science, and custom development services focused on cost reduction and operational effectiveness.",
        "og_title": "Our services | CERNIS",
        "og_description": "Cloud, data and software solutions that reduce costs and improve effectiveness.",
        "headline": "Our services",
        "intro": "We deliver integrated solutions across cloud infrastructure, data science, and custom development—always focused on reducing costs and improving how you operate.",
    },
    "about": {
        "title": "About us | CERNIS",
        "meta_description": "Learn about CERNIS, a technology consultancy helping organisations reduce costs and improve effectiveness through cloud, data and software solutions.",
        "og_title": "About us | CERNIS",
        "og_description": "A technology consultancy focused on practical outcomes.",
        "headline": "About us",
        "intro": "Cernis is a technology consultancy founded on a simple belief: technology should deliver measurable business value.",
        "story": """
            We work with organisations that want practical outcomes, not theoretical frameworks. 
            Our team brings deep expertise in cloud platforms, data engineering, and software development—
            combined with the pragmatism that comes from years of hands-on delivery.
            
            Whether you need to reduce cloud costs, unlock insights from your data, or build 
            applications that genuinely improve how you work, we focus on what matters: 
            results you can measure and sustain.
        """,
        "company_values": [
            {
                "title": "Outcomes over outputs",
                "description": "We measure success by the value delivered to your organisation, not by hours worked or documents produced.",
            },
            {
                "title": "Pragmatism over perfection",
                "description": "We choose solutions that work in the real world, balancing technical excellence with practical constraints.",
            },
            {
                "title": "Transparency always",
                "description": "We communicate openly about progress, challenges, and trade-offs. No surprises, no jargon.",
            },
        ],
    },
    "how_we_work": {
        "title": "How we work | CERNIS",
        "meta_description": "Our approach to technology consulting: understand, design, deliver, and support. Practical solutions focused on your outcomes.",
        "og_title": "How we work | CERNIS",
        "og_description": "A practical approach to technology consulting.",
        "headline": "How we work",
        "intro": "Our approach is straightforward: understand your challenges deeply, design practical solutions, deliver incrementally, and stay engaged until you succeed.",
    },
    "case_studies": {
        "title": "Case studies | CERNIS",
        "meta_description": "Examples of how we have helped organisations reduce technology costs and improve operational effectiveness.",
        "og_title": "Case studies | CERNIS",
        "og_description": "Real results from real projects.",
        "headline": "Case studies",
        "intro": "See how we have helped organisations achieve measurable outcomes through cloud, data and software solutions.",
    },
    "insights": {
        "title": "Insights | CERNIS",
        "meta_description": "Thoughts on cloud, data, software development, and technology strategy from the CERNIS team.",
        "og_title": "Insights | CERNIS",
        "og_description": "Practical perspectives on technology.",
        "headline": "Insights",
        "intro": "Practical perspectives on cloud, data, and software development from our team.",
        "coming_soon": "We are preparing our first articles. Check back soon for insights on cloud optimisation, data strategy, and modern software development.",
    },
    "contact": {
        "title": "Contact | CERNIS",
        "meta_description": "Get in touch with CERNIS to discuss how we can help reduce your technology costs and improve operational effectiveness.",
        "og_title": "Contact | CERNIS",
        "og_description": "Start a conversation about your technology challenges.",
        "headline": "Contact",
        "intro": "Ready to discuss your technology challenges? We would love to hear from you.",
        "form_note": "Send us a message and we will respond within one working day.",
    },
    "privacy": {
        "title": "Privacy notice | CERNIS",
        "meta_description": "How CERNIS collects, uses, and protects your personal information.",
        "og_title": "Privacy notice | CERNIS",
        "og_description": "Our commitment to protecting your privacy.",
        "headline": "Privacy notice",
        "last_updated": "December 2025",
        "content": """
            <h2>Introduction</h2>
            <p>Cernis is committed to protecting your privacy. This notice explains how we collect, use, and safeguard your personal information when you interact with our website and services.</p>
            
            <h2>Information we collect</h2>
            <p>We may collect the following information:</p>
            <ul>
                <li>Contact information you provide (name, email, phone number)</li>
                <li>Information about your organisation and requirements</li>
                <li>Technical data (IP address, browser type, pages visited)</li>
            </ul>
            
            <h2>How we use your information</h2>
            <p>We use your information to:</p>
            <ul>
                <li>Respond to your enquiries</li>
                <li>Provide our services</li>
                <li>Improve our website and communications</li>
                <li>Comply with legal obligations</li>
            </ul>
            
            <h2>Data protection</h2>
            <p>We implement appropriate technical and organisational measures to protect your personal information against unauthorised access, alteration, or destruction.</p>
            
            <h2>Your rights</h2>
            <p>You have the right to access, correct, or delete your personal information. Contact us at the details below to exercise these rights.</p>
            
            <h2>Contact</h2>
            <p>For privacy-related enquiries, please contact us at the email address provided on our contact page.</p>
        """,
    },
    "terms": {
        "title": "Terms of use | CERNIS",
        "meta_description": "Terms and conditions for using the CERNIS website.",
        "og_title": "Terms of use | CERNIS",
        "og_description": "Website terms and conditions.",
        "headline": "Terms of use",
        "last_updated": "December 2025",
        "content": """
            <h2>Acceptance of terms</h2>
            <p>By accessing and using this website, you accept and agree to be bound by these terms of use.</p>
            
            <h2>Use of website</h2>
            <p>This website is provided for informational purposes about Cernis and our services. You may not use this website for any unlawful purpose or in any way that could damage or impair the website.</p>
            
            <h2>Intellectual property</h2>
            <p>All content on this website, including text, graphics, logos, and images, is the property of Cernis or our licensors and is protected by intellectual property laws.</p>
            
            <h2>Disclaimer</h2>
            <p>While we strive to keep the information on this website accurate and up to date, we make no warranties about the completeness, reliability, or suitability of the information provided.</p>
            
            <h2>Limitation of liability</h2>
            <p>Cernis shall not be liable for any direct, indirect, incidental, or consequential damages arising from your use of this website.</p>
            
            <h2>Governing law</h2>
            <p>These terms are governed by the laws of England and Wales. Any disputes shall be subject to the exclusive jurisdiction of the courts of England and Wales.</p>
            
            <h2>Changes to terms</h2>
            <p>We may update these terms from time to time. Continued use of the website after changes constitutes acceptance of the updated terms.</p>
        """,
    },
    "404": {
        "title": "Page not found | CERNIS",
        "meta_description": "The page you are looking for could not be found.",
        "headline": "Page not found",
        "message": "Sorry, we could not find the page you were looking for. It may have been moved or no longer exists.",
        "cta": "Return to home",
        "cta_url": "index.html",
    },
}

# CTA section (reused across pages)
CTA_SECTION = {
    "headline": "Start a conversation",
    "text": "Ready to reduce costs and improve how your technology works? Let us discuss your challenges.",
    "button_text": "Get in touch",
    "button_url": "contact.html",
}
