continued = int("1")

while  (continued <2) :

 first_number = int(input("Donner moi un nombre "))
 second_number = int(input("Interraissent. Et ton 2e nombre ? "))
 
 operation = int(input("Okay\nQuel opération voullez vous faire ?  \nAddition (1) \nSoustraction (2) \nDivision (3) \nMultiplication (4)\n"))
 if(second_number==0) or (first_number==0):
               print("Imposible!!!!")
                
 elif(operation == 1):
        result= first_number + second_number
        print("votre calcul est " + str(first_number) + " + " + str(second_number) + " = " +str(result)+"   😎")
 elif(operation == 2):
        result = first_number - second_number
        print("votre calcul est " + str(first_number) + " - " + str(second_number) + " = " +str(result)+"   😎") 
 elif(operation == 3):
        
        result = first_number / second_number
        print("votre calcul est " + str(first_number) + " / " + str(second_number) + " = " +str(result)+"   😎") 
 elif(operation == 4):
        result = first_number * second_number
        print("votre calcul est " + str(first_number) + " * " + str(second_number) + " = " +str(result)+"   😎") 
 while(operation >=5):
        print("Désoler,ce choit n'est pas disponible.Veut tu réessayer ? ")
        operation = int(input("Quel opération voullez vous faire ?  \nAddition (1) \nSoustraction (2) \nDivision (3) \nMultiplication (4)\n"))
 
 
 continued= int(str(input("Vouler vous continuer a calculer ? \noui[1]\nnon[2] ")))
 
 while(continued >=3):
         print("Désoler,ce choit n'est pas disponible.Veut tu réessayer ? ")
         continued= int(str(input("Vouler vous continuer a calculer ? \noui[1]\nnon[2] ")))


 









         
         

 





    
