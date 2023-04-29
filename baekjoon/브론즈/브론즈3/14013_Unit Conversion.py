import sys
input = sys.stdin.readline


a, b = map(float, input().split())
for _ in range(int(input())):
    x, t = input().split()
    print(float(x) / b * a if t == 'B' else float(x) / a * b)
