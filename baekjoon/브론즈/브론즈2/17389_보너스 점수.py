input()
total = bonus = 0

for i, ch in enumerate(input(), start=1):
    if ch == 'O':
        total += i + bonus
        bonus += 1
    else:
        bonus = 0

print(total)
