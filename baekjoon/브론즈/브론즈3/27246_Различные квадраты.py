n = int(input())
k = 1
while n >= k ** 2:
    n -= k ** 2
    k += 1
print(k - 1)
