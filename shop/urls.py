from django.urls import path

from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('phones/', views.PhoneListView.as_view(), name='phone_list'),
]

