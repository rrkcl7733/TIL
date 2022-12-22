for _ in range(int(input())):
    a, b, c = map(float, input().split())
    print(f'${round(a * b * c, 2):.2f}')
