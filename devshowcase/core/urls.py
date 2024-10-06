from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.main, name='main'),

    # User profile page
    path('p/<str:username>/', views.profile, name='p'),

    # Like a project
    path('like/<int:project_id>/', views.like_project, name='like_project'),

    # Add more URL patterns for other pages as needed
]
