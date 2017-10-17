#-*- coding: utf-8 -*-
import os
import json
import smtplib
import datetime
import reportlab
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from reportlab.pdfgen import canvas
from reportlab.lib.colors import PCMYKColor
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart



def mainmenu():
   os.system('cls')
   print("********Ya estas registrado?********")
   print("si-presiona 0")
   print("no-presiona 1")

correo_destinatario=[]
usuario_destinatario=[]
countexits=len(usuario_destinatario)
def login():
    mainmenu()
    data={}
    opcionMenu=raw_input("Inserta un numero valor >> ")
    if opcionMenu=="1":
        correo_dado= raw_input("Agrega una direccion de correo >> ")
        if "@gmail.com" not in correo_dado and "@hotmail.com" not in correo_dado and "@outlook.com" not in correo_dado:
            raw_input("El correo electronico brindado no tiene la estructura correcta, presione enter")
            login()
        else:
            with open('usuarios.json','r') as lista:
                d=json.load(lista)
                x=len(d["usuarios"])
                for i in range(0,x):
                    if d["usuarios"][i]["correo"]==correo_dado:
                        raw_input("Un usuario con ese correo electronico ya esta registado, presione enter")
                        login()
                    else:
                        nombre_dado=raw_input("Selecciona un nombre de usuario >> ")
                        if " " in nombre_dado or "." in nombre_dado or "@" in nombre_dado:
                            raw_input("El nombre de usuario no puede tener espacios, ni puntos, ni arrobas, presione enter") 
                            login()
                        else: 
                            for i in range(0,x):
                                if d["usuarios"][i]["nombre"]==nombre_dado:
                                    raw_input("Un usuario con ese nombre ya esta registado, presione enter") #
                                    login()
                                else:
                                    password_dado=raw_input("Introduzca una password >> ")
                                    d["usuarios"].append({
                                        "nombre": nombre_dado,
                                        "correo": correo_dado,
                                        "password": password_dado
                                    })
                                    with open('usuarios.json','w') as entrada:
                                        json.dump(d, entrada)
                                        raw_input("Enhorabuena, has creado tu usuario")
                                        login()
    elif opcionMenu=="0":
        cuenta_dado= raw_input("Ingrese correo o nombre de usuario >> ")
        with open('usuarios.json','r') as lista:
            d=json.load(lista)
            x=len(d['usuarios'])
            indices =[]
            i=0
            while i<x:
                if d['usuarios'][i]['nombre']==cuenta_dado or d['usuarios'][i]['correo']==cuenta_dado:
                    indices.append(i)
                    i+=1
                else:
                    i+=1
            if len(indices)==0:
                raw_input("Ese nombre de usuario o correo no está registrado")
                login()
            else: 
                j=indices[0]
                password_dado=raw_input("Ingrese la password >> ")
                if password_dado==d['usuarios'][j]['password']:
                    correo_destinatario.append(d['usuarios'][j]['correo'])
                    usuario_destinatario.append(d['usuarios'][j]['nombre'])
                    menu()
                else: 
                    raw_input ("La contraseña no es correcta, presione enter")
                    login()
    else:
        raw_input("Esa entrada no es válida, presione enter")
        login()

