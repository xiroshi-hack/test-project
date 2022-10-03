from email.policy import default
from operator import mod
from pyexpat import model
from statistics import mode
from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Title(models.Model):
    text = models.CharField(max_length=70)
    btn = models.CharField(max_length=30)
    
class Abaout(models.Model):
    title = models.CharField(max_length=30, default="abaut page")
    text = models.CharField(max_length=300, default="your text here")
    btn = models.CharField(max_length=20, default="click here")
    
    
class Expertises(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField()
    text = models.CharField(max_length=200)
    
    
class Products(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=70)
    
    
class Testmonials(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    develop = models.CharField(max_length=70)