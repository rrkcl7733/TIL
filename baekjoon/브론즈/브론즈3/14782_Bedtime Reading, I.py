n = int(input())
x = 0
for i in range(1, int(n ** .5) + 1):
  if not n % i:
    x += i + n // i
    if i == n // 2:
      x -= i
print(x)
