from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ 
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField


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



class CommentPhone(models.Model):
    SCORE_VEY_BAD='1'
    SCORE_BAD='2'
    SCORE_NORMAL='3'
    SCORE_GOOD='4'
    SCORE_PERFECT='5'

    SCORE_CHOICES = (
        (SCORE_PERFECT,_('perfect')),
        (SCORE_GOOD,_('good')),
        (SCORE_NORMAL,_('normal')),
        (SCORE_BAD,_(' bad')),
        (SCORE_VEY_BAD,_('very bad')),
    )
    author = models.ForeignKey(get_user_model(), verbose_name=_("author"), on_delete=models.CASCADE)
    product = models.ForeignKey(Phone, verbose_name=_("product"), on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField(_("email"), max_length=254)
    text = models.TextField(_("text comment"))
    score = models.CharField(choices=SCORE_CHOICES, max_length=2)
    active = models.BooleanField(_("active"), default=True)
    date_time_created = models.DateTimeField(_("date time created"), auto_now_add=True)

    def __str__(self):
        return f'{self.author} : {self.product}'


























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
    brand = models.ForeignKey(LaptopBrand, on_delete=models.CASCADE, related_name='laptops', verbose_name=_("Brand"))
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

    def get_absolute_url(self):
        return reverse('shop:laptop_detail', args=[self.id])






