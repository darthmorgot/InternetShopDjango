from django.db import models
from django.urls import reverse

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


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products',
                                 verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
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
