import math
lado=float(input("Ingrese la medida de uno de los lados del hexagono:"))
apotema_1=(lado*lado)-((lado/2)**2)
apotema= math.sqrt(apotema_1)
area=(3*lado)*(apotema)
print("El area del hexagono es:", area, "centimetros cuadrados")
