import sys
input = sys.stdin.readline

N = int(input())

freq = {}

for _ in range(N):
    word_count = len(input().split())
    freq[word_count] = freq.get(word_count, 0) + 1

for count in sorted(freq.items()):
    print(*count)
