from django.contrib import admin

from shop.models import CategoryDigitalProducts, ProductsTypeDigital, ProductsDigital


@admin.register(CategoryDigitalProducts)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title',] 
    search_fields = ['title'] 
    list_filter = ['title']  
    list_per_page = 10  


@admin.register(ProductsTypeDigital)
class ProductTypeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','group'] 
    search_fields = ['name', 'group'] 
    list_filter = ['name'] 
    list_per_page = 10  


@admin.register(ProductsDigital)
class ProductTypeCategoryAdmin(admin.ModelAdmin):
    list_display = ['digital_group','type_product', 'type', 'title', 'price'] 
    search_fields = ['title', 'type' ,'type_product'] 
    list_filter = ['title','type_product'] 
    list_per_page = 10     