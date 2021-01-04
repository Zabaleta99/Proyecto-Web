from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EstadoCivil, Ciudad, Usuario, Aficion, Post, Comentario

class EstadoCivilAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Descripción', {'fields': ['nombreEstadoCivil']}),
        ('Representación de la Populación', {'fields': ['representacion']})
    ]


admin.site.register(EstadoCivil, EstadoCivilAdmin)

class CiudadAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nombre de la ciudad', {'fields': ['nombreCiudad']}),
        ('Ubicacion', {'fields': ['pais', 'provincia', 'comunidad']}),
        ('Imagen de la ciudad', {'fields': ['foto']})
    ]

admin.site.register(Ciudad, CiudadAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Datos del usuario', {'fields': ['nombreUsuario', 'contraseña', 'fotoPerfil']}),
        ('Datos Personales', {'fields': ['nombre', 'apellidoUno', 'apellidoDos','fecha_nacimiento', 'ciudad', 'estadoCivil', 'telefono', 'email']}),
        ('Descripción', {'fields': ['descripcion', 'sobreMi', 'fotoDescripcion', 'aficiones']}),
        ('Interacción', {'fields': ['segidos', 'segidores']})
    ]

admin.site.register(Usuario, UsuarioAdmin)


class AficionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Descripción', {'fields': ['nombreAficion']}),
        ('Información General', {'fields': ['edadMedia', 'estimacionSeguidores']}),
        ('Imagen de la aficion', {'fields': ['foto']})
    ]

admin.site.register(Aficion, AficionAdmin)

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Titulo', {'fields': ['titulo']}),
        ('Información General', {'fields': ['autor']}),
        ('Contenido', {'fields': ['texto']}),
        ('Impacto', {'fields': ['likes']}),
        ('Imágenes', {'fields': ['foto', 'foto1', 'foto2']})
	]
    list_display = ('titulo', 'fecha_publicacion', 'was_published_recently')
    list_filter = ['fecha_publicacion']
    search_fields = ['titulo']

    

admin.site.register(Post, PostAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Titulo', {'fields': ['titulo']}),
        ('Información General', {'fields': ['nombreUsuario', 'fecha_publicacion']}),
        ('Contenido', {'fields': ['texto']}),
        ('Impacto', {'fields': ['likes']})
    ]
    list_display = ('titulo', 'texto', 'fecha_publicacion')
    list_filter = ['fecha_publicacion']
    search_fields = ['texto']


admin.site.register(Comentario, ComentarioAdmin)
