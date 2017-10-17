for i in range(1,59):
    a="curl -H"
    b= '"token:lJnIkgSpuItyqVowVZuPZskxZUemIoJG"'
    c= '"https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid=FIPS:'
    if i<10:
        print a+" "+b+" "+c+"0"+str(i)+'"' +">>estaciones"+str(i)+".json" 
    else:
        print a+" "+b+" "+c+str(i)+'"' +">>estaciones"+str(i)+".json" 