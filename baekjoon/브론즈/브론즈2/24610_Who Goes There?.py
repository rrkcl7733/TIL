n, m = map(int, input().split())
teams = [int(input()) for _ in range(m)]
accepted = [0] * m
remaining_capacity = n

for i in range(100):
    for j in range(m):
        if teams[j] > 0 and remaining_capacity > 0:
            accepted[j] += 1
            teams[j] -= 1
            remaining_capacity -= 1

print(*accepted, sep='\n')
