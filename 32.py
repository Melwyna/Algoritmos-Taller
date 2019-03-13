n1_a= int(input("introduce la primera nota (15%) :"))
n2_b= int(input("introduce la segunda nota (20%) :"))
n3_c= int(input("introduce la tercera nota (15%) :"))
n4_d= int(input("introduce la cuarta nota (30%) :"))
n5_e= int(input("introduce la quinta nota (20%) :"))
n1= (n1_a*15)/100
n2= (n2_b*20)/100
n3= (n3_c*15)/100
n4= (n4_d*30)/100
n5= (n5_e*20)/100
nf=int(n1+n2+n3+n4+n5)
if nf>45:
 print("Felicidades tu nota final es mayor a cuatro cinco")
else:
 if nf>=30:
  print("Tu nota final es mayor igual a tres por ello, se aprobo")
  if nf<30:
    print ("Tu nota final es menor a tres por ello, se reprobo")
  else:
    if nf<20:
      print ("Tu nota final es menor a dos por ello, no se puede habilitar")
