a = input()
x = 0
for i in range(0, len(a) - 3):
    if a[i:i + 4] == 'kick':
        x += 1
print(x)
