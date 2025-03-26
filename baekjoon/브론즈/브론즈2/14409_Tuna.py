N = int(input())
X = int(input())

total_value = 0

for _ in range(N):
    P1, P2 = map(int, input().split())

    if abs(P1 - P2) <= X:
        total_value += max(P1, P2)
    else:
        P3 = int(input())
        total_value += P3

print(total_value)
