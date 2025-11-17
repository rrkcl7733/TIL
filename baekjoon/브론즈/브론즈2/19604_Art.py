xs, ys = [], []
for _ in range(int(input())):
    x_str, y_str = input().split(',')
    x, y = int(x_str), int(y_str)
    xs.append(x)
    ys.append(y)

min_x = min(xs)
min_y = min(ys)
max_x = max(xs)
max_y = max(ys)

print(f"{min_x - 1},{min_y - 1}")
print(f"{max_x + 1},{max_y + 1}")
