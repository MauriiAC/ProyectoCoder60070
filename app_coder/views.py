from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Curso, Profesor
from .forms import CursoFormulario, ProfesorFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


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


def lista_profesores(req):

  profesores = Profesor.objects.all()

  return render(req, "leer_profesores.html", { "profesores": profesores })


def crea_profesor(req):

  print('method', req.method)
  print('data', req.POST)

  if req.method == 'POST':

    mi_formulario = ProfesorFormulario(req.POST)

    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data

      nuevo_profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
      nuevo_profesor.save()

      return HttpResponseRedirect('/app-coder')
    
    else:
      return render(req, "profesor_formulario.html", { "mi_formulario": mi_formulario })
  
  else:

    mi_formulario = ProfesorFormulario()
    return render(req, "profesor_formulario.html", { "mi_formulario": mi_formulario })


def eliminar_profesor(req, id):

  if req.method == 'POST':

    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    profesores = Profesor.objects.all()

    return render(req, "leer_profesores.html", { "profesores": profesores })
  

def editar_profesor(req, id):

  profesor = Profesor.objects.get(id=id)

  if req.method == 'POST':
    
    mi_formulario= ProfesorFormulario(req.POST)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data

      profesor.nombre = data["nombre"]
      profesor.apellido = data["apellido"]
      profesor.email = data["email"]
      profesor.profesion = data["profesion"]
      profesor.save()

      return HttpResponseRedirect('/app-coder')
    
    else:
      return render(req, "profesor_formulario.html", { "mi_formulario": mi_formulario })

  else:

    mi_formulario = ProfesorFormulario(initial={
      "nombre": profesor.nombre,
      "apellido": profesor.apellido,
      "email": profesor.email,
      "profesion": profesor.profesion,
    })
    return render(req, "editar_profesor.html", { "mi_formulario": mi_formulario, "id": profesor.id })


class CursoList(ListView):

  model = Curso
  template_name = 'curso_list.html'
  context_object_name = 'cursos'

class CursoDetail(DetailView):

  model = Curso
  template_name = 'curso_detail.html'
  context_object_name = 'curso'

class CursoCreate(CreateView):

  model = Curso
  template_name = 'curso_create.html'
  fields = ['nombre', 'camada']
  success_url = '/app-coder'

class CursoUpdate(UpdateView):

  model = Curso
  template_name = 'curso_update.html'
  fields = ('__all__')
  success_url = '/app-coder'
  context_object_name = 'curso'

class CursoDelete(DeleteView):

  model = Curso
  template_name = 'curso_delete.html'
  success_url = '/app-coder'

