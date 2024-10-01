from django.test import TestCase
from django.urls import reverse
from .models import Profesor

# Create your tests here.
class EliminarProfesor(TestCase):

  def setUp(self):
    self.profesor1 = Profesor.objects.create(
      nombre="Cristiano",
      apellido="Ronaldo",
      email="cr7@gmail.com",
      profesion="futbolista"
    )
    self.url = reverse('EliminaProfesor', args=[self.profesor1.id])
  
  def test_eliminar_profesor(self):
    respuesta = self.client.post(self.url)
    self.assertEqual(respuesta.status_code, 200)
    self.assertTemplateUsed(respuesta, "leer_profesores.html")
    self.assertQuerySetEqual(Profesor.objects.all(), [])