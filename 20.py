dg=int(input("ingrese el digito:"))
dd=dg*11
ddd=dg*111
suma=(dg+dd+ddd)
if 9>=dg>=0:
 print("los valores generados son:", dg, ",", dd, ",", ddd, "y la suma de todos ellos es:", suma)
else:
  print("el digito ingresado no se encuentra en el limite de 0 a 9")
