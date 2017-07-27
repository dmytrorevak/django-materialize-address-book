from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, blank=False)
    surname = models.CharField(max_length=30, blank=False)
    age = models.PositiveIntegerField(null=False)
    phone_number = models.IntegerField(null=False)
    # avatar = models.ImageField(upload_to='avatars/')
    address = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name
