from django.db import models


class Noise(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    decibels = models.FloatField()
    frequency = models.FloatField()
    datetime = models.DateTimeField()

    def __str__(self):
        return f"Noise at ({self.latitude}, {self.longitude})"
