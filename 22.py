se=int(input("ingrese los segundos:"))
mi=float(se/60)
if se>=60:
 print("los segundos ingresados dan como resultado", ("%.1f" % mi))
else:
  print("Los segundos ingresados respresentan menos de un minuto")
