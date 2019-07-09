

from .base import *
import os

DEBUG = True

# security warning: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
    # 'default': {
    # 'engine': 'django.db.backends.postgresql_psycopg2',
    # 'NAME': 'blog',
    # 'USER': 'postgres',
    # 'PASSWORD': 'ichoose',
    # 'HOST': '127.0.0.1',
    # 'PORT': '5432'
    # }
# }

