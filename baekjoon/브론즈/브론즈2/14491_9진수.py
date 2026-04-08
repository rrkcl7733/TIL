T = int(input())

digits = []
while T > 0:
    digits.append(str(T % 9))
    T //= 9

print(''.join(reversed(digits)))
