p, q = map(int, input().split())
r, s = map(int, input().split())
t, u = map(int, input().split())
print(p + t - r, q + u - s)
print(p + r - t, q + s - u)
print(t + r - p, u + s - q)
