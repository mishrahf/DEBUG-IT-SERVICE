from django.db import models

class Service(models.Model):
    """Service offering model"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-code')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    """Client testimonial model"""
    client_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    message = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.client_name} - {self.company}"


class Partner(models.Model):
    """Technology and business partner model"""
    PARTNER_TYPES = [
        ('ai', 'AI Partner'),
        ('it', 'IT Partner'),
        ('cloud', 'Cloud Partner'),
        ('infrastructure', 'Infrastructure Partner'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    partner_type = models.CharField(max_length=20, choices=PARTNER_TYPES, default='it')
    description = models.TextField()
    logo = models.ImageField(upload_to='partners/', null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.get_partner_type_display()}"
