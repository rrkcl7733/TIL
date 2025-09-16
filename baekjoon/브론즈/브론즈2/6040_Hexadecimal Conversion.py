hex_input = input()

if hex_input == "0":
    print("0")
    exit()

binary = bin(int(hex_input, 16))[2:]

padding = (3 - len(binary) % 3) % 3
binary = '0' * padding + binary

octal = ''
for i in range(0, len(binary), 3):
    three_bits = binary[i:i+3]
    octal += str(int(three_bits, 2))

print(octal.lstrip('0'))
