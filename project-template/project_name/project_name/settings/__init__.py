import os, sys, datetime

##### PATH SETTINGS ###########################################################

# Project root
PROJECT_ROOT = "%s%s" % (os.path.realpath(os.path.dirname(__file__)), "/../")

# Additional Python paths
sys.path.append(os.path.join(PROJECT_ROOT, 'lib'))


##### CORE SETTINGS ###########################################################

# People
ADMINS = (
    ('Jeff Croft', 'jeff@thirdavenuedesign.com'),
)
MANAGERS = ADMINS


# Locale
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'

# Site
SITE_ID = 1
SECRET_KEY = '{{ secret_key }}'


# Internationalization/Localization
USE_I18N = True
USE_L10N = True
USE_TZ = True

# URLs
ROOT_URLCONF = '{{ project_name }}.urls'

# Authentication
LOGIN_URL = '/sign-in/'
LOGOUT_URL = '/sign-out/'
LOGIN_REDIRECT_URL = '/'


# Static configuration
STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Template configuration
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  #'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.debug',
  'django.core.context_processors.i18n',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  'django.core.context_processors.tz',
  'django.core.context_processors.request',
  'django.contrib.messages.context_processors.messages',
)

# Middleware
MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  # Uncomment the next line for simple clickjacking protection:
  # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'jeffcroft.middleware.exceptions.UserBasedExceptionMiddleware',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Applications
INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.admin',
  'django.contrib.humanize',
  'django.contrib.markup',

  'south',
  'compressor',
  'typogrify',
  'sorl.thumbnail',
)




##### PRODUCTION ENVIROMENT SETTINGS ##########################################

# Debugging
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Environment
DEPLOYMENT_ENV = 'production'

# WSGI
WSGI_APPLICATION = '{{ project_name }}.wsgi.production.application'

# Databases
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': '{{ project_name }}',           # Or path to database file if using sqlite3.
    'USER': '',                             # Not used with sqlite3.
    'PASSWORD': '',                         # Not used with sqlite3.
    'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
  }
}

# Caches
CACHES = {
  'default' : {
    'BACKEND':    'django.core.cache.backends.memcached.MemcachedCache',
    'LOCATION':   ['127.0.0.1:11211'],
    'KEY_PREFIX': '{{ project_name }}_production',
  }
}

# E-mail
EMAIL_HOST          = ''
EMAIL_HOST_USER     = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS       = True
DEFAULT_FROM_EMAIL  = ''
SERVER_EMAIL        = ''
REPLY_EMAIL         = ''
EMAIL_SUBJECT_PREFIX= ''

# Static files
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'compressor.finders.CompressorFinder',
)

# User-uploaded media
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media') + '/'
MEDIA_URL = STATIC_URL + 'media/'

# Templates
TEMPLATE_DIRS = (
  os.path.join(PROJECT_ROOT, 'templates'),
)

# Django compressor
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_PRECOMPILERS = (
  ('text/x-sass', 'sass {infile} {outfile}'),
)
COMPRESS_CSS_FILTERS = (
  'compressor.filters.css_default.CssAbsoluteFilter',
  'compressor.filters.cssmin.CSSMinFilter',
)
COMPRESS_OFFLINE = True


# Rackspace Cloud Files Storage

DEFAULT_FILE_STORAGE      = 'cumulus.storage.CloudFilesStorage'
CUMULUS_USERNAME          = ''
CUMULUS_API_KEY           = ''
CUMULUS_CONTAINER         = ''
CUMULUS_TIMEOUT           = 15

CUMULUS_STATIC_CONTAINER  = ''
CUMULUS_USE_SERVICENET    = True
CUMULUS_FILTER_LIST       = []

# Thumbnails
THUMBNAIL_STORAGE         = 'cumulus.storage.CloudFilesStorage'