from django.shortcuts import redirect,render
from Archivo.models import Post, Archivo
# Create your views here.

def home(request):
    result = ''
    if request.method == 'POST':
        if 'send' in request.POST:
            Files = Archivo.objects.all()
            return render(request, 'ProyectoWebApp/home.html', {'Files':Files})
    else:    
        Files = Archivo.objects.all()
        return render(request, 'ProyectoWebApp/home.html',{'Files':Files})