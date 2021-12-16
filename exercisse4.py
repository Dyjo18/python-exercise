first_name = input("Quel est votrre prénom? ")
last_name = input("Quel est votre nom ")
birthday_date= int(input("Quel est votre année de naissance? "))
today_date = int(input("En quel anee sommes nous? "))

age =str(today_date-birthday_date)


print("Bienvenu(e) " + first_name + " " + last_name)

print("Vu que tu es né en " + str(birthday_date) + " " + ",je sais que tu as " + age + " ans!")