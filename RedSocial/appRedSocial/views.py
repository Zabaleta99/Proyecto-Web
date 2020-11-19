from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Aficion, Usuario, Post, Ciudad, EstadoCivil

#devuelve la lista de los Usuarios registrados
def show_login(request):
	return render(request, 'login.html')

def inicio(request):
	usuario = 'usuario' in request.POST and request.POST['usuario']
	password = 'password' in request.POST and request.POST['password']
	usuario1 = 'usuario1' in request.POST and request.POST['usuario1']
	password1 = 'password1' in request.POST and request.POST['password1']
	nombre = 'nombre' in request.POST and request.POST['nombre']
	apellidoUno = 'apellidoUno' in request.POST and request.POST['apellidoUno']
	apellidoDos = 'apellidoDos' in request.POST and request.POST['apellidoDos']
	correo = 'correo' in request.POST and request.POST['correo']
	telefono = 'telefono' in request.POST and request.POST['telefono']
	fecha_nacimiento = 'fecha_nacimiento' in request.POST and request.POST['fecha_nacimiento']
	descripcion = 'descripcion' in request.POST and request.POST['descripcion']
	fotoPerfil = 'fotoPerfil' in request.FILES and request.FILES['fotoPerfil']

	usuariosaVerificar =  get_list_or_404(Usuario.objects.all())
	aficiones =  get_list_or_404(Aficion.objects.all())
	estadoCivil =  get_list_or_404(EstadoCivil.objects.all())
	ciudad =  get_list_or_404(Ciudad.objects.all())

	p = Usuario()

	for usu in usuariosaVerificar:
		if (usu.nombreUsuario == usuario):
			if(usu.contraseña == password):
				usuario_logeado = Usuario.objects.get(pk=usuario)
				posts = Post.objects.order_by('-fecha_publicacion')
				context = {'lista_posts': posts, 'usuario': usuario_logeado}
				return render(request, 'inicio.html', context)

	if correo is not False:
		p.nombreUsuario = usuario1
		p.contraseña = password1
		p.nombre = nombre
		p.apellidoUno = apellidoUno
		p.apellidoDos = apellidoDos
		p.email = correo
		p.telefono= telefono
		p.fecha_nacimiento = fecha_nacimiento
		p.descripcion = descripcion
		p.estadoCivil = estadoCivil[0]
		p.ciudad = ciudad[0]
		p.fotoPerfil = fotoPerfil

		p.save()
		posts = Post.objects.order_by('-fecha_publicacion')
		context = {'lista_posts': posts, 'usuario': p}
		return render(request, 'inicio.html', context)
	return render(request, 'login.html')


def perfil(request, username):
	usuario = get_object_or_404(Usuario, pk=username)
	aficiones = usuario.aficiones.all()
	context = {'usuario': usuario, 'aficiones': aficiones}
	return render(request, 'perfil.html', context)


def ciudad(request, ciudad_id):
	ciudad = get_object_or_404(Ciudad, pk=ciudad_id)
	context = {'ciudad': ciudad }
	return render(request, 'ciudad.html', context)

def aficion(request, aficion_id):
	aficion = get_object_or_404(Aficion, pk=aficion_id)
	context = {'aficion': aficion }
	return render(request, 'aficion.html', context)

def estadoCivil(request, estadoCivil_id):
	estadoCivil = get_object_or_404(EstadoCivil, pk=estadoCivil_id)
	context = {'estadoCivil': estadoCivil }
	return render(request, 'estadoCivil.html', context)
