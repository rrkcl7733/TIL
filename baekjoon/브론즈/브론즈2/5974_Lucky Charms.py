L, C, N = map(int, input().split())
for _ in range(C):
    S, P = map(int, input().split())
    droop = abs(P - N) + S
    print(droop)
