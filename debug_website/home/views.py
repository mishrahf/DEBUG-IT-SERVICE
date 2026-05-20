from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
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
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you would send an email
        # For now, just show success message
        context = {'success': True}
        return render(request, 'home/contact.html', context)
    
    return render(request, 'home/contact.html')
