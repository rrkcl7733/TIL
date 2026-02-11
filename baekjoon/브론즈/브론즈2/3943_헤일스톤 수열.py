import sys


input = sys.stdin.readline
for _ in range(int(input())):
    cur = max_val = int(input())
    while cur != 1:
        if cur % 2:
            cur = cur * 3 + 1
        else:
            cur //= 2
        if cur > max_val:
            max_val = cur
    print(max_val)
