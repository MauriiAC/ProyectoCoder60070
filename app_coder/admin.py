from django.contrib import admin
from .models import Curso, Entregable, Estudiante, Profesor, Avatar


# Register your models here.
admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Avatar)