for _ in range(int(input())):
    n, x, y = map(int ,input().split())
    a = list(map(int, input().split()))
    print('BOTH' if a[0] == x and a[-1] a== y else 'EASY' if a[0] == x else 'HARD' if a[-1] == y else 'OKAY')
