from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='E-mail')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# class Address(models.Model):
#     pass
