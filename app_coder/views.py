from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.
def crea_curso(req, nombre, camada):

  nuevo_curso = Curso(nombre=nombre, camada=camada)
  nuevo_curso.save()

  return HttpResponse(f"""
    <p>Curso: {nuevo_curso.nombre} - Camada {nuevo_curso.camada} creado con éxito!</p>
  """)

def lista_cursos(req):

  lista = Curso.objects.all()

  return render(req, "lista_cursos.html", {"lista_cursos": lista})