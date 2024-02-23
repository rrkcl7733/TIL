n = int(input())
ret = 2
color = input()
for _ in range(1, n):
    c = input()

    if c != color:
        ret += 1
        color = c

print(ret)
