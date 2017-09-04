import numpy as np

def leerNumero(ruta):
    archivo = open(ruta, 'r')
    numero =  ''
    for linea in archivo:
        numero  = numero + linea
    return numero

def matrixbuilt(cadena):
    i=0
    x=[['08','02','22','97','38','15','00','40','00','75','04','05','07','78','52','12','50','77','91','08']]
    while i<20:
        if i==0:
          x=[['08','02','22','97','38','15','00', '40','00','75','04','05','07','78','52','12','50','77','91','08']]
          i+=1
        else:
          fila=[]
          for j in range(0,59,3):
            entrada= cadena[60*i+j:60*i+j+2]
            fila.append(entrada)
          x=np.vstack([x,fila])
          i+=1
          if i==20:
            return x
def products(matriz):
    list=[]
    m=matriz
    #Horizontales
    greatp_1=1
    i=0
    while i<20:
      for j in range (17):
        product=int(m[j][i])*int(m[j+1][i])*int(m[j+2][i])*int(m[j+3][i])
        if greatp_1>product:
         greatp_1=greatp_1
        else:
         greatp_1=product
      i+=1
      if i==20:
          a= greatp_1
          list.append(a)
    #Verticales
    greatp_2=1
    i=0
    while i<20:
      for j in range (17):
        product=int(m[i][j])*int(m[i][j+1])*int(m[i][j+2])*int(m[i][j+3])
        if greatp_2>product:
         greatp_2=greatp_2
        else:
         greatp_2=product
      i+=1
      if i==20:
          b= greatp_2
          list.append(b)
    #Diagonales por izquierda
    greatp_3=1
    i=0
    while i<17:
      for j in range (17):
        product=int(m[i][j])*int(m[i+1][j+1])*int(m[i+2][j+2])*int(m[i+3][j+3])
        if greatp_3>product:
         greatp_3=greatp_3
        else:
         greatp_3=product
      i+=1
      if i==17:
          c= greatp_3
          list.append(c)
    #Diagonales por la derecha
    greatp_4=1
    i=0
    while i<17:
      for j in range (17):
        product=int(m[i][j+3])*int(m[i+1][j+2])*int(m[i+2][j+1])*int(m[i+3][j])
        if greatp_4>product:
         greatp_4=greatp_4
        else:
         greatp_4=product
      i+=1
      if i==17:
          d= greatp_4
          list.append(d)
    print max(list)



products(matrixbuilt(leerNumero('Documents/USAC/Progra1/Tareas/Tarea 5/grid.txt')))
