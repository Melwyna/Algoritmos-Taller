vv= int(input("introduce el valor de la venta:"))
vv_iva1=(vv*19)/100
vv_iva=(vv+vv_iva1)
if vv>150000:
 des_1=(vv*5)/100
 des=(vv-des_1)
 print("el valor de la venta con iva incluido", vv_iva ,"y con el descuento del 5% es:", des)
else:
 if vv<150000:
  print("el valor de la venta con iva incluido es:", vv_iva)
