def luhn_check(card_number):
    total = 0
    for i, digit in enumerate(reversed(card_number)):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n >= 10:
                n = n // 10 + n % 10
        total += n
    return total % 10 == 0


for _ in range(int(input())):
    card_number = input().strip()
    print("T" if luhn_check(card_number) else "F")
