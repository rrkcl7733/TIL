words = input()
l = len(words) // 3
a = [words[i:i+l] for i in range(0, len(words), l)]

if a[0] in (a[1], a[2]):
    print(a[0])
else:
    print(a[1])
