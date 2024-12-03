a, aa = input().split()
b, bb = input().split()

if a.isdigit():
    if b.isdigit():
        print(abs(int(a) - int(b)))
    else:
        print(abs(int(a) + int(bb)) - 1)
else:
    if b.isdigit():
        print(abs(int(aa) + int(b)) - 1)
    else:
        print(abs(int(aa) - int(bb)))
