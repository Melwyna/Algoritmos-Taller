contbultos=0
promedbultos=0
bultopes=0
bultoliv=0
valor0=0
valor36=0
valor301=0
b0=0
b1=0
b2=0
b3=0
b4=0
b5=0
b6=0
b7=0
b8=0
b9=0
b10=0
b11=0
b12=0
b13=0
b14=0
b15=0
b16=0
for x in range(0,17):
 bulto=float(input("Escribe el bulto en (kg):"))
 if x==0:
  b0+=bulto
 if x==1:
  b1+=bulto
 if x==2:
  b2+=bulto
 if x==3:
  b3+=bulto
 if x==4:
  b4+=bulto
 if x==5:
  b5+=bulto
 if x==6:
  b6+=bulto
 if x==7:
  b7+=bulto
 if x==8:
  b8+=bulto
 if x==9:
  b9+=bulto
 if x==10:
  b10+=bulto
 if x==11:
  b11+=bulto
 if x==12:
  b12+=bulto
 if x==13:
  b13+=bulto
 if x==14:
  b14+=bulto
 if x==15:
  b15+=bulto
 if x==16:
  b16+=bulto
 if bulto>=500:
  print("el avion no puede llevar esa carga")
  break
  if bulto>=18000:
   print("el avion no puede llevar esa carga")
   break
 else:
  if bulto>=0 and bulto<=25:
   valor0+=1
   contbultos+=1
  if bulto>=36 and bulto<=300:
   valor36+=1
   contbultos+=1
  if bulto>=301 and bulto<=500:
   valor301+=1
   contbultos+=1
v1=valor0*0
v2=valor36*1500
v3=valor301*2500
promedbultos=(v1+v2+v3)/17
suma=(b0+b1+b2+b3+b4+b5+b6+b7+b8+b9+b10+b11+b12+b13+b14+b15+b16)
print("la suma de todos los bultos es de:", suma,",promedio:", promedbultos, "y bultos de 0-25:", valor0, "y bultos de 36-300:", valor36, "y bultos de 301-500:", valor301)
