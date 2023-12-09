for i in range(int(input())):
  print(f'Data Set {i + 1}:')
  c = 0
  n = int(input())
  x = input()
  for _ in range(n):
    for t in input():
      if t in x:
        c += 1
        break
  print(c)
  print()
