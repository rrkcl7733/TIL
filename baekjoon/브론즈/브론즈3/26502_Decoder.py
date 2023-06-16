a = ['a', 'e', 'i', 'o', 'u', 'y']
b = ['A', 'E', 'I', 'O', 'U', 'Y']
for _ in range(int(input())):
    x = ''
    for i in input():
        if i in a:
            x += a[(a.index(i) + 1) % 6]
        elif i in b:
            x += b[(b.index(i) + 1) % 6]
        else:
            x += i
    print(x)
