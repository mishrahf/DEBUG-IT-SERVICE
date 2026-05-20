#!/usr/bin/env python
"""
Script to populate DEBUG IT SERVICE database with fake data
"""
import os
import django
from datetime import datetime, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debug_it.settings')
django.setup()

from home.models import Testimonial, Service
from blog.models import BlogPost
from portfolio.models import Project
from django.utils.text import slugify

# Sample data
FAKE_TESTIMONIALS = [
    {
        "client_name": "Rajesh Kumar",
        "company": "Tech Innovations India",
        "message": "DEBUG IT SERVICE transformed our business with their exceptional SaaS platform. Their team's expertise and dedication made all the difference. Highly recommended!",
        "rating": 5
    },
    {
        "client_name": "Priya Sharma",
        "company": "E-Commerce Solutions Pvt Ltd",
        "message": "Outstanding work on our AI agentic system. The automation capabilities have increased our efficiency by 300%. Best decision we made!",
        "rating": 5
    },
    {
        "client_name": "Amit Patel",
        "company": "Digital Marketing Hub",
        "message": "Their web application development is world-class. The team understands modern tech stack and delivers quality code. Very professional!",
        "rating": 5
    },
    {
        "client_name": "Neha Gupta",
        "company": "Financial Tech Solutions",
        "message": "DEBUG IT SERVICE's mobile app development gave us a competitive edge. Responsive, fast, and user-friendly. Exceeded expectations!",
        "rating": 5
    },
    {
        "client_name": "Vikram Singh",
        "company": "Enterprise Solutions Ltd",
        "message": "Great DevOps support and deployment expertise. Our infrastructure is now scalable and reliable. Excellent service!",
        "rating": 5
    },
]

FAKE_BLOGS = [
    {
        "title": "The Future of SaaS Development in 2026",
        "content": """
        <p>The SaaS industry is rapidly evolving with new technologies and methodologies emerging every day. In this article, we explore the key trends that will shape SaaS development in 2026.</p>
        
        <h3>1. AI Integration</h3>
        <p>Artificial Intelligence is no longer optional for SaaS platforms. Companies are integrating AI to provide smarter features, better user experience, and automated workflows.</p>
        
        <h3>2. Multi-Tenancy Architecture</h3>
        <p>Modern SaaS platforms require robust multi-tenancy architecture to serve multiple customers with isolated data and customizable experiences.</p>
        
        <h3>3. Real-time Collaboration</h3>
        <p>Users expect real-time collaboration features. Technologies like WebSockets and operational transformation are becoming standard in SaaS applications.</p>
        
        <h3>4. Enhanced Security</h3>
        <p>Data security and privacy regulations are tightening. Implementing end-to-end encryption and zero-trust architecture is crucial.</p>
        
        <p>At DEBUG IT SERVICE, we help businesses build next-generation SaaS applications that incorporate these modern practices and technologies.</p>
        """,
        "tags": "SaaS, AI, Development, 2026",
        "status": "published"
    },
    {
        "title": "Building Intelligent Autonomous Agents with AI",
        "content": """
        <p>Autonomous agents powered by AI are revolutionizing how businesses operate. Let's explore what makes them powerful and how to build effective ones.</p>
        
        <h3>Understanding AI Agents</h3>
        <p>AI agents are software entities that can perceive their environment, make decisions, and take actions autonomously to achieve specified goals.</p>
        
        <h3>Key Components</h3>
        <ul>
        <li>Perception: Gathering data from environment</li>
        <li>Decision Making: Using ML models to decide actions</li>
        <li>Action: Taking steps to achieve goals</li>
        <li>Learning: Improving through feedback</li>
        </ul>
        
        <h3>Real-World Applications</h3>
        <p>From customer service chatbots to supply chain optimization, AI agents are transforming industries.</p>
        
        <p>Our team at DEBUG IT SERVICE specializes in developing custom AI agentic systems tailored to your business needs.</p>
        """,
        "tags": "AI, Agents, Automation, Machine Learning",
        "status": "published"
    },
    {
        "title": "Web Development Best Practices 2026",
        "content": """
        <p>Modern web development requires following best practices to ensure performance, security, and maintainability. Here are the key practices we follow.</p>
        
        <h3>1. Responsive Design</h3>
        <p>All applications must work seamlessly on mobile, tablet, and desktop devices. Mobile-first approach is now standard.</p>
        
        <h3>2. Performance Optimization</h3>
        <p>Fast loading times are critical. Techniques like lazy loading, code splitting, and CDN usage are essential.</p>
        
        <h3>3. Accessibility</h3>
        <p>Web applications must be usable by everyone, including people with disabilities. WCAG 2.1 compliance is important.</p>
        
        <h3>4. Testing</h3>
        <p>Comprehensive testing including unit tests, integration tests, and end-to-end tests ensures quality.</p>
        
        <h3>5. DevOps</h3>
        <p>Continuous Integration and Continuous Deployment pipelines ensure rapid and reliable releases.</p>
        
        <p>DEBUG IT SERVICE applies all these best practices in every project we undertake.</p>
        """,
        "tags": "Web Development, Best Practices, Performance",
        "status": "published"
    },
    {
        "title": "Mobile App Development: iOS vs Android",
        "content": """
        <p>In this comprehensive guide, we compare iOS and Android development and help you choose the right platform for your application.</p>
        
        <h3>Development Approach</h3>
        <p>iOS uses Swift and Xcode, while Android uses Kotlin and Android Studio. Each has unique advantages.</p>
        
        <h3>Market Reach</h3>
        <p>Android dominates in market share globally, while iOS has strong presence in premium segments.</p>
        
        <h3>Monetization</h3>
        <p>iOS users typically have higher spending potential, while Android has larger user base.</p>
        
        <h3>Our Recommendation</h3>
        <p>The best approach is often cross-platform development using Flutter or React Native for faster time-to-market.</p>
        
        <p>Let DEBUG IT SERVICE help you build a mobile application that works perfectly on all platforms.</p>
        """,
        "tags": "Mobile, iOS, Android, Development",
        "status": "published"
    },
    {
        "title": "Cybersecurity in SaaS Applications",
        "content": """
        <p>Security is paramount in SaaS applications. This guide covers essential security measures for protecting user data.</p>
        
        <h3>Authentication & Authorization</h3>
        <p>Implement strong authentication using OAuth 2.0 and multi-factor authentication. Fine-grained authorization controls ensure users only access what they need.</p>
        
        <h3>Data Encryption</h3>
        <p>Encrypt data both at rest and in transit. Use industry-standard algorithms like AES-256 and TLS 1.3.</p>
        
        <h3>Regular Audits</h3>
        <p>Conduct regular security audits and penetration testing to identify and fix vulnerabilities.</p>
        
        <h3>Compliance</h3>
        <p>Ensure compliance with regulations like GDPR, CCPA, and industry-specific standards.</p>
        
        <p>DEBUG IT SERVICE implements comprehensive security measures in all applications we develop.</p>
        """,
        "tags": "Security, Cybersecurity, SaaS, Privacy",
        "status": "published"
    },
]

