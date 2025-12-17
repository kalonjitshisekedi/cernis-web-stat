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
    "description": "CERNIS helps South African organisations reduce technology costs and operate more effectively through integrated cloud, data and software solutions.",
    "url": "https://www.cernis.co.za",
    "locale": "en_ZA",
    "twitter": "@cernis_za",
    "google_analytics_id": "",  # Add your GA4 measurement ID (e.g., G-XXXXXXXXXX)
    "google_ads_id": "",  # Add your Google Ads conversion ID (e.g., AW-XXXXXXXXX)
}

# Contact details
CONTACT = {
    "email": "hello@cernis.co.za",
    "phone": "+27 (0) 11 XXX XXXX",
    "address": {
        "line1": "1 Sandton Drive",
        "line2": "Sandton",
        "city": "Johannesburg",
        "province": "Gauteng",
        "postcode": "2196",
        "country": "South Africa",
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
        "meta_description": "How CERNIS collects, uses, and protects your personal information in compliance with POPIA.",
        "og_title": "Privacy notice | CERNIS",
        "og_description": "Our commitment to protecting your privacy under South African law.",
        "headline": "Privacy notice",
        "last_updated": "December 2025",
        "content": """
            <h2>Introduction</h2>
            <p>Cernis is committed to protecting your privacy in accordance with the Protection of Personal Information Act (POPIA). This notice explains how we collect, use, and safeguard your personal information when you interact with our website and services.</p>
            
            <h2>Responsible party</h2>
            <p>Cernis is the responsible party for the processing of your personal information as defined in POPIA.</p>
            
            <h2>Information we collect</h2>
            <p>We may collect the following information:</p>
            <ul>
                <li>Contact information you provide (name, email, phone number)</li>
                <li>Information about your organisation and requirements</li>
                <li>Technical data (IP address, browser type, pages visited)</li>
            </ul>
            
            <h2>Purpose of processing</h2>
            <p>We process your information for the following purposes:</p>
            <ul>
                <li>Respond to your enquiries</li>
                <li>Provide our services</li>
                <li>Improve our website and communications</li>
                <li>Comply with legal obligations</li>
            </ul>
            
            <h2>Data protection</h2>
            <p>We implement appropriate technical and organisational measures to protect your personal information against unauthorised access, alteration, or destruction, as required by POPIA.</p>
            
            <h2>Your rights under POPIA</h2>
            <p>You have the right to:</p>
            <ul>
                <li>Request access to your personal information</li>
                <li>Request correction of inaccurate information</li>
                <li>Request deletion of your personal information</li>
                <li>Object to the processing of your personal information</li>
                <li>Lodge a complaint with the Information Regulator</li>
            </ul>
            
            <h2>Contact</h2>
            <p>For privacy-related enquiries or to exercise your rights, please contact us at the email address provided on our contact page.</p>
            
            <h2>Information Regulator</h2>
            <p>If you are unsatisfied with our response to any privacy concern, you may lodge a complaint with the Information Regulator of South Africa at <a href="https://www.justice.gov.za/inforeg/">www.justice.gov.za/inforeg/</a>.</p>
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
            <p>All content on this website, including text, graphics, logos, and images, is the property of Cernis or our licensors and is protected by intellectual property laws, including the South African Copyright Act.</p>
            
            <h2>Disclaimer</h2>
            <p>While we strive to keep the information on this website accurate and up to date, we make no warranties about the completeness, reliability, or suitability of the information provided.</p>
            
            <h2>Limitation of liability</h2>
            <p>Cernis shall not be liable for any direct, indirect, incidental, or consequential damages arising from your use of this website, to the extent permitted by South African law.</p>
            
            <h2>Governing law</h2>
            <p>These terms are governed by the laws of the Republic of South Africa. Any disputes shall be subject to the exclusive jurisdiction of the courts of South Africa.</p>
            
            <h2>POPIA compliance</h2>
            <p>We comply with the Protection of Personal Information Act (POPIA) in our handling of personal information. See our Privacy Notice for details.</p>
            
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

# Blog posts / Insights
BLOG_POSTS = [
    {
        "id": "cloud-cost-optimisation-south-africa",
        "title": "Cloud Cost Optimisation for South African Businesses: A Practical Guide",
        "slug": "cloud-cost-optimisation-south-africa",
        "author": "CERNIS Team",
        "date": "2025-12-15",
        "summary": "With the rand's volatility and dollar-denominated cloud pricing, South African businesses face unique challenges. Here's how to optimise your cloud spend effectively.",
        "meta_description": "Practical strategies for South African businesses to reduce cloud costs while dealing with currency volatility and dollar-denominated pricing.",
        "category": "Cloud",
        "read_time": "6 min read",
        "content": """
            <p class="lead">South African businesses face a unique challenge when it comes to cloud computing: most major providers price their services in US dollars, which means rand volatility directly impacts your operational costs. Here's a practical guide to managing and reducing your cloud spend.</p>
            
            <h2>Understanding the Currency Challenge</h2>
            <p>When the rand weakens against the dollar, your cloud bill increases—even if your usage stays the same. This unpredictability makes budgeting difficult and can catch finance teams off guard at month-end.</p>
            <p>The good news is that there are concrete steps you can take to reduce costs and build more predictability into your cloud spending.</p>
            
            <h2>1. Right-size Your Resources</h2>
            <p>One of the most common sources of cloud waste is over-provisioned resources. Many organisations deploy larger virtual machines than needed "just in case" and never revisit the decision.</p>
            <ul>
                <li>Review CPU and memory utilisation across your estate monthly</li>
                <li>Use cloud provider recommendations (Azure Advisor, AWS Cost Explorer)</li>
                <li>Consider reserved instances for predictable workloads—savings of 30-60% are typical</li>
            </ul>
            
            <h2>2. Leverage Local Data Centres</h2>
            <p>Both Azure and AWS now have data centre regions in South Africa. While not always the cheapest option, keeping data local can reduce egress costs and improve latency for your users.</p>
            <p>For compliance-sensitive workloads, local data residency may be a requirement under POPIA anyway.</p>
            
            <h2>3. Implement Tagging and Cost Allocation</h2>
            <p>You cannot optimise what you cannot measure. Implement a consistent tagging strategy across all cloud resources so you can attribute costs to specific projects, departments, or clients.</p>
            <p>This visibility is the foundation of any serious cost optimisation effort.</p>
            
            <h2>4. Automate Shutdown of Non-Production Resources</h2>
            <p>Development and test environments often run 24/7 when they're only needed during business hours. Automating shutdown schedules can reduce these costs by 60-70%.</p>
            
            <h2>Taking Action</h2>
            <p>Cloud cost optimisation is not a one-time project—it requires ongoing attention. Start with visibility, implement quick wins like right-sizing and auto-shutdown, then build towards more sophisticated FinOps practices.</p>
            <p>If you'd like help assessing your cloud spend and identifying savings opportunities, we'd be happy to discuss your situation.</p>
        """,
    },
    {
        "id": "data-driven-decision-making-smes",
        "title": "Data-Driven Decision Making for South African SMEs",
        "slug": "data-driven-decision-making-smes",
        "author": "CERNIS Team",
        "date": "2025-12-10",
        "summary": "You don't need a massive budget to become a data-driven organisation. Here's how South African SMEs can start using data effectively without breaking the bank.",
        "meta_description": "Practical guidance for South African small and medium businesses to implement data-driven decision making on a limited budget.",
        "category": "Data",
        "read_time": "5 min read",
        "content": """
            <p class="lead">There's a perception that data analytics is only for large enterprises with dedicated data science teams and big budgets. The reality is quite different—South African SMEs can start benefiting from data-driven insights with modest investment and the right approach.</p>
            
            <h2>Start With the Questions, Not the Tools</h2>
            <p>Before investing in any technology, identify the key business questions you need to answer. Common starting points include:</p>
            <ul>
                <li>Which customers are most profitable, and why?</li>
                <li>What's driving our operational costs?</li>
                <li>Where are we losing money without realising it?</li>
                <li>Which products or services should we focus on?</li>
            </ul>
            <p>Clear questions lead to focused data collection and faster time to value.</p>
            
            <h2>Leverage Tools You Already Have</h2>
            <p>Many SMEs already have powerful analytics capabilities they're not fully using:</p>
            <ul>
                <li><strong>Microsoft Excel / Google Sheets:</strong> Still remarkably capable for many analytical tasks</li>
                <li><strong>Accounting software reports:</strong> Sage, Xero, and QuickBooks all have built-in reporting</li>
                <li><strong>Google Analytics:</strong> Free and powerful for understanding website and customer behaviour</li>
                <li><strong>Power BI (free tier):</strong> Create professional dashboards without licence costs</li>
            </ul>
            
            <h2>Fix Your Data Quality First</h2>
            <p>The biggest obstacle to data-driven decisions isn't technology—it's data quality. Before building dashboards, invest time in:</p>
            <ul>
                <li>Standardising how data is captured and entered</li>
                <li>Cleaning up inconsistencies in customer and product records</li>
                <li>Establishing simple data governance processes</li>
            </ul>
            <p>Garbage in, garbage out applies everywhere.</p>
            
            <h2>Build Incrementally</h2>
            <p>Don't try to create a complete data platform from day one. Start with one well-defined use case, prove the value, then expand. This approach manages risk and builds organisational buy-in.</p>
            
            <h2>The South African Context</h2>
            <p>Operating in South Africa means dealing with load shedding, connectivity challenges, and a smaller pool of specialised talent. When designing your data approach:</p>
            <ul>
                <li>Consider cloud-based solutions that don't rely on local infrastructure</li>
                <li>Build in resilience for connectivity interruptions</li>
                <li>Look for partners who understand the local context</li>
            </ul>
            
            <h2>Getting Started</h2>
            <p>The best time to start using data better was years ago. The second best time is now. Pick one business question, gather the relevant data, and start learning from it.</p>
        """,
    },
    {
        "id": "digital-transformation-load-shedding",
        "title": "Building Resilient Systems: Digital Transformation in the Age of Load Shedding",
        "slug": "digital-transformation-load-shedding",
        "author": "CERNIS Team",
        "date": "2025-12-05",
        "summary": "Load shedding has become a fact of life for South African businesses. Here's how to design technology systems that keep working when the power doesn't.",
        "meta_description": "How South African businesses can build technology systems resilient to load shedding and power interruptions through cloud and modern architecture.",
        "category": "Technology",
        "read_time": "7 min read",
        "content": """
            <p class="lead">Load shedding isn't going away anytime soon. For South African businesses investing in technology, this reality must inform how systems are designed and deployed. The good news is that the same approaches that build load-shedding resilience often deliver other benefits too.</p>
            
            <h2>The Problem With On-Premises Systems</h2>
            <p>Traditional on-premises infrastructure—servers in your office or a local data centre—is directly exposed to power interruptions. While UPS systems and generators help, they add cost, require maintenance, and have limits.</p>
            <p>More fundamentally, if your staff can't get to the office during load shedding (dead traffic lights, no fuel at petrol stations), having servers running doesn't help much.</p>
            
            <h2>Cloud as a Resilience Strategy</h2>
            <p>Moving workloads to cloud platforms like Azure or AWS effectively outsources the power problem. Major cloud providers have multiple layers of redundancy, backup power, and geographic distribution that no typical South African business could match.</p>
            <p>This doesn't mean "lift and shift" everything blindly. A thoughtful migration prioritises:</p>
            <ul>
                <li><strong>Customer-facing systems:</strong> Your clients shouldn't suffer because your office has no power</li>
                <li><strong>Collaboration tools:</strong> Staff can work from anywhere with power</li>
                <li><strong>Critical business processes:</strong> Invoicing, orders, and approvals that can't wait</li>
            </ul>
            
            <h2>Enabling Remote Work</h2>
            <p>Load shedding has accelerated the shift to remote and hybrid work. If your systems require staff to be physically in the office, you're losing productive hours every time Eskom sheds load.</p>
            <p>Key enablers include:</p>
            <ul>
                <li>Cloud-based productivity suites (Microsoft 365, Google Workspace)</li>
                <li>Secure remote access to business applications</li>
                <li>Mobile-friendly systems that work on cellular connections</li>
                <li>Collaboration tools that don't require real-time connectivity</li>
            </ul>
            
            <h2>Designing for Intermittent Connectivity</h2>
            <p>Even with cloud systems, your users' connectivity will be interrupted. Good system design accounts for this:</p>
            <ul>
                <li>Offline-capable applications where feasible</li>
                <li>Graceful handling of connection drops (don't lose work in progress)</li>
                <li>Automatic sync and retry logic</li>
                <li>Low-bandwidth options for users on mobile data</li>
            </ul>
            
            <h2>Business Continuity Planning</h2>
            <p>Technology is only part of the solution. Load shedding resilience requires:</p>
            <ul>
                <li>Clear policies on remote work during outages</li>
                <li>Communication channels that work without office systems</li>
                <li>Prioritisation of what work can wait versus what must continue</li>
                <li>Regular testing of backup systems and processes</li>
            </ul>
            
            <h2>The Silver Lining</h2>
            <p>Organisations that invest in load-shedding resilience often find they've also improved agility, reduced costs, and built systems that are more robust overall. The South African power crisis, frustrating as it is, can be a catalyst for modernisation that delivers lasting value.</p>
        """,
    },
]
