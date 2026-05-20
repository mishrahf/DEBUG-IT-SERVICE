#!/usr/bin/env python
"""
Setup script for DEBUG IT SERVICE website
This script helps with initial setup and configuration
"""

import os
import sys
import django

def setup_project():
    """Initial project setup"""
    print("=" * 60)
    print("DEBUG IT SERVICE - Project Setup")
    print("=" * 60)
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debug_it.settings')
    django.setup()
    
    from django.core.management import call_command
    
    print("\n1. Running migrations...")
    call_command('migrate')
    
    print("\n2. Creating superuser (admin account)...")
    call_command('createsuperuser')
    
    print("\n3. Collecting static files...")
    call_command('collectstatic', verbosity=0, interactive=False)
    
    print("\n" + "=" * 60)
    print("Setup Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Run: python manage.py runserver")
    print("2. Visit: http://localhost:8000")
    print("3. Admin Panel: http://localhost:8000/admin")
    print("\nStart adding your content in the admin panel!")
    print("=" * 60)

if __name__ == '__main__':
    setup_project()
