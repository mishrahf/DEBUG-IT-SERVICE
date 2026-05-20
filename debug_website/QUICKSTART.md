# DEBUG IT SERVICE - Quick Start Guide

Get your DEBUG IT SERVICE website up and running in 5 minutes!

## Quick Installation (Windows)

### Step 1: Open Terminal/Command Prompt
Navigate to the `debug_website` folder

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database
```bash
python manage.py migrate
```

### Step 5: Create Admin Account
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 6: Load Sample Data (Optional)
```bash
python manage.py seed_data
```

### Step 7: Start Server
```bash
python manage.py runserver
```

## Access Your Website

- **Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **Stop Server**: Press `Ctrl + C` in terminal

## Quick Installation (Mac/Linux)

### Step 1: Open Terminal
Navigate to the `debug_website` folder

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4-7: Same as Windows above

## Adding Content

1. Visit http://localhost:8000/admin
2. Log in with your superuser credentials
3. Add:
   - Services (under "Home" > Services)
   - Service Categories (under "Services" > Service Categories)
   - Projects (under "Portfolio" > Projects)
   - Blog Posts (under "Blog" > Blog Posts)
   - Testimonials (under "Home" > Testimonials)

## File Structure Quick Reference

```
debug_website/
├── templates/          # HTML pages
├── static/            # CSS, JavaScript, images
├── manage.py          # Django management
├── db.sqlite3         # Database (created after migration)
└── requirements.txt   # Python packages
```

## Common Commands

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Deactivate virtual environment
deactivate

# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data
python manage.py seed_data

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Access admin
# Go to http://localhost:8000/admin/
```

## Customization Tips

### Change Brand Color
Edit `static/css/style.css` and change:
```css
--primary-color: #dc3545;  /* Change this */
```

### Update Contact Information
Edit `templates/base.html` and `templates/home/contact.html`:
- Email: info@debugit.com
- Phone: +1 (XXX) XXX-XXXX
- Address: Your City, Country

### Update Company Info
Edit `templates/home/about.html`:
- Company mission
- Vision statement
- Team information

### Customize Home Page
Edit `templates/home/index.html`:
- Hero section text
- Services overview
- Call-to-action buttons

## Troubleshooting

### "command not found: python" or "python is not recognized"
- Make sure Python is installed
- Try `python3` instead of `python`

### "ModuleNotFoundError: No module named 'django'"
- Activate virtual environment: `venv\Scripts\activate`
- Install packages: `pip install -r requirements.txt`

### "Address already in use" port 8000
- The port is being used by another app
- Stop other Django servers or use different port:
  ```bash
  python manage.py runserver 8001
  ```

### Database errors
- Run migrations: `python manage.py migrate`
- Delete `db.sqlite3` and restart (will lose data)

### Admin panel won't load
- Create superuser: `python manage.py createsuperuser`
- Check if you're logged in

## Next Steps

1. ✓ Install and run locally
2. Add your company information
3. Add services and projects
4. Customize colors and fonts
5. Add your contact details
6. Deploy to production (see DEPLOYMENT.md)

## Need Help?

- **Django Documentation**: https://docs.djangoproject.com
- **Bootstrap Documentation**: https://getbootstrap.com/docs
- **Font Awesome Icons**: https://fontawesome.com/icons

---

**Ready to go live?** Check out DEPLOYMENT.md for production setup instructions!
