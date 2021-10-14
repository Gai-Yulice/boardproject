from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class ChatModel(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()