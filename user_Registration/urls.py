from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url('^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/login.html'}, name='logout'),
    url(r'^register/', views.register, name='register'),

]
