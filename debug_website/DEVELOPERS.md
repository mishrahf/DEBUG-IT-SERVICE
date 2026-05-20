# DEBUG IT SERVICE - Developer's Guide

## Project Overview

DEBUG IT SERVICE is a professional Django-based website for showcasing IT services, specifically SaaS solutions and AI agentic projects. The system includes a full content management system for managing services, portfolio projects, blog posts, and client testimonials.

## Technology Stack

- **Backend**: Django 4.2
- **Frontend**: HTML5, Bootstrap 5, CSS3
- **Database**: SQLite (Dev) / PostgreSQL (Prod)
- **Server**: Gunicorn
- **Web Server**: Nginx (Production)
- **Container**: Docker & Docker Compose
- **Icons**: Font Awesome 6

## Project Architecture

### Apps Structure

```
debug_it/          - Django project settings
home/              - Homepage, about, contact, services
services/          - Service categories and detailed services
portfolio/         - Project portfolio showcase
blog/              - Blog post management
```

### Database Models

#### Home App
- **Service**: Main service offerings
- **Testimonial**: Client testimonials with ratings

#### Services App
- **ServiceCategory**: Service categories
- **DetailedService**: Detailed service descriptions with features

#### Portfolio App
- **Project**: Portfolio projects with status and technologies

#### Blog App
- **BlogPost**: Blog articles with auto-generated slugs

## API Endpoints Reference

### Public Routes

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage |
| `/about/` | GET | About page |
| `/contact/` | GET/POST | Contact form |
| `/services/` | GET | Services list |
| `/services/detail/<id>/` | GET | Service details |
| `/portfolio/` | GET | Portfolio list (paginated) |
| `/portfolio/project/<id>/` | GET | Project details |
| `/blog/` | GET | Blog list (paginated) |
| `/blog/post/<slug>/` | GET | Blog post details |
| `/admin/` | GET | Admin panel |

## Customization Guide

### Adding a New Service

1. Go to Django admin (`/admin/`)
2. Navigate to "Services" > "Service Categories"
3. Create a new category
4. Navigate to "Services" > "Detailed Services"
5. Create a new service in that category

### Adding Portfolio Projects

1. Admin → "Portfolio" > "Projects"
2. Fill in project details:
   - Title
   - Description
   - Client name
   - Technologies used
   - Featured status
   - Project status (completed/in progress)

### Creating Blog Posts

1. Admin → "Blog" > "Blog posts"
2. Fill in post details:
   - Title (slug auto-generates)
   - Excerpt
   - Content
   - Author
   - Featured image
   - Tags (comma-separated)
   - Status (draft/published)

### Adding Client Testimonials

1. Admin → "Home" > "Testimonials"
2. Fill in:
   - Client name
   - Company
   - Rating (1-5 stars)
   - Message
   - Optional image

## CSS Customization

### Color Scheme
Edit `static/css/style.css`:

```css
:root {
    --primary-color: #dc3545;      /* Main brand color */
    --dark-color: #212529;          /* Dark background */
    --light-color: #f8f9fa;         /* Light background */
    --border-radius: 0.5rem;        /* Rounded corners */
    --transition: all 0.3s ease;    /* Animation duration */
}
```

### Add Custom Styles
Create `static/css/custom.css` and link in `base.html`:

```html
<link rel="stylesheet" href="{% static 'css/custom.css' %}">
```

## JavaScript Usage

### Main Functions Available

```javascript
// Animate number counter
DEBUG_IT.animateCounter(element, endValue, duration);

// Handle form submission
DEBUG_IT.handleContactSubmit(event);

// Lazy load images
DEBUG_IT.lazyLoadImages();
```

### Add Custom Scripts
Create `static/js/custom.js` and link in `base.html`:

```html
<script src="{% static 'js/custom.js' %}"></script>
```

## Database Management

### Create Backup
```bash
python manage.py dumpdata > backup.json
```

### Restore from Backup
```bash
python manage.py loaddata backup.json
```

### Clear Database
```bash
python manage.py flush
```

## Testing

### Run Tests
```bash
python manage.py test
```

### Run Specific App Tests
```bash
python manage.py test home
python manage.py test services
python manage.py test portfolio
python manage.py test blog
```

### Run Specific Test Class
```bash
python manage.py test home.tests.ServiceTestCase
```

## Performance Optimization

### Enable Caching
Add to `settings.py`:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### Database Optimization
- Add indexes to frequently queried fields
- Use `select_related()` for ForeignKey relationships
- Use `prefetch_related()` for reverse ForeignKey and M2M

### Static File Optimization
```bash
# Minify CSS and JavaScript
# Use CDN for static files
# Enable gzip compression
```

## Security Best Practices

1. **Environment Variables**
   - Never commit secrets
   - Use `.env` file (add to `.gitignore`)
   - Use `django-environ` package

2. **HTTPS**
   - Enable SSL in production
   - Set `SECURE_SSL_REDIRECT = True`

3. **CSRF Protection**
   - Always include `{% csrf_token %}` in forms
   - Django handles automatically

4. **SQL Injection Prevention**
   - Always use Django ORM
   - Never write raw SQL queries

5. **XSS Prevention**
   - Use `{{ variable }}` instead of `{{ variable|safe }}`
   - Escape user input automatically in templates

## Deployment Checklist

- [ ] Set `DEBUG = False`
- [ ] Update `SECRET_KEY` (unique, strong)
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up HTTPS/SSL
- [ ] Configure email backend
- [ ] Set up database backups
- [ ] Enable logging
- [ ] Configure static files
- [ ] Set up media files storage
- [ ] Test all functionality
- [ ] Set up monitoring
- [ ] Configure security headers

## Troubleshooting

### Static Files Not Loading
- Run `python manage.py collectstatic`
- Check `STATIC_ROOT` and `STATIC_URL` settings
- Verify web server configuration

### Database Issues
- Check PostgreSQL connection string
- Verify database credentials
- Run migrations: `python manage.py migrate`

### Performance Issues
- Use Django Debug Toolbar
- Check query count
- Enable caching
- Optimize database queries

### Email Not Sending
- Verify email configuration
- Check email backend
- Test with console backend first

## Development Tools

### Django Debug Toolbar
```bash
pip install django-debug-toolbar
```

### Django Extensions
```bash
pip install django-extensions
```

### Code Quality
```bash
pip install flake8 black isort
```

## Common Git Commands

```bash
# Clone repository
git clone <url>

# Create new branch
git checkout -b feature/name

# Commit changes
git add .
git commit -m "Description"

# Push to remote
git push origin feature/name

# Create pull request
# On GitHub, create PR
```

## File Organization Tips

- Keep templates organized by app
- Store static files by type (css, js, images)
- Separate media uploads directory
- Use meaningful file names
- Document complex components

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Font Awesome Icons](https://fontawesome.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)

## Getting Help

- Check existing code for examples
- Read Django documentation
- Use Stack Overflow for common issues
- Join Django community forums

---

**Happy coding! 🚀**
