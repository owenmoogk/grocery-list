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
from items.views import itemsDetailView, itemCreateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from users.views import dashboard

urlpatterns = [
    path('', views.homeView),
    path("home/", views.homeView),
    path('about/', views.aboutView),
    path('admin/', admin.site.urls),
    path("items/", itemsDetailView),
    path("create/", itemCreateView),
    url(r"^", include("users.urls")),
]

urlpatterns += staticfiles_urlpatterns()