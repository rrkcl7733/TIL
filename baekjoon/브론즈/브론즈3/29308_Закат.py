a = []
for _ in range(int(input())):
    n, x, c = input().split()
    if c == 'Russia':
        a.append((int(n), x))
a.sort()
print(a[-1][1])
