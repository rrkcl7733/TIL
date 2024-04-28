n = int(input())
x = 0
for i in range(1, n + 1):
    if not n % i:
        x += i
print(x * 5 - 24)
