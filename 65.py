contr=0
conts=0
promediop=0
promediop1=0
suma = 0
for x in range (0,10):
 n1=int(input("escribe el numero"))
 suma = suma+n1
 if suma%2==0:
  conts+=1
  promediop=(suma)/conts
 if suma%2!=0:
  contr+=1
  promediop1=(suma)/contr
print("el promedio de los numeros pares es:", promediop, "el promedio de los numeros impares es:", promediop1)
