from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
from .forms import CursoFormulario

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

def inicio(req):

  return render(req, "inicio.html", {})

def cursos(req):

  return render(req, "cursos.html", {})

def profesores(req):

  return render(req, "profesores.html", {})

def estudiantes(req):

  return render(req, "estudiantes.html", {})

def entregables(req):

  return render(req, "entregables.html", {})

def curso_formulario(req):

  print('method', req.method)
  print('data', req.POST)

  if req.method == 'POST':

    mi_formulario = CursoFormulario(req.POST)

    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data

      nuevo_curso = Curso(nombre=data["curso"], camada=data["camada"])
      nuevo_curso.save()

      return render(req, "inicio.html", {})
    
    else:
      return render(req, "curso_formulario.html", { "mi_formulario": mi_formulario })
  
  else:

    mi_formulario = CursoFormulario()
    return render(req, "curso_formulario.html", { "mi_formulario": mi_formulario })

def busqueda_camada(req):

  return render(req, "busqueda_camada.html")

def buscar_camada(req):

  num_camada = req.GET["camada"]

  cursos = Curso.objects.filter(camada__icontains=num_camada)

  return render(req, "resultado_busqueda.html", { "cursos": cursos, "camada": num_camada })


