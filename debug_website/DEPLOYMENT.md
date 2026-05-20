# DEBUG IT SERVICE - Deployment Guide

This guide covers various deployment options for the DEBUG IT SERVICE website.

## Table of Contents

1. [Local Development](#local-development)
2. [Docker Deployment](#docker-deployment)
3. [Heroku Deployment](#heroku-deployment)
4. [AWS Deployment](#aws-deployment)
5. [DigitalOcean Deployment](#digitalocean-deployment)
6. [PythonAnywhere Deployment](#pythonanywhere-deployment)

## Local Development

### Prerequisites
- Python 3.9+
- pip and virtualenv

### Setup Steps

```bash
# Clone the repository
git clone <repository-url>
cd debug_website

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit `http://localhost:8000`

---

## Docker Deployment

### Prerequisites
- Docker
- Docker Compose

### Setup Steps

```bash
# Build and start containers
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Collect static files
docker-compose exec web python manage.py collectstatic
```

Visit `http://localhost`

### Docker Commands

```bash
# View logs
docker-compose logs -f web

# Stop containers
docker-compose down

# Rebuild images
docker-compose build --no-cache

# Scale web service
docker-compose up -d --scale web=3
```

---

## Heroku Deployment

### Prerequisites
- Heroku CLI
- Git repository

### Setup Steps

```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create debug-it-service

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set ALLOWED_HOSTS=your-app.herokuapp.com

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# View logs
heroku logs --tail
```

### Procfile

Create a `Procfile` in the root directory:

```
web: gunicorn debug_it.wsgi
release: python manage.py migrate
```

### runtime.txt

Create a `runtime.txt` file:

```
python-3.11.0
```

---

## AWS Deployment

### Option 1: Using Elastic Beanstalk

```bash
# Install EB CLI
pip install awsebcli

# Initialize EB application
eb init -p python-3.11 debug-it-service

# Create environment
eb create debug-it-prod

# Deploy
eb deploy

# View logs
eb logs
```

### Option 2: Using EC2

```bash
# Connect to EC2 instance
ssh -i your-key.pem ec2-user@your-instance-ip

# Update system
sudo yum update -y

# Install Python and dependencies
sudo yum install python3 python3-pip -y

# Clone repository
git clone <repository-url>
cd debug_website

# Install requirements
pip3 install -r requirements.txt

# Set up environment
export DEBUG=False
export SECRET_KEY=your-secret-key

# Run with gunicorn
gunicorn debug_it.wsgi:application --bind 0.0.0.0:8000
```

### Using RDS for Database

```bash
# Create RDS PostgreSQL instance via AWS Console
# Get connection details
# Update settings.py with RDS credentials
# Run migrations
python manage.py migrate
```

---

## DigitalOcean Deployment

### Using App Platform

1. Push code to GitHub
2. Connect your repository to DigitalOcean
3. Create new app from repository
4. Configure environment variables
5. Set up PostgreSQL database
6. Deploy

### Using Droplet

```bash
# SSH into droplet
ssh root@your-droplet-ip

# Update system
apt update && apt upgrade -y

# Install dependencies
apt install python3-pip python3-venv postgresql postgresql-contrib nginx -y

# Clone repository
git clone <repository-url>
cd debug_website

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create PostgreSQL database
sudo -u postgres psql
CREATE DATABASE debug_it_db;
CREATE USER debug_user WITH PASSWORD 'your-password';
ALTER ROLE debug_user SET client_encoding TO 'utf8';
ALTER ROLE debug_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE debug_user SET default_transaction_deferrable TO on;
ALTER ROLE debug_user SET default_transaction_read_committed TO on;
GRANT ALL PRIVILEGES ON DATABASE debug_it_db TO debug_user;
\q

# Configure Gunicorn
pip install gunicorn

# Create systemd service file
sudo nano /etc/systemd/system/debug-it.service
```

Add the following:

```ini
[Unit]
Description=DEBUG IT SERVICE
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/debug_website
ExecStart=/path/to/venv/bin/gunicorn debug_it.wsgi:application --bind 0.0.0.0:8000

[Install]
WantedBy=multi-user.target
```

```bash
# Enable service
sudo systemctl enable debug-it
sudo systemctl start debug-it

# Configure Nginx
sudo nano /etc/nginx/sites-available/debug-it
```

Add configuration similar to `nginx.conf` provided.

Enable and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/debug-it /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

---

## PythonAnywhere Deployment

### Setup Steps

1. Sign up at pythonanywhere.com
2. Upload code or clone from GitHub
3. Create virtual environment in Web tab
4. Configure Python path and WSGI file
5. Add environment variables
6. Configure PostgreSQL or MySQL database
7. Reload web app

### WSGI Configuration

Create `debug_it_pythonanywhere_com_wsgi.py`:

```python
import os
import sys

path = '/home/yourusername/debug_website'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'debug_it.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

---

## Production Checklist

- [ ] Set `DEBUG = False`
- [ ] Update `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set up HTTPS/SSL certificate
- [ ] Configure email backend
- [ ] Set up database backups
- [ ] Configure static file serving
- [ ] Set up media file handling
- [ ] Configure logging
- [ ] Set up monitoring and alerts
- [ ] Configure security headers
- [ ] Test all functionality
- [ ] Set up CI/CD pipeline
- [ ] Document deployment process

---

## Environment Variables Reference

```env
# Django
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=debug_it_db
DATABASE_USER=debug_user
DATABASE_PASSWORD=your-password
DATABASE_HOST=db.example.com
DATABASE_PORT=5432

# Email
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# AWS S3 (if using)
USE_S3=True
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
```

---

## Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic --noinput
```

### Database errors
```bash
python manage.py migrate
```

### Permission errors
```bash
sudo chown -R user:user /path/to/debug_website
```

### Module not found
```bash
pip install -r requirements.txt
```

---

## Support

For deployment issues, refer to:
- Django Documentation: https://docs.djangoproject.com
- Docker Documentation: https://docs.docker.com
- Heroku Documentation: https://devcenter.heroku.com
- AWS Documentation: https://aws.amazon.com/documentation
