n, P = map(int, input().split())
tot = 1
for i in range(2, n+1):
    tot = (tot * i) % P

print(tot % P)
