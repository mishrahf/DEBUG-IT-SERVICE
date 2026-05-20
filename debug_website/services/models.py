from django.db import models


class ServiceCategory(models.Model):
    """Service category model"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Service Categories'
    
    def __str__(self):
        return self.name


class DetailedService(models.Model):
    """Detailed service model"""
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=500)
    features = models.TextField(help_text="Enter features separated by comma")
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    
    def __str__(self):
        return self.title
