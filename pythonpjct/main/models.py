from django.db import models

# Create your models here.
class registration(models.Model):
    name        =   models.CharField(max_length=100,unique=True)
    password    =   models.CharField(max_length=100)
class test(models.Model):
    name        =   models.CharField(max_length=100,unique=True)
    password    =   models.CharField(max_length=100)