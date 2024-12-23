time = input()
digits = [int(d) for d in time]
binary_digits = [format(d, '04b') for d in digits]

watch_face = [[' ' for _ in range(9)] for _ in range(4)]

for col, binary in enumerate(binary_digits):
    for row in range(4):
        watch_face[row][col * 2] = '*' if binary[3 - row] == '1' else '.'


for row in watch_face[::-1]:
    print(row[0] + ' ' + row[2] + '   ' + row[4] + ' ' + row[6])
