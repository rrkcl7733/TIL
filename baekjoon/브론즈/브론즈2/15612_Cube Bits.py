import sys


input = sys.stdin.readline
n = int(input())

for number in [int(input()) for _ in range(n)]:
    if not number:
        print(0)
        continue
    digits = []
    while number:
        digits.append(int(number % 3))
        number //= 3
    print(*digits[::-1], sep='')
