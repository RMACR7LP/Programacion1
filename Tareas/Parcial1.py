
list=[]

d=9

while  d>6:
    list.append (6*d+6*(d-2)+6*(d-4)+6*(d-6))
    list.append ((6*d+6*(d-2)+6*(d-4)+6*(d-6))*10)
    list.append ((6*d+6*(d-2)+6*(d-4)+6*(d-6))*100)
    list.append ((6*d+6*(d-2)+6*(d-4)+6*(d-6))*1000)
    d -= 1
print sum(list)
