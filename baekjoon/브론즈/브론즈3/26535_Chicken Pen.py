n = int(input())
if n == (n ** .5)** 2:
    n = int(n ** .5)
else:
    n = int(n ** .5) + 1
print('x' * (n + 2))
for _ in range(n):
    print('x' + '.' * n + 'x')
print('x' * (n + 2))
