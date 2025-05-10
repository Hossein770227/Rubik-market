from django.urls import path

from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    # phone urls
    path('phones/', views.PhoneListView.as_view(), name='phone_list'),
    path('phones/<int:pk>/', views.PhoneDetailView.as_view(), name='phone_detail'),
    path('phone/comment/<int:pk>/',views.comment_phone_view,name='phone_comment'),
    # laptop urls
    path('laptop/', views.LaptopListView.as_view(), name='laptop_list'),
    path('laptop/<int:pk>/', views.LaptopDetailView.as_view(), name='laptop_detail'),
]

