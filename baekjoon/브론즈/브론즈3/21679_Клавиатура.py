input()
k = list(map(int, input().split()))
input()
for i in map(int, input().split()):
    k[i - 1] -= 1
for i in k:
    print('yes' if i < 0 else 'no')
