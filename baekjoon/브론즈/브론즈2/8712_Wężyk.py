n = int(input())

for i in range(n):
    row = range(n * i + 1, n * i + n + 1)
    if i % 2:
        print(*row[::-1])
    else:
        print(*row)
