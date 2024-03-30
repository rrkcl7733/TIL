k = int(input()) ** 2
d1, d2 = map(int, input().split())
print(k - ((d1 - d2) / 2) ** 2)
