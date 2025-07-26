import sys

inpout = sys.stdin.readline
t_count = s_count = 0

for _ in range(int(input())):
    for ch in input():
        if ch in ('t', 'T'):
            t_count += 1
        elif ch in ('s', 'S'):
            s_count += 1

if t_count > s_count:
    print('English')
else:
    print('French')
