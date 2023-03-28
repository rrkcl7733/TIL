a, b = map(int, input().split())
x, y = map(int, input().split())
b, y = b // x + (1 if b % x else 0), y // a + (1 if y % a else 0)
print('DRAW' if b == y else 'PLAYER A' if b > y else 'PLAYER B')
