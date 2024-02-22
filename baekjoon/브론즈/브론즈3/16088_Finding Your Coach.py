import sys


input = sys.stdin.readline
for _ in range(int(input())):
    l, r, n, m = map(int, input().split())
    is_exist_left = abs(n - m) <= l
    is_exist_right = abs(n - m) <= r

    if n == m:
        print("G")
    elif is_exist_left and not is_exist_right:
        print("L")
    elif not is_exist_left and is_exist_right:
        print("R")
    else:
        print("E")
