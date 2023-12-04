a, b = map(int, input().split())
if not a or not b:
  print(0)
  exit()
c = 1 / a + 1 / b
print(int(1 / c))
