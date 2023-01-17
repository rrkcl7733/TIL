a, b, x, y = map(int, input().split())
a *= b
x *= y
print('M' if a > x else 'P' if a < x else 'E')
