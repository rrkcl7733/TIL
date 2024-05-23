n = int(input()) - 1
ret = 1

while n > 0:
    n //= 2
    ret += 1

print(ret)
