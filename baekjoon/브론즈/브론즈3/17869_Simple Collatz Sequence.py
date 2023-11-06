n = int(input())
x = 0
while n != 1:
  x += 1
  if n % 2:
    n += 1
  else:
    n //= 2
print(x)
