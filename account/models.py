from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name='E-mail')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Address(models.Model):
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=6, verbose_name='Номер дома')
    city = models.CharField(max_length=100, verbose_name='Город/Населенный пункт')
    region = models.CharField(max_length=100, verbose_name='Регион')
    post_code = models.CharField(max_length=6, verbose_name='Почтовый индекс')
    phone_validator = RegexValidator(regex=r'(?:(?:8|\+7)[\- ]?)?(?:\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}',
                                     message='Введен неверный номер телефона')
    phone = models.CharField(max_length=16, validators=[phone_validator], verbose_name='Телефон')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='addresses', verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
