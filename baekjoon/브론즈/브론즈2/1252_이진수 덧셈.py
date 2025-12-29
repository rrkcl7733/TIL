a, b = input().split()

result = int(a, 2) + int(b, 2)
binary_result = bin(result)[2:]

print(binary_result)
