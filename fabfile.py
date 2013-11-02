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
