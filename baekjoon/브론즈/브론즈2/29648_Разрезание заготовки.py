a, b, S = map(int, input().split())
L = (a + b + ((a + b) ** 2 - 4 * (a * b - S)) ** .5) / 2

print(int(L) if L.is_integer() else -1)
