import decimal


_, inc0, _, mul1, inc1 = input().split()
inc0 = int(inc0)
mul1 = decimal.Decimal(mul1)
inc1 = int(inc1)
if inc0 * mul1 > inc1:
    print('Power up, Evolve')
elif inc0 * mul1 < inc1:
    print('Evolve, Power up')
else:
    print('Whatever')
