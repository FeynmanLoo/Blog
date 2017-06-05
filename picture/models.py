from django.db import models

# Create your models here.

class image(models.Model):
    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    size = models.IntegerField()
    type = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name