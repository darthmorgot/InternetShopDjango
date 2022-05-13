from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Родительская')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_by_category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    class MPTTMeta:
        order_insertion_by = ['name']


def upload_product_image(instance, filename):
    return f'product_images/{instance.slug}/{filename}'


def validate_range(value):
    if value > 100:
        raise ValidationError('Размер скидки не может быть больше 100%')


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    discount = models.PositiveIntegerField(default=0, validators=[validate_range], verbose_name='Скидка, %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products',
                                 verbose_name='Категория')
    image = models.ImageField(upload_to=upload_product_image, verbose_name='Картинка', null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    def get_discount_price(self):
        return int(self.price - (self.price * self.discount / 100))

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']


def upload_gallery_image(instance, filename):
    return f'product_images/{instance.product.slug}/{filename}'


class Image(models.Model):
    image = models.ImageField(upload_to=upload_gallery_image, verbose_name='Картинка')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'
        ordering = ['id']
