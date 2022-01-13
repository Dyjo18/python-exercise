a = int(input("Donner moi un nombre svp : "))

while (a < 1 ):
  print ("Réessayer , il faut que A soit différent de 0 ")
  a = int(input("Donner moi un nombre svp : "))

b = int(input("Donner moi un nombre svp : "))
c = int(input("Donner moi un nombre svp : "))


print ("A est égal à : " + str(a))
print ("B est égal à : " + str(b))
print ("C est égal à : " + str(c))

delta= int(b**2 - 4*a*c)

print ("Delta est égal à : " + str(delta))


if (delta < 0 ):
    print("Pas de solution .")
    calcul= 


if (delta == 0 ):
    print("l’équation a une unique solution .")

if( delta > 0 ):
    print ("L'équation a 2 solution . ")