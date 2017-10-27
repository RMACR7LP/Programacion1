# Haciendo manipulaciones algebraicas llegamos a que se debe cumplir
# que (1000-a)(1000-b)=2^5 * 5^6, de donde
for x in range(0,6):
    for y in range(0,7):
        a=1000-2**(x)*5**(y)
        b=1000-500000/(1000-a)
        if 0<a<b<1000-a-b and a**2 +b**2==(1000-a-b)**2: 
            print (a*b*(1000-a-b))
            
