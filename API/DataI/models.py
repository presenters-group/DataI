import os

from django.db import models

# Create your models here.

class Document(models.Model):
  path = 'uploads/'

  docfile = models.FileField(upload_to=path)

class SVGDocument(models.Model):
  path = 'uploads/svg/'

  docfile = models.FileField(upload_to=path)

