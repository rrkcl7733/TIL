import sys
input = sys.stdin.readline


w = int(input())
x = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    x += a * b
print(x // w)
