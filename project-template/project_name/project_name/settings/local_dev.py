from __init__ import *

# Debugging
DEBUG = True

# WSGI
WSGI_APPLICATION = '{{ project_name }}.wsgi.local_dev.application'

# Databases
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': '../db/{{ project_name }}.db',    # Or path to database file if using sqlite3.
  }
}

# Caching
CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
  }
}

# Compressor
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False