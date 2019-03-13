se=int(input("ingrese los segundos:"))
h=float(se/3600)
if se>=3600:
 print("los segundos ingresados dan como resultado", ("%.1f" % h))
else:
  print("Los segundos ingresados respresentan menos de una hora")
