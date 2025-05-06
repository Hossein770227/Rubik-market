from django.urls import path

from . import views

app_name = 'website'


# Frequently asked questions

urlpatterns = [
    path('about/', views.about_view,name='about_us' ),
    path('contact/', views.contact_view,name='contact' ),
    path('questions/', views.question_view,name='question'),
]


