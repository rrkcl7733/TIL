a, b = map(int, input().split())
t = input()[-1]
if t == 'e':
    print(b if b < a else a)
elif t == 't':
    print(b if a < b else a)
elif t == 'o':
    print(b)
else:
    print(a)
