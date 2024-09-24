from django import forms

class CursoFormulario(forms.Form):

  curso = forms.CharField()
  camada = forms.IntegerField()
    

class ProfesorFormulario(forms.Form):

  nombre = forms.CharField()
  apellido = forms.CharField()
  email = forms.EmailField()
  profesion = forms.CharField()

