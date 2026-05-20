from django.test import TestCase
from .models import Project


class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(
            title="Test Project",
            description="A test project description",
            short_description="Test project",
            client="Test Client",
            technologies="Django, React",
            status="completed",
            featured=True
        )
    
    def test_project_creation(self):
        project = Project.objects.get(title="Test Project")
        self.assertEqual(project.client, "Test Client")
        self.assertTrue(project.featured)
        self.assertEqual(str(project), "Test Project")
    
    def test_project_ordering(self):
        projects = Project.objects.all()
        self.assertEqual(len(projects), 1)
