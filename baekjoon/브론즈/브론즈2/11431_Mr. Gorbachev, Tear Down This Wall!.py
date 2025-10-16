import math


for idx in range(int(input())):
    n, s, p = map(int, input().split())
    points = [list(map(int, input().split())) for _ in range(n + 1)]
    total_length = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        segment_length = abs(x2 - x1) + abs(y2 - y1)
        total_length += segment_length
        
    rounded_time = math.ceil(total_length * s / p)
    print(f"Data Set {idx + 1}:\n{rounded_time}\n")
