input()
a = sorted(list(set(map(int, input().split()))))
print(*a, sep='\n')
