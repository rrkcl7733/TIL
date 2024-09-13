import sys
input = sys.stdin.read
data = input().split()

    
for i in range(1, int(data[0]) + 1):
    x = data[i]
    if sum(int(digit) % 9 for digit in x) % 9:
        print('NO')
    else:
        print('YES')
