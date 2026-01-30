import sys


for line in sys.stdin:
    N, B, M = map(float, line.strip().split())
    years = 0
    while N < M:
        N *= (1 + B/100)
        years += 1
    print(years)
