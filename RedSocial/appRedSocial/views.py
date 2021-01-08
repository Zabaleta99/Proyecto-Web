from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Aficion, Usuario, Post, Ciudad, EstadoCivil, Comentario

#varibale estatica que guarda el usuario logeado
class variable:
	usuarioEstatico= Usuario()

#devuelve la lista de los Usuarios registrados
def show_login(request):
	
	ciudades =  get_list_or_404(Ciudad.objects.all())
	aficiones =  get_list_or_404(Aficion.objects.all())
	estadoCivil =  get_list_or_404(EstadoCivil.objects.all())
	context = {'lista_Ciudad': ciudades, 'lista_EstadoCivil' : estadoCivil, 'lista_Aficiones' : aficiones}
	return render(request, 'login.html', context)

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
	descripcionAmplia = 'descripcionAmplia' in request.POST and request.POST['descripcionAmplia']
	fotoPerfil = 'fotoPerfil' in request.FILES and request.FILES['fotoPerfil']
	if('ciudad' in request.POST):
		ciudadSelecionada = request.POST['ciudad']
		ciudad =  get_list_or_404(Ciudad, nombreCiudad=ciudadSelecionada)
	if('estadoCivil' in request.POST):
		estadoCivilSelecionado = request.POST['estadoCivil']
		estadoCivil =  get_list_or_404(EstadoCivil, nombreEstadoCivil=estadoCivilSelecionado)
	if('aficiones' in request.POST):
		aficionesSelecionados = request.POST['aficiones']
		aficiones =  get_list_or_404(Aficion, nombreAficion=aficionesSelecionados)
	
	p = Usuario()
	usuariosaVerificar = get_list_or_404(Usuario.objects.all())

	for usu in usuariosaVerificar:
		if (usu.nombreUsuario == usuario):
			if(usu.contraseña == password):
				usuario_logeado = Usuario.objects.get(pk=usuario)
				posts = Post.objects.order_by('-fecha_publicacion')
				variable.usuarioEstatico = usuario_logeado

				postFiltados = list();
				for post in posts:
					for usuario in usuariosaVerificar:
						if post.autor ==usuario.segidos.all():
							postFiltados.append(post)

				context = {'lista_posts': postFiltados, 'usuario': usuario_logeado}
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
		p.sobreMi = descripcionAmplia
		p.ciudad = ciudad[0]
		p.fotoPerfil = fotoPerfil

		p.save()
		#primero se crea el usuario, y luego se le da las aficiones
		p.aficiones.add(aficiones[0])
		variable.usuarioEstatico = p

		posts = Post.objects.order_by('-fecha_publicacion')
		postFiltados = list();
		for post in posts:
			for usuario in usuariosaVerificar.segidos.all():
				if post.autor ==usuario:
					postFiltados.append(post)

		context = {'lista_posts': postFiltados, 'usuario': p}
		return render(request, 'inicio.html', context)
	return render(request, 'login.html')

def like(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	posts = Post.objects.order_by('-fecha_publicacion')
	like = False

	for usuario in post.usuariosLike.all():
		if(usuario == variable.usuarioEstatico):
			post.usuariosLike.remove(usuario)
			like = True
			post.likes = post.likes - 1
			post.save()

	if like == False:
		post.usuariosLike.add(variable.usuarioEstatico)
		post.likes = post.likes + 1
		post.save()

	context = {'lista_posts': posts, 'usuario': variable.usuarioEstatico}
	return render(request, 'inicio.html', context)
		
def post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	comentarios = get_list_or_404(Comentario.objects.all())

	comentsPost = []
	for i in comentarios:
		if (str(i.titulo) == str(post.titulo)):
			comentsPost.append(i)
	context = {'post': post, 'comentarios': comentsPost}
	return render(request, 'post.html', context)

# return HttpResponse(comentsPost)
def perfil(request, username):
	usuario = get_object_or_404(Usuario, pk=username)
	aficiones = usuario.aficiones.all()
	verificador = False
	esPerfilPropio = False
	segidos = variable.usuarioEstatico.segidos.all()
	if (variable.usuarioEstatico.nombreUsuario == usuario.nombreUsuario):
			verificador = True
			esPerfilPropio = True
	for segido in segidos:
		if (segido.nombreUsuario == usuario.nombreUsuario):
			verificador = True
			break

	context = {'usuario': usuario, 'aficiones': aficiones, 'verificador' : verificador, 'esPerfilPropio' : esPerfilPropio}
	return render(request, 'perfil.html', context)

def actualizar(request, username):
	usuario = get_object_or_404(Usuario, pk=username)
	usuarioLogin = variable.usuarioEstatico.segidos.all()
	verificador = False
	for segido in usuarioLogin:
		if (segido.nombreUsuario == usuario.nombreUsuario):
			#guarda los cambios en el atributo segidores del usuario
			usuario.segidores.remove(variable.usuarioEstatico)
			usuario.save()
			#guarda los cambios en el atributo segidos del usuaurio de login o estatico
			verificador = True
			variable.usuarioEstatico.segidos.remove(segido) 
			variable.usuarioEstatico.save()
			break

	if(verificador == False):
		#guarda los cambios en el atributo segidores del usuario
		usuario.segidores.add(variable.usuarioEstatico)
		usuario.save()
		#guarda los cambios en el atributo segidos del usuaurio de login o estatico
		variable.usuarioEstatico.segidos.add(usuario) 
		variable.usuarioEstatico.save()

	context = {'usuario': usuario}
	return perfil(request, username)

def ciudad(request, ciudad_id):
	ciudad = get_object_or_404(Ciudad, pk=ciudad_id)
	usuarios= get_list_or_404(Usuario.objects.order_by('nombreUsuario'))

	usuarioSeleccionado = list()
	for usuario in usuarios:
		if (usuario.ciudad.id == ciudad.id):
			usuarioSeleccionado.append(usuario)

	context = {'ciudad': ciudad, 'usuarioSeleccionado': usuarioSeleccionado}
	return render(request, 'ciudad.html', context)

def aficion(request, aficion_id):
	aficion = get_object_or_404(Aficion, pk=aficion_id)
	usuarios= get_list_or_404(Usuario.objects.order_by('nombreUsuario'))

	usuarioSeleccionado = list()
	for usuario in usuarios:
		for afi in usuario.aficiones.all():
			if (afi.id == aficion.id):
				usuarioSeleccionado.append(usuario)
	
	context = {'aficion': aficion, 'usuarioSeleccionado': usuarioSeleccionado}
	return render(request, 'aficion.html', context)

def estadoCivil(request, estadoCivil_id):
	estadoCivil = get_object_or_404(EstadoCivil, pk=estadoCivil_id)
	usuarios= get_list_or_404(Usuario.objects.order_by('nombreUsuario'))

	usuarioSeleccionado = list()
	for usuario in usuarios:
		if (usuario.estadoCivil.id == estadoCivil.id):
			usuarioSeleccionado.append(usuario)
	
	context = {'estadoCivil': estadoCivil, 'usuarioSeleccionado': usuarioSeleccionado}
	return render(request, 'estadoCivil.html', context)
