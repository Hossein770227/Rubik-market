from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('shop.urls')),
    path('', include('website.urls')),
    path('dashboard/', include('dashboard.urls')),

    # rosetta url for translate
    path('rosetta/', include('rosetta.urls')),
]
