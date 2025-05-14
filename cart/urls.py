from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add/<int:pk>/', views.add_to_cart_view, name='cart_add'),
    path('remove/<int:pk>/', views.remove_form_cart, name= 'cart_remove'),
    path('clear/', views.clear_cart, name= 'cart_clear'),
]
