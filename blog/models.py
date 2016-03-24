from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Spot(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()
    date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    lnglat = models.CharField(max_length=50, blank=True, null=True)

    @property
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]

    @property
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[1]

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=200)


