import sys


input = sys.stdin.readline
N = int(input())
start = 0 # 팬들이 온 최소시각
end = 1e5 # 팬들이 떠난 최대시각

for _ in range(N):
    a, b = map(int, input().split())
    start = max(start, a)
    end = min(end, b)

print(0 if end > start else start - end)
