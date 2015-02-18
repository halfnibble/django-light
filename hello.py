import sys

"""
Settings
========
Would normally go in project_app/settings.py
"""
from django.conf import settings

settings.configure(
    DEBUG = True,
    SECRET_KEY = 'yourrandomsecretkey',
    ROOT_URLCONF = __name__,
    MIDDLEWARE_CLASSES = (),
)

"""
Views
=====
Would normally go in app/views.py
"""
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

"""
URLs
====
The root URL config normally goes in project_app/urls.py
"""
from django.conf.urls import url

urlpatterns = (
    url(r'^$', index),
)

"""
Manage.py
=========
Some setup code typically found in manage.py
"""
if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
