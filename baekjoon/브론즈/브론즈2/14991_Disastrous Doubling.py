MOD = 10**9 + 7

n = int(input())
b = list(map(int, input().split()))
bacteria = 1
for i in range(n):
    bacteria *= 2
    if bacteria < b[i]:
        print('error')
        break
    bacteria -= b[i]
else:
    print(bacteria % MOD)
