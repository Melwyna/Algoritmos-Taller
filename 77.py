usua="g0812"
cotr="081215"
for x in range(0,3):
 usuario=str(input("Ingrese su usuario:"))
 contraseña=str(input("Ingrese su contraseña:"))
 if usuario==usua and contraseña==cotr:
  print("SU USUARIO Y CONTRASEÑA SON CORRECTOS")
 else:
  print("SU USUARIO Y CONTRASEÑA SON INCORRECTOS")
print("YA LLEVA 3 INTENTOS, VUELVA A INTENTAR EN 1 MINUTO")
