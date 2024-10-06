
from django.urls import path

from . import views

urlpatterns = [

    # Add more URL patterns for other pages

    path('login', views.log_in, name='login'),

    path('signin', views.signin, name='signin'),

    path('profile', views.profile, name='profile')


]