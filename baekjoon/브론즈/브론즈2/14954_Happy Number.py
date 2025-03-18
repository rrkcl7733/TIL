n = int(input())
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = sum(int(digit) ** 2 for digit in str(n))

print('HAPPY' if n == 1 else 'UNHAPPY')
