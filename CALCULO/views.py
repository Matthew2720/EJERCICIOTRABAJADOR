from django.shortcuts import render,redirect
from .forms import *
from .models import *

def index(request):
    trabajadores = Trabajador.objects.all()
    return render(request,'index.html',{'trabajadores' : trabajadores})

def registro(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid:
            form.save()
    form = TrabajadorForm
    context = {'form': form }
    return render(request,'registro.html',context)

def actualizar(request,id):
    trabajador = Trabajador.objects.get(id=id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST,instance=trabajador)
        if form.is_valid:
            form.save()
            return redirect('index')
    form = TrabajadorForm(instance=trabajador)
    context = {'form': form }
    return render(request,'registro.html',context)

def eliminar(request,id):
    trabajador = Trabajador.objects.get(id = id)
    trabajador.delete()
    return redirect('index')