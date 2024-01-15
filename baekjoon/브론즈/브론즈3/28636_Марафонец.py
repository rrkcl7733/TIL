n = int(input())
total_sec = 0
for _ in range(n):
    m, s = map(int, input().split(':'))
    total_sec += m * 60 + s
h = total_sec // 3600
m = (total_sec % 3600) // 60
s = total_sec % 60
print(f'{h:02}:{m:02}:{s:02}')
