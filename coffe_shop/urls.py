"""
URL configuration for coffe_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import inc
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("productos/", include("products.urls")),  # Incluir las URLs de la app products
    path("usuarios/", include("users.urls")),  # Incluir las URLs de la app users
    path("orders/", include("orders.urls")),  # Incluir las URLs de la app orders
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Servir archivos multimedia en desarrollo
