import os

from django.db import models

# Create your models here.

class Document(models.Model):
  dirName = os.path.dirname(__file__)
  filename = os.path.join(dirName, '../')
  filename = filename[1:]
  path = 'uploaded/'
  docfile = models.FileField(upload_to=path)
