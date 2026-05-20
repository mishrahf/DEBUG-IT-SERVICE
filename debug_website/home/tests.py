from django.test import TestCase
from django.urls import reverse
from .models import Service, Testimonial


class ServiceTestCase(TestCase):
    def setUp(self):
        Service.objects.create(
            title="Test Service",
            description="Test Description",
            icon="fas fa-code"
        )
    
    def test_service_creation(self):
        service = Service.objects.get(title="Test Service")
        self.assertEqual(service.title, "Test Service")
        self.assertEqual(str(service), "Test Service")


class TestimonialTestCase(TestCase):
    def setUp(self):
        Testimonial.objects.create(
            client_name="John Doe",
            company="Test Company",
            message="Great service!",
            rating=5
        )
    
    def test_testimonial_creation(self):
        testimonial = Testimonial.objects.get(client_name="John Doe")
        self.assertEqual(testimonial.rating, 5)


class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)

    def test_logo_redirects_to_home(self):
        response = self.client.get(reverse('home:home'))
        self.assertContains(response, '<a class="navbar-brand" href="/">')


class AllPagesTests(TestCase):
    def test_all_pages_status_code(self):
        pages = [
            reverse('home:home'),
            reverse('home:about'),
            reverse('home:partners'),
            reverse('home:contact'),
            reverse('services:list'),
            reverse('portfolio:list'),
            reverse('blog:list'),
        ]
        for page in pages:
            with self.subTest(page=page):
                response = self.client.get(page)
                self.assertEqual(response.status_code, 200)
