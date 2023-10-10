q, w, r = map(int, input().split())
o, e = [], []
for i in (q * w, w * r, q * r, q * w * r, q, w, r):
  if i % 2:
    o.append(i)
  else:
    e.append(i)
o.sort(reverse=True)
e.sort(reverse=True)
if o:
  print(o[0])
else:
  print(e[0])
