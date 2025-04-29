from django.urls import path

from . import views

app_name = 'website'


urlpatterns = [
    path('about/', views.about_view,name='about-us' )
]
