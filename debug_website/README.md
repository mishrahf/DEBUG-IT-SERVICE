# DEBUG IT SERVICE - Website

A professional website for DEBUG IT SERVICE, an IT software services company specializing in SaaS and AI agentic projects.

## Built With

- **Backend**: Django 4.2
- **Frontend**: HTML5, Bootstrap 5, CSS3
- **Database**: SQLite (Development), PostgreSQL (Production)
- **Icons**: Font Awesome 6
- **Version Control**: Git

## Features

- **Home Page**: Attractive landing page with services overview and featured projects
- **About Page**: Company information, mission, vision, and team details
- **Services**: Comprehensive service listings with detailed descriptions
- **Portfolio**: Showcase of completed and ongoing projects
- **Blog**: Article management system with tags and author information
- **Contact**: Contact form with business hours and location
- **Fully Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- **Admin Panel**: Django admin interface for content management

## Project Structure

```
debug_website/
├── debug_it/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── home/                  # Home app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── __init__.py
├── services/              # Services app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── __init__.py
├── portfolio/             # Portfolio app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── __init__.py
├── blog/                  # Blog app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── __init__.py
├── templates/             # HTML templates
│   ├── base.html
│   ├── home/
│   ├── services/
│   ├── portfolio/
│   └── blog/
├── static/                # Static files (CSS, JS, images)
│   └── css/
│       └── style.css
├── media/                 # User uploaded files
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Installation & Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone or Download the Project

```bash
cd debug_website
```

### Step 2: Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 6: Collect Static Files (Optional but Recommended)

```bash
python manage.py collectstatic
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000/` in your browser.

## Admin Panel Access

Access the Django admin panel at `http://localhost:8000/admin/` using your superuser credentials.

From the admin panel, you can:
- Manage services and service categories
- Add and edit portfolio projects
- Create and publish blog posts
- Add client testimonials
- View and manage other content

## Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Settings File

Edit `debug_it/settings.py` to:
- Change the SECRET_KEY for production
- Set DEBUG to False in production
- Configure email settings for contact forms
- Set up static and media file paths

## Adding Sample Data

1. Go to Django admin (`http://localhost:8000/admin/`)
2. Create Service Categories under Services
3. Add Services under each category
4. Create Portfolio Projects
5. Publish Blog Posts
6. Add Testimonials

## Customization

### Brand Colors

Edit `static/css/style.css` and modify the `:root` CSS variables:

```css
:root {
    --primary-color: #dc3545;  /* Change this to your brand color */
    --dark-color: #212529;
    --light-color: #f8f9fa;
    --border-radius: 0.5rem;
    --transition: all 0.3s ease;
}
```

### Contact Information

Update contact details in:
- `templates/base.html` (footer)
- `templates/home/contact.html` (contact page)

### Company Information

Update company information in:
- `templates/home/about.html` (About page)
- `templates/base.html` (Footer)

## Deployment

### For Production:

1. Set `DEBUG = False` in `settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Use PostgreSQL instead of SQLite
4. Set up proper email configuration
5. Use environment variables for sensitive data
6. Collect static files: `python manage.py collectstatic`
7. Use a production WSGI server like Gunicorn

### Example Production Deployment with Gunicorn:

```bash
gunicorn debug_it.wsgi:application --bind 0.0.0.0:8000
```

## Security Checklist

- [ ] Change SECRET_KEY in production
- [ ] Set DEBUG to False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up HTTPS
- [ ] Configure CSRF settings
- [ ] Set up email backend for contact forms
- [ ] Use environment variables for sensitive data
- [ ] Enable CORS only for trusted domains
- [ ] Set up proper database backups

## API Endpoints

- `/` - Home page
- `/about/` - About page
- `/contact/` - Contact page
- `/services/` - Services list
- `/services/detail/<id>/` - Service detail
- `/portfolio/` - Portfolio list
- `/portfolio/project/<id>/` - Project detail
- `/blog/` - Blog list
- `/blog/post/<slug>/` - Blog post detail
- `/admin/` - Admin panel

## Troubleshooting

### Issue: Static files not loading

**Solution**: Run `python manage.py collectstatic` and check STATIC_ROOT and STATIC_URL settings.

### Issue: Images not displaying

**Solution**: Ensure MEDIA_ROOT and MEDIA_URL are properly configured in settings.py.

### Issue: Database error

**Solution**: Run `python manage.py migrate` to apply all migrations.

### Issue: Admin page not accessible

**Solution**: Create a superuser with `python manage.py createsuperuser`.

## Contributing

1. Create a new branch for features
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or feature requests, please contact:
- Email: info@debugitservice.com
- Website: https://debugitservice.com

## Authors

- **DEBUG IT SERVICE Development Team**

---

**Last Updated**: April 2026
**Django Version**: 4.2.0
**Bootstrap Version**: 5.3.0
**Font Awesome Version**: 6.4.0
