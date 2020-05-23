from django.db import models 

# Create your models here.
class Location(models.Model):
    place=models.CharField(max_length=50)
    def __str__(self):
        return self.place
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
    @classmethod
    def update(cls,id,name):
        location = Location.objects.filter(id=id)
        location.update(place=name)


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
