import sys

duration = input('Quelle durée (en jours) pour votre formation ? ')
try:
    days = int(duration)
except ValueError:
    print("La durée n'est pas de type entier")
    sys.exit(1)

day_duration = 7
print(str(days) + " days of " + str(day_duration) + " hours")
print("total duration: " + str(days * day_duration) + " hours")
