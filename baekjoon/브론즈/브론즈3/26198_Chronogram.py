import sys
input = sys.stdin.readline


d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
for _ in range(int(input())):
    x = 0
    for i in input():
        if i in d.keys():
            x += d[i]
    print(x)
