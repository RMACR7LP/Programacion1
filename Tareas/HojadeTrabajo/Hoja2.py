def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

x=[]
for i in range(1,1000000):
    if isprime(i):
        x.append(i)

count_1=0
for m in range(0,len(x)):
    if 10>x[m]>1:
        a=x[m]
        if a in x:
            count_1+=1
print count_1

count_2=0
for m in range(0,len(x)):
    if 10>(x[m]/10)>=1:
        a=x[m]
        b=(x[m]/10)+((x[m]%10)*10)
        if b in x:
            count_2+=1
print count_2

count_3=0
for m in range(0,len(x)):
    if 10>(x[m]/100)>=1:
        a=x[m]
        b=(x[m]/10)+((x[m]%10)*100)
        c=(b/10)+((b%10)*100)
        if b in x and c in x:
            count_3+=1
print count_3
count_4=0
for m in range(0,len(x)):
    if 10>(x[m]/1000)>=1:
        a=x[m]
        b=(x[m]/10)+((x[m]%10)*1000)
        c=(b/10)+((b%10)*1000)
        d=(c/10)+((c%10)*1000)
        if b in x and c in x and d in x:
            count_4+=1

print count_4

count_5=0
for m in range(0,len(x)):
    if 10>(x[m]/10000)>=1:
        a=x[m]
        b=(x[m]/10)+((x[m]%10)*10000)
        c=(b/10)+((b%10)*10000)
        d=(c/10)+((c%10)*10000)
        e=(d/10)+((d%10)*10000)
        if b in x and c in x and d in x and e in x:
            count_5+=1

print count_5
count_6=0
for m in range(0,len(x)):
    if 10>x[m]/100000>=1:
        a=x[m]
        b=(x[m]/10)+((x[m]%10)*100000)
        c=(b/10)+((b%10)*100000)
        d=(c/10)+((c%10)*100000)
        e=(d/10)+((d%10)*100000)
        f=(e/10)+((e%10)*100000)
        if b in x and c in x and d in x and e in x and f in x:
            count_6+=1

print count_6

print count_1 + count_2 + count_3 + count_4 + count_5 + count_6







