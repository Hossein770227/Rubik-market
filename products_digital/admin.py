from django.contrib import admin
from .models import DigitalRadio
from django.utils.translation import gettext as _

@admin.register(DigitalRadio)
class DigitalRadioAdmin(admin.ModelAdmin):
    list_display = ('title_brand', 'brand', 'name', 'Price_without_discount', 'discounted_price', 'created_at')  # Columns in the list view
    list_filter = ('brand', 'created_at')  
    search_fields = ('title_brand', 'brand', 'name', ) 
    prepopulated_fields = {'slug': ('name',)}  
    ordering = ('-created_at',) 
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title_brand', 'brand', 'name', 'slug', 'description', 'image')
        }),
        (_('Pricing'), {
            'fields': ('Price_without_discount', 'discounted_price'),
            'classes': ('collapse',)  # Make this section collapsible
        }),
        (_('Dates'), {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
