import sys
import math

input = sys.stdin.readline

coords = [list(map(float, input().split())) for _ in range(int(input()))]

for _ in range(int(input())):
    p = int(input())
    route = list(map(int, input().split()))
    
    total_dist = 0.0
    for i in range(p - 1):
        x1, y1 = coords[route[i]]
        x2, y2 = coords[route[i + 1]]
        dx = x2 - x1
        dy = y2 - y1
        total_dist += math.hypot(dx, dy)
    
    rounded = math.floor(total_dist + 0.5)
    print(rounded)
