from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('detail/', views.cart_detail_view, name='cart_detail'),
    path('add/phone/<int:product_id>/', views.phone_add_to_cart_view, name='phone_add'),

]
