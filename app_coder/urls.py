from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path('lista-cursos/', lista_cursos),
    path('', inicio),
    path('profesores/', profesores),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]
