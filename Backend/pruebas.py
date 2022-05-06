import re
import json
from textwrap import indent
from fecha import Fecha
import xml.etree.ElementTree as ET
from xml.dom import minidom


def algoritmo():
    diccionario = {'positivos': ['bueno', 'excelente', 'cool', 'satisfecho'], 'negativos': ['malo', 'pesimo', 'triste', 'molesto', 'decepcionado', 'enojo'], 'empresas': [{'empresa': 'usac', 'servicio': [[{'nombre': 'inscripcion', 'alias': ['inscribi', 'inscrito']}], [{'nombre': 'asignacion', 'alias': ['asignado']}], [{'nombre': 'graduacion', 'alias': []}]]}, {'empresa': 'irtra', 'servicio': [[{'nombre': 'inscripcion', 'alias': ['inscribi', 'inscrito']}], [{'nombre': 'asignacion', 'alias': ['asignado']}], [{'nombre': 'graduacion', 'alias': []}]]}], 'mensajes': [{'mensaje': 'lugar y fecha: guatemala, 01/04/2022 15:01\n            usuario: map0001@usac.edu\n            red social: twitter\n            el servicio en la usac para inscripcion fue muy bueno en la usac y me siento muy satisfecho en irtra.'}, {'mensaje': 'lugar y fecha: guatemala, \n            01/04/2022 15:20 usuario: map0002@usac.edu\n            red social: facebook\n            hoy me inscribi \n            en la usac, no encontre parqueo e inicie molesto mi gestion, luego tuve que hacer \n            cola y me indicaron que era la cola incorrecta, esto me enojo mucho y mejor me\n            fui.'}, {'mensaje': 'lugar y fecha: guatemala, 01/04/2023 15:43\n            usuario: map0003@usac.edu \n            red social: whatsapp\n            ya estoy inscrito en la usac, el proceso fue muy bueno, pero al salir, \n            mi carro tenia pinchadas las llantas, esto me preocupo \n            y me fui decepcionado.'}]} 
    
    list_reserver = list()
    list_fechas = list()
    dict_data = dict()
    messages = diccionario['mensajes']
    for msg in messages:
        message = msg['mensaje']
        mjs_lugar = re.search('[L|l][A-Za-z0-9]*[\s]*[Y|y][\s]*[F|f][A-Za-z0-9]*[\s]*:[\s]*[A-Za-z0-9]*,',message)
        lugar = mjs_lugar.group()
        lugar = re.sub('[L|l][A-Za-z0-9]*[\s]*[Y|y][\s]*[F|f][A-Za-z0-9]*[\s]*:','',lugar)
        lugar = re.sub(',','',lugar)
        lugar = lugar.strip()
        message = re.sub('[L|l][A-Za-z0-9]*[\s]*[Y|y][\s]*[F|f][A-Za-z0-9]*[\s]*:[\s]*[A-Za-z0-9]*,','',message)
        mjs_fecha = re.search('(\d+/\d+/\d+)',message)
        fecha = mjs_fecha.group()
        fecha = fecha.strip()
        message = re.sub('(\d+/\d+/\d+)','',message)
        mjs_hora = re.search('([01]?[0-9]|2[0-3]):[0-5][0-9]',message)
        hora = mjs_hora.group()
        hora = hora.strip()
        message = re.sub('([01]?[0-9]|2[0-3]):[0-5][0-9]','',message)
        mjs_usuario = re.search('[U|u][A-Za-z0-9]*[\s]*:[\s]*[\s]*[A-Za-z0-9\S*]*|@([A-Za-z]*.)*', message)
        usuario = mjs_usuario.group()
        usuario = re.sub('[U|u][A-Za-z0-9]*[\s]*:[\s]*','',usuario)
        usuario = usuario.strip()
        message = re.sub('[U|u][A-Za-z0-9]*[\s]*:[\s]*[\s]*[A-Za-z0-9\S*]*|@([A-Za-z]*.)*','',message)
        mjs_red = re.search('[R|r][E|e][A-Za-z][\s]*[A-Za-z]*[\s]*:[\s]*[A-Za-z]*',message)
        red_social = mjs_red.group()
        red_social = re.sub('[R|r][E|e][A-Za-z][\s]*[A-Za-z]*[\s]*:[\s]*:','',red_social)
        red_social = red_social.strip()
        message = re.sub('[R|r][E|e][A-Za-z][\s]*[A-Za-z]*[\s]*:[\s]*[A-Za-z]*','',message)
        mjs_comment = re.search('[A-Za-z0-9\S|\s]*',message)
        comment = mjs_comment.group()
        comment = comment.strip()
        message = re.sub('[A-Za-z0-9\S|\s]*','',message)
        if fecha not in list_fechas:
            list_fechas.append(fecha)
            nuevoOrden = Fecha(fecha)
            list_reserver.append(nuevoOrden)
        for dato in list_reserver:
            if fecha == dato.fecha:
                dato.comentarios.append(comment)

    #algoritmo
    positive_emotions = diccionario['positivos']
    negative_emotions = diccionario['negativos']
    company = diccionario['empresas']
    total_content = list()
    
    for dato in list_reserver: 
        comments_positives = 0
        comments_negatives = 0
        comments_nulls = 0
        print(dato.fecha)#04
        for text in dato.comentarios:
            print(text)
            response_positive = []
            response_negative = []
            for palabra in positive_emotions:
                x = re.findall('\\b(' + palabra + ')\\b',text)
                response_positive.append({palabra:len(x)})
            #print(response_positive)
            for palabra in negative_emotions:
                x = re.findall('\\b(' + palabra + ')\\b',text)
                response_negative.append({palabra:len(x)})
            #print(response_negative)
            cont_positive = 0
            for positive in response_positive:
                key = positive.keys()
                key = list(key)
                cont_positive += positive[key[0]]
            #print(cont_positive)
            cont_negative = 0
            for negatives in response_negative:
                key = negatives.keys()
                key = list(key)
                cont_negative += negatives[key[0]]
            #print(cont_negative)
            if cont_positive > cont_negative:
                comments_positives += 1
            elif cont_positive < cont_negative:
                comments_negatives += 1
            elif cont_positive == cont_negative:
                comments_nulls += 1
        lista_empresas_comments = []
        for empresas in company:
            empresa = empresas['empresa']
            comments_positives_ent = 0
            comments_negatives_ent = 0
            comments_nulls_ent = 0
            print(empresa)
            for dato_1 in list_reserver:
                for text_1 in dato_1.comentarios:
                    ditc_cont_ent = {empresa:0}
                    if dato.fecha == dato_1.fecha:
                        x = re.findall('\\b(' + empresa + ')\\b',text_1)
                        ditc_cont_ent = {empresa:len(x)}
                    if ditc_cont_ent[empresa] > 0:
                        response_positive_ent = []
                        response_negative_ent = []
                        for palabra in positive_emotions:
                            x = re.findall('\\b(' + palabra + ')\\b',text_1)
                            response_positive_ent.append({palabra:len(x)})
                        #print(response_positive_ent)
                        for palabra in negative_emotions:
                            x = re.findall('\\b(' + palabra + ')\\b',text_1)
                            response_negative_ent.append({palabra:len(x)})
                        #print(response_negative_ent)
                        cont_positive = 0
                        for positive in response_positive_ent:
                            key = positive.keys()
                            key = list(key)
                            cont_positive += positive[key[0]]
                        #print(cont_positive)
                        cont_negative = 0
                        for negatives in response_negative_ent:
                            key = negatives.keys()
                            key = list(key)
                            cont_negative += negatives[key[0]]
                        #print(cont_negative)
                        if cont_positive > cont_negative:
                            comments_positives_ent += 1
                        elif cont_positive < cont_negative:
                            comments_negatives_ent += 1
                        elif cont_positive == cont_negative:
                            comments_nulls_ent += 1
            lista_servicios_comments = []
            for servicios in empresas['servicio']:
                for service in servicios:
                    servicio = service['nombre']
                    alias = service['alias']
                    comments_positives_sr = 0
                    comments_negatives_sr = 0
                    comments_nulls_sr = 0
                    for dato_2 in list_reserver:
                        for text_2 in dato_2.comentarios:
                            ditc_cont_sr = {servicio:0}
                            if dato.fecha == dato_2.fecha:
                                x = re.findall('\\b(' + servicio + ')\\b',text_2)
                                ditc_cont_sr = {servicio:len(x)}
                                if len(alias) != 0:
                                    for word in alias:
                                        if word in text_2:
                                            x = re.findall('\\b(' + word + ')\\b',text_2)
                                            ditc_cont_sr = {servicio:len(x)}
                            if ditc_cont_sr[servicio] > 0:
                                response_positive_sr = []
                                response_negative_sr = []
                                for palabra in positive_emotions:
                                    x = re.findall('\\b(' + palabra + ')\\b',text_2)
                                    response_positive_sr.append({palabra:len(x)})
                                #print(response_positive_sr)
                                for palabra in negative_emotions:
                                    x = re.findall('\\b(' + palabra + ')\\b',text_2)
                                    response_negative_sr.append({palabra:len(x)})
                                #print(response_negative_sr)
                                cont_positive = 0
                                for positive in response_positive_sr:
                                    key = positive.keys()
                                    key = list(key)
                                    cont_positive += positive[key[0]]
                                #print(cont_positive)
                                cont_negative = 0
                                for negatives in response_negative_sr:
                                    key = negatives.keys()
                                    key = list(key)
                                    cont_negative += negatives[key[0]]
                                #print(cont_negative)
                                if cont_positive > cont_negative:
                                    comments_positives_sr += 1
                                elif cont_positive < cont_negative:
                                    comments_negatives_sr += 1
                                elif cont_positive == cont_negative:
                                    comments_nulls_sr += 1    
                    total_comments_sr = comments_positives_sr + comments_negatives_sr + comments_nulls_sr
                    lista_servicios_comments.append({'servicio':servicio,'total_mgs':total_comments_sr,'positivos_mgs':comments_positives_sr,'negativos_mgs':comments_negatives_sr,'neutros_msg':comments_nulls_sr})
            
            total_comments_ent = comments_positives_ent + comments_negatives_ent + comments_nulls_ent
            lista_empresas_comments.append({'empresa':empresa,'total_mgs':total_comments_ent,'positivos_mgs':comments_positives_ent,'negativos_mgs':comments_negatives_ent,'neutros_msg':comments_nulls_ent,'servicios':lista_servicios_comments})
            
            
                           
        total_comments = comments_positives + comments_negatives + comments_nulls
        total_content.append({'fecha':dato.fecha,'total_mgs':total_comments,'positivos_mgs':comments_positives,'negativos_mgs':comments_negatives,'neutros_msg':comments_nulls,'empresas':lista_empresas_comments})

    print(json.dumps(total_content, indent=4))
    return total_content


