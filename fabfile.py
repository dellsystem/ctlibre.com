from fabric.api import local


def up():
    local('python manage.py runserver')
