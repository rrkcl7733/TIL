n = int(input())
print(str(chr((n % 8 if n % 8 else 8) + 96)) + str((n - 1) // 8 + 1))
