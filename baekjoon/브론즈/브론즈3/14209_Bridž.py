n = int(input())
t = ['X', 'J', 'Q', 'K', 'A']

r = 0
for _ in range(n):
    for i in input():
        r += t.index(i)
print(r)
