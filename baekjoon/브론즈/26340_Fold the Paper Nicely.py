for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(f'Data set: {a} {b} {c}')
    while c:
        a, b = max(a, b), min(a, b)
        a //= 2
        c -= 1
    a, b = max(a, b), min(a, b)
    print(a, b)
    print()
