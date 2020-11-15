# Create your models here.
from django.db import models

class EstadoCivil(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombreEstadoCivil = models.CharField( max_length=20)
 representacion = models.DecimalField(max_digits=4, decimal_places=2)

 def __str__(self):
        return self.nombreEstadoCivil

class Ciudad(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombreCiudad = models.CharField( max_length=25)
 provincia = models.CharField(max_length=40)
 comunidad = models.CharField(max_length=40)
 pais = models.CharField(max_length=40)
 def __str__(self):
        return self.nombreCiudad

class Aficion(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombreAficion = models.CharField(max_length=50)
 edadMedia = models.DecimalField(max_digits=4, decimal_places=2)
 estimacionSeguidores = models.IntegerField(default=0) 
 def __str__(self):
        return self.nombreAficion

class Usuario(models.Model):
 # Campo para la relación one-to-many
 nombreUsuario = models.CharField( max_length=40, primary_key=True)
 estadoCivil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
 aficiones = models.ManyToManyField(Aficion)
 nombre = models.CharField(max_length=40)
 apellidoUno = models.CharField(max_length=40)
 apellidoDos = models.CharField(max_length=40)
 telefono = models.IntegerField(default=0)
 fecha_nacimiento = models.DateField()
 ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
 fotoPerfil = models.ImageField(upload_to='imagenes/',blank=True, null=True)
 descripcion = models.CharField(max_length=250)

 def __str__(self):
        return self.nombreUsuario


class Seguidores(models.Model):
	nombreUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name = 'Seguidor')
	seguidores = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name = 'friends')
 

class Seguidos(models.Model):
	nombreUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name = 'Seguido')
	seguidos =  models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name = 'amigos')


class Post(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 titulo = models.CharField(max_length=50)
 nombreUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
 fecha_publicacion = models.DateField()
 hora = models.DateTimeField(auto_now_add=True, blank=True)
 texto = models.CharField(max_length=500)
 likes = models.IntegerField(default=0)
 
 def __str__(self):
        return self.titulo


class Comentario(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 titulo = models.ForeignKey(Post, on_delete=models.CASCADE)
 nombreUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
 fecha_publicacion = models.DateField()
 texto = models.CharField(max_length=500)
 likes = models.IntegerField(default=0)
 
 def __str__(self):
        return self.titulo