time = int(input("Donner moi un temps en seconde "))

hours = round((time/3600) , 2)
minutes = time/60

print (str(hours)+" H")
print (str(minutes)+" M")
print (str(time)+" S")
