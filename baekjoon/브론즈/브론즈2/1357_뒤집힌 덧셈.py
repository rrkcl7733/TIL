def rev(n):
    return int(str(n)[::-1])


X, Y = map(int, input().split())

result = rev(rev(X) + rev(Y))
print(result)
