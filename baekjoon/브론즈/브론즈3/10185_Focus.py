for _ in range(int(input())):
    a, b = map(int, input().split())
    print(f'f = {round(a * b / (a + b), 1)}')
