import math
n=float(input("Ingrese un numero decimal:"))
binario=""
if (n > 0):
  while (n>0):
    if (n%2==0):
      binario = "0" + binario
    else:
      binario ="1" + binario
    n = int(math.floor(n/2))
else:
  if (n == 0):
   binario= "0"
  else:
   binario="el numero ingresado no se puede convertir, solo ingrese numeros positivos"
print("El resultado de la conversion es: ", binario)
