
# render: combina una plantilla con datos
# redirect: redirige a otra pagina
# get_object_or_404: busca un registro o muestra error 404
from django.shortcuts import render, redirect, get_object_or_404

# connection: permite consultar la configuracion de la base de datos
from django.db import connection

# login_required: exige iniciar sesion
from django.contrib.auth.decorators import login_required

# Servicio: modelo de la base de datos
from .models import Servicio

# ServicioForm: formulario creado en forms.py
from .forms import ServicioForm


# Vista de inicio de la Semana 3
def inicio(request):
    # Obtiene la informacion de la base de datos
    info_bd = connection.settings_dict

    # Datos que se envian a la plantilla
    contexto = {
        'motor': info_bd['ENGINE'],
        'host': info_bd['HOST'],
    }

    # Muestra la pagina de inicio
    return render(request, 'core/inicio.html', contexto)


# Vista que muestra todos los servicios
def servicios(request):
    # Obtiene los servicios guardados en MySQL
    lista_servicios = Servicio.objects.all()

    # Envia los servicios a la plantilla
    return render(request, 'core/servicios.html', {
        'servicios': lista_servicios
    })


# Exige que el usuario inicie sesion
@login_required
def crear_servicio(request):

    # Comprueba si se envio el formulario
    if request.method == 'POST':

        # Recibe los datos escritos
        form = ServicioForm(request.POST)

        # Comprueba que los datos sean correctos
        if form.is_valid():

            # Crea el servicio sin guardarlo todavia
            nuevo = form.save(commit=False)

            # Asigna el usuario que inicio sesion
            nuevo.propietario = request.user

            # Guarda el servicio en la base de datos
            nuevo.save()

            # Regresa al listado de servicios
            return redirect('servicios')

    else:
        # Crea un formulario vacio
        form = ServicioForm()

    # Muestra el formulario
    return render(request, 'core/servicio_form.html', {
        'form': form,
        'titulo_pagina': 'Nuevo servicio'
    })


# Exige que el usuario inicie sesion para editar
@login_required
def editar_servicio(request, pk):

    # Busca el servicio por su ID
    # Si no existe, muestra error 404
    servicio = get_object_or_404(Servicio, pk=pk)

    # Comprueba si el usuario envio cambios
    if request.method == 'POST':

        # Carga los datos nuevos sobre el servicio existente
        form = ServicioForm(request.POST, instance=servicio)

        # Comprueba que los datos sean validos
        if form.is_valid():

            # Guarda los cambios en MySQL
            form.save()

            # Regresa al listado de servicios
            return redirect('servicios')

    else:
        # Muestra el formulario con los datos actuales
        form = ServicioForm(instance=servicio)

    # Utiliza el mismo formulario de crear servicios
    return render(request, 'core/servicio_form.html', {
        'form': form,
        'titulo_pagina': 'Editar servicio'
    })


# Exige que el usuario inicie sesion para eliminar
@login_required
def eliminar_servicio(request, pk):

    # Busca el servicio por su ID
    # Si no existe, muestra error 404
    servicio = get_object_or_404(Servicio, pk=pk)

    # Solo elimina cuando el usuario confirma
    if request.method == 'POST':

        # Elimina el servicio de MySQL
        servicio.delete()

        # Regresa al listado de servicios
        return redirect('servicios')

    # Muestra la pantalla para confirmar
    return render(request, 'core/servicio_confirm_delete.html', {
        'servicio': servicio
    })
