n = int(input())
a3 = n // 3
n -= a3 * 3
if n == 1:
  a3 -= 1
  a2 = 2
elif n == 2:
  a2 = 1
else:
  a2 = 0
print(a2, a3)
