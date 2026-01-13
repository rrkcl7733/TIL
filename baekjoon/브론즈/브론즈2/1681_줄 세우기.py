N, L = map(int, input().split())
L = str(L)

count = 0
num = 0
while 1:
    num += 1
    if L in str(num):
        continue
    count += 1
    if count == N:
        print(num)
        break
