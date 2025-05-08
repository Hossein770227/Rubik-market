from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('info/', views.personal_info, name='personal_info'),
]
