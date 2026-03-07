def sum_digits_in_base(n, base):
    total = 0
    while n > 0:
        n, r = divmod(n, base)
        total += r
    return total


for num in range(1000, 10000):
    s10 = sum_digits_in_base(num, 10)
    s12 = sum_digits_in_base(num, 12)
    s16 = sum_digits_in_base(num, 16)
    if s10 == s12 == s16:
        print(num)
