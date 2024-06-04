l, r = map(int, input().split())

for x in range(l, r+1):
    if len(str(x)) == len(set(str(x))):
        print(x)
        break

else:
    print(-1)
