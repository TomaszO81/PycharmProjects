from django.db import models

class Films(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    director = models.CharField(max_length=100)
