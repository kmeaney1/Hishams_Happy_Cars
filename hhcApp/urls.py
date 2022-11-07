from django.urls import path

from hhcApp import views

urlpatterns = [
    path('', views.index, name='index'),
]
