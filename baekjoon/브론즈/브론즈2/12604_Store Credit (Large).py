import sys

input = sys.stdin.readline


def solve(C, I, L):
    for i in range(I):
        for j in range(i + 1, I):
            if L[i] + L[j] == C:
                return i + 1, j + 1


for t in range(1, int(input()) + 1):
    C = int(input())
    I = int(input())
    L = list(map(int, input().split()))
    res = solve(C, I, L)
    print(f"Case #{t}: {res[0]} {res[1]}")
