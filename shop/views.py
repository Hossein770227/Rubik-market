from django.shortcuts import render
from django.views.generic import TemplateView


class ShopListView(TemplateView):
    template_name = 'shop/product_list.html'

