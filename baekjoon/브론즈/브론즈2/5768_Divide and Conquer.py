import sys


def count_divisors(x):
    count = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            count += 2 if i != x // i else 1
    return count


while 1:
    M, N = map(int, input().split())
    if M < 1:
        exit()

    max_divisors = best_x = -1

    for x in range(M, N + 1):
        y = count_divisors(x)
        if y > max_divisors or (y == max_divisors and x > best_x):
            max_divisors = y
            best_x = x

    print(best_x, max_divisors)
