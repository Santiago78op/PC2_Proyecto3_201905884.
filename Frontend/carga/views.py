from django.shortcuts import redirect, render
from .forms import DocumentForm
from .models import Diccionario

# Create your views here.

def cargar(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = DocumentForm()
    return render(request, 'carga/carga.html',{'form': form})