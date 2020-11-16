from django.urls import path
from . import views

urlpatterns = [
 path('', views.show_login, name='index'),
  path('respuesta/', views.post_formulario, name='respuesta'),]