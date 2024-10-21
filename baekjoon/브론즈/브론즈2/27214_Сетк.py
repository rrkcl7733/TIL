k = int(input())
w = int(input())
h = int(input())
t = int(input())

line = '*' * (w * k + (w + 1) * t)
x = '*' * t
for _ in range(w):
    x += '.' * k + '*' * t

for _ in range(h):
    for _ in range(t):
        print(line)
    for _ in range(k):
        print(x)

for _ in range(t):
    print(line)
