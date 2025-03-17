w, s = map(int, input().split())

difference = w - (29260 * s * (s + 1) // 2)

print(difference // 110)
