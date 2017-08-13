def isprime(n):
 for x in range (2,int(n**0.5)+1):
   if n % x == 0: return False
 return True

list=[]
n=2
while len(list)<10001:
  if isprime(n):
    list.append(n)
    n+=1
  else:
    n+=1
if len(list)== 10001:
    print n-1
