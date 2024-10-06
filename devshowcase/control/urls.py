
from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    # Add more URL patterns for other pages

    path('login', views.log_in, name='login'),

    path('signin', views.signin, name='signin'),

    path('profile', views.profile, name='profile'),

    path('logout/', views.logout, name='logout'),


]