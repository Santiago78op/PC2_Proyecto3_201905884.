import io
from django.shortcuts import render, redirect
from carga.models import Documents,Diccionario,Imagen
from django.core.files import File
from django.core.files.images import ImageFile
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np 
import requests as req
import json
from shutil import rmtree

# Create your views here.

def rango(request):
    files = Documents.objects.all() 
    if request.method == 'POST':
        if 'rangos' in request.POST:
            files = Documents.objects.all()
            file_name = request.POST.get('archivo')
            if file_name != 'Files':
                for file in files:
                    if file.titulo == file_name:
                        archivos = Documents.objects.get(id=file.id)
                        diccionario = Diccionario.objects.filter(categorias=archivos)
                        if diccionario:
                            diccionario = Diccionario.objects.get(categorias=archivos)
                            return redirect('rangofecha',fehca_rango=file.id)
                        else:
                            respuesta = "EL archivo debe ser Procesado antes"
                            return render(request,'rango/aviso_rango.html', {'respuesta':respuesta})
                            
            else:
                return render(request,'rango/rango_fecha.html', {'documentos':files})     
        elif 'clsr' in request.POST:
            files = Documents.objects.all()
            file_name = request.POST.get('archivo')
            if file_name != 'Files':
                for file in files:
                    if file.titulo == file_name:
                        archivos = Documents.objects.get(id=file.id)
                        imgs = Imagen.objects.filter(categorias=archivos)
                        if imgs:
                            for img in imgs:
                                img.delete()
                            rmtree("media/img")  
                        else:
                            respuesta = "EL archivo no contiene Graficas"
                            return render(request,'rango/aviso_rango.html', {'respuesta':respuesta})
                            
            else:
                return render(request,'rango/rango_fecha.html', {'documentos':files})  
    else:
        files = Documents.objects.all()       
    return render(request,'rango/rango_fecha.html', {'documentos':files})

