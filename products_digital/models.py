from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class DigitalRadio(models.Model):
    title_brand = models.CharField(_("title brand"), max_length=150)
    brand = models.CharField(_("brand"), max_length=100)
    name = models.CharField(_("name"), max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    Price_without_discount = models.PositiveIntegerField(_("price without discount"))
    discounted_price = models.PositiveIntegerField(_("price with discount"))
    description = models.TextField(_("description"))
    image = models.ImageField(_("image"), upload_to='cover/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _("Digital Radios")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.brand}") 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand} - {self.name}"
