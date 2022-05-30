from django.shortcuts import render, redirect
from carga.models import Documents,Diccionario
import requests as req
import json
# Create your views here.

def prueba(request):
    result = ''
    files = Documents.objects.all() 
    if request.method == 'POST':
        if 'test' in request.POST:
            files = Documents.objects.all()
            file_name = request.POST.get('archivo')
            if file_name != 'Files':
                for file in files:
                    if file.titulo == file_name:
                        archivos = Documents.objects.get(id=file.id)
                        diccionario = Diccionario.objects.filter(categorias=archivos)
                        if diccionario:
                            return redirect('Probar',prueba=file.id)
                        else:
                            respuesta = "EL archivo debe ser Procesado antes"
                            return render(request,'prueba/aviso_prueba.html', {'respuesta':respuesta})
    else:
        files = Documents.objects.all()
    return render(request, 'prueba/consulta_prueba.html',{'documentos':files})


def probar(request,prueba):
    resultado = ''
    if request.method == 'POST':
        if 'probar' in request.POST:
            archivos = Documents.objects.get(id=prueba)
            diccionario = Diccionario.objects.get(categorias=archivos)
            datos = diccionario.diccionario
            text_prueba = request.POST.get('Textarea1')
            salida_prueba = sendPrueba(text_prueba,datos)['data']
            return render(request, 'prueba/prueba.html', {'data':salida_prueba})
    else:
        resultado = ''
    return render(request, 'prueba/prueba.html', {'data':resultado})

def sendPrueba(text_prueba,datos):
    text_prueba = str(text_prueba)
    data = {'prueba': text_prueba,'datos':datos}
    response = req.post('http://127.0.0.1:5000/prueba', json = data)
    return json.loads(response.text)