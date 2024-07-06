a = list(input())
b = list(input())

answer = ''.join(sorted(a + b))[:len(a)]
print(answer)