def crearXML(intrucciones):
    data = ET.Element('lista_respuestas')
    for valor in intrucciones:
        
        items1 = ET.SubElement(data, 'respuesta')

        item1 = ET.SubElement(items1, 'fecha')
        item1.text= valor['fecha']
        
        items2 = ET.SubElement(items1, 'mensajes')
        
        item2 = ET.SubElement(items2, 'total')
        item2.text = str(valor['total_mgs'])
        item3 = ET.SubElement(items2, 'positivos')
        item3.text = str(valor['positivos_mgs'])
        item4 = ET.SubElement(items2, 'negativos')
        item4.text = str(valor['negativos_mgs'])
        item5 = ET.SubElement(items2, 'neutros')
        item5.text = str(valor['neutros_msg'])
        
        items3 = ET.SubElement(items1, 'analisis')
        for empresa in valor['empresas']:
            items5 = ET.SubElement(items3, 'empresa', {"name": empresa['empresa']})
            items4 = ET.SubElement(items5, 'mensajes')
            
            item7 = ET.SubElement(items4, 'total')
            item7.text = str(empresa['total_mgs'])
            item8 = ET.SubElement(items4, 'positivos')
            item8.text = str(empresa['positivos_mgs'])
            item9 = ET.SubElement(items4, 'negativos')
            item9.text = str(empresa['negativos_mgs'])
            item10 = ET.SubElement(items4, 'neutros')
            item10.text = str(empresa['neutros_msg'])
            
            items6 = ET.SubElement(items5, 'servicios')
            for servicio in empresa['servicios']:
                items7 = ET.SubElement(items6, 'servicio', {"name": servicio['servicio']})
                items8 = ET.SubElement(items7, 'mensajes')
                
                item11 = ET.SubElement(items8, 'total')
                item11.text = str(servicio['total_mgs'])
                item12 = ET.SubElement(items8, 'positivos')
                item12.text = str(servicio['positivos_mgs'])
                item13 = ET.SubElement(items8, 'negativos')
                item13.text = str(servicio['negativos_mgs'])
                item14 = ET.SubElement(items8, 'neutros')
                item14.text = str(servicio['neutros_msg'])
    
    my = prettify(data)
    my = str(my)
    file = open("Backend/prueba2.xml", 'w')
    file.write(my)

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

          

alg = algoritmo()
crearXML(alg)