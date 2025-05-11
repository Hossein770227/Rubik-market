from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from django.utils import timezone 



class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE, primary_key=True)
    province = models.CharField(_("province"), max_length=150)
    city = models.CharField(_("city "), max_length=150)
    full_address = models.CharField(_("full address"), max_length=500)
    postal_code= models.CharField(_("postal code"), max_length=50)
    date_time_created = models.DateTimeField(_("date time created"), default=timezone.now )
    date_time_modified = models.DateTimeField(_("date modified"), auto_now=True)

    def __str__(self):
        return f'{self.user.full_name} : {self.full_address}'
    
   



