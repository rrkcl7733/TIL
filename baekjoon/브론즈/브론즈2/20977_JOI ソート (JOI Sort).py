input()
S = input()

count_J = S.count('J')
count_O = S.count('O')
count_I = S.count('I')

result = 'J' * count_J + 'O' * count_O + 'I' * count_I

print(result)
