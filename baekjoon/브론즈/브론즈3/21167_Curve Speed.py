try:
  while 1:
    r, s= map(float, input().split())
    print(round(((r * (s + .16)) / .067) ** .5))
except:
  pass
