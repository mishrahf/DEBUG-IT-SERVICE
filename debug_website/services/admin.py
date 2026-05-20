from django.contrib import admin
from .models import ServiceCategory, DetailedService


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(DetailedService)
class DetailedServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
