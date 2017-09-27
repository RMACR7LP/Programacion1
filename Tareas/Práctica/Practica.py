# -*- coding:utf-8 -*-
import os
import json

def menu():
   os.system('cls')
   print("********Necesitas registrarte********")
   print("no-presiona 0")
   print("si-presiona 1")

with open('usuarios.json') as json_data:
    usuario =json.load(json_data)


def login():
 menu()

 opcionMenu = input("Inserta un numero valor >> ")
 if opcionMenu==1:
    print ("")
    correo_dado = raw_input("Agrega tu correo >>")
    if correo_dado in usuario:
        raw_input("Esa direccion de correo ya esta registrada, presione enter")
        login()
    else:
      print ("")
      nombre_dado = raw_input("Agrega tu nombre >>")
      if "nombre_dado" in usuario:
        raw_input ("Ese nombre ya fue tomado,  presione enter")
        login()
      else:
         print ("")
         password_dado = raw_input("Introduzca una password >>")
         usuario[nombre_dado] = {
          "correo":correo_dado,
          "nombre":nombre_dado,
          "password": password_dado
         }
         if 1==1:
          x= raw_input ("Has creado tu usuario con exito, presione enter")
          s = json.dumps(usuario)
          print(s)
          archivo = open('usuarios.json','a')
          archivo.write(s)
          archivo.close()
          login()
 else:
  if opcionMenu==0:
     print ("")
     correo_dado = raw_input("Introduzca su nombre o correo >>")
     if "correo_dado" in usuario:
       print("")
       password_dado = raw_input("Introduzca su password >>")
       if usuario["correo_dado"]["password"] == password_dado:
        raw_input("Has ingresado con exito, presione enter")
        # ingresar a la pagina
     else:
       print ""
       raw_input("Este correo o nombre no está registrado, preseione enter")
       login()
  else:
     raw_input("Caracter invalido, presione enter")
     login()



login()
