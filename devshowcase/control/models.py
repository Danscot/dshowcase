from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from django.db import models

class CustomUser(AbstractUser):

    description = models.TextField(blank=True, null=True)

    git = models.URLField(blank=True, null=True)

    pict = models.ImageField(upload_to='bg', default='pp.png')

    cover = models.ImageField(upload_to='bg', default='bg.png')

    tech = models.TextField(default='python, javascript')

    def __str__(self):

        return self.username

class Project(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    name = models.CharField(blank=False, max_length=20)

    img = models.ImageField(upload_to='project', default='bg.png')

    description = models.TextField(default='A cool project', max_length=256)

    git = models.URLField(blank=True)

    tech = models.CharField(blank=True, max_length=20)

    likes = models.PositiveIntegerField(default=0)


class Like(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'project')  # Ensure one like per user per project

    def __str__(self):
        return f"{self.user.username} liked {self.project.name}"