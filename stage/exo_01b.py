
duration = input('Quelle durée (en jours) pour votre formation ? ')

days = int(duration)
day_duration = 7
print(str(days) + " days of " + str(day_duration) + " hours")
print("total duration: " + str(days * day_duration) + " hours")