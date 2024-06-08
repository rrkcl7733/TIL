from decimal import Decimal


for _ in range(int(input())):
    a, b, c, d = map(Decimal, input().split())

    ret1 = a + b.sqrt()
    ret2 = c + d.sqrt()

    if ret1 < ret2:
        print("Less")
    elif ret1 > ret2:
        print("Greater")
    else:
        print("Equal")
