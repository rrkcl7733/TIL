A, B = input().split()

sum_A = sum(int(digit) for digit in A)
sum_B = sum(int(digit) for digit in B)

print(sum_A * sum_B)
