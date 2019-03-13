con100=0
con5=0
contn=0
while con100<=100 and con5<80:
 x=int(input("Escribe el numero:"))
 contn+=1
 if x==5:
  con5+=1
 if x%2==0:
  con100+=1
print("La cantidad de numero leidos fue de:", contn)


