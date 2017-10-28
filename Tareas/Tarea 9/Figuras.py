#-*- coding:utf-8 -*-
import os 

def menu():
    os.system('cls')
    print("¿Qué figura deseas hacer?")
    print("Rectángulo --presiona 1")
    print("Un triángulo --presiona 2")
    optionMenu = raw_input("Selecciona la opción que desees >> ")
    if int(optionMenu) == 1: 
        rbase= raw_input("Medida de la base? >> ")
        raltura =raw_input("Medida de la altura? >> ")
        print "Lo quieres relleno? ;)"
        print "Si --presiona 1"
        print "No --presiona 2"
        optionFigure = raw_input("Selecciona la opción que desses >> ")
        if int(optionFigure)==1:
            for i in range (0,int(raltura)):
                print ". "*int(rbase)
        elif int(optionFigure)==2:
            print ". "*int(rbase)
            for i in range(0,int(raltura)-1):
                print ". "+"  "*(int(rbase)-2)+"."
            print ". "*int(rbase)
            print ""
            print "Hacer otra figura --presiona 1"
            print "Salir de Programa --presiona 2"
            final=raw_input("Selecciona la opción que desees >>")
            if int(final)==1:
                menu()
            elif int(final)==2:
                exit()
    if int(optionMenu) == 2: 
        lado= raw_input("Medida del lado? >> ")
        print "Lo quieres relleno? ;)"
        print "Si --presiona 1"
        print "No --presiona 2"
        optionFigure = raw_input("Selecciona la opción que desses >> ")
        if int(optionFigure)==1:
            for i in range (0,int(lado)):
                print ". "*(int(lado)-i)
        elif int(optionFigure)==2:
            print ". "*int(lado)
            for i in range(0,int(lado)-2):
                print "."+"  "*(int(lado)-2-i)+"."
            print "."
            print ""
            print "Hacer otra figura --presiona 1"
            print "Salir de Programa --presiona 2"
            final=raw_input("Selecciona la opción que desees >>")
            if int(final)==1:
                menu()
            elif int(final)==2:
                exit()
        
    
menu()


        
    

        
    


