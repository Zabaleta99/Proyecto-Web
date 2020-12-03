from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EstadoCivil, Ciudad, Usuario, Aficion, Post, Comentario
admin.site.register(EstadoCivil)
admin.site.register(Ciudad)
admin.site.register(Usuario)
admin.site.register(Aficion)
admin.site.register(Post)
admin.site.register(Comentario)
