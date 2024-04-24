input()
sequence = input()

roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
found_numbers = []

for i in range(12):
    if roman_numerals[i] in sequence:
        found_numbers.append(i + 1)

print(*found_numbers)
