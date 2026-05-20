from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'status', 'featured')
    list_filter = ('status', 'featured', 'created_at')
    search_fields = ('title', 'client')