FAKE_PROJECTS = [
    {
        "title": "E-Commerce Platform for Fashion Retail",
        "short_description": "Built a scalable multi-vendor SaaS e-commerce platform with AI-powered recommendations",
        "description": """
        <h3>Project Overview</h3>
        <p>Developed a comprehensive e-commerce platform for a leading fashion retailer in India.</p>
        
        <h3>Key Features</h3>
        <ul>
        <li>Multi-vendor support with commission management</li>
        <li>AI-powered product recommendations</li>
        <li>Real-time inventory management</li>
        <li>Advanced payment gateway integration</li>
        <li>Mobile app (iOS & Android)</li>
        <li>Admin dashboard with analytics</li>
        </ul>
        
        <h3>Technologies Used</h3>
        <p>Django, React, PostgreSQL, Redis, AWS, Machine Learning</p>
        
        <h3>Results</h3>
        <p>Increased online sales by 250%, reduced manual work by 80%, improved customer satisfaction to 4.8/5 stars</p>
        """,
        "client": "Fashion Retail India",
        "technologies": "Django, React, PostgreSQL, AWS, AI/ML",
        "status": "completed",
        "featured": True,
        "project_url": "https://debugitservice.com"
    },
    {
        "title": "Financial Analytics AI Agent System",
        "short_description": "Intelligent agent system for automated financial analysis and reporting",
        "description": """
        <h3>Project Overview</h3>
        <p>Created an AI agentic system for automated financial data analysis and decision making.</p>
        
        <h3>Key Features</h3>
        <ul>
        <li>Autonomous data collection from multiple sources</li>
        <li>Real-time financial analysis using advanced algorithms</li>
        <li>Automated report generation</li>
        <li>Predictive analytics for trend forecasting</li>
        <li>Integration with existing financial systems</li>
        </ul>
        
        <h3>Technologies Used</h3>
        <p>Python, TensorFlow, PostgreSQL, RabbitMQ, Apache Kafka</p>
        
        <h3>Impact</h3>
        <p>Reduced analysis time from days to minutes, improved accuracy to 99.2%, saved 40% in operational costs</p>
        """,
        "client": "Financial Analytics Corp",
        "technologies": "Python, AI, TensorFlow, Kafka, PostgreSQL",
        "status": "completed",
        "featured": True,
        "project_url": "https://debugitservice.com"
    },
    {
        "title": "Healthcare Patient Management System",
        "short_description": "HIPAA-compliant web and mobile platform for patient data management",
        "description": """
        <h3>Project Overview</h3>
        <p>Developed a comprehensive patient management system for a healthcare provider network.</p>
        
        <h3>Key Features</h3>
        <ul>
        <li>Secure patient records management</li>
        <li>Appointment scheduling and reminders</li>
        <li>Digital prescriptions</li>
        <li>Telemedicine integration</li>
        <li>Insurance billing automation</li>
        <li>Mobile app for patients</li>
        </ul>
        
        <h3>Compliance</h3>
        <p>HIPAA, GDPR, and local healthcare regulations</p>
        
        <h3>Results</h3>
        <p>Improved patient engagement by 180%, reduced manual administrative work by 70%, zero security incidents</p>
        """,
        "client": "Healthcare Solutions Inc",
        "technologies": "Django, React, PostgreSQL, AWS, HIPAA",
        "status": "completed",
        "featured": False,
        "project_url": "https://debugitservice.com"
    },
    {
        "title": "Supply Chain Optimization Platform",
        "short_description": "Real-time supply chain tracking and optimization using IoT and AI",
        "description": """
        <h3>Project Overview</h3>
        <p>Built an intelligent platform for real-time supply chain visibility and optimization.</p>
        
        <h3>Key Features</h3>
        <ul>
        <li>Real-time GPS tracking of shipments</li>
        <li>IoT sensor integration for temperature/humidity monitoring</li>
        <li>AI-powered route optimization</li>
        <li>Predictive maintenance alerts</li>
        <li>Supplier management portal</li>
        <li>Advanced analytics dashboard</li>
        </ul>
        
        <h3>Technologies Used</h3>
        <p>Node.js, Vue.js, MongoDB, IoT, Machine Learning</p>
        
        <h3>Business Impact</h3>
        <p>Reduced delivery time by 35%, decreased shipping costs by 25%, improved on-time delivery to 98%</p>
        """,
        "client": "Logistics Global",
        "technologies": "Node.js, Vue.js, IoT, AI, MongoDB",
        "status": "completed",
        "featured": True,
        "project_url": "https://debugitservice.com"
    },
    {
        "title": "Social Learning Platform",
        "short_description": "Interactive platform for collaborative learning with gamification",
        "description": """
        <h3>Project Overview</h3>
        <p>Developed a social learning platform combining education with gamification and peer interaction.</p>
        
        <h3>Key Features</h3>
        <ul>
        <li>Interactive video courses</li>
        <li>Live classroom sessions with screen sharing</li>
        <li>Peer review and collaboration tools</li>
        <li>Gamification with badges and leaderboards</li>
        <li>Progress tracking and analytics</li>
        <li>Content creation tools for educators</li>
        </ul>
        
        <h3>Technologies Used</h3>
        <p>React, Django, WebRTC, PostgreSQL, Redis</p>
        
        <h3>Success Metrics</h3>
        <p>10,000+ active users, 95% retention rate, 4.9/5 app rating, 50+ educational institutions using the platform</p>
        """,
        "client": "EduTech Innovations",
        "technologies": "React, Django, WebRTC, PostgreSQL, Redis",
        "status": "completed",
        "featured": False,
        "project_url": "https://debugitservice.com"
    },
]

