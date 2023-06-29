w, h, d = map(int, input().split())
w -= 2 * d
h -= 2 * d
print(w * h if w > 0 and h > 0 else 0)
