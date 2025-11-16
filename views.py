from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Carro
from .forms import CarroForm

def lista_carros(request):
    """Vista para mostrar la lista de todos los carros"""
    carros = Carro.objects.all()
    return render(request, 'carros/lista.html', {'carros': carros})

def crear_carro(request):
    """Vista para crear un nuevo carro"""
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_carros')
    else:
        form = CarroForm()
    return render(request, 'carros/crear_editar.html', {
        'form': form,
        'titulo': 'Crear Nuevo Carro',
        'boton': 'Crear Carro'
    })

def editar_carro(request, pk):
    """Vista para editar un carro existente"""
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('lista_carros')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'carros/crear_editar.html', {
        'form': form,
        'titulo': f'Editar Carro: {carro.marca} {carro.modelo}',
        'boton': 'Guardar Cambios',
        'carro': carro
    })

@require_http_methods(["POST"])
def eliminar_carro(request, pk):
    """Vista para eliminar un carro"""
    carro = get_object_or_404(Carro, pk=pk)
    carro.delete()
    return redirect('lista_carros')
