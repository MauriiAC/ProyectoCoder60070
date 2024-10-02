from django.contrib import admin
from .models import Curso, Entregable, Estudiante, Profesor, Avatar
from datetime import datetime

class CursoAdmin(admin.ModelAdmin):

  list_display = ['nombre', 'camada']
  search_fields = ['nombre', 'camada']
  list_filter = ['nombre']

class EntregableAdmin(admin.ModelAdmin):

  list_display = ['nombre', 'fecha_entrega', 'entregado', 'antiguedad']

  def antiguedad(self, object):
    if object.fecha_entrega:
      return (datetime.now().date() - object.fecha_entrega).days

# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Entregable, EntregableAdmin)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Avatar)
