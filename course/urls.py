import django
from django import views

from django.urls import path
from . import views

urlpatterns = [
    path('bca', views.bca),
    path('mca', views.mca),
    path('',views.bca),

]