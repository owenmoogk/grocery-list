"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from pages import views
from products.views import productDetailView, productCreateView, productDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homeView),
    path("home/", views.homeView),
    path('about/', views.aboutView),
    path('admin/', admin.site.urls),
    path("items/", productDetailView),
    path("create/", productCreateView),
    path("delete/<int:id>", productDeleteView, name="product-delete")
]

urlpatterns += staticfiles_urlpatterns()