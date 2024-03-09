import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a = int(input())
    t = int(bin(a)[2:])
    if t & (-t) == a:
        print(1)
    else:
        print(0)
