from django.core.management.base import BaseCommand
from home.models import Service, Testimonial
from services.models import ServiceCategory, DetailedService
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Seed initial data for DEBUG IT SERVICE website'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data seeding...'))

        # Create Services
        services_data = [
            {
                'title': 'SaaS Development',
                'description': 'Build scalable, secure, and user-friendly SaaS applications',
                'icon': 'fas fa-cloud',
                'order': 1
            },
            {
                'title': 'AI Agentic Systems',
                'description': 'Develop intelligent autonomous agents for process automation',
                'icon': 'fas fa-robot',
                'order': 2
            },
            {
                'title': 'Web & Mobile Apps',
                'description': 'Create responsive applications for web and mobile platforms',
                'icon': 'fas fa-mobile-alt',
                'order': 3
            },
            {
                'title': 'Machine Learning',
                'description': 'Integrate advanced ML models for data insights',
                'icon': 'fas fa-brain',
                'order': 4
            },
            {
                'title': 'Cybersecurity',
                'description': 'Protect your applications with comprehensive security solutions',
                'icon': 'fas fa-shield-alt',
                'order': 5
            },
            {
                'title': 'DevOps & Deployment',
                'description': 'Streamline development with modern DevOps practices',
                'icon': 'fas fa-cogs',
                'order': 6
            }
        ]

        for service_data in services_data:
            Service.objects.get_or_create(**service_data)
        
        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(services_data)} services'))

        # Create Service Categories
        categories_data = [
            {
                'name': 'Cloud Solutions',
                'description': 'SaaS and cloud-based solutions',
                'icon': 'fas fa-cloud'
            },
            {
                'name': 'AI & Automation',
                'description': 'Artificial Intelligence and Process Automation',
                'icon': 'fas fa-robot'
            },
            {
                'name': 'Software Development',
                'description': 'Custom software development services',
                'icon': 'fas fa-code'
            }
        ]

        for category_data in categories_data:
            ServiceCategory.objects.get_or_create(**category_data)

        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(categories_data)} service categories'))

        # Create Testimonials
        testimonials_data = [
            {
                'client_name': 'Sarah Johnson',
                'company': 'TechStart Inc',
                'message': 'The team at DEBUG IT SERVICE delivered an exceptional SaaS platform that exceeded our expectations. Highly professional and detail-oriented.',
                'rating': 5
            },
            {
                'client_name': 'Michael Chen',
                'company': 'Global Tech Solutions',
                'message': 'Outstanding work on our AI agentic project. The implementation was flawless and the support has been excellent.',
                'rating': 5
            },
            {
                'client_name': 'Emma Williams',
                'company': 'Digital Innovations Ltd',
                'message': 'Great communication and quality deliverables. DEBUG IT SERVICE is our go-to development partner.',
                'rating': 4
            }
        ]

        for testimonial_data in testimonials_data:
            Testimonial.objects.get_or_create(**testimonial_data)

        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(testimonials_data)} testimonials'))

        # Create Sample Projects
        projects_data = [
            {
                'title': 'ECommerce SaaS Platform',
                'description': 'A comprehensive multi-vendor e-commerce SaaS platform with advanced features like inventory management, payment integration, and analytics.',
                'short_description': 'Multi-vendor e-commerce platform',
                'client': 'TechStart Inc',
                'technologies': 'Django, React, PostgreSQL, AWS',
                'status': 'completed',
                'featured': True
            },
            {
                'title': 'AI Customer Service Bot',
                'description': 'Intelligent chatbot system powered by AI that handles customer inquiries automatically, reducing support costs by 60%.',
                'short_description': 'AI-powered customer service automation',
                'client': 'Global Tech Solutions',
                'technologies': 'Python, TensorFlow, Django, OpenAI',
                'status': 'completed',
                'featured': True
            },
            {
                'title': 'Real Estate Management System',
                'description': 'SaaS platform for real estate agencies to manage properties, agents, deals, and customer relationships.',
                'short_description': 'Real estate management software',
                'client': 'Digital Innovations Ltd',
                'technologies': 'Django, Vue.js, PostgreSQL',
                'status': 'completed',
                'featured': True
            }
        ]

        for project_data in projects_data:
            Project.objects.get_or_create(**project_data)

        self.stdout.write(self.style.SUCCESS(f'✓ Created {len(projects_data)} projects'))

        self.stdout.write(self.style.SUCCESS('\n✓ Data seeding completed successfully!'))
        self.stdout.write(self.style.WARNING('\nNext steps:\n1. Visit admin panel: http://localhost:8000/admin/\n2. Add more content as needed\n3. Visit homepage: http://localhost:8000/'))
