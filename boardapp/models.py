from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class BoardModel(models.Model):
    #title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    #sns_image = models.ImageField(upload_to='',null=True, blank=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.TextField(null=True, blank=True)