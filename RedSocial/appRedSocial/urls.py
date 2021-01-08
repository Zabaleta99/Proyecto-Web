from django.urls import path
from . import views

urlpatterns = [
 path('', views.show_login, name='login'),
 path('inicio/', views.inicio, name='inicio'), 
 path('inicio/<int:post_id>', views.like, name='like'),
 path('post/<int:post_id>', views.post, name='post'),
 path('perfil/<slug:username>', views.perfil, name='perfil'),
 path('<slug:username>', views.actualizar, name='actualizar'),
 path('ciudad/<int:ciudad_id>/', views.ciudad, name='ciudad'),
 path('aficion/<int:aficion_id>/', views.aficion, name='aficion'),
 path('estadoCivil/<int:estadoCivil_id>/', views.estadoCivil, name='estadoCivil'),]
