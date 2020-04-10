"""Datashows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from yqshows import views_api, views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('detials_api', views_api.Details_api, name='details_api'),
    path('province_api', views_api.Province_api, name='province_api'),
    path('total_api', views_api.TotalAdd_api, name='total_api'),
    path('pie_api', views_api.pie_api, name='pie_api'),
    path('bar_api', views_api.bar_api,name = 'bar_api'),

]