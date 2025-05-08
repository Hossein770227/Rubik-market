from django.shortcuts import render
from django.views import generic

from shop.models import Laptop, Phone

class ProductList(generic.TemplateView):
    template_name = 'shop/product_list.html'


class PhoneListView(generic.ListView):
    model = Phone
    template_name = 'shop/phone_list.html'
    context_object_name = 'phones'

    def get_queryset(self):
        return Phone.objects.filter(is_active=True)


class PhoneDetailView(generic.DetailView):
    model = Phone
    template_name = 'shop/phone_detail.html'
    context_object_name = 'phone'


class LaptopListView(generic.ListView):
    model = Laptop
    template_name = 'shop/laptop_list.html'
    context_object_name = 'laptops'

    def get_queryset(self):
        return Laptop.objects.filter(is_active=True)
    


class LaptopDetailView(generic.DetailView):
    model = Laptop
    template_name = 'shop/laptop_detail.html'
    context_object_name = 'laptop'