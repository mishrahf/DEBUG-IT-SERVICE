from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Testimonial, Partner
from portfolio.models import Project


class HomeView(TemplateView):
    """Home page view"""
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()[:6]
        context['testimonials'] = Testimonial.objects.all()[:3]
        context['projects'] = Project.objects.filter(featured=True)[:3]
        context['partners'] = Partner.objects.filter(featured=True)
        return context


class AboutView(TemplateView):
    """About page view"""
    template_name = 'home/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class PartnersView(TemplateView):
    """Partners page view"""
    template_name = 'home/partners.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ai_partners'] = Partner.objects.filter(partner_type='ai')
        context['it_partners'] = Partner.objects.filter(partner_type='it')
        context['cloud_partners'] = Partner.objects.filter(partner_type='cloud')
        context['infra_partners'] = Partner.objects.filter(partner_type='infrastructure')
        context['all_partners'] = Partner.objects.all()
        return context


def contact_view(request):
    """Contact form view"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            # Validate required fields
            if not all([name, email, subject, message]):
                context = {
                    'error': 'All fields are required',
                    'form_data': request.POST
                }
                return render(request, 'home/contact.html', context)
            
            # Send email to admin
            send_mail(
                subject=f'Contact Form: {subject}',
                message=f'From: {name} ({email})\n\n{message}',
                from_email=email,
                recipient_list=['info@debugitservice.com'],
                fail_silently=False,
            )
            
            # Send confirmation email to user
            send_mail(
                subject='We received your inquiry',
                message=f'Hi {name},\n\nThank you for contacting us. We have received your inquiry and will get back to you soon.\n\nBest regards,\nDEBUG IT SERVICE',
                from_email='info@debugitservice.com',
                recipient_list=[email],
                fail_silently=False,
            )
            context = {'success': True}
            return render(request, 'home/contact.html', context)
        except Exception as e:
            context = {
                'error': f'Failed to send email: {str(e)}',
                'form_data': request.POST
            }
            return render(request, 'home/contact.html', context)
                
    return render(request, 'home/contact.html')
