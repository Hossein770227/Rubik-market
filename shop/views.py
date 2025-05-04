from django.shortcuts import render
from django.views import generic

from shop.models import Phone

class ProductList(generic.TemplateView):
    template_name = 'shop/product_list.html'


class PhoneListView(generic.ListView):
    model = Phone
    template_name = 'shop/phone_list.html'
    context_object_name = 'phones'