import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for _ in range(m):
    com, *k = map(int, input().split())
    if com == 1:
        print(n - bisect_left(arr, k[0]))
    elif com == 2:
        print(n - bisect_right(arr, k[0]))
    else:
        print(bisect_right(arr, k[1]) - bisect_left(arr, k[0]))
