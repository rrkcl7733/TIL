N = int(input())
c = 0
for _ in range(N):
    p, q, r, s = input().split()
    c += p[:2] != r[:2]
print(2 * N / c)
