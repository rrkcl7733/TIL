N = int(input())
A = list(map(int, input().split()))

max_len = cur_len = 1

for i in range(1, N):
    if A[i-1] <= A[i]:
        cur_len += 1
    else:
        cur_len = 1
    max_len = max(max_len, cur_len)

print(max_len)
