from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='E-mail')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='Телефон')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


# class Address(models.Model):
#     pass
