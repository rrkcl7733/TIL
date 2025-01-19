a, b = map(int, input().split())
c = input()
b %= 3
a //= 4
if not b:
    print(c)
elif b == 1:
    print(c[:a] + c[3 * a:] + c[a:3 * a])
else:
    print(c[:a] + c[2 * a:] + c[a:2 * a])
