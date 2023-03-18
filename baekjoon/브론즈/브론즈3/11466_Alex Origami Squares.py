h, w = map(int, input().split())
a, b = max(h, w), min(h, w)
print(max(a/3 if a/3 <= b else b, b/2))
