for i in range(int(input())):
  print(f'Data Set {i + 1}:')
  t, n = map(int, input().split())
  a = list(map(int, input().split()))
  x = 1
  t -= 1
  while a[t]:
    t = a[t] - 1
    x += 1
  print(x)
  print()