def rango_fecha(request,fehca_rango):
    if request.method == 'POST':
        if 'graficar' in request.POST: 
            archivos = Documents.objects.get(id=fehca_rango)
            diccionario = Diccionario.objects.get(categorias=archivos)
            date_name = request.POST.getlist('checks')
            emp_name = request.POST.get('empresa_cls')
            if emp_name != 'Empresa' and len(date_name) != 0:
                lista_dates = list()
                cont = 0
                for fecha in date_name:
                    date_positive = list()
                    date_negative = list()
                    date_neutral = list()
                    for fechas in diccionario.newDiccionario:
                        if fecha == fechas['fecha']:
                            cont += 1
                            div_name = f'container_{cont}'
                            date = fechas['fecha']
                            mgs_positivos = fechas['positivos_mgs']
                            date_positive.append(mgs_positivos)
                            mgs_negativos = fechas['negativos_mgs']
                            date_negative.append(mgs_negativos)
                            mgs_neutros = fechas['neutros_msg']
                            date_neutral.append(mgs_neutros)
                            positivos = json.dumps(date_positive)
                            negativos = json.dumps(date_negative)
                            neutrales = json.dumps(date_neutral)
                            nombre = 'Fechas'
                            name = f'Clasificaci??n por {fecha}'
                            cantidad = 1
                            imageRango(name,archivos,cantidad,nombre,[date],date_positive,date_negative,date_neutral)
                            if emp_name != 'empresas':
                                lista_empresas = []
                                lista_pistivos = []
                                lista_negativos = []
                                lista_neutros = []
                                div_name_emp = f'div_name_emp{cont}'
                                for empresa in fechas['empresas']:
                                    if emp_name == empresa['empresa']:
                                        emp = empresa['empresa']
                                        lista_empresas.append(emp)
                                        mgs_positivos = empresa['positivos_mgs']
                                        lista_pistivos.append(mgs_positivos)
                                        mgs_negativos = empresa['negativos_mgs']
                                        lista_negativos.append(mgs_negativos)
                                        mgs_neutros = empresa['neutros_msg']
                                        lista_neutros.append(mgs_neutros) 
                                emps = json.dumps(lista_empresas)
                                positivos_emp = json.dumps(lista_pistivos)
                                negativos_emp = json.dumps(lista_negativos)
                                neutrales_emp = json.dumps(lista_neutros)
                                nombre = 'Empresas'
                                name = f'Clasificaci??n empresas a {fecha}'
                                cantidad = len(lista_empresas)
                                imageRango(name,archivos,cantidad,nombre,lista_empresas,lista_pistivos,lista_negativos,lista_neutros)
                                emp_mgs = {'div_name_emp':div_name_emp,'emps':emps,'positivos_emp':positivos_emp,'negativos_emp':negativos_emp,'neutros_emp':neutrales_emp}
                            else:
                                lista_empresas = []
                                lista_pistivos = []
                                lista_negativos = []
                                lista_neutros = []
                                div_name_emp = f'div_name_emp{cont}'
                                for empresa in fechas['empresas']:
                                    emp = empresa['empresa']
                                    lista_empresas.append(emp)
                                    mgs_positivos = empresa['positivos_mgs']
                                    lista_pistivos.append(mgs_positivos)
                                    mgs_negativos = empresa['negativos_mgs']
                                    lista_negativos.append(mgs_negativos)
                                    mgs_neutros = empresa['neutros_msg']
                                    lista_neutros.append(mgs_neutros) 
                                emps = json.dumps(lista_empresas)
                                positivos_emp = json.dumps(lista_pistivos)
                                negativos_emp = json.dumps(lista_negativos)
                                neutrales_emp = json.dumps(lista_neutros)
                                nombre = 'Empresas'
                                name = f'Clasificaci??n empresas a {fecha}'
                                cantidad = len(lista_empresas)
                                imageRango(name,archivos,cantidad,nombre,lista_empresas,lista_pistivos,lista_negativos,lista_neutros)
                                emp_mgs = {'div_name_emp':div_name_emp,'emps':emps,'positivos_emp':positivos_emp,'negativos_emp':negativos_emp,'neutros_emp':neutrales_emp}
                                
                    dates_mgs = {'class':'page-section cta','date':date,'div_name':div_name,'positivos_date':positivos,'negativos_date':negativos,'neutros_date':neutrales,'emp_mgs':emp_mgs}
                    lista_dates.append(dates_mgs)
                return render(request,'rango/grafica_rango.html',{'lista_dates':lista_dates})  
            else:
                return render(request,'rango/rangos_fecha.html',{'datos':diccionario})
    else:
        archivos = Documents.objects.get(id=fehca_rango)
        diccionario = Diccionario.objects.get(categorias=archivos)
    return render(request,'rango/rangos_fecha.html',{'datos':diccionario})


def imageRango(name,archivos,cantidad,nombre,dato,comment_positive,comment_negative,comment_neutral):
    figure = io.BytesIO()
    x = np.arange(cantidad) 
    y1 = comment_positive
    y2 = comment_negative
    y3 = comment_neutral
    width = 0.2
    
    plt.title(f'Grafica por {nombre}')
    plt.bar(x-0.2, y1, width, color='skyblue') 
    plt.bar(x, y2, width, color='brown') 
    plt.bar(x+0.2, y3, width, color='green') 
    plt.xticks(x, dato) 
    plt.xlabel(f'{nombre}') 
    plt.ylabel("Puntos") 
    plt.legend(["Mgs Positivos", "Mgs Negativos", "Mgs Neutros"]) 
    plt.savefig(f'rango/images_rango/{nombre}.png')
    plt.close()
    # plt.savefig(figure, format="png")
    # content_file = ImageFile(figure)
    imagen = Imagen.objects.create(categorias=archivos, nombre=name)
    imagen.imagenes = ImageFile(open(f'rango/images_rango/{nombre}.png', "rb"))
    imagen.save()
    # diccionario.imagen.save(f'{nombre}.png', content_file)
    # diccionario.save()
    #plt.show()

def setClFecha(info_dict):
    data = {'dict': info_dict}
    response = req.post('http://127.0.0.1:5000/clasificacion', json = data)
    return json.loads(response.text)