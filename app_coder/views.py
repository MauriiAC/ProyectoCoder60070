from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Curso, Profesor, Avatar, Estudiante, Entregable
from .forms import CursoFormulario, ProfesorFormulario, UserEditForm, AvatarFormulario

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

def lista_cursos(req, page):

  print('page:', page)

  cant_por_pagina = 3

  if req.GET.get("direction") == 'next':
    page += 1
  elif req.GET.get("direction") == 'previous':
    page -= 1

  inicio = int(page-1)*cant_por_pagina
  final = int(page)*cant_por_pagina

  lista = Curso.objects.all()[inicio:final]
  print(lista)

  return render(req, "lista_cursos.html", {"lista_cursos": lista, "current_page": page})

def inicio(req):

  try:
    
    avatar = Avatar.objects.get(user=req.user.id)
    return render(req, "inicio.html", {'url': avatar.imagen.url})

  except:
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

@login_required
def lista_profesores(req):

  try:

    if req.user.profesor:

      profesores = Profesor.objects.all()

      return render(req, "leer_profesores.html", { "profesores": profesores })
    
    else:

      return HttpResponseRedirect('/app-coder/')
  
  except:

    return HttpResponseRedirect('/app-coder/')


def crea_profesor(req):

  print('method', req.method)
  print('data', req.POST)

  if req.method == 'POST':

    info = req.POST

    mi_formulario = ProfesorFormulario(
      {
        "nombre": info["nombre"],
        "apellido": info["apellido"],
        "email": info["email"],
        "profesion": info["profesion"],
      }
    )

    user_form = UserCreationForm(
      {
        "username": info["username"],
        "password1": info["password1"],
        "password2": info["password2"],
      }
    )

    if mi_formulario.is_valid() and user_form.is_valid():

      data = mi_formulario.cleaned_data
      data.update(user_form.cleaned_data)

      user = User(username=data["username"])
      user.set_password(data["password1"])
      user.save()

      nuevo_profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"], user_id=user)

      nuevo_profesor.save()

      return HttpResponseRedirect('/app-coder')
    
    else:
      return render(req, "profesor_formulario.html", { "mi_formulario": mi_formulario })
  
  else:

    mi_formulario = ProfesorFormulario()
    user_form = UserCreationForm()
    return render(req, "profesor_formulario.html", { "mi_formulario": mi_formulario, "user_form": user_form })


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


class CursoList(LoginRequiredMixin, ListView):

  model = Curso
  template_name = 'curso_list.html'
  context_object_name = 'cursos'

  def get_queryset(self):
    value = self.kwargs["camada"]
    cursos = Curso.objects.filter(camada__gt=value)
    return cursos
  

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
  context_object_name = 'curso'


def login_view(req):

  if req.method == 'POST':
    
    mi_formulario= AuthenticationForm(req, data=req.POST)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data
      usuario = data['username']
      psw = data['password']

      user = authenticate(username=usuario, password=psw)

      if user:
        login(req, user)
        return render(req, "inicio.html", { "mensaje": f"Bienvenido {usuario}"})
      else:
        return render(req, "inicio.html", { "mensaje": f"Datos incorrectos!"})

    else:
      return render(req, "login.html", { "mi_formulario": mi_formulario })  

  else:

    mi_formulario = AuthenticationForm()
    return render(req, "login.html", { "mi_formulario": mi_formulario })  


def register(req):

  if req.method == 'POST':
    
    mi_formulario= UserCreationForm(req.POST)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data
      usuario = data['username']
      mi_formulario.save()

      return render(req, "inicio.html", { "mensaje": f"Usuario {usuario} creado exitosamente!"})

    else:
      return render(req, "registro.html", { "mi_formulario": mi_formulario })    

  else:

    mi_formulario = UserCreationForm()
    return render(req, "registro.html", { "mi_formulario": mi_formulario })

@login_required()
def editar_perfil(req):

  usuario = req.user

  if req.method == 'POST':
    
    mi_formulario= UserEditForm(req.POST, instance=req.user)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data
      usuario.first_name = data['first_name']
      usuario.last_name = data['last_name']
      usuario.email = data['email']
      usuario.set_password(data["password1"])
      usuario.save()

      return render(req, "inicio.html", { "mensaje": f"Datos actualizados exitosamente!"})

    else:
      return render(req, "editar_perfil.html", { "mi_formulario": mi_formulario })    

  else:

    mi_formulario = UserEditForm(instance=req.user)
    return render(req, "editar_perfil.html", { "mi_formulario": mi_formulario })  
  
@login_required()
def agregar_avatar(req):

  if req.method == 'POST':
    
    mi_formulario= AvatarFormulario(req.POST, req.FILES)
    if mi_formulario.is_valid():

      data = mi_formulario.cleaned_data
      avatar = Avatar(user=req.user, imagen=data["imagen"])
      avatar.save()

      return render(req, "inicio.html", { "mensaje": f"Avatar cread correctamente!"})

    else:
      return render(req, "agregar_avatar.html", { "mi_formulario": mi_formulario })    

  else:

    mi_formulario = AvatarFormulario()
    return render(req, "agregar_avatar.html", { "mi_formulario": mi_formulario })
  
def get_entregables_by_estudiante(req, id):

    estudiante = Estudiante.objects.get(id=id)
    
    entregables = Entregable.objects.filter(estudiante=estudiante)
    
    context = {
        'estudiante': estudiante,
        'entregables': entregables
    }
    
    return render(req, 'entregables_por_estudiante.html', context)

def get_estudiantes_by_curso(req, id):

    curso = Curso.objects.get(id=id)
    
    estudiantes = curso.estudiantes.all()
    
    context = {
        'curso': curso,
        'estudiantes': estudiantes
    }
    
    return render(req, 'estudiantes_por_curso.html', context)

