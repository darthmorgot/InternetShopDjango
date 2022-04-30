from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Product, Category


class CustomMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20
    list_display = ['tree_actions', 'indented_title']
    list_display_links = ['indented_title']


admin.site.register(Product)
admin.site.register(Category, CustomMPTTModelAdmin)
