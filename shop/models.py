from django.db import models
from django.utils.translation import gettext as _

class Category(models.Model):
    title = models.CharField(_("title"), max_length=150)
    description =models.CharField(_("description for category"), max_length=700, blank=True)
 
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['title']  

    def __str__(self):
        return self.title