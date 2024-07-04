from itertools import product

N, K = map(int, input().split())
length = len(str(N))
t = list(map(int, input().split()))
t.sort(reverse=True)

while 1:
    for n in list(product(t, repeat=length)):
        num = int(''.join(map(str, n)))
        if num <= N:
            print(num)
            exit()
    length -= 1
