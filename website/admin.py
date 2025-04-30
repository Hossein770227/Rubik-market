import jdatetime
from django.contrib import admin
from django.utils.translation import gettext as _

from website.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user','email', 'message_subject', 'date_time_persian',]
    list_filter = ['user', 'email',]
    search_fields = ['email', 'message_subject', ]

    def has_add_permission(self, request):
        return False
    
    def date_time_persian(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.date_time).strftime("%Y/%m/%d")

    date_time_persian.short_description = _('date time')
    date_time_persian.admin_order_field = 'date_time'