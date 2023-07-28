a = input()
b = input()
x = 0
for i in range(4):
    if a[i] != b[i]:
        x += 1
print(2 ** x)
