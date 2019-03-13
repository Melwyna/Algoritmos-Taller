se=int(input("ingrese los segundos:"))
seg=float(se/60)
mi=float(seg/60)
segu=(se%60)
mit=(seg%60)
mic=mi-int(mi)
mid=mi-mic
mit1=mit-int(mit)
mie=mit-mit1
print("los segundos ingresados dan como resultado: ", ("%.0f" % mid), ":", ("%.0f" % mie), ":",("%.0f" % segu))
