"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'user'

urlpatterns = [
    path(r'login', auth_views.login, {'template_name': 'user/login.html'},
         name='login'),
    path(r'logout', auth_views.logout, {'template_name': 'user/logout.html'},
         name='logout'),
    path(r'register/', register_view, name='register'),
    path(r'create/', create_view, name='create'),
    url(r'article/(?P<id>\d+)/$', article_view, name='article'),
    path(r'', index_view, name='index'),
]
