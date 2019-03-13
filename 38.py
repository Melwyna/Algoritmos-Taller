año=float(input("Escribe el año:"))
if año%4==0 and año%100!=1 and año%400==0:
  print("El año es bisiesto")
else:
  print("El año no es bisiesto")
