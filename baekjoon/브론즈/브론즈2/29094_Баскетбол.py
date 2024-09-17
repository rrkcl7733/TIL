d = {input(): 0 for _ in range(int(input()))}
prev = 0
for _ in range(int(input())):
    p, q, r = input().replace(*': ').split()
    d[r] -= prev - (prev := int(p) + int(q))
t = sorted(list(d.items()), key=lambda s: s[1])
print(*t[-1])
