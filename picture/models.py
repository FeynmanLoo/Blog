from django.db import models
# Create your models here.
import time
from . import utils

class Image(models.Model):
    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    size = models.IntegerField()
    content_type = models.CharField(max_length=255, blank=True)
    host = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    img = models.ImageField(upload_to=utils.path_and_rename(time.strftime("images/%Y/%m/%d")))

    def __str__(self):
        return self.name
