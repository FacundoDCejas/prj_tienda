from django.shortcuts import render, redirect
from .models import *
from .forms import PersonaForm,EmpleadoForm,ArticuloForm

def index(request,template_name="tienda/index.html"):
    return render(request,template_name)


def persona_listar(request, template_name='tienda/personas.html'):
    personas = Persona.objects.all()
    dato_persona = {'personas': personas}
    return render(request, template_name, dato_persona)


def empleado_listar(request, template_name='tienda/empleados.html'):
    empleados = Empleado.objects.all()
    dato_empleado = {'empleados': empleados}
    return render(request, template_name, dato_empleado)


def nueva_persona(request, template_name='tienda/persona_form.html'):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('persona_listar')
        else:
            print(form.errors)
    else:
        form = PersonaForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def modificar_persona(request, pk, template_name='tienda/persona_form.html'):
    persona = Persona.objects.get(num_doc=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect("persona_listar")
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request,template_name,datos)

def modificar_empleado(request, pk, template_name='tienda/empleado_form.html'):
    empleado = Empleado.objects.get(legajo=pk)
    form = EmpleadoForm(request.POST or None, instance=empleado)
    if form.is_valid():
        form.save(commit=True)
        return redirect("empleado_listar")
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request,template_name,datos)


def eliminar_persona(request,pk ,template_name='tienda/persona_confirmar_eliminacion.html'):
    persona = Persona.objects.get(num_doc=pk)
    if request.method =="POST":
        persona.delete()
        return redirect('persona_listar')
    else:
        dato ={"form": persona}
        return render(request,template_name,dato)

def articulos_listar(request, template_name='tienda/articulos.html'):
    articulos = Articulo.objects.all()
    dato_articulo = {'articulos': articulos}
    return render(request, template_name, dato_articulo)

def nuevo_articulo(request, template_name='tienda/articulo_form.html'):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('articulos_listar')
        else:
            print(form.errors)
    else:
        form = ArticuloForm()
    dato = {"form": form}
    return render(request, template_name, dato) 

def modificar_articulo(request, pk, template_name='tienda/articulo_form.html'):
    articulo = Articulo.objects.get(id=pk)
    form = ArticuloForm(request.POST or None, instance=articulo)
    if form.is_valid():
        form.save(commit=True)
        return redirect("articulos_listar")
    else:
        print(form.errors)
    datos = {'form':form}
    return render(request,template_name,datos)

def eliminar_articulo(request,pk ,template_name='tienda/articulo_confirmar_eliminacion.html'):
    articulo = Articulo.objects.get(id=pk)
    if request.method =="POST":
        articulo.delete()
        return redirect('articulos_listar')
    else:
        dato ={"form": articulo}
        return render(request,template_name,dato)