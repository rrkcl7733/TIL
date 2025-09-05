ans = 0
try:
    while 1:
        line = input()
        ans += line.count('joke')

except:
    print(ans)
