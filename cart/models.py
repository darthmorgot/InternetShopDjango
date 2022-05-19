from django.db import models

# from account.models import User
from products.models import Product


class Cart(models.Model):
    pass
#     # user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Продукт')
#     quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
#     date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#
#     def __str__(self):
#         return f'Корзина для user | Продукт {self.product.name}'
