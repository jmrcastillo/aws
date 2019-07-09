

from .base import *
import os

DEBUG = False

# security warning: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['ec2-34-207-140-110.compute-1.amazonaws.com']

DATABASES = {
    'default': {
    'engine': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'blog',
    'USER': 'postgres',
    'PASSWORD': 'ichoose',
    'HOST': '127.0.0.1',
    'PORT': '5432'
    }
}

