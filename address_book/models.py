from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):

    user = models.ManyToManyField(User)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    age = models.PositiveIntegerField() 
    phone_number = models.IntegerField()
    # avatar = models.ImageField(upload_to='avatars/')
    address = models.CharField(max_length=100)
    description = models.TextField()
