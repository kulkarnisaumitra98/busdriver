from django.db import models

# Create your models here.

# {'timestamp': 1557856014378, 'mocked': False,
# 'coords': {'heading': 0, 'longitude': 73.8508702, 'speed': 0, 'altitude': 0, 'latitude': 18.4534931, 'accuracy': 16}}


# class Location(models.Model):


class Trackie(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    user_id = models.IntegerField()

    def __str__(self):
        return self.name


class Tracker(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    tlatitude = models.FloatField(default=0.0)
    tlongitude = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class PolyLine(models.Model):
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)


class Busdriver(models.Model):
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)