import operator
def product(list):
    p=1
    for i in list:
        p*=1
    return p


lista=[]
with open('Numerote.txt','r') as f:
    greatest=1
    for i in range (0,986):
        f.seek(i)
        j=f.read(13)
        lista.append(j)
        for r in lista:
            if product(list(int(r)))>greatest:
                greatest=product(list(lista[r]))
        
def product_of_digits(number):
    d, s = str(number), 0
    while s <= (len(d)-13):
        lista.append(int(d[s]) * int(d[s+1]) * int(d[s+2]) * int(d[s+3]) * int(d[s+5]* int(d[s+6])* int(d[s+7])* int(d[s+8])* int(d[s+9]) * int(d[s+10]) * int(d[s+11]) * int(d[s+12]))
    s
 