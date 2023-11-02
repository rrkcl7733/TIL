n, x, s = map(int, input().split())
for _ in range(s):
    print('KEEP' if x in list(map(int, input().split()))[1:] else 'REMOVE')
