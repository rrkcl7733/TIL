import sys
from math import ceil

input = sys.stdin.readline
N, K = map(int, input().split())

group_12 = group_34_f = group_34_m = group_56_f = group_56_m = 0

for _ in range(N):
    S, Y = map(int, input().split())
    if Y <= 2:
        group_12 += 1
    elif Y <= 4:
        if S:
            group_34_m += 1
        else:
            group_34_f += 1
    else:
        if S:
            group_56_m += 1
        else:
            group_56_f += 1

rooms = (ceil(group_12 / K) + ceil(group_34_f / K) + ceil(group_34_m / K) +
         ceil(group_56_f / K) + ceil(group_56_m / K)
         )

print(rooms)
