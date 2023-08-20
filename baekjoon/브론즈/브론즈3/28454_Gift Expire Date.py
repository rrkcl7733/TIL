from datetime import datetime


date1 = datetime.strptime(input(), '%Y-%m-%d')
x = 0
for _ in range(int(input())):
    if (date1 - datetime.strptime(input(), '%Y-%m-%d')).days <= 0:
        x += 1
print(x)
