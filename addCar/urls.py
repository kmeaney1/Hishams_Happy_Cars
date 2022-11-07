from django.urls import path

from addCar import views

urlpatterns = [
    path('', views.index, name='index'),
]
