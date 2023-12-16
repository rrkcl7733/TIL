t, n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
t += sum([int(input()) for _ in range(m)])
for i in a:
  if t - i >= 0:
    t -= i
    m += 1
  else:
    break
print(m)
