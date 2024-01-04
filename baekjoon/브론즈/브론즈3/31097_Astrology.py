date = input()
month, day = int(date[5:7]), int(date[8:10])
x = ''
if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    x = "Aquarius"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    x = "Pisces"
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    x = "Aries"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    x = "Taurus"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    x = "Gemini"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    x = "Cancer"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    x = "Leo"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    x = "Virgo"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    x = "Libra"
elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
    x = "Scorpio"
elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
    x = "Sagittarius"
else:
    x = "Capricorn"
print(x)
