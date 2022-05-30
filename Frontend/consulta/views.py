from django.shortcuts import render
from carga.models import Documents,Diccionario
import requests as req
import json

# Create your views here.

def registro(request):
    result = ''
    files = Documents.objects.all() 
    if request.method == 'POST':
        if 'consulta' in request.POST:
            files = Documents.objects.all()
            file_name = request.POST.get('archivo')
            if file_name != 'Files':
                for file in files:
                    if file.titulo == file_name:
                        archivos = Documents.objects.get(id=file.id)
                        diccionario = Diccionario.objects.filter(categorias=archivos)
                        if diccionario:
                            root = file.documento
                            result = sendInfo(root)['data']
                            diccionario = Diccionario.objects.get(categorias=archivos)
                            info_dict = diccionario.diccionario
                            data = setInfo(info_dict)
                            return render(request,'consulta/consulta.html', {'result':result,'documentos':files,'data':data['data']})
                        else:
                            respuesta = "EL archivo debe ser Procesado antes"
                            return render(request,'consulta/aviso_consulta.html', {'respuesta':respuesta})
                            
            else:
                return render(request,'consulta/registro.html', {'result':result,'documentos':files})      
    else:
        files = Documents.objects.all()        
    return render(request,'consulta/registro.html', {'result':result,'documentos':files})

def sendInfo(root):
    root = str(root)
    data = {'ruta': root}
    response = req.post('http://127.0.0.1:5000/contenido', json = data)
    return json.loads(response.text)

def setInfo(info_dict):
    data = {'dict': info_dict}
    response = req.post('http://127.0.0.1:5000/respuesta', json = data)
    return json.loads(response.text)