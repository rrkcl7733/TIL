N, X = map(int, input().split())
H = list(map(int, input().split()))

max_count = 1
cnt = [1] * N

for i in range(1, N):
    if H[i] <= H[i - 1] + X:
        cnt[i] = cnt[i - 1] + 1
        max_count = max(max_count, cnt[i])

print(max_count)
