from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ 
from django.utils.text import slugify

class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_("Brand Name"))  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class Phone(models.Model):

    RATING_CHOICES = [
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),
    ]
    
    title = models.CharField(_("title"), max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phones', verbose_name=_("Brand"))
    text = models.TextField(_("text"))
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
        verbose_name = _("Phone")
        verbose_name_plural = _("Phones")
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
        return reverse('shop:phone_detail', args=[self.id])


class LaptopBrand(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_("Brand Name"))  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("LaptopBrand")
        verbose_name_plural = _("LaptopBrand")



class Laptop(models.Model):

    RATING_CHOICES = [
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),
    ]
    
    title = models.CharField(_("title"), max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='laptops', verbose_name=_("Brand"))
    text = models.TextField(_("text"))
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
        verbose_name = _("laptop")
        verbose_name_plural = _("laptop")
        ordering = ['release_date']
        indexes = [
            models.Index(fields=['title', 'brand']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)




