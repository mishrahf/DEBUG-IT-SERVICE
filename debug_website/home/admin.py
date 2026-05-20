from django.contrib import admin
from .models import Service, Testimonial, Partner


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating')
    list_filter = ('rating', 'created_at')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'partner_type', 'featured', 'order')
    list_filter = ('partner_type', 'featured')
    list_editable = ('featured', 'order')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'partner_type', 'description')
        }),
        ('Media & Links', {
            'fields': ('logo', 'website')
        }),
        ('Display Options', {
            'fields': ('featured', 'order')
        }),
    )
