from django.db import models
from 


# Create your models here.
class Location(models.Model):
    place=models.CharField(max_length=50)
    def __str__(self):
        return self.place


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField(upload_to= )
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)