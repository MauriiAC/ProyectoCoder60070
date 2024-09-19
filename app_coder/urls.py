from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path('lista-cursos/', lista_cursos),
    path('', inicio),
    path('profesores/', profesores, name='Profesores'),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('curso-formulario/', curso_formulario, name='CursoFormulario'),
    path('busqueda-camada/', busqueda_camada, name='BusquedaCamada'),
    path('buscar-camada/', buscar_camada, name='BuscarCamada'),
]
