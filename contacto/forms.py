from django import forms

class FormularioContacto(forms.Form):
  nombre = forms.CharField(label='Nombre*', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder':'Ingrese su nombre', 'class':'form-control my-2'}))
  email = forms.CharField(label='Email*', required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder':'nombre@ejemplo.com', 'class':'form-control my-2'}))
  contenido = forms.CharField(label='Contenido*', max_length=200, required=True, widget=forms.Textarea(attrs={'placeholder':'Escriba su comentario', 'cols':30, 'rows': 5, 'class':'form-control my-2'}))