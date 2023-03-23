from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
  formulario_contacto = FormularioContacto()
  if request.method=='POST':
    formulario_contacto = FormularioContacto(data=request.POST)
    if formulario_contacto.is_valid():
      nombre = request.POST.get('nombre')
      email = request.POST.get('email')
      contenido = request.POST.get('contenido')

      email = EmailMessage("Mensaje desde contacto backend", f"El usuario con nombre {nombre} con correo electrónico {email} escribe lo siguiente: \n\n {contenido}", "", ['jairo251180@gmail.com'], reply_to=[email])

      try:
        email.send()
        return redirect('/contacto/?valid')
      except:
        return redirect('/contacto/?novalid')

  return render(request, 'contacto/contacto.html', {'mi_form':formulario_contacto})