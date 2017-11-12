if opcionMenu=="1":
    with open('usuarios.json','r') as lista:
        d=json.load(lista)
        x=len(d["usuarios"])
        for i in range(0,x):
            if d["usuarios"][i]["nombre"]==nombre_dado:
                raw_input("Un usuario con ese nombre ya esta registado, presione enter") #
            else:
                password_dado=textentry2.get()
                d["usuarios"].append({
                    "nombre": nombre_dado,
                    "correo": correo_dado,
                    "password": password_dado
                })
                with open('usuarios.json','w') as entrada:
                    json.dump(d, entrada)
                    Label(ventana,text="Enhorabuena, has creado tu usuario")
                   
