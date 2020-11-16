from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Aficion, Usuario, Post

#devuelve la lista de los Usuarios registrados
def show_login(request):
	return render(request, 'index.html')

def post_formulario(request):
	usuario = request.POST["usuario"]
	password = request.POST["password"]

	usuariosaVerificar =  get_list_or_404(Usuario.objects.order_by('nombreUsuario'))
	for usu in usuariosaVerificar:
		if (usu.nombreUsuario == usuario):
			if(usu.contraseña == password ):
				return render(request, 'login.html')
			else:
				return render(request, 'index.html')
		else:
			return render(request, 'index.html')
	