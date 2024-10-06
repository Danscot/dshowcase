from django.contrib import admin

from .models import CustomUser, Project

# Register your models here.

admin.site.register(CustomUser)

admin.site.register(Project)