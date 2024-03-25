n = int(input())
t = input().count('2')
e = n - t
print('2' if t > e else 'e' if e > t else 'yee')
