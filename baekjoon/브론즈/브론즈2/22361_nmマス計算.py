def count_digits(n, m, a, b):
    digit_count = [0] * 10
    for i in range(n):
        for j in range(m):
            product = a[i] * b[j]
            for digit in str(product):
                digit_count[int(digit)] += 1
    return digit_count


while 1:
    n, m = map(int, input().split())
    if not n:
        break
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*count_digits(n, m, a, b))
