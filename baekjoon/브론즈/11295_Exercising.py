i = 1
while 1:
    x = int(input())
    if not x:
        exit()
    print(f'User {i}')
    for _ in range(int(input())):
        print(f'{int(input()) * x / 100000:.5f}')
    i += 1