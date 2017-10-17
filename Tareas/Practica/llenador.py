import json

datos = {}

datos["usuarios"] = []

datos["usuarios"].append({
   'nombre': 'pringles',
   'correo': 'pringles@gmail.com',
   'password': 'papas'
   })



with open('usuarios.json','w') as entrada:
  json.dump(datos, entrada)


#with open('usuarios.json','r') as fp:
 #   d= json.load(fp)
  #  x= len(d["usuarios"])
    #print x

