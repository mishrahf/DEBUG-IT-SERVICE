from django.test import TestCase
from .models import BlogPost


class BlogPostTestCase(TestCase):
    def setUp(self):
        BlogPost.objects.create(
            title="Test Blog Post",
            excerpt="This is a test excerpt",
            content="This is the full blog post content",
            author="Test Author",
            status="published",
            tags="django, python"
        )
    
    def test_blog_post_creation(self):
        post = BlogPost.objects.get(title="Test Blog Post")
        self.assertEqual(post.author, "Test Author")
        self.assertEqual(post.status, "published")
    
    def test_slug_generation(self):
        post = BlogPost.objects.get(title="Test Blog Post")
        self.assertEqual(post.slug, "test-blog-post")
    
    def test_blog_post_ordering(self):
        posts = BlogPost.objects.all()
        self.assertEqual(posts[0].title, "Test Blog Post")
