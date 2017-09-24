# -*- coding:utf-8 -*-
import os

def menu():
   os.system('cls')
   print("********Necesitas registrarte********")
   print("no-presiona 0")
   print("si-presiona 1")

book={}

def login():
 menu()

 opcionMenu = input("Inserta un numero valor >> ")
 if opcionMenu==1:
    print ("")
    correo_dado = raw_input("Agrega tu correo >>")
    if "correo_dado" in book:
        raw_input("Esa direccion de correo ya esta registrada, presione enter")
        login()
    else:
      print ("")
      nombre_dado = raw_input("Agrega tu nombre >>")
      if "nombre_dado" in book:
        raw_input ("Ese nombre ya fue tomado,  presione enter")
        login()
      else:
         print ("")
         password_dado = raw_input("Introduzca una password >>")
         book["correo_dado"] = {
          "correo":"correo_dado",
          "nombre":"nombre_dado",
          "password": "password_dado"
         }
         if 1==1:
          x= raw_input ("Has creado tu usuario con exito, presione enter")
          login()
 else:
  if opcionMenu==0:
     print ("")
     correo_dado = raw_input("Introduzca su nombre o correo >>")
     if "correo_dado" in book:
       print("")
       password_dado = raw_input("Introduzca su password >>")
       if book["correo_dado"]["password"] == password_dado:
        raw_input("Has ingresado con exito, presione enter")
        # ingresar a la pagina
     else:
       print ""
       raw_input("Este correo o nombre no está registrado, preseione enter")
       login()
  else:
     raw_input("Caracter invalido, presione enter")
     login()
import json
s = json.dumps(book)

login()
