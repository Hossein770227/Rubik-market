from django.utils.translation import gettext as _
from django.contrib import admin
from .models import Brand, Phone, Laptop, LaptopBrand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',)  


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price_with_discount', 'rating_display', 'release_date')  
    list_filter = ('brand', 'rating')  
    search_fields = ('title', 'brand__name')  
    prepopulated_fields = {'slug': ('title',)}  

    def rating_display(self, obj):
        return obj.rating.replace('⭐', '⭐')  

    rating_display.short_description = _("Rating") 


# laptop admin

@admin.register(LaptopBrand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',)  


@admin.register(Laptop)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price_with_discount', 'rating_display', 'release_date')  
    list_filter = ('brand', 'rating')  
    search_fields = ('title', 'brand__name')  
    prepopulated_fields = {'slug': ('title',)}  

    def rating_display(self, obj):
        return obj.rating.replace('⭐', '⭐')  

    rating_display.short_description = _("Rating") 

