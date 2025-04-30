from django.db import models
from django.utils.translation import gettext as _

class  Contact(models.Model):
    email = models.EmailField(_("email"), max_length=254)
    message_subject = models.CharField(_("message subject"), max_length=100)
    message = models.TextField(_("message"))
    date_time = models.DateTimeField(_("date time"), auto_now_add=True)

    def __str__(self):
        return f'{self.email} : {self.message_subject}' 
