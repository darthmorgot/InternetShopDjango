from django.contrib import admin

from account.models import User


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('email', 'password')}),
        ('Персональные данные', {'fields': ('first_name', 'last_name')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Временные метки', {'fields': ('last_login', 'date_joined')}),
    ]

    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['pk']


admin.site.register(User, UserAdmin)

admin.site.site_header = 'Админ-панель интернет-магазина VeloSam'
admin.site.site_title = 'Админ-панель интернет-магазина VeloSam'
admin.site.index_title = 'Администрирование интернет-магазина VeloSam'
