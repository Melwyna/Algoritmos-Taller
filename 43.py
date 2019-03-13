n_1=0
n_2=0
n_3=0
for x in range(0,3):
 n1=float(input("Escribe un numero:"))
 if x==0:
  n_1+=n1
 if x==1:
  n_2+=n1
 if x==2:
  n_3+=n1
  if n_1>n_2 and n_1<n_3:
   print ("Ni se incrementa ni se disminuyendo")
  if n_1>n_2 and n_2>n_3 and n_1>n_3:
   print ("esta dismininuyendo")
  if n_1<n_2 and n_2<n_3 and n_1<n_3:
   print ("esta aumentando")