ingresos=[]
Menulist=[]
def menu():
    os.system('cls')
    print "///////////////////////////////////// Bienvenido al Menú ///////////////////////////////////////"
    print "Como puedes ver todos los estados de EEUU están enlistados, puedes presionar la tecla que desees" 
    print "para poder ver las estaciones que se encuentran en un especifico estado o bien, elegir la opcion"
    print "de enlistar todas las posibles estaciones en el país"
    with open('estados.json','r') as lista1:
        x= json.load(lista1)
        for i in range (0,50,3): 
            print '%-25s' '%-25s' '%s' % (str(i+1)+" "+x['results'][i]["name"],str(i+2)+" "+x['results'][i+1]["name"],str(i+3)+" "+x['results'][i+2]["name"])
        
        print "52 Todas las estaciones            Para salir presione 0"
    
    
    
    optionMenu=raw_input("Ingrese el número del estado que quiera seleccionar >> ")
    if  int(optionMenu)>52:
        raw_input("El número ingresado no es valido, presione enter")
        menu()
    elif int(optionMenu)==1 or int(optionMenu)==2:
        m="estaciones"+str(optionMenu)+".json"
    elif 2<int(optionMenu)<6:
        m="estaciones"+str(int(optionMenu)+1)+".json"
    elif 5<int(optionMenu)<12:
        m="estaciones"+str(int(optionMenu)+2)+".json"
    elif 11<int(optionMenu)<40:
        m="estaciones"+str(int(optionMenu)+3)+".json"
    elif 39<int(optionMenu)<52:
        m="estaciones"+str(int(optionMenu)+4)+".json"
    elif int(optionMenu) == 0:
        print "¿Qué desea hacer?"
        print "1) Seguir en el programa -presione 1"
        print "2) Cerrar sesión -presione 2 "
        print "3) Cerrar el programa -presione 3"
        exitoption = raw_input(">> ")
        if int(exitoption) == 1:
            menu()
        elif int(exitoption)==2:
            terminate()
            login()
        elif int(exitoption)==3:
            terminate()
            exit()
        else: 
            raw_input("La opción ingresada no es válida")
            menu()
    elif int(optionMenu)==52:
        for i in range (1,57):
            if i !=3 and  i !=7 and i !=14 and i !=43 and i !=52:
                o = "estaciones"+str(i)+".json"
                with open(o,'r') as allstations:
                    p=json.load(allstations)
                    l=len(p['results'])
                    for j in range(0,l):
                        print p['results'][j]['name']
                        
        raw_input('Presione enter para regresar al menu')
        menu()

    os.system('cls')
    with open(m,'r') as estaciones:
        n=json.load(estaciones)
        l=len(n['results'])
        for i in range(0,l):
            print str(i+1)+") "+n['results'][i]['name']
    
    optionStation= raw_input("Seleccione la estación que desee o presione 0 para regresar>> ")
    if optionStation == "s":
        menu()
    elif 0<int(optionStation)<26:
        print "Nombre: "+n['results'][int(optionStation)-1]['name']
        print "-Fecha Inicial: "+n['results'][int(optionStation)-1]['mindate']
        print "-FechaFinal: "+n['results'][int(optionStation)-1]['maxdate']    
        print "-Latitude: "+str(n['results'][int(optionStation)-1]['latitude'])
        print "-Longitud: "+str(n['results'][int(optionStation)-1]['longitude'])
        print "-Cobertura de Datos: "+str(n['results'][int(optionStation)-1]["datacoverage"])
        print "-ID: "+n['results'][int(optionStation)-1]["id"]
        print "" 
        a= "Se visitó la estación número "+str(optionStation)+" correspondiente al estado "+str(optionMenu)+" en "+str(datetime.datetime.now())
        ingresos.append(a)
        Menulist.append([int(optionStation),int(optionMenu)])
        raw_input("Para regresar al menú, presione enter" )        
        menu()
    else: 
        raw_input("La opción ingresada no es válida, presione enter")
        menu()


def terminate():
            
    def create_bar_graph():
        d = Drawing(250, 220)
        bar = VerticalBarChart()
        bar.x = 50  
        bar.y = 85
        data = [[12,2,3,None,None,None,5],
                [5,7,2,8,8,2,5],
                [2,10,2,1,8,9,5],
                ]
        bar.data = data
        bar.categoryAxis.categoryNames = ['Year2', 'Year3',
                                        'Year4', 'Year5', 'Year6',
                                        'Year7']
        
        bar.bars[0].fillColor   = PCMYKColor(0,100,100,40,alpha=85)
        bar.bars[1].fillColor   = PCMYKColor(23,51,0,4,alpha=85)
        bar.bars.fillColor       = PCMYKColor(100,0,90,50,alpha=85)
    
        d.add(bar, '')
    
        d.save(formats=['jpg'], outDir='.', fnRoot='grafica')
    
    if __name__ == '__main__':
        create_bar_graph()

    r=len(ingresos)
    c=canvas.Canvas("Resumen.pdf")
    c.setFont('Times-Roman',40)
    c.drawCentredString(200,750,"Resumen de Actividad")
    c.setFont('Times-Roman',13)
    c.drawString(20,710,'A continuación se presenta información de la actividad del usuario '+ str(usuario_destinatario[countexits])+";")
    for i in range(0,r):
        c.drawString(20,680-i*15,"-"+ingresos[i])
    grafica= "grafica.jpg"
    c.drawImage(grafica,160,450-r*15,width=None,height=None)
    c.save()

    f = open('Resumen.html','w')
    _head='<head>A continuación se presenta información de la actividad del usuario '+ str(usuario_destinatario[countexits])+";</head>"
    w=[]
    w.append(_head)
    for i in range(0,r):
        estacion="<p>"+ingresos[i]+"</p>"
        w.append(estacion)
        # Insert newlines between every element, with a * prepended
    inserted_list = '\n'.join([x for x in w])

    template = '''<html>
<title>Attributes</title>

%s 
</html>''' %(inserted_list)
    f.write(template)
    f.close()


    server=smtplib.SMTP            
    email_user = 'RMACR7LP@gmail.com'
    email_password = 'hugoelpeepers' 
    email_send = correo_destinatario[0]

    subject = 'Resumen de '+"usuario "+"en Práctica de Cristian"

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = '¡Le agradecemos haber usado la Práctica de Cristian! Adjuntos se encuentran un archivo pdf y uno html con una breve descripción de su actividad'
    msg.attach(MIMEText(body,'plain'))

    filename= "Resumen.pdf"
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    filename2= "Resumen.html"
    attachment2 = open(filename2,'rb')

    part1 = MIMEBase('application','octet-stream')
    part1.set_payload((attachment2).read())
    encoders.encode_base64(part)
    part1.add_header('Content-Disposition',"attachment; filename= "+filename2)
    
    msg.attach(part)
    msg.attach(part1)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)

    server.sendmail(email_user,email_send,text)
    server.quit()
    del ingresos[:]
    del correo_destinatario[:]

login()
