from django.shortcuts import render, redirect
from Archivo.models import Post, Archivo
from .forms import DocumentForm
from django.contrib import messages

# Create your views here.

def Archivo(request):
    if request.method == 'POST':
        form =  DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')            
    else:
        form =  DocumentForm()
    return render(request, 'archivo/archivo.html', {'form':form})