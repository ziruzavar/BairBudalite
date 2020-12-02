from django.contrib.auth.models import User
from django.db import models


class Pohodi(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return f"{self.title}"


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
They are connected to the Pohod with ForeignKey
"""
class Images(models.Model):
    image = models.CharField(max_length=255)
    pohod = models.ForeignKey(Pohodi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pohod}"


class Klipove(models.Model):
    pass


"""
Model fot the comments,  it is connected to
the Pohod with ForeignKey
"""
class Comment(models.Model):
    comment = models.TextField()
    pohod = models.ForeignKey(Pohodi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pohod}"
