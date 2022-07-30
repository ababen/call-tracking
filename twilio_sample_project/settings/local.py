'''
Local settings

- Run in Debug mode
'''

from .common import *  # noqa

# Allow all hosts, so we can run on PaaS's like Heroku
ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]', '2107-2601-582-8500-5640-8d81-c3a4-c530-6bde.ngrok.io']

# Use DEBUG for local development
DEBUG = True

DJANGO_TWILIO_FORGERY_PROTECTION = False

CSRF_TRUSTED_ORIGINS = ['*']