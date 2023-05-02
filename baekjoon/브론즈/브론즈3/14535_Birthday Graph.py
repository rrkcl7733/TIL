i = 1
while 1:
    n = int(input())
    if not n:
        exit()
    x = [['Jan', 0], ['Feb', 0], ['Mar', 0], ['Apr', 0], ['May', 0], ['Jun', 0], ['Jul', 0], ['Aug', 0], ['Sep', 0], ['Oct', 0], ['Nov', 0], ['Dec', 0]]
    for _ in range(n):
        q, a, b = input().split()
        x[int(a) - 1][1] += 1
    print(f'Case #{i}:')
    for a, b in x:
        print(f'{a}:{"*" * b}')
    i += 1
