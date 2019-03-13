cantidad=input("¿Qué cantidad quiere retirar?")
cant_float=float(cantidad)
cant_int=int(cant_float)
divisible_5=cant_int % 5000
x=(cant_int%50000)
y=(x%20000)
z=(y%10000)
w=(z%5000)
nx=(cant_int-x)/50000
ny=(x-y)/20000
nz=(y-z)/10000
nw=(z-w)/5000
if cant_float-cant_int == 0:
  if divisible_5==0 :
    if cant_int<5000:
     print("No se puede retirar esa cantidad")
    if nx>=1:
     print(int(nx), "billetes de 50.000")
    if ny>=1:
     print(int(ny), "billetes de 20.000")
    if nz>=1:
     print(int(nz), "billetes de 10.000")
    else:
     print(int(nw), "billetes de 5.000")
  else:
   print("Esta cantidad no es válida")
