#-*- coding:utf-8 -*-
from Tkinter import *
import ttk
import datetime
import json
import subprocess
import sys
import os
import socket
import reportlab
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from reportlab.lib.colors import PCMYKColor
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
try:
    import cPickle as pickle 
except ImportError:
    import pickle
#-------------------------------------------Funciones y Clases-------------------------------------------------------
cities=[]
datac=[]
estaciones_visitadas=[]
aviso=[]

def signupclick():
    nombre_dado=textentry1.get()
    password_dado=textentry2.get()
    with open('usuarios.json','r') as lista:
        d=json.load(lista)
        x=len(d["usuarios"])
        i=0
        while i<x:
            if d["usuarios"][i]["nombre"]==nombre_dado:
                Label(ventana,text="Un usuario con ese nombre ya está registado").grid(row=5,column=0,columnspan=4)
                i=x+1
            else:
                i+=1
                if i==x:
                    password_dado=textentry2.get()
                    d["usuarios"].append({
                        "nombre": nombre_dado,
                        "password": password_dado
                    })
                    with open('usuarios.json','w') as entrada:
                        json.dump(d, entrada)
                        Label(ventana,text="Felicidades! Te has registrado con éxito.").grid(row=5,column=0,columnspan=4)

def loginclick():
    global textentry1
    global cuenta_dado
    global aviso
    cuenta_dado=textentry1.get()
    password_dado=textentry2.get ()
    with open('usuarios.json','r') as lista:
                d=json.load(lista)
                x=len(d['usuarios'])
                indices =[]
                i=0
                while i<x:
                    if d['usuarios'][i]['nombre']==cuenta_dado:
                        indices.append(i)
                        i+=1
                    else:
                        i+=1
                if len(indices)==0:
                    Label(ventana,text="Ese nombre de usuario o correo no está registrado").grid(row=5,column=0)
                else: 
                    j=indices[0]
                    if password_dado==d['usuarios'][j]['password']:
                        aviso=['hola']
                        ventana.destroy()
                    else: 
                        print "La contraseña no es correcta, presione enter"

class Usuario():
    
    def __init__(self,nombre):
        self.nombre = nombre
        
        
    def asignar_ultimasciudades(self,cities):
        self.cities=cities
    
    def asignar_datos(self,datac):
        self.datac=datac
    
    def asignar_estaciones(self,estaciones_visitadas):
        self.estaciones_visitadas=estaciones_visitadas
    
def guardar(nombre,cities,datac,estaciones_visitadas):
    
    if len(estaciones_visitadas)!=0 and len(cities)!=0:
        jugador = Usuario(nombre)
        jugador.asignar_ultimasciudades(cities)
        jugador.asignar_datos(datac)
        jugador.asignar_estaciones(estaciones_visitadas)
        archivo = open(str(nombre)+".txt", "w")
        pickle.dump(jugador, archivo,1)
        archivo.close()            
    elif len(estaciones_visitadas)==0:
        estaciones_visitadas=['None']
        jugador = Usuario(nombre)
        jugador.asignar_ultimasciudades(cities)
        jugador.asignar_datos(datac)
        jugador.asignar_estaciones(estaciones_visitadas)
        archivo = open(str(nombre)+".txt", "w")
        pickle.dump(jugador, archivo,1)
        archivo.close()
    elif len(cities)==0:
        cities=['None']
        jugador = Usuario(nombre)
        jugador.asignar_ultimasciudades(cities)
        jugador.asignar_datos(datac)
        jugador.asignar_estaciones(estaciones_visitadas)
        archivo = open(str(nombre)+".txt", "w")
        pickle.dump(jugador, archivo,1)
        archivo.close()

