django-project-template
=======================

My personal django project template, for use with django-admin.py&#39;s startproject command.

This is probably not useful as-is to other people, but hopefully it'll give you a starting point for creating your own, similar template.

This includes my base requirements.txt file, as well as my default fabfile for deployments. You'll note that it's set up to pull in my CSS framework, as well.

Here are the basic steps I take to get started with a new Django project:

1. `virtualenv my_project`
2. `cd my_project`
3. `source bin/activate`
4. `pip install Django`
5. `django-admin.py startproject --template=/path/to/project_template/project_name my_project`
6. `cd my_project`
7. `pip install -r requirements.txt`
8. `Configure local environment in fabfile.py`
9. `fab local clone_css_framework`
10. `fab local sync_database`

Once you've done that, you can easily start up Django's built in webserver:

`python manage.py runserver --settings=my_project.settings.local_dev`

