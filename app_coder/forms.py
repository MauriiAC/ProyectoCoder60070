from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Curso, Avatar

# class CursoFormulario(forms.Form):

#   curso = forms.CharField()
#   camada = forms.IntegerField()

class CursoFormulario(forms.ModelForm):

  class Meta:
    model=Curso
    fields=('__all__')
    widgets = {
      'nombre': forms.TextInput(
        attrs={
          'placeholder': "Nombre curso...",
          "class": "input-curso-nombre"
        }
      )
    }

class ProfesorFormulario(forms.Form):

  nombre = forms.CharField()
  apellido = forms.CharField()
  email = forms.EmailField()
  profesion = forms.CharField()


class UserEditForm(UserChangeForm):

  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
  )

  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('email', 'first_name', 'last_name')

  def clean_password2(self):
    
    print(self.cleaned_data)

    password1 = self.cleaned_data["password1"]
    password2 = self.cleaned_data["password2"]

    if password2 != password1:
      raise forms.ValidationError("Las contraseñas no son iguales")
    
    else:
      return password2

class AvatarFormulario(forms.ModelForm):

  class Meta:
    model=Avatar
    fields=('imagen',)