from django.db import models


class User(models.Model):

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    phone_number = models.IntegerField()
    avatar = models.ImageField(upload_to='avatars/')
    address = models.CharField(max_length=100)
