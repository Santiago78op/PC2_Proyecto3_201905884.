from email import message
from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET
from readXML import XML

app = Flask(__name__)
read = XML()

@app.route('/')
def index():
    return '<h1>Hello!</h1>'


@app.route('/contenido',methods = ['POST'])
def parseInfo():
    body = request.get_json()
    ruta = body['ruta']
    content = read.entrada(ruta)
    dict_content = read.readXML(ruta)
    resp = read.reserver(dict_content)
    intrucciones = read.algoritmo()
    return jsonify({'data': content,'dict':dict_content,'newData':intrucciones})

@app.route('/respuesta',methods = ['POST'])
def setInfo():
    body = request.get_json()
    dict = body['dict']
    resp = read.reserver(dict)
    intrucciones = read.algoritmo()
    read.createXML(intrucciones)
    root = 'documents/salida.xml'
    respuesta = read.entrada(root)
    return jsonify({'data': respuesta, 'newData':intrucciones})

@app.route('/clasificacion',methods = ['POST'])
def clasificacionFecha():
    body = request.get_json()
    dict = body['dict']
    resp = read.reserver(dict)
    intrucciones = read.algoritmo()
    return jsonify({'data': intrucciones})

@app.route('/prueba',methods = ['POST'])
def pruebaFile():
    body = request.get_json()
    message = body['prueba']
    datos = body['datos']
    root = read.prueba(message)
    dict = read.readXMLPrueba(root)
    resp = read.reserverPrueba(dict)
    algoritmo =  read.algoritmoPrueba(datos,resp)
    return jsonify({'data': algoritmo})


if __name__ == '__main__':
    app.run(port = 5000,debug = True)