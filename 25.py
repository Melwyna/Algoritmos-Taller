num=int(input("Escribe el numero:"))
p=int(num/1000)
p2=int(p*1000)
s2=int(p2-num)
s=int(s2/100)
s3=int(s*100)
s4=int(-(s*10))
t=int(s2-s3)
t2=int(t/10)
t3=int(t2*10)
t4=int(-(t2*100))
c=int(t3-t)
c2=int(c*1000)
inv=(p+c2+t4+s4)
print ("El numero reordenado es:", inv)
