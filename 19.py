import math
x1=float(input("ingrese la coordenada x1:"))
y1=float(input("ingrese la coordenada y1:"))
x2=float(input("ingrese la coordenada x2:"))
y2=float(input("ingrese la coordenada y2:"))
dist= (((x2-x1)**2)+(y2-y1)**2)
dt=math.sqrt(dist)
print("la distancia es:", dt)
