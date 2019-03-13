num1=int(input("cuantos divisores quiere imprimir: "))
cant=0
num=int(input("ingrese un numero:"))
for x in range(1,num1+1):
	if num%x==0:
	 print("tiene como divisor a:",x)
	 cant=cant+1
print("La cantidad de numeros en los que se puede dividir:",cant)

