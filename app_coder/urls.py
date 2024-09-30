from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path('lista-cursos-old/', lista_cursos),
    path('', inicio, name='Inicio'),
    path('profesores/', profesores, name='Profesores'),
    path('cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('curso-formulario/', curso_formulario, name='CursoFormulario'),
    path('busqueda-camada/', busqueda_camada, name='BusquedaCamada'),
    path('buscar-camada/', buscar_camada, name='BuscarCamada'),
    path('lista-profesores/', lista_profesores, name='ListaProfesores'),
    path('crea-profesor/', crea_profesor, name='CreaProfesor'),
    path('elimina-profesor/<int:id>', eliminar_profesor, name='EliminaProfesor'),
    path('editar-profesor/<int:id>', editar_profesor, name='EditarProfesor'),
    path('lista-cursos/', CursoList.as_view(), name='ListaCursos'),
    path('detalle-curso/<pk>', CursoDetail.as_view(), name='DetalleCurso'),
    path('crea-curso/', CursoCreate.as_view(), name='CreaCurso'),
    path('actualiza-curso/<pk>', CursoUpdate.as_view(), name='ActualizaCurso'),
    path('elimina-curso/<pk>', CursoDelete.as_view(), name='EliminaCurso'),
    path('login/', login_view, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='Logout'),
]
