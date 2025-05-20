for _ in range(int(input())):
    alpha, beta = input().split()
    if set(alpha) == set(beta):
        print('YES')
    else:
        print('NO')
