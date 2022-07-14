from django.contrib import admin
from django.urls import path, re_path

from blog.views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('about/', about, name='about'),
    path('themes/<slug:theme>', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
