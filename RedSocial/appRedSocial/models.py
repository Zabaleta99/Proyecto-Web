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
 foto = models.ImageField(upload_to='img/', null=True, blank=True)
 def __str__(self):
        return self.nombreCiudad

class Aficion(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombreAficion = models.CharField(max_length=50)
 edadMedia = models.DecimalField(max_digits=4, decimal_places=2)
 estimacionSeguidores = models.IntegerField(default=0)
 foto = models.ImageField(upload_to='img/', null=True, blank=True)
 def __str__(self):
        return self.nombreAficion

class Usuario(models.Model):
 # Campo para la relación one-to-many
 nombreUsuario = models.CharField( max_length=40, primary_key=True)
 contraseña = models.CharField( max_length=8, default='contraseña')
 estadoCivil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
 aficiones = models.ManyToManyField(Aficion, default=[0])#null=False, blank=False
 nombre = models.CharField(max_length=40)
 apellidoUno = models.CharField(max_length=40)
 apellidoDos = models.CharField(max_length=40)
 telefono = models.IntegerField(default=0)
 fecha_nacimiento = models.DateField()
 ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
 fotoPerfil = models.ImageField(upload_to='img/',blank=True, null=True)
 descripcion = models.CharField(max_length=250)
 sobreMi = models.TextField(null=True, blank=True)
 email = models.EmailField(max_length = 100)
 fotoDescripcion = models.ImageField(upload_to='img/', null=True, blank=True)
 segidos = models.ManyToManyField("self")
 segidores = models.ManyToManyField("self")

 def __str__(self):
        return self.nombreUsuario


class Post(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 titulo = models.CharField(max_length=50)
 autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
 fecha_publicacion = models.DateTimeField(auto_now_add=True)
 texto = models.CharField(max_length=500)
 likes = models.IntegerField(default=0)
 foto = models.ImageField(upload_to='img/',blank=True, null=True)

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
