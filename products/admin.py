from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category, Product, Image


class CustomMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20
    list_display = ['tree_actions', 'indented_title']
    list_display_links = ['indented_title']


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    max_num = 4


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(Product, ProductAdmin)
