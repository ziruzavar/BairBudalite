from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_images')
    description = models.TextField(max_length=150, default='Няма информация')
    instagram = models.URLField(blank=True)

    def __str__(self):
        return f'{self.user.username} {self.user.email}'
