import math
h=float(input("Cual es la altura de la que se suelta el objeto?"))
g=9.8
t_1= (2*h)/g
t= math.sqrt(t_1)
print("El tiempo de caida del objeto fue:", t,"segundos")
