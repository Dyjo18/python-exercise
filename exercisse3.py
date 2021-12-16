first_name = str(input("Quel est votre prénom?"))
first_name_reversed = ""


for letter in first_name :
    first_name_reversed = letter + first_name_reversed
print("votre prénom a l'enver est " + first_name_reversed)
