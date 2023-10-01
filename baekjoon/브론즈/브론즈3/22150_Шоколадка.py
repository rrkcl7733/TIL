for _ in range(int(input())):
  n, *a = map(int, input().split())
  for i in range(0, 2 * n, 2):
    if a[i] + a[i + 1] != n:
      print('yes')
      break
  else:
    print('no')
