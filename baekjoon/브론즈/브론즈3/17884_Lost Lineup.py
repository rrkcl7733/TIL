n = int(input())
x = [0] * n
x[0] = 1
t = 2
for i in map(int, input().split()):
    x[i + 1] = t
    t += 1
print(*x)
