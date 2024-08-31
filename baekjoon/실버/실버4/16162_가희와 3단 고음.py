n, a, d = map(int, input().split())
n_list = list(map(int, input().split()))

ans = 0
temp = a

for i in range(n):
    if n_list[i] == temp:
        ans += 1
        temp += d

print(ans)
