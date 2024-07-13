from django.shortcuts import render,HttpResponse, redirect
#importando las funciones para la autenticacion de usuarios
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from BaseDeDatos.forms import ContactoForms
from BaseDeDatos.models import Contacto
from django.template import loader
from django.contrib import messages

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render())

def contacto(request):
    return render(request,"core/contact.html")

def portafolio(request):
    return render(request,"core/portfolios.html")

#codigo logueo con django
@login_required
def ingreso_registro(request):
    group_name = None
    if request.user.is_authenticated:
        group = Group.objects.filter(user=request.user).first()
        if group:
            group_name = group.name

    context = {
        'group_name': group_name
    }
    return render(request, 'core/gerente.html', context)


def cerrar_sesion(request):
    logout(request)
    return redirect("/")


def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForms(request.POST)
        if formulario.is_valid():
            contacto = formulario.save(commit=False)
            # Asigna un valor incremental al campo código
            try:
                ultimo_contacto = Contacto.objects.order_by('-codigo').first()
            except Contacto.DoesNotExist:
                ultimo_contacto = None

            nuevo_codigo = ultimo_contacto.codigo + 1 if ultimo_contacto else 1
            contacto.codigo = nuevo_codigo
            contacto.save()
            messages.success(request,"Formulario enviado exitosamente")
            return redirect(to="contact")
    else:
        formulario = ContactoForms()
    return render(request, "core/contact.html", {'form': formulario})



