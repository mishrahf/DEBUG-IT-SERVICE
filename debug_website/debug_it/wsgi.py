"""
WSGI config for debug_it project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'debug_it.settings')

application = get_wsgi_application()
