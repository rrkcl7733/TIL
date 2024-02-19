n = int(input())
arr = input().split()
for i in range(1, n + 1):
    if arr[i - 1] not in (str(i), 'mumble'):
        print('something is fishy')
        break
else:
    print('makes sense')
