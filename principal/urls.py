from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('servicios/', views.servicios, name='servicios'),
    path('dinamico/', views.dinamico, name='dinamico'),
]