from django.urls import path
from . import views

urlpatterns = [
 path('', views.show_login, name='login'),
 path('inicio/', views.inicio, name='inicio'),
 path('perfil/', views.perfil, name='perfil'),
 path('ciudad/<int:ciudad_id>/', views.ciudad, name='ciudad'),
 path('aficion/<int:aficion_id>/', views.aficion, name='aficion'),
 path('estadoCivil/<int:estadoCivil_id>/', views.estadoCivil, name='estadoCivil'),]