def load():
    fichero=open(str(cuenta_dado)+".txt","r+")
    jugador=pickle.load(fichero)
    lista_ciudades=jugador.cities
    lista_datos=jugador.datac
    lista_estaciones=jugador.estaciones_visitadas
    print jugador.nombre
    print lista_ciudades
    print lista_datos
    global cities
    global datac
    global estaciones_visitadas
    cities=lista_ciudades
    datac=lista_datos
    estaciones_visitadas=lista_estaciones

def stateclick():
    global tab1_estado
    global tab1_state
    global tab1_estacion
    global stationsr
    tab1_state=tab1_estado.get()
    try:
        if int(tab1_state)==1 or int(tab1_state)==2:
            m="estaciones"+str(tab1_state)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
                w=""
                for i in range(0,l):         
                    w= w+str(i+1)+") "+n['results'][i]['name']+"\n"
        elif 2<int(tab1_state)<6:
            m="estaciones"+str(int(tab1_state)+1)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
                w=""
                for i in range(0,l):         
                    w= w+str(i+1)+") "+n['results'][i]['name']+"\n"
        elif 5<int(tab1_state)<12:
            m="estaciones"+str(int(tab1_state)+2)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
                w=""
                for i in range(0,l):         
                    w= w+str(i+1)+") "+n['results'][i]['name']+"\n"
        elif 11<int(tab1_state)<40:
            m="estaciones"+str(int(tab1_state)+3)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
                w=""
                for i in range(0,l):         
                    w= w+str(i+1)+") "+n['results'][i]['name']+"\n"
        elif 39<int(tab1_state)<52:
            m="estaciones"+str(int(tab1_state)+4)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
                w=""
                for i in range(0,l):         
                    w= w+str(i+1)+") "+n['results'][i]['name']+"\n"
        else:
            w="La opción ingresada no es válida"
    except ValueError:
        w="La opción no es válida"

    stationsr = Text(tab1,width=32,height=30,wrap=WORD,background="white")
    stationsr.grid(row=0,rowspan=60,column=10, columnspan=10, sticky=E)
    stationsr.insert (END,str(w)) 
    
    tab1_estado.grid(row=60,column=10)
    Button(tab1,text="OpciónEstado",command=stateclick).grid(row=60,column=11,columnspan=2,sticky=W)
    tab1_estacion= Entry(tab1, width=3, bg="white")
    tab1_estacion.grid(row=60,column=13,sticky=E)
    Button(tab1,text="Estación",command=stationclick).grid(row=60,column=14,sticky=E)

def stationclick():
    global tab1_station
    global estaciones_visitadas
    try:
        if int(tab1_state)==1 or int(tab1_state)==2:
            m="estaciones"+str(tab1_state)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
        elif 2<int(tab1_state)<6:
            m="estaciones"+str(int(tab1_state)+1)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
        elif 5<int(tab1_state)<12:
            m="estaciones"+str(int(tab1_state)+2)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
        elif 11<int(tab1_state)<40:
            m="estaciones"+str(int(tab1_state)+3)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
        elif 39<int(tab1_state)<52:
            m="estaciones"+str(int(tab1_state)+4)+".json"
            with open(m,'r') as estaciones:
                n=json.load(estaciones)
                l=len(n['results'])
        tab1_station=int(tab1_estacion.get())
        if 0<tab1_station<26:
            stationsr.delete(0.0,END)
            stationsr.insert (END,"Nombre: "+n['results'][int(tab1_station)-1]['name']
            +"\n"+ "-Fecha Inicial: "+n['results'][int(tab1_station)-1]['mindate']
            +"\n"+ "-FechaFinal: "+n['results'][int(tab1_station)-1]['maxdate']    
            +"\n"+ "-Latitude: "+str(n['results'][int(tab1_station)-1]['latitude'])
            +"\n"+ "-Longitud: "+str(n['results'][int(tab1_station)-1]['longitude'])
            +"\n"+ "-Cobertura de Datos: "+str(n['results'][int(tab1_station)-1]["datacoverage"])
            +"\n"+ "-ID: "+n['results'][int(tab1_station)-1]["id"]) 
            q="Se visitó la estación número "+str(tab1_station)+" correspondiente al estado "+str(tab1_state)+" en "+str(datetime.datetime.now())
            estaciones_visitadas.append(q)
        else:
            stationsr.delete(0.0,END)
            stationsr.insert (END,"La opción ingresada no es válida")

    except ValueError:
        stationsr.delete(0.0,END)
        stationsr.insert(END,"La opción ingresada no es válida")
      
