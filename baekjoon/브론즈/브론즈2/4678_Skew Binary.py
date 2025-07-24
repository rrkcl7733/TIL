def skew_to_decimal(s):
    n = len(s)
    total = 0
    for i, ch in enumerate(s):
        d = int(ch)
        weight = (1 << (n - i)) - 1
        total += d * weight
    return total

while 1:
    s = input()
    if s == "0":
        exit()
    print(skew_to_decimal(s))
