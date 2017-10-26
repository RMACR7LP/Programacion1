names=["ALONSO","BRODERICK"]
with open('names.txt','r') as f:
     coma1=0
     f.seek(0)
     coma2= f.read().find(",")+1
     f.seek(0)
     m=f.read().find("ALONSO")
     f.seek(0)
     while coma2<m-2:
        f.seek(coma1+1)
        x= f.read(coma2-coma1-3)
        names.append(x)
        coma1=coma2
        f.seek(coma1)
        coma2=f.read().find(',')+coma1+1


names= sorted(names)

letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

suma=[]
for i in range(0,len(names)):
    lista=list(names[i])
    l=len(lista)
    x=0
    for j in range(0,l):
       x=x+(letras.index(lista[j])+1)
    
    y=(i+1)*x
    suma.append(y)

print sum(suma)