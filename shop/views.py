from django.shortcuts import render
from django.views import generic

class ProductList(generic.TemplateView):
    template_name = 'shop/product_list.html'
