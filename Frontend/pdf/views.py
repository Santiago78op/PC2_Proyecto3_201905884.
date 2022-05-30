from django.shortcuts import render, redirect
from carga.models import Documents,Diccionario,Imagen
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
# Create your views here.

def pdf(request):
    files = Documents.objects.all() 
    if request.method == 'POST':
        if 'pdfs' in request.POST:
            files = Documents.objects.all()
            file_name = request.POST.get('archivo')
            if file_name != 'Files':
                for file in files:
                    if file.titulo == file_name:
                        archivos = Documents.objects.get(id=file.id)
                        diccionario = Diccionario.objects.filter(categorias=archivos)
                        if diccionario:
                            diccionario = Diccionario.objects.get(categorias=archivos)
                            imagen = Imagen.objects.filter(categorias=archivos)
                            if imagen:
                                context = {'dict': diccionario, 'img':imagen,'name':archivos}
                            else:
                                context = {'dict': diccionario,'name':archivos}
                            template_path = get_template('pdf/pdf.html')
                            # Create a Django response object, and specify content_type as pdf
                            response = HttpResponse(content_type='application/pdf')
                            response['Content-Disposition'] = f'attachment; filename="report_{file.titulo}.pdf"'
                            # find the template and render it.
                            html = template_path.render(context)

                            # create a pdf
                            pisa_status = pisa.CreatePDF(
                            html, dest=response)
                            # if error then show some funny view
                            if pisa_status.err:
                                return HttpResponse('We had some errors <pre>' + html + '</pre>')
                            return response
                        else:
                            respuesta = "EL archivo debe ser Procesado antes"
                            return render(request,'pdf/aviso_pdf.html', {'respuesta':respuesta})
                            
            else:
                return render(request,'pdf/consulta_pdf.html', {'documentos':files})      
    else:
        files = Documents.objects.all()       
    return render(request,'pdf/consulta_pdf.html', {'documentos':files})