def weatherclick():
    city=entry1.get()
    country=entry2.get()
    weather= subprocess.Popen(["curl ","http://api.openweathermap.org/data/2.5/weather?q="+str(city)+","+str(country)+"&APPID=88e766988b7e28f66160c1bf837bbc54","-o", str(city)+'.json'])
    weather.communicate()
    output.delete(0.0,END)
    with open(str(city)+'.json','r') as f:
        datos=json.load(f)
        try:
            temperatura= "Temperatura: "+ str(datos['main']['temp']-273.15)+"°C"
            presion="Presión: " + str(datos['main']['pressure'])+" hPa"
            humedad="Humedad: "+ str(datos['main']['humidity'])+"%"
            minTemp="Temperatura Mínima: " + str(datos['main']['temp_min']-273.15)+"°C"
            maxTemp="Temperatura Máxima: " + str(datos['main']['temp_max']-273.15)+"°C"
            wind="Viento: "+ str(datos['wind']['speed'])+" m/s"
            cities.append(city)
        except:
            temperatura="Lo sentimos pero la ciudad que ha seleccionada no existe\n tome en cuenta que el nombre de la ciudad debe comenzar en mayúscula,\n debe estar escrito en ingles y el codigo del pais en minusculas."
            presion= ""
            humedad=""
            minTemp=""
            maxTemp= ""
            wind=""
        output.insert (END,str(temperatura)+"\n"+str(presion)+"\n"+str(humedad)+"\n"+ str(minTemp) +"\n"+str(maxTemp)+"\n"+str(wind))
        datac.append(datos['main']['temp']-273.15)
        if datos['weather'][0]['main']=="Thunderstorm":
            photo1=PhotoImage(file="Thunderstorm.gif")
            label=Label (tab2,image=photo1) .grid(row=3,column=15)    
            label2= Label (tab2,text='Clouds',fg='clouds') .grid(row=5,column=15)
        elif datos['weather'][0]['main']== "Drizzle":
            photo1=PhotoImage(file="Drizzle.gif")
            label=Label (tab2,image=photo1) .grid(row=3,column=15)    
            label2= Label (tab2,text='Clouds',fg='clouds') .grid(row=5,column=15)
        elif datos['weather'][0]['main']== "Rain":
            photo1=PhotoImage(file="Rain.gif")
            label=Label (tab2,image=photo1) .grid(row=3,column=15)    
            label2= Label (tab2,text='Clouds',fg='clouds') .grid(row=5,column=15) 
        elif datos['weather'][0]['main']== "Snow":
            photo1=PhotoImage(file="Snow.gif")
            label=Label (tab2,image=photo1) .grid(row=3,column=15)    
            label2= Label (tab2,text='Clouds',fg='clouds') .grid(row=5,column=15) 
        elif datos['weather'][0]['main']== "Clear":
            photo1=PhotoImage(file="Clear.gif")
            label=Label (tab2,image=photo1) .grid(row=3,column=15)    
            label2= Label (tab2,text='Clouds',fg='clouds') .grid(row=5,column=15)    
        elif datos['weather'][0]['main']== "Clouds":
            photo1=PhotoImage(file="Clouds.gif")
            label=Label (tab2,image=photo1) .grid(row=3,column=15)    
            label2= Label (tab2,text='Clouds',fg='clouds') .grid(row=5,column=15) 
            
def tabla():
    global estaciones_visitadas
    print estaciones_visitadas
    for i in range(0,len(estaciones_visitadas)):
        Label(tab3,text=str(estaciones_visitadas[i]),fg="black").grid(row=i,column=0,sticky=W)

