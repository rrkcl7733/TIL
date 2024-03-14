K = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
cnt = 0
for p in range(N):
    for q in range(M):
        if A[p] + K == B[q]:
            cnt += 1
print(cnt)
