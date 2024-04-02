a, b = map(int, input().split())
for _ in range(a):
    x, y = map(int, input().split())
    if x != y:
        print('Wrong Answer')
        exit()
for _ in range(b):
    x, y = map(int, input().split())
    if x != y:
        print('Why Wrong!!!')
        exit()
print('Accepted')
