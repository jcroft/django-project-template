from __init__ import *

# Debugging
DEBUG = False

# WSGI
WSGI_APPLICATION = '{{ project_name }}.wsgi.local_dev.application'

# Enviroment
DEPLOYMENT_ENV = 'staging'

# Debug toolbar
INTERNAL_IPS = ('',)
DEBUG_TOOLBAR_CONFIG = {
  'INTERCEPT_REDIRECTS': False,
  'HIDE_DJANGO_SQL': True,
}
MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES)
MIDDLEWARE_CLASSES += (
  'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Caching
CACHES['default']['KEY_PREFIX'] = '{{ project_name }}_staging'

# Compressor
COMPRESS = True