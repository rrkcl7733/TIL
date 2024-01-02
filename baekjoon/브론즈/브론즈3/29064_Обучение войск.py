n = int(input())
a = list(map(int, input().split())).count(1)
if a >= n / 2:
    print(0)
else:
    if n % 2:
        n = n // 2 + 1
    else:
        n //= 2
    print(n - a)
