from django.db import models


class Pohodi(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description_small = models.TextField(blank=False)

    def __str__(self):
        return f"{self.title}"


class Budali(models.Model):
    name = models.CharField(max_length=15, blank=False)
    pohodi = models.IntegerField(blank=False)
    image_src = models.CharField(max_length=50, blank=False)


class Images(models.Model):
    image = models.CharField(max_length=255)
    pohod = models.ForeignKey(Pohodi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pohod}"


class Klipove(models.Model):
    pass


