w = float(input())
x = w / float(input()) ** 2
print('Underweight' if x < 18.5 else 'Overweight' if x > 25 else 'Normal weight')
