import sys

input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    n, v = map(int, input().split())

    ad = [[0, 0] for _ in range(n + 1)]
    for j in range(1, n + 1):
        ad[j][0], ad[j][1] = map(int, input().split())

    cost = 0
    for _ in range(v):
        aj1, aj2, cj = map(int, input().split())

        if ad[aj1][0] == 1:
            cost += ad[aj1][1]
        if ad[aj2][0] == 1:
            cost += ad[aj2][1]
        if cj == 1 and ad[aj1][0] == 0:
            cost += ad[aj1][1]
        if cj == 2 and ad[aj2][0] == 0:
            cost += ad[aj2][1]

    print(f'Data Set {i}:')
    print(cost)
    print()
