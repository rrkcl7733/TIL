import sys
from collections import Counter


input = sys.stdin.readline
N = int(input())
numbers = [int(input()) for _ in range(N)]

freq = Counter(numbers)

print(max(freq.values()))
