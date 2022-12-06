from django.urls import path, include

from hhcApp import views

urlpatterns = [
    path('', views.index, name='index'),

]