def populate_testimonials():
    """Populate testimonials"""
    print("Adding testimonials...")
    for data in FAKE_TESTIMONIALS:
        testimonial, created = Testimonial.objects.get_or_create(
            client_name=data['client_name'],
            company=data['company'],
            defaults={
                'message': data['message'],
                'rating': data['rating'],
            }
        )
        if created:
            print(f"  ✓ Added testimonial from {data['client_name']}")
        else:
            print(f"  - Testimonial from {data['client_name']} already exists")

def populate_blogs():
    """Populate blog posts"""
    print("\nAdding blog posts...")
    base_date = datetime.now()
    
    for i, data in enumerate(FAKE_BLOGS):
        slug = slugify(data['title'])
        post_date = base_date - timedelta(days=i*7)
        
        blog, created = BlogPost.objects.get_or_create(
            slug=slug,
            defaults={
                'title': data['title'],
                'content': data['content'],
                'tags': data['tags'],
                'status': data['status'],
                'created_at': post_date,
                'updated_at': post_date,
            }
        )
        if created:
            print(f"  ✓ Added blog: {data['title']}")
        else:
            print(f"  - Blog '{data['title']}' already exists")

def populate_projects():
    """Populate portfolio projects"""
    print("\nAdding portfolio projects...")
    
    for data in FAKE_PROJECTS:
        project, created = Project.objects.get_or_create(
            title=data['title'],
            defaults={
                'short_description': data['short_description'],
                'description': data['description'],
                'client': data['client'],
                'technologies': data['technologies'],
                'status': data['status'],
                'featured': data['featured'],
                'project_url': data['project_url'],
            }
        )
        if created:
            print(f"  ✓ Added project: {data['title']}")
        else:
            print(f"  - Project '{data['title']}' already exists")

def main():
    """Main function"""
    print("=" * 60)
    print("DEBUG IT SERVICE - Populating Fake Data")
    print("=" * 60)
    
    try:
        populate_testimonials()
        populate_blogs()
        populate_projects()
        
        print("\n" + "=" * 60)
        print("✓ Data population completed successfully!")
        print("=" * 60)
        
        # Print summary
        print(f"\nSummary:")
        print(f"  Testimonials: {Testimonial.objects.count()}")
        print(f"  Blog Posts: {BlogPost.objects.filter(status='published').count()}")
        print(f"  Projects: {Project.objects.count()}")
        
    except Exception as e:
        print(f"\n✗ Error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
