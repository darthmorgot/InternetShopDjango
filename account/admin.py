from django.contrib import admin

from account.models import User, Address


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('email', 'password', 'username')}),
        ('Персональные данные', {'fields': ('first_name', 'last_name')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Временные метки', {'fields': ('last_login', 'date_joined')}),
    ]

    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['pk']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'street', 'house_number', 'region', 'post_code']


admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)

admin.site.site_header = 'Админ-панель интернет-магазина VeloSam'
admin.site.site_title = 'Админ-панель интернет-магазина VeloSam'
admin.site.index_title = 'Администрирование интернет-магазина VeloSam'
