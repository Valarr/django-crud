from django.urls import path
from webdev.consultas import views

app_name='consultas'

urlpatterns=[
    path('', views.home, name='home')
]