n = int(input())
print('|' + '-' * (n - 2) + '|')

for i in range(1, n - 1):
    line = [' '] * (n - 2)
    line[i - 1] = '*'
    line[n - i - 2] = '*'
    print('|' + ''.join(line) + '|')

print('|' + '-' * (n - 2) + '|')
