import sys


input = sys.stdin.readline
costs = {}
for _ in range(int(input())):
    X, T, C = map(int, input().split())
    costs[T - X] = costs.get(T - X, 0) + C

print(max(costs.values()))
