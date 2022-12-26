n = int(input())
for i in range(n, int(input()) + 1):
    if not (i - n) % 60:
        print(f'All positions change in year {i}')
