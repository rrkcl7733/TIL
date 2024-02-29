k, d = map(int, input().split())
sum = 0
i = 0

while 1:
    sum += k
    if sum > d:
        break
    k *= 2
    i += 1

print(i)
