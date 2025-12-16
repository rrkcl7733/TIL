import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    s1, s2 = input().split()

    if len(s1) != len(s2):
        print('Impossible')
        continue

    if Counter(s1) == Counter(s2):
        print('Possible')
    else:
        print('Impossible')
