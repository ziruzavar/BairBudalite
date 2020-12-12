from django.contrib.auth.models import User
from django.db import models

from budalite_authentication.models import UserProfile

"""
Model for our hikes
"""
class Pohodi(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return f"{self.title}"


"""
Model for our Mountain projects
"""
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    done = models.BooleanField(default=False)
    first_image = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
"""
Model for our People, who come to our hikes.
"""
class Budali(models.Model):
    name = models.CharField(max_length=15, blank=False)
    pohodi = models.IntegerField(blank=False)
    image_src = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.name


"""
Model for the images.
You can add new images within the admin page
They are connected to the Pohod and Project with ForeignKey
"""
class Images(models.Model):
    image = models.CharField(max_length=255)
    pohod = models.ForeignKey(Pohodi, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.pohod:
            return f"{self.pohod}"
        return f"{self.project}"


class Klipove(models.Model):
    pass


"""
Model fot the comments,  it is connected to
the Pohod with ForeignKey
"""
class Comment(models.Model):
    comment = models.TextField()
    pohod = models.ForeignKey(Pohodi, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pohod}-{self.user_profile.user.username}"

