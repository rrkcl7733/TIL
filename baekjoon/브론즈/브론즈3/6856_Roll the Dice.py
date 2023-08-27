n = int(input())
m = int(input())
x = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i + j == 10:
            x += 1
print('There', end=' ')
print(f'is {x} way' if x == 1 else f'are {x} ways', end=' ')
print('to get the sum 10.')
