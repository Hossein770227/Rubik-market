from django.urls import path

from . import views 

app_name = 'products'

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name='product_detail'),
    # url phone  
    path("phones/", views.PhoneListView.as_view(), name='phone_list'),   
    path("phones/<int:pk>/", views.PhoneDetailView.as_view(), name='phone_detail'),
    # url laptop  
    path("laptops/", views.LaptopListView.as_view(), name='laptop_list'),   
    path("laptops/<int:pk>/", views.LaptopDetailView.as_view(), name='laptop_detail'),
]
