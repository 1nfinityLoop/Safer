from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.CharField(max_length=100)
    date_begin = models.DateField()
    date_end = models.DateField()
    pays = models.CharField(max_length=10)
    ville = models.CharField(max_length=10)
    adress = models.TextField()
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to='image_pro')


class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    type_food = models.CharField(max_length=100)
    rate = models.IntegerField()
    pays = models.CharField(max_length=10)
    ville = models.CharField(max_length=10)
    adress = models.TextField()
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to='image_pro')




class Place(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pays = models.CharField(max_length=10)
    ville = models.CharField(max_length=10)
    adress = models.TextField()
    image = models.ImageField(upload_to='image_pro')

