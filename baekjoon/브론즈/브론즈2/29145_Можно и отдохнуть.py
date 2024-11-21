n, k = map(int, input().split())
total_penguins = 0
for a, b, c in [map(int, input().split()) for _ in range(n)]:
    if (k - a) % b == 0 and k >= a:
        total_penguins += c
print(total_penguins)
