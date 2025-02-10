for i in range(int(input())):
    a, b = map(int, input().split())
    remainder = a % b
    print(f'Case {i + 1}: {remainder}')
