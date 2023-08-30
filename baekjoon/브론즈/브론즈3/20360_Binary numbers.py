for i, j in enumerate(bin(int(input()))[2:][::-1]):
    if j == '1':
        print(i, end=' ')
