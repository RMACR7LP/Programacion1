#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fibo(i):
 if i==1 or i==2:
  print 1
 else:
  x=0
  n=0
  list=[1,1]
 while x<i-1:
   n=sum(list)
   list.append(n)
   list.pop(0)
   x+=1
   if x==i-2:
    print "El numero", i, "de Fibonacci es", n

i= input("Ingrese un numero")
fibo(i)
