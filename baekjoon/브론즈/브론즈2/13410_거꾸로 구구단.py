N, K = map(int, input().split())

max_val = 0
for i in range(1, K + 1):
    val = int(str(N * i)[::-1])
    if val > max_val:
        max_val = val

print(max_val)
