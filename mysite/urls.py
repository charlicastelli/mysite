"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, serializers, viewsets
from imobiliariaSA import views
from django.conf.urls.static import static
from django.conf import settings



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'imoveis', views.ImoveisViewSet)
router.register(r'categorias', views.CategoriasViewSet)
router.register(r'tiposImoveis', views.TipoImovelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), #Quando acessar /admin/ pega as urls do admin.py
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),#Quando acessar /api-auth/ pega as urls do rest-framenwork
    re_path(r'^', include(router.urls)),
    re_path('login/', views.login),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
