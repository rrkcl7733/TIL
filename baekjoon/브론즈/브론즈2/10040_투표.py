N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

votes = [0] * N

for bj in B:
    for i in range(N):
        if A[i] <= bj:
            votes[i] += 1
            break

print(votes.index(max(votes)) + 1)
