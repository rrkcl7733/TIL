R, B = map(int, input().split())
T = R + B

for L in range(1, int(T**0.5) + 1):
    if not T % L:
        W = T // L
        if (L - 2) * (W - 2) == B:
            print(max(L, W), min(L, W))
            exit()
