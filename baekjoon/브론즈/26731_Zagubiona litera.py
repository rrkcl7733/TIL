a = [0] * 26
for i in input():
    a[ord(i) - 65] += 1
print(chr(a.index(0) + 65))
