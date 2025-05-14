
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ 
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_("category Name"))  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("categories")
        verbose_name_plural = _("categories")



class Product(models.Model):

    RATING_CHOICES = [
        (5, "⭐⭐⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (3, "⭐⭐⭐"),
        (2, "⭐⭐"),
        (1, "⭐"),
    ]
    
    title = models.CharField(_("title"), max_length=150)
    brand =models.CharField(_("brand"), max_length=150)
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE, related_name='products')
    text = RichTextField(_("text"))
    price_without_discount =models.PositiveIntegerField(_("price without discount"))
    price_with_discount =models.PositiveIntegerField(_("price with discount"))
    image = models.ImageField(_("image"), upload_to='cover/', null=True, blank=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    is_active = models.BooleanField(_("active ?"), default=True )
    release_date = models.DateField(_("Release Date"), null=True, blank=True)

    rating = models.CharField(
        _("rating"),
        max_length=10,
        choices=RATING_CHOICES,
        blank=True,
    )


    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ['title']
        indexes = [
            models.Index(fields=['title', 'brand']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id])




