
def is_prime(n):

    if n % 2 == 0: return False

    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True

list=[]
n=3
while n <2000000:
   if is_prime(n):
       list.append(n)
       n +=2
   else:
       n +=2

if n==2000001:
  print sum(list)+2
