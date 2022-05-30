from django.shortcuts import render
from carga.models import Documents,Diccionario
from shutil import rmtree
import requests as req
import json
import os

# Create your views here.

def home(request):
    result = ''
    if request.method == 'POST':
        if 'send' in request.POST:
            files = Documents.objects.all()
            file_name = request.POST.get('archivo')
            if file_name != 'Files':
                for file in files:
                    if file.titulo == file_name:
                        root = file.documento
                        result = sendInfo(root)
                        archivos = Documents.objects.get(id=file.id)
                        diccionario = Diccionario.objects.filter(categorias=archivos)
                        if diccionario:
                            result = 'Este Archivo ya fue Procesado'
                            files = Documents.objects.all()
                            return render(request,'home/home.html', {'result':result,'documentos':files})
                        else:
                            diccionario = Diccionario.objects.create(categorias=archivos,diccionario=result['dict'],newDiccionario=result['newData'])
                            diccionario.save()
                        return render(request,'home/home.html', {'result':result['data'],'documentos':files})
            else:
                return render(request,'home/home.html', {'result':result,'documentos':files})                
        elif 'reset' in request.POST:
            files = Documents.objects.all()
            if files:
                for file in files:
                    file.delete()
                    path = "media/{}".format(file.documento)
                    os.remove(path)
                exitste = os.path.exists('"media/img"')
                if exitste:
                    rmtree("media/img")
                respuesta = "Los Archivos se Eliminaron"
            else:
                respuesta = "No se Encontraron Archivos"
            return render(request,'home/aviso.html', {'respuesta':respuesta})
    else:
        documentos = Documents.objects.all()
        result = ''
    return render(request, 'home/home.html', {'result':result,'documentos':documentos})


def sendInfo(root):
    root = str(root)
    data = {'ruta': root}
    response = req.post('http://127.0.0.1:5000/contenido', json = data)
    return json.loads(response.text)
