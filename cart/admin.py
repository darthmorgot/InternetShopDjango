from django.contrib import admin

from cart.models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'cost', 'date_creation']


admin.site.register(Cart, CartAdmin)
