xs, ys = [], []

for _ in range(int(input())):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

# x축과 y축의 길이 중 더 큰 값이 정사각형 변의 길이임
side = max(max_x - min_x, max_y - min_y)

print(side ** 2)
