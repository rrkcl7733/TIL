values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
          'C': 100, 'D': 500, 'M': 1000}

total = 0
aromatic = input()
pairs = [(int(aromatic[i]), aromatic[i+1]) for i in range(0, len(aromatic), 2)]

for i in range(len(pairs)):
    value = pairs[i][0] * values[pairs[i][1]]
    if i < len(pairs) - 1 and values[pairs[i][1]] < values[pairs[i+1][1]]:
        total -= value
    else:
        total += value

print(total)
