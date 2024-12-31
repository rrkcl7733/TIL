A = input().split()
b = input()
print(sum(a.startswith(b) and a != b for a in A))
