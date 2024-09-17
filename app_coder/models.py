from django.db import models

# Create your models here.
class Curso(models.Model):

  nombre = models.CharField(max_length=50)
  camada = models.IntegerField()

  def __str__(self):
    return f'{self.nombre} - {self.camada}'
  
  class Meta():

    verbose_name = 'Course'
    verbose_name_plural = 'My courses...'
    ordering = ('-nombre', 'camada')

class Estudiante(models.Model):

  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField()

  def __str__(self):
    return f'{self.nombre} {self.apellido}'

class Profesor(models.Model):

  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField()
  profesion = models.CharField(max_length=50, null=True)

class Entregable(models.Model):

  nombre = models.CharField(max_length=50)
  fecha_entrega = models.DateField()
  entregado = models.BooleanField()
  estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)


  def __str__(self):
    return f'{self.nombre}'

