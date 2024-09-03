X, Y = map(int, input().split())

a = -Y / X
b = Y * 2
c = - X * Y / 2
t = (b ** 2 - 4 * a * c) ** .5

r1 = (t - b) / (2 * a)
r2 = (-t - b) / (2 * a)

print(r1 if 0 <= r1 <= X else r2)
