from django.utils.translation import gettext as _
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',)  


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand','category', 'price_with_discount', 'rating_display', 'release_date')  
    list_filter = ('brand', 'rating')  
    search_fields = ('title', 'category__name')  
    prepopulated_fields = {'slug': ('title',)}  

    def rating_display(self, obj):
        return obj.rating.replace('⭐', '⭐')  

    rating_display.short_description = _("Rating") 
