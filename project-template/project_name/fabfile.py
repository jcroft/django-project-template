from fabric.api import env, run, sudo
from fabric.context_managers import cd, hide
from fabric.contrib.files import exists
from fabric.colors import *

# Project configuration - set to your project name.
PROJECT_NAME                = '{{ project_name }}'
PROJECT_APP_REPO            = 'git@github.com:jcroft/{{ project_name }}.git'
PROJECT_CSS_FRAMEWORK_REPO  = 'git@github.com:jcroft/jeffcroft-css-framework-v2.git'

# Deployment environments  - add as many as necessary.
def production():
  config = {
    'name':             'production',           # A name for this environment
    'host':             '',                     # The host we'll be SSHing to
    'web_hostname':     '',                     # The domain name for this web site/app
    'username':         '',                     # Your username on the SSH host
    'password':         '',                     # Your password on the SSH host
    'virtualenv':       '{{ project_name }}',   # The name for this virtualenv
    'virtualenvs_dir':  '',                     # The path to your virtualenvs directory
  }
  environment(config)


def staging():
  config = {
    'name':             'staging',
    'host':             '',
    'web_hostname':     '',
    'username':         '',
    'password':         '',
    'virtualenv':       '{{ project_name }}',
    'virtualenvs_dir':  '',
  }
  environment(config)


def local():
  config = {
    'name':             'local',
    'host':             'localhost',
    'web_hostname':     '',                       # Leave blank for local environment, we'll just use Django's built-in server
    'username':         '',
    'password':         '',
    'virtualenv':       '',
    'virtualenvs_dir':  '',
  }
  environment(config)



# Deployment tasks - call these from the fab command.
def deploy():
  """
  Deploys the app.
  """
  activate_virtualenv()
  update_css_framework()
  update_app()
  restart_apache()
  collect_static()
  compress_static()


def full_deploy():
  """
  Deploys the app, but runs some additional stuff that we don't need to do often.
  """
  activate_virtualenv()
  update_css_framework()
  update_app()
  update_requirements()
  sync_database()
  run_migrations()
  restart_apache()
  collect_static()
  compress_static()


def initial_deploy():
  """
  Does a full deploy of the app, but first sets up the environment on the remote server.
  """
  create_virtualenv()
  clone_app()
  clone_css_framework()
  configure_apache()
  configure_nginx()
  restart_nginx()
  full_deploy()




# Utility functions - you shouldn't need to modify these.
def environment(config):
  """
  Sets up an environment.
  """
  env.hosts           = [config['host']]
  env.user            = config['username']
  env.password        = config['password']

  global ENVIROMENT
  global VIRTUALENVS_DIR
  global VIRTUALENV_NAME
  global PATH_TO_VIRTUALENV
  global PATH_TO_GIT_REPO
  global HOSTNAME
  ENVIROMENT          = config['name']
  VIRTUALENV_NAME     = config['virtualenv']
  VIRTUALENVS_DIR     = config['virtualenvs_dir']
  PATH_TO_VIRTUALENV  = '%s/%s' % (VIRTUALENVS_DIR, VIRTUALENV_NAME)
  PATH_TO_GIT_REPO    = '%s/%s' % (PATH_TO_VIRTUALENV, PROJECT_NAME)
  HOSTNAME            = config['web_hostname']


def create_virtualenv():
  """
  Creates a new virtualenv for the project
  """
  print(green('\nCreating the virtualenv...'))

  # Create the virtualenv itself
  if not exists(PATH_TO_VIRTUALENV):
    with cd(VIRTUALENVS_DIR):
      run('virtualenv %s' % VIRTUALENV_NAME)
  else:
    print(red('virtualenv already exists.'))

  # Add a logs directory to it for web logs
  LOG_PATH = PATH_TO_VIRTUALENV + '/logs'
  if not exists(LOG_PATH):
    with cd(PATH_TO_VIRTUALENV):
      run('mkdir logs')
  else:
    print(red('logs directory already exists.'))


def activate_virtualenv():
  """
  Activates the virtualenv.
  """
  with cd(PATH_TO_VIRTUALENV):
    with hide('running'):
      run('source bin/activate')


