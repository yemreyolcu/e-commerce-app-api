from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('default/', include('default.urls')),
    path('computer/', include('computer.urls')),
    path('product/', include('product.urls')),
]
