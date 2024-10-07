s = input().split('.')
answer = [' '.join(i.split()[::-1]) + '.' if i else '' for i in s]

print(*answer)
