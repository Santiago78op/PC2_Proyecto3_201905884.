from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
from readXML import XML
import re

app = Flask(__name__)
read = XML()

@app.route('/')
def index():
    return '<h1>Hello!</h1>'


@app.route('/contenido',methods = ['POST'])
def parseInfo():
    body = request.get_json()
    ruta = body['ruta']


    content = read.readXML(ruta)
    read.reserver(content)
    return jsonify({'data':read.entrada})

@app.route('/respuesta',methods = ['POST'])
def setInfo():    
    contenido = read.algoritmo()
    read.createXML(contenido)
    
    file = open("../Frontend/media/documents/xml/salida.xml",'r', encoding="utf-8")
    salida = ''
    for line in file:
        salida += line
    file.close() 
        
    return jsonify({'input':read.entrada,'out':salida})

# if __name__ == '__main__':
#     app.run(port = 5000,debug = True)