def update_requirements():
  """
  Runs 'pip install -r requirements.txt', updating/installing any dependencies.
  """
  print(green('\nUpdating the dependencies for the app...'))
  with cd(PATH_TO_GIT_REPO):
    run('%s/bin/pip install -r requirements.txt' % PATH_TO_VIRTUALENV)


def clone_css_framework():
  print(green('\nCloning the CSS framework from its git repository...'))
  CSS_FRAMEWORK_PATH = PATH_TO_VIRTUALENV + '/css-framework'
  if not exists(CSS_FRAMEWORK_PATH):
    with cd(PATH_TO_VIRTUALENV):
      run('git clone %s css-framework' % PROJECT_CSS_FRAMEWORK_REPO)
  else:
    print(red('Git repo has already been cloned'))  


def update_css_framework():
  """
  Updates the CSS framework from git and touches the files in it to ensure
  django-compressor will re-compile them.
  """
  print(green('\nUpdating the CSS framework from its git repository...'))
  CSS_FRAMEWORK_PATH = PATH_TO_VIRTUALENV + '/css-framework'
  with cd(CSS_FRAMEWORK_PATH):
    run('git pull')
    run('find . -exec touch {} \;')


def clone_app():
  print(green('\nCloning the app from its git repository...'))
  if not exists(PATH_TO_GIT_REPO):
    with cd(PATH_TO_VIRTUALENV):
      run('git clone %s' % PROJECT_APP_REPO) 
  else:
    print(red('Git repo has already been cloned'))


def update_app():
  print(green('\nUpdating the app from its git repository...'))
  with cd(PATH_TO_GIT_REPO):
    run('git pull')


def configure_apache():
  """
  Configures Apache.
  """
  print(green('\nConfiguring Apache...'))
  if not exists('/etc/apache2/sites-available/%s' % HOSTNAME):
    with cd('/etc/apache2/sites-available'):
      sudo('ln -s %s/deployment/%s.apache_conf %s' % (PATH_TO_GIT_REPO, ENVIROMENT, HOSTNAME))
    with cd('/etc/apache2/sites-enabled'):
      sudo('ln -s ../sites-available/%s %s' % (HOSTNAME, HOSTNAME))
  else:
    print(red('Apache is already configured for %s.' % HOSTNAME))


def restart_apache():
  """
  Restarts Apache.
  """
  print(green('\nRestarting Apache...'))
  sudo('sudo /etc/init.d/apache2 stop')
  sudo('sudo /etc/init.d/apache2 start')


def configure_nginx():
  """
  Configures nginx.
  """
  print(green('\nConfiguring nginx...'))
  if not exists('/etc/nginx/sites-available/%s' % HOSTNAME):
    with cd('/etc/nginx/sites-available'):
      sudo('ln -s %s/deployment/%s.nginx_conf %s' % (PATH_TO_GIT_REPO, ENVIROMENT, HOSTNAME))
    with cd('/etc/nginx/sites-enabled'):
      sudo('ln -s ../sites-available/%s %s' % (HOSTNAME, HOSTNAME))
  else:
    print(red('nginx is already configured for %s.' % HOSTNAME))


def restart_nginx():
  """
  Restarts nginx.
  """
  print(green('\nRestarting nginx...'))
  sudo('sudo /etc/init.d/nginx stop')
  sudo('sudo /etc/init.d/nginx start')


def manage(command):
  """
  Runs a manage.py command.
  """
  activate_virtualenv()
  print(cyan('\'manage.py %s\'' % command))
  with cd(PATH_TO_GIT_REPO):
    run('%s/bin/python manage.py %s' % (PATH_TO_VIRTUALENV, command))


def compress_static():
  """
  Runs django-compressor's compress command, compiling and compressing any
  static files.
  """
  print(green('\nCompressing static files...'))
  with cd('%s/%s/static/assets/' % (PATH_TO_GIT_REPO, PROJECT_NAME)):
    run('find . -exec touch {} \;')
  manage('compress --force')


def sync_database():
  """
  Runs syncdb for the app.
  """
  print(green('\nRunning syncdb...'))
  manage('syncdb')


def run_migrations():
  """
  Runs south migrations for the app.
  """
  print(green('\nRunning database migrations...'))
  manage('migrate')


def collect_static():
  """
  Runs collectstatic for the app.
  """
  print(green('\nCollecting static files...'))
  manage('collectstatic --noinput')