def graph():
    ciudad1=str(cities[len(cities)-1])
    ciudad2='m'
    if len(cities)>2:
        counter=1
        i=2
        while i<len(cities)+1:
            if ciudad1==str(cities[len(cities)-i]) or ciudad2==str(cities[len(cities)-i]):
                i+=1
            elif ciudad2=='m':
                ciudad2=str(cities[len(cities)-i])
                counter +=1
                if counter<4:
                    i+=1
                else:
                    i=len(cities)+2
            elif ciudad2 !='m':
                if ciudad1==str(cities[len(cities)-i]) or ciudad2==str(cities[len(cities)-i]):
                    i+=1
                else:
                    ciudad3 =str(cities[len(cities)-i])
                    i=len(cities)+2 
    
    indices1=[]
    indices2=[]
    indices3=[]
    for i in range(0,len(cities)):
        if ciudad1==cities[i]:
            indices1.append(i)
        elif ciudad2==cities[i]:
            indices2.append(i)
        elif ciudad3==cities[i]:
            indices3.append(i)
    
    temp1=0
    temp2=0
    temp3=0
    for m in indices1:
        temp1=temp1+datac[m]
    for m in indices2:
        temp2=temp2+datac[m]
    for m in indices3:
        temp3=temp3+datac[m]

    temp1=temp1/len(indices1)
    temp2=temp2/len(indices2)
    temp3=temp3/len(indices3)
        
    d = Drawing(220, 180)
    bar = VerticalBarChart()
    bar.x = 25  
    bar.y = 55
    data = [[temp1,0,temp2,0,temp3]
                    ]
    bar.data = data
                        
    try:
        bar.categoryAxis.categoryNames = [ciudad1, '', ciudad2, '', ciudad3,'']
        bar.bars[0].fillColor = PCMYKColor(100,0,90,50,alpha=85)
        d.add(bar, '')
        d.save(formats=['gif'], outDir='.', fnRoot='grafica')
    except:
        bar.categoryAxis.categoryNames = [str(cities[len(cities)-1])]
        bar.bars[0].fillColor = PCMYKColor(100,0,90,50,alpha=85)
        d.add(bar, '')
        d.save(formats=['gif'], outDir='.', fnRoot='grafica')
    
    photo1=PhotoImage(file="grafica.gif")
    label=Label (tab4,image=photo1) .grid(row=5,column=0)    
    label2= Label (tab4,text='grafica',fg="grafica") .grid(row=5,column=3)



