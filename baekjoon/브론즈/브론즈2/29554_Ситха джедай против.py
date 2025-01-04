def find_first_day(n, j, l, s, d):
    day = 0
    while 1:
        for i in range(n):
            if j[i] + day * l[i] < s[i] + day * d[i]:
                break
        else:
            return day
        day += 1
        if day > 10000:
            return 'Strong is dark side of the force.'

n = int(input())
j = list(map(int, input().split()))
l = list(map(int, input().split()))
s = list(map(int, input().split()))
d = list(map(int, input().split()))

result = find_first_day(n, j, l, s, d)

print(result)
