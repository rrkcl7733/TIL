n = int(input())
m = int(input())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in a:
    for j in b:
        print(f'{i} as {j}')
