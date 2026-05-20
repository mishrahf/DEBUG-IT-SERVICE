from django.test import TestCase
from .models import ServiceCategory, DetailedService


class ServiceCategoryTestCase(TestCase):
    def setUp(self):
        ServiceCategory.objects.create(
            name="Development",
            description="Development Services",
            icon="fas fa-code"
        )
    
    def test_category_creation(self):
        category = ServiceCategory.objects.get(name="Development")
        self.assertEqual(str(category), "Development")


class DetailedServiceTestCase(TestCase):
    def setUp(self):
        category = ServiceCategory.objects.create(
            name="Development",
            description="Development Services",
            icon="fas fa-code"
        )
        DetailedService.objects.create(
            category=category,
            title="Web Development",
            description="Professional web development",
            short_description="Build amazing web apps",
            features="Responsive, Fast, Secure"
        )
    
    def test_service_creation(self):
        service = DetailedService.objects.get(title="Web Development")
        self.assertEqual(service.category.name, "Development")
