#-*- coding:utf-8 -*-
#Si n es el valor de una moneda, establecemos la cota q de la forma; nq=200
counter=0
for j in range(0,5): #q=4
    for k in range(0,11): #q=10
        for l in range (0,21): #q=20 
            for m in range(0,41):#q=40
                for n in range(0,101):#q=100
                    for o in range(0,201):#q=200
                        if (n*2+o)%5==0: #como 200 es múltiplo de 5, esta relación deja fuera los casos en los que la suma de la monedas 1 y 2 no sumen un multipo de 5.
                            if j*50+k*20+l*10+m*5+n*2+o==100 or j*50+k*20+l*10+m*5+n*2+o==200:
                                counter+=1
                                
print counter +2 
#Nota: la línea 10 considera los casos en los cuales hay una moneda de 1 libra o no hay ninguna, esto para evitar el uso del "for"
#además, al counter le sumamos 2 considerando los casos en los que hay una moneda de 2 libras o 2 monedas de 1 libra pues son casos únicos.
