from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project


class PortfolioListView(ListView):
    """List all portfolio projects"""
    model = Project
    template_name = 'portfolio/portfolio_list.html'
    context_object_name = 'projects'
    paginate_by = 9


class ProjectDetailView(DetailView):
    """Detailed project view"""
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    slug_field = 'id'
    slug_url_kwarg = 'id'
