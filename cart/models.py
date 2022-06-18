from django.db import models

from account.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='cart_users', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='cart_products', verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    cost = models.PositiveIntegerField(default=0, blank=True, verbose_name='Общая стоимость')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'Корзина для {self.user.first_name} {self.user.last_name} | Продукт {self.product.name}'

    def save(self, *args, **kwargs):
        if not self.cost:
            self.cost = self.product.price * self.quantity
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ['-date_creation']
