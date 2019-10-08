from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from .forms import cuestionario_form, pregunta_form
# Create your views here.

def index(request):
    return render_to_response('index.html')

def nuevo_cuestionario(request):
    if request.method=='POST':
        form = cuestionario_form(request.POST)
        if form.is_valid():
            cuest = form.save()
            cuest.save()
            return redirect('index')
    else:
        form = cuestionario_form()
    return render(request,'cuestionario_nuevo.html',{'form':form})

def nueva_pregunta(request, pk):
    if request.method=='POST':
        f = pregunta_form(request.POST)
        if f.is_valid():
            preg = f.save()
            preg.id_cuestionario = pk
            preg.save()
            return redirect('index')
    else:
        f = pregunta_form()
    return render(request,'pregunta_nueva.html',{'form':f})
            
    