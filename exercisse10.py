time = int(input("Donner moi un temps en seconde : "))

hours = int(time/3600)
hours_reminder= int(time%3600)
minutes = int(hours_reminder/60)
minutes_reminder= int(minutes%60)
second = minutes_reminder/60


print (str(hours)+"  Heures  " +str(minutes)+"  Minutes  "+str(second)+"  Secondes")