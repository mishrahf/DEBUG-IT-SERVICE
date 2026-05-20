from django.db import models


class Project(models.Model):
    """Portfolio project model"""
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    client = models.CharField(max_length=200)
    technologies = models.CharField(max_length=500, help_text="Enter technologies used, separated by comma")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    featured = models.BooleanField(default=False)
    project_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
