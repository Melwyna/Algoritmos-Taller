may100=0
men100=0
igu100=0
for x in range (0,20):
 n1=int(input("Ingresa un numero:"))
 if n1<100:
  men100+=1
 if n1>100:
  may100+=1
 if n1==100:
  igu100+=1
print(men100, "Fueron menores, ", may100, "fueron mayores y", igu100, "fueron iguales a 100")

