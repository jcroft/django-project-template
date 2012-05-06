django-project-template
=======================

My personal django project template, for use with django-admin.py&#39;s startproject command.

Here are the basic steps I take to get started with a new Django project:

1. virtualenv my_project
2. workon my_project
3. pip install Django 
4. django-admin.py startproject --template=/path/to/project_template/project_name my_project
5. cd my_project
6. pip install -r requirements.txt
7. Configure local environment in fabfile.py
8. fab local clone_css_framework
9. fab local sync_database
10. python manage.py runserver --settings=testproject.settings.local_dev