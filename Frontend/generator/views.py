from distutils.command.upload import upload
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import Document
import shutil
import requests as req
import json

# Create your views here.
def Home(request):
    result = ''
    if request.method == 'POST' and 'send' in request.POST:
        file_name = request.POST.get('archivo')
        files = Document.objects.all()
        for file in files:
            if file.title == file_name:
                root = file.document
                result = sendInfo(root)['data']
                context = {'result':result}
                data = ''
                return render(request,'page/home.html', {'result':result,'Files': Document.objects.all(),'data':data})
    if  request.method == 'POST' and 'reset' in request.POST:
        Document.objects.all().delete()
        dir_path = 'media/documents/xml'
        shutil.rmtree(dir_path)
        data = ''
        return render(request,'page/home.html', {'result':result,'Files': Document.objects.all(),'data':data})
    data = ''
    return render(request,'page/home.html', {'result':result,'Files': Document.objects.all(),'data':data})

def UploadFile(request):
    if request.method == 'POST':
        context = {}
        # upload_file = request.FILES['document']
        upload_file = DocumentForm(request.POST,request.FILES)
        if upload_file.is_valid():
            #Document.objects.create(title = request.POST.get('title'),document = request.FILES['document'])
            # print(request.POST.get('title'))
            # print(request.FILES['document']) id = titulo, id = ruta
            upload_file.save()
        form = DocumentForm()
        context = {
            'form':form,
        }
        return render(request, 'page/upload.html', context)
    else:
        form = DocumentForm()
        context = {
            'form':form,
        }
        return render(request, 'page/upload.html', context)

def consultData(request):
    valor = setInfo()
    return render(request,'page/home.html', {'result':valor['input'],'Files': Document.objects.all(),'data':valor['out']})

def sendInfo(root):
    root = str(root)
    data = {'ruta': root}
    print(data)
    response = req.post('http://127.0.0.1:5000/contenido',json = data)
    return json.loads(response.text)

def setInfo():
    response = req.post('http://127.0.0.1:5000/respuesta')
    return json.loads(response.text)
