 
five_number=""
print("Hello")
print ("Tu veut calculer la moyenne de ta classe ?\nLa note est obligatoirement sur 20!")
first_number = int(input("Donner moi la note 1 ")) 
while  (first_number>=21) :
    print("OOPS votre note n'est pas sur 20 !")
    first_number = int(input("Donner moi la note 1 ")) 
second_number = int(input("Donner moi la note 2 "))
while  (second_number>=21) :
    print("OOPS votre note n'est pas sur 20 !")
    second_number = int(input("Donner moi la note 2 ")) 
third_number = int(input("Donner moi la note 3 ")) 
while  (third_number>=21) :
    print("OOPS votre note n'est pas sur 20 !")
    third_number = int(input("Donner moi la note 3 ")) 
four_number = int(input("Donner moi la note 4 ")) 
while  (four_number>=21) :
    print("OOPS votre note n'est pas sur 20 !")
    four_number = int(input("Donner moi la note 4 ")) 
int(input("Donner moi la note 5 ")) 
while  (five_number >= 21) :
    print("OOPS votre note n'est pas sur 20 !")
    five_number = int(input("Donner moi la note 5 "))


moyenne = round((str(first_number)+str(second_number)+str(third_number)+str(four_number)+str(five_number))/5)
print('Ta moyenne est de '+str(moyenne))

if(moyenne<=4):
     print('Ta moyenne est '"pas terrible.")
elif(moyenne>=5 and moyenne<=9):
    print('Ta moyenne est '"pas au top. Motivez-vous les gars.")
elif(moyenne>=10 and moyenne<=14):
    print('Ta moyenne est '"bonne! Continuez comme ça.")
elif(moyenne>=15 and moyenne<=19):
    print('Ta moyenne est '"au top! Vous êtes les meilleurs.")
elif(moyenne==20):
    print('Ta moyenne est '"INSANE! Prenez ma place.")
   