from django.shortcuts import render

from django.views.generic import ListView, DetailView

from products.models import Product


class ProductListView(ListView):
    model = Product
    template_name ='products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name ='products/product_detail.html'
    context_object_name='product'   


class PhoneListView(ListView):
    model = Product
    template_name = 'products/phone_list.html'
    context_object_name = 'phones'

    def get_queryset(self):
        return Product.objects.filter(category=1)

class PhoneDetailView(DetailView):
    model = Product
    template_name ='products/phone_detail.html'
    context_object_name='phone'


class LaptopListView(ListView):
    model = Product
    template_name = 'products/laptop_list.html'
    context_object_name = 'laptops'

    def get_queryset(self):
        return Product.objects.filter(category=2)

class LaptopDetailView(DetailView):
    model = Product
    template_name ='products/laptop_detail.html'
    context_object_name='laptop'