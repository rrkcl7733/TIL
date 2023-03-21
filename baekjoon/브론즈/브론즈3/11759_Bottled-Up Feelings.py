s, v1, v2 = map(int, input().split())
a = s // v1
while a >= 0:
    if not (s - a * v1) % v2:
        print(a, (s - a * v1) // v2)
        exit()
    else:
        a -= 1
print("Impossible")
