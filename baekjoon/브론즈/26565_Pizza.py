from math import pi


for _ in range(int(input())):
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    a /= b
    x = x ** 2 * pi / y
    print('Whole pizza' if a < x else 'Slice of pizza')
