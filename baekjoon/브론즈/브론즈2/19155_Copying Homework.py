N = int(input())
A = list(map(int, input().split()))

indexed_A = sorted([(val, idx) for idx, val in enumerate(A)])

B = [0] * N
for (val, idx), b in zip(indexed_A, list(range(N, 0, -1))):
    B[idx] = b

print(*B)
