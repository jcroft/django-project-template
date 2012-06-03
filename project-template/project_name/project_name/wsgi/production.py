import os
import site
import sys

# Configure the paths for our virtualenv.
site.addsitedir('/home/jcroft/Development/Python/_VirtualEnvs/{{ project_name }}/lib/python2.7/site-packages')
sys.path.insert(0, '/home/jcroft/Development/Python/_VirtualEnvs/{{ project_name }}/lib/python2.7/site-packages')
sys.path.insert(0, '/home/jcroft/Development/Python/_VirtualEnvs/{{ project_name }}/{{ project_name }}')

# Configure the DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

# Reference the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
