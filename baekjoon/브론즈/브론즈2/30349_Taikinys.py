M, N = map(int, input().split())
A, B = map(int, input().split())
X, Y = map(int, input().split())

min_penalty = float('inf')
for xp in range(M):
    for yp in range(N):
        if 0 <= (tx := xp + X) < A and 0 <= (ty := yp + Y) < B:
            min_penalty = min(min_penalty, tx + ty)
print(min_penalty if min_penalty != float('inf') else 'NEPATAIKYS')
