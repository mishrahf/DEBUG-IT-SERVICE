# Useful Commands & Reference

## Django Management Commands

### Database Operations
```bash
# Create database migrations
python manage.py makemigrations

# Apply database migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Reverse to previous migration
python manage.py migrate [app_name] [migration_name]

# Dump database data
python manage.py dumpdata > backup.json

# Load data from dump
python manage.py loaddata backup.json

# Clear database (WARNING: deletes all data)
python manage.py flush
```

### Admin & Users
```bash
# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword [username]

# Create user
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_user('username', 'email@example.com', 'password')
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic

# Find static files
python manage.py findstatic [filename]

# Clear collected static files
python manage.py collectstatic --clear
```

### Testing
```bash
# Run all tests
python manage.py test

# Run app tests
python manage.py test home

# Run specific test class
python manage.py test home.tests.ServiceTestCase

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Development
```bash
# Start development server
python manage.py runserver

# Run on different port
python manage.py runserver 8001

# Open Django shell
python manage.py shell

# Create data
python manage.py seed_data

# Check for problems
python manage.py check
```

## Useful Development Workflow

### Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Deactivate
deactivate

# Install packages
pip install -r requirements.txt

# Freeze packages
pip freeze > requirements.txt

# Uninstall package
pip uninstall package_name
```

### Git Commands
```bash
# Clone repository
git clone [url]

# Check status
git status

# Add changes
git add .
git add filename

# Commit
git commit -m "message"

# Push
git push origin branch_name

# Pull
git pull

# Create branch
git checkout -b feature/name

# Switch branch
git checkout branch_name

# Merge branch
git merge branch_name

# View log
git log

# Undo last commit
git reset HEAD~1
```

### Docker Commands
```bash
# Build image
docker build -t debug-it .

# Run container
docker run -p 8000:8000 debug-it

# View containers
docker ps

# View images
docker images

# Stop container
docker stop [container_id]

# Remove container
docker rm [container_id]

# Remove image
docker rmi [image_id]

# Docker Compose up
docker-compose up

# Docker Compose down
docker-compose down

# View logs
docker-compose logs -f
```

### Useful Python Commands
```bash
# Check Python version
python --version

# List installed packages
pip list

# Search package
pip search keyword

# Show package info
pip show package_name

# Upgrade package
pip install --upgrade package_name
```

## Database Queries in Shell

```python
# Enter Django shell
python manage.py shell

# Import models
from home.models import Service, Testimonial
from services.models import ServiceCategory, DetailedService
from portfolio.models import Project
from blog.models import BlogPost

# Query examples
Service.objects.all()
Service.objects.filter(title__contains='SaaS')
Service.objects.get(id=1)
Service.objects.create(title='New Service', description='Desc')
service = Service.objects.get(id=1)
service.delete()
service.title = 'Updated Title'
service.save()

# Count
Service.objects.count()

# Order
Service.objects.all().order_by('-created_at')

# Pagination
Service.objects.all()[:10]
Service.objects.all()[10:20]

# Relationships
category = ServiceCategory.objects.get(id=1)
category.services.all()

# Exit shell
exit()
```

## Environment Variables

### Create .env file
```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

## Common Errors & Solutions

### 1. ModuleNotFoundError: No module named 'django'
```bash
# Solution: Activate virtual environment and install packages
source venv/bin/activate
pip install -r requirements.txt
```

### 2. RuntimeError: no such table: home_service
```bash
# Solution: Run migrations
python manage.py migrate
```

### 3. TemplateDoesNotExist
```bash
# Solution: Check TEMPLATES setting in settings.py
# Ensure template path is correct
# Restart development server
```

### 4. CSRF token missing or incorrect
```bash
# Solution: Add {% csrf_token %} to forms in templates
```

### 5. Address already in use Port 8000
```bash
# Solution 1: Use different port
python manage.py runserver 8001

# Solution 2: Kill process on port 8000
# Windows: netstat -ano | findstr :8000
# Mac/Linux: lsof -i :8000 | kill [PID]
```

## Performance Tips

### Optimize Queries
```python
# Use select_related for ForeignKey
Project.objects.select_related('category')

# Use prefetch_related for M2M
BlogPost.objects.prefetch_related('tags')

# Filter early
Service.objects.filter(active=True).count()

# Use only()
Service.objects.only('title', 'description')

# Use values() for specific fields
Service.objects.values('title', 'description')
```

### Caching
```python
# Cache query result
cache.set('services', Service.objects.all(), 3600)
services = cache.get('services')

# Cache template fragment
{% load cache %}
{% cache 300 service_list %}
  ...template code...
{% endcache %}
```

## Security Checklist

- [ ] Change SECRET_KEY
- [ ] Set DEBUG=False in production
- [ ] Update ALLOWED_HOSTS
- [ ] Enable HTTPS
- [ ] Set SECURE_SSL_REDIRECT=True
- [ ] Set SESSION_COOKIE_SECURE=True
- [ ] Use environment variables
- [ ] Regular backups
- [ ] Update dependencies
- [ ] Monitor logs
- [ ] Test security vulnerabilities

## Performance Checklist

- [ ] Enable database query caching
- [ ] Minimize database queries
- [ ] Use CDN for static files
- [ ] Enable gzip compression
- [ ] Optimize images
- [ ] Minify CSS/JavaScript
- [ ] Use database indexing
- [ ] Enable browser caching
- [ ] Monitor response times
- [ ] Use pagination

## Backup & Recovery

### Backup Database
```bash
# Backup
python manage.py dumpdata > backup_$(date +%Y%m%d).json

# Backup on schedule
# Add to crontab (Linux):
0 2 * * * cd /path/to/project && python manage.py dumpdata > backups/backup_$(date +\%Y\%m\%d).json
```

### Restore Database
```bash
# Restore
python manage.py loaddata backup_20260406.json

# Restore specific app
python manage.py loaddata backup_20260406.json --app home
```

### Backup Media Files
```bash
# Linux/Mac
tar -czf media_backup_$(date +%Y%m%d).tar.gz media/

# Windows (using 7-Zip or similar)
7z a media_backup.7z media\
```

## Monitoring Commands

```bash
# Check Django health
python manage.py check

# List all URL patterns
python manage.py show_urls

# Analyze models
python manage.py graph_models -a -o models.png

# Database statistics
python manage.py sqlsequencereset [app_name]
```

## Quick Reference URLs

- Homepage: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- Services: http://localhost:8000/services/
- Portfolio: http://localhost:8000/portfolio/
- Blog: http://localhost:8000/blog/
- Contact: http://localhost:8000/contact/

---

For more information, refer to:
- Django Documentation: https://docs.djangoproject.com
- Python Documentation: https://python.org/docs
- Bootstrap Documentation: https://getbootstrap.com/docs
