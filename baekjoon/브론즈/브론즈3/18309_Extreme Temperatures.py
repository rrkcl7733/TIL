m, M = 1e9, -1e9
while 1:
  try:
    a = input().split()[1:]
    for i in range(len(a)):
      p = int(a[i])
      m = min(p, m)
      M = max(p, M)
  except:
    print(m, M)
    break
