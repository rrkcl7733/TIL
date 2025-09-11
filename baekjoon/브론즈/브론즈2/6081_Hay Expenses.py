N, Q = map(int, input().split())
hay_counts = [0] + [int(input()) for _ in range(N)]

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + hay_counts[i]

for _ in range(Q):
    S, E = map(int, input().split())
    print(prefix_sum[E] - prefix_sum[S - 1])
