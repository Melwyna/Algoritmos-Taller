pos=0
neg=0
par=0
imp=0
mul8=0
for x in range (0,5):
 n1=int(input("Ingresa un numero:"))
 if n1>=0:
  pos+=1
 if n1<0:
  neg+=1
 if n1%2==0:
  par+=1
 if n1%2!=0:
  imp+=1
 if n1%8==0:
  mul8+=1
print("Hubo un total de:", pos, "numeros positivos,", neg, "numeros negativos,", par, "numeros pares,", imp, "numeros impares y ", mul8, "numeros multiplos de ocho")
