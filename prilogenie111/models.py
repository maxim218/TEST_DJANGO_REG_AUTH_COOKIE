from django.db import models
from django.utils import timezone

class Town(models.Model):
    town_name = models.TextField()
    country = models.ForeignKey('Country')
    def __str__(self):
        return self.town_name


class Country(models.Model):
    country_name = models.TextField()
    def __str__(self):
        return self.country_name
