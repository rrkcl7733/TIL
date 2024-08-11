N = int(input())
ans = 0

while N:
    N, r = divmod(N, 256)
    ans = ans * 256 + r

print(ans)
