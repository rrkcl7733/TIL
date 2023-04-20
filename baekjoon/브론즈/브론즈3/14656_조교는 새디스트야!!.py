i, x = 1, 0
input()
for n in map(int, input().split()):
    if n != i:
        x += 1
    i += 1
print(x)
