import math
n= int(input("introduce el numero:"))
#a
if (n%2==0) or (n%7!=0):
#c
 if (int(math.sqrt(n))**2 == n) and (n%4==0):
#e
  if ((n%7!=0) and (n%10!=0)) or (((int(math.sqrt(n))**2 == n) and (n%4==0))):
   print("Es un numero Craft")
else:
  #b
 if (n%10!=0) or (n%7!=0):
#d
  if (n%10!=0) and (n%4==0):
#f
   if ((n&10!=0) or (n%7!=0)) and (((n%4==0) and (int(math.sqrt(n))**2 == n))):
    print("No es un numero Craft")
