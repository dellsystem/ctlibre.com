from fabric.api import local


def up():
    local('python manage.py runserver')

def loadfr():
    local('django-admin.py compilemessages')

def makefr():
    local('django-admin.py makemessages -l fr')
