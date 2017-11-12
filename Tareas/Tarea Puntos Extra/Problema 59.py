#-*- coding: utf-8 -*-
import os
b=os.path.getsize("cipher.txt")
numbers=[]
with open('cipher.txt','r') as cipher:
    coma1=0
    cipher.seek(0)
    coma2= cipher.read().find(",")
    cipher.seek(0)
    while coma2<3199:
        cipher.seek(coma1)
        x=cipher.read(coma2-coma1)
        numbers.append(x)
        coma1=coma2+1
        cipher.seek(coma1)
        coma2=cipher.read().find(",")+coma1

numbers.append(22)
numbers.append(73)



chosen1=[]
for i in range(97,123):
   if 96<79^i<123 or 64<79^109<91:
        chosen1.append(79^109)

print chosen1

print 40^79 #Buscamos el primer caracter de clave usando xor con la palabra original y la cifrada, (=40

chosen=[]
for i in range (97,123):
    for k in range (97,123):
        for j in range(0,10,3):
            chosen.append(int(numbers[j])^103)
            chosen.append(int(numbers[j+1])^i)
            chosen.append(int(numbers[j+2])^k)
        chosen.append(int(32)) # esto fue para separar los resultados

#print ''.join(chr(i) for i in chosen)

print 84^59 #Aquí buscamos el segundo caracter de la clave, T=84 
print 104^12 #Aquí encontramos el tercero h=104

#Luego hacemos xor sobre la lista con la clave
chosen2=[]

for j in range(0,len(numbers)-2,3):
    chosen2.append(int(numbers[j])^103)
    chosen2.append(int(numbers[j+1])^111)
    chosen2.append(int(numbers[j+2])^100)

print len(numbers)

print len(chosen2)

print sum(chosen2)+int(numbers[1200]^103)

print ''.join(chr(i) for i in chosen2)

print 46^100
