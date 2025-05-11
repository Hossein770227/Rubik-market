from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('info/', views.personal_info, name='personal_info'),
    path('address/', views.AddressView.as_view(), name='address'),
    path('address/<int:pk>/update/', views.UpdateAddressView.as_view(), name='update_address'),
    path('address/<int:pk>/delete/', views.DeleteAddressView.as_view(), name='delete_address'),
]

