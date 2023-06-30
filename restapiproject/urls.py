"""restapiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from mainapp.views import *
from mainapp import views as user_views 
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registartion.as_view(), name='user-register'),
    path('authenticate/', UserAuthenticationAPIView.as_view(), name='user-authenticate'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/<int:pk>/purchase/', PurchaseCreateAPIView.as_view(), name='purchase-create'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('register1/',user_views.register_user, name='user-register1'),
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
   
    

