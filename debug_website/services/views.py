from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import ServiceCategory, DetailedService


class ServicesListView(ListView):
    """List all service categories"""
    model = ServiceCategory
    template_name = 'services/services_list.html'
    context_object_name = 'categories'


class ServiceDetailView(DetailView):
    """Detailed service view"""
    model = DetailedService
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    slug_field = 'id'
    slug_url_kwarg = 'id'
