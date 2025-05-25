import sys


lines = sys.stdin.read().splitlines()

max_length = max(len(line) for line in lines)

raggedness = sum((max_length - len(line)) ** 2 for line in lines[:-1])

print(raggedness)
