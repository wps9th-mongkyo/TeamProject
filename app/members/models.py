from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    img_profile = models.ImageField(upload_to='user', blank=True)
    phone = models.PositiveIntegerField(max_length=13)
    reviews = models.TextField(blank=True)


class Restaurant:
    pass