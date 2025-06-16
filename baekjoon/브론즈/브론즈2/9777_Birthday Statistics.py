import sys


input = sys.stdin.readline
month_count = [0] * 13

for _ in range(int(input())):
    line = input()
    date = line.split()[1]
    _, month, _ = date.split('/')
    month_count[int(month)] += 1

for month in range(1, 13):
    print(month, month_count[month])
