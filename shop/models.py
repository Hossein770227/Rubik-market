from django.db import models
from django.utils.translation import gettext as _

class CategoryDigitalProducts(models.Model):
    title = models.CharField(_("title"), max_length=150)
    description =models.CharField(_("description for category"), max_length=700, blank=True)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['title']  

    def __str__(self):
        return self.title
    
    
class ProductsTypeDigital(models.Model):
    name = models.CharField(_("name"), max_length=150)
    group = models.ForeignKey(CategoryDigitalProducts, verbose_name=_("group"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("product type digital")
        verbose_name_plural =  _("product type digital")
        ordering = ['name']  

    def __str__(self):
        return self.name
    

class ProductsDigital(models.Model):
    digital_group = models.ForeignKey(ProductsTypeDigital, verbose_name=_("digital_group"), on_delete=models.CASCADE)
    type_product = models.CharField(_("name product"), max_length=100)
    type = models.CharField(_("type"), max_length=100)
    title = models.CharField(_("title"), max_length=255)
    price= models.PositiveIntegerField(_("price "))
    date_time_add = models.DateTimeField(_("date time add"), auto_now_add=True)

    class Meta:
        verbose_name = _("products digital ")
        verbose_name_plural =  _("products digital ")
        ordering = ['title']  

    def __str__(self):
        return f'{self.type}'
    

