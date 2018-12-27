# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import RegModelForm, ContacForm

from django.shortcuts import render

from .models import Registrados

# Create your views here.
def inicio(request):
    titulo = "Registro"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" %(request.user)
   
    form = RegModelForm(request.POST or None)
    
    context = {
        "titulo" : titulo,
        "formulario": form 
    }
    #print (dir(form))
    if form.is_valid():
      instance = form.save(commit=False)
      if not instance.nombre :
          instance.nombre = "Persona"
      instance.save()
      print instance
      print instance.fecha
      context = {
          "titulo" : "Gracias por registrarse",
          
      }

    #    #print form.cleaned_data
    #    formData = form.cleaned_data
    #    print formData.get("nombre")
    #    print formData.get("email")
    #    email = formData.get("email")
    #    nombre = formData.get("nombre")
    #    obj = Registrados.objects.create(email=email,nombre=nombre)
    
    return render(request, "inicio.html", context)

def home(request):
    
    context = {
        "titulo":"Home"
    }
    return render(request, "base.html",context)


def contact(request):
    form = ContacForm (request.POST or None)
    if form.is_valid() :
        email = form.cleaned_data.get("email")
        nombre = form.cleaned_data.get("nombre")
        mensaje = form.cleaned_data.get("mensaje")
    context = {
        "titulo" : "Contacto",
        "formulario" : form
    }

    return render(request, "contacto.html", context)