def digit_sum(n):
    return sum(int(d) for d in str(n))


def find_min_p(n):
    original_sum = digit_sum(n)
    p = 11
    while True:
        if digit_sum(n * p) == original_sum:
            return p
        p += 1


while 1:
    n = int(input())
    if n < 1:
        exit()
    original_sum = digit_sum(n)
    p = 11
    while 1:
        if digit_sum(n * p) == original_sum:
            print(p)
            break
        p += 1
