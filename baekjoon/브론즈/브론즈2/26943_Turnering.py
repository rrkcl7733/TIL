n, r = map(int, input().split())

ns = [0] * n
for i in range(n - 1):
    t = i - r + 2
    if t <= 0:
        t += n - 1
    ns[i] = t
ns[-1] = n

for i in range(n // 2):
    print(f'{ns[i]}-{ns[n - i - 1]}')
