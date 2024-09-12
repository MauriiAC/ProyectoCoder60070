from django.db import models

# Create your models here.
class Curso(models.Model):

  nombre = models.CharField(max_length=50)
  camada = models.IntegerField()

class Estudiante(models.Model):

  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField()

class Profesor(models.Model):

  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField()
  profesion = models.CharField(max_length=50, null=True)

class Entregable(models.Model):

  nombre = models.CharField(max_length=50)
  fecha_entrega = models.DateField()
  entregado = models.BooleanField()



