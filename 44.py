n_1=0
n_2=0
for x in range(0,2):
 n1=float(input("Escribe un numero:"))
 if x==0:
  n_1+=n1
 if x==1:
  n_2+=n1
  if n_1>=0 and n_1<=5 and n_2>=0 and n_2<=5:
   print (n_1, "-", n_2, "==> true")
  if n_1<0 or n_2<0 or n_1>5 or n_2>5:
   print (n_1, "-", n_2, "==> false")
