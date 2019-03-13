d1=float(input("ingrese la distancia a recorrer (km):"))
ne1=float(input("ingrese el numero de dias de estancia:"))
precd=(d1*5000)
if d1>1000 and ne1>7:
 f_1=(precd*15)/100
 f1=(precd-f_1)
 print ("El tikete de avion con el descuento del 15% por tener una distancia mayor a 1000 km y una estancia mayor a 7 dias es de:", f1)
else:
 print("El valor del tikete es:", precd)
