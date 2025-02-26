import sys

input = sys.stdin.readline


def sum_squared_digits(b, n):
    total = 0
    while n > 0:
        digit = n % b
        total += digit ** 2
        n //= b
    return total


for i in range(int(input())):
    k, b, n = map(int, input().split())
    ssd = sum_squared_digits(b, n)
    print(f'{i + 1} {ssd}')
