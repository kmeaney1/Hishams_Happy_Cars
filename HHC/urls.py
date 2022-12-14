"""HHC URL Configuration

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
from django.urls import path
from hhcApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('form', views.add_car_form, name='form'),
    path('carProf', views.get_car_info, name='carProf'),
    path('carProf/<int:car_vin>/', views.get_car_info, name='profile'),

    path('search/', views.search, name='search'),
    path('purchase/', views.purchase, name='purchase'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('signup', views.signUp, name='signup'),
    path('register', views.register, name='register')

]
