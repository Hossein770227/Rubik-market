from django.contrib import admin

from shop.models import Category

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass
