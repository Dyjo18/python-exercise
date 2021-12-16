# Créé par jody.vanachter, le 02-12-2021 en Python 3.7

first_name = input("quel est ton prénom?")

last_name = input("quel est ton nom?")

age = int(input("quel est ton age?"))


print("Salut " + first_name + " " + last_name + " et tu as " + str(age) + " ans!")

if (age >=18) :
    print("Génial! Tu peut commencer à conduire.")
elif (age >= 12) and (age < 18) :
     print("J'ai entre 12 et 17 ans!")

else :
    print("Tu ne peut pas conduire. ")

#if (reponse == "oui") or (reponse == "ouais") or (reponse == "yep") :

#while = tant que (boucle)
#while (age <18) :
   # print("Je ne peut pas conduire car j'ai " + str(age) + " ans!")
   # age = age + 1

#print("Let's go je peut conduire")


#while ( play == False) :
#while (play == True) :
#!play = a play == False
#play = a play == True

#for i  in range(5, 11) :#plage 0 a (max-1) -->10
   # print(i)
    #i = i + 1  cette ligne n'est pas obligée sa le fait auto!


for Letter  in first_name :
    print(Letter)

fruit1 = "pomme"
fruit2 = "banane"
fruit3 = "poire"
fruit4 = "cerise"
fruit5 = "fraise"

fruits = ["pomme", "banane", "poire", "cerise", "fraise"]

for fruit in fruits :
    print(fruit)

    if (fruit == "poire") :
        print("OMG! Je kiffe les " + fruit + "s!")