REMOTE_SERVER = "www.google.com"
def internet_on():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False
print internet_on()
#------------------------------------------Ventana de Inicio---------------------------------------------------
internet_on()
ventana=Tk()
background_image=ImageTk.PhotoImage(Image.open("cielo.jpg"))
background_label=Label(ventana,image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
ventana.title("Proyecto Cristian")
ventana.geometry('600x400')
ventana.configure(background="gray")


Label (ventana,text="Usuario", bg="gray",fg="black").grid(row=0, column=0, sticky=W)
Label (ventana,text="Password", bg="gray",fg="black").grid(row=0+2, column=0, sticky=W)
textentry1=Entry(ventana, width=20, bg="white")
textentry1.grid(row=0, column=1,sticky=W)
textentry2=Entry(ventana, width=20, bg="white", show='*')
textentry2.grid(row=0+2, column=1,sticky=W)
Button(ventana,text="Login",width=5,command=loginclick).grid(row=4,column=0,sticky=W)
Button(ventana,text="Sign Up",command=signupclick).grid(row=4,column=1,sticky=W)
ventana.mainloop()
#--------------------------------------------Ventana de Menu----------------------------------------------
if len(aviso)==1:
    ventana2=Tk()
    background_image=ImageTk.PhotoImage(Image.open("mar.jpg"))
    background_label=Label(ventana2,image=background_image)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    ventana2.title("Menu")
    ventana2.geometry('800x600')

    rows=0
    while rows<50:
        ventana2.rowconfigure(rows,weight=1)
        ventana2.columnconfigure(rows,weight=1)
        rows +=1

    nb=ttk.Notebook(ventana2)
    nb.grid(row=3,column=0,columnspan=50,rowspan=49,sticky='NESW')


    Button(ventana2,text="Guardar",width=6,command=lambda : guardar(cuenta_dado,cities,datac,estaciones_visitadas)).grid(row=0,column=1,sticky=W)
    Button(ventana2,text="Load", width=5, command=lambda : load()).grid(row=0, column=2,sticky=W)

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Pestaña 1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    tab1=ttk.Frame(nb)
    nb.add(tab1,text='Estaciones\n NOAA')

    Label(tab1,text="Como puedes ver todos los estados de EEUU están enlistados, puedes presionar la tecla que desees \n para poder ver las estaciones que se encuentran en un especifico estado o bien, elegir la opcion \n de enlistar todas las posibles estaciones en el país",fg="black"). grid(row=0, columnspan=3, sticky=W)
    with open('estados.json','r') as lista1:
        x= json.load(lista1)
        for i in range (0,50,3): 
            Label(tab1,text = str(i+1)+" "+x['results'][i]["name"],fg="black").grid(row=1+i,column=0,sticky=W)
            Label(tab1,text=str(i+2)+" "+x['results'][i+1]["name"],fg="black").grid(row=1+i,column=1,sticky=W)
            Label(tab1,text= str(i+3)+" "+x['results'][i+2]["name"], fg="black").grid(row=1+i,column=2,sticky=W)
        
        tab1_estado= Entry(tab1,width=3,bg="white")
        tab1_estado.grid(row=0,column=10,sticky=W)
        Button(tab1,text="Opcion Estado",command=stateclick).grid(row=0,column=11,sticky=W)
        
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Pestaña 2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    temperatura=""
    presion=""
    humedad=""
    minTemp=""
    maxTemp=""

    tab2=ttk.Frame(nb)

    nb.add(tab2,text='Datos por Ciudad\n OpenStreetMap')

    Label (tab2,text="Ciudad:",fg="black").grid(row=0, column=0, sticky=W)
    entry1=Entry(tab2, width=20, bg="white")
    entry1.grid(row=0, column=1,sticky=W)


    Label (tab2,text="Pais:",fg="black").grid(row=1, column=0, sticky=W)
    entry2=Entry(tab2, width=20, bg="white")
    entry2.grid(row=1, column=1,sticky=W)

    Button(tab2,text="Buscar",width=5,command=weatherclick).grid(row=4,column=0,sticky=W)
    output= Text(tab2,width=30,height=20,wrap=WORD,background="white")
    output.grid(row=0,rowspan=20,column=2, columnspan=10, sticky=E)


    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Pestaña 3!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    tab3=ttk.Frame(nb)
    nb.add(tab3,text='Tabla de Estaciones\n Visitadas')


    Button(tab3,text="Registro Estaciones", command=tabla).grid(row=0,column=0)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Pestaña 4!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    tab4=ttk.Frame(nb)
    nb.add(tab4,text='Grafico ciudades \n consultadas, historico')

    Label(tab4,text="Una vez que se hayan visitado 3 o más ciudades puedes crear una gráfica con la temperatura promedio de las últimas tres ciudades visitadas.", fg="black").grid(row=0,column=0,sticky=W)
    Button(tab4,text="Crear Gráfica", width=10, command=graph).grid(row=3,column=0)



    ventana2.mainloop()

#----------------------------------------------------------------------

# api key: 88e766988b7e28f66160c1bf837bbc54
# http://api.openweathermap.org/data/2.5/weather?q=Lakewood,us&APPID=88e766988b7e28f66160c1bf837bbc54