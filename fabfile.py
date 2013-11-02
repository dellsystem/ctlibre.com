from fabric.api import local


def up():
    local('python manage.py runserver')

def loadfr():
    local('django-admin.py compilemessages')

def makefr():
    local('django-admin.py makemessages -l fr')

def less():
    local('lessc static/css/ctlibre.less -x > static/css/ctlibre.css')
    local('lessc static/css/mobile.less -x > static/css/mobile.css')

def static():
    local('python manage.py collectstatic --noinput')

def restart():
    local('kill -HUP `cat /tmp/gunicorn.pid`')
