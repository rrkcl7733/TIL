import sys
from collections import Counter

text = sys.stdin.read()
counter = Counter()

for ch in text:
    if ch.isalpha():
        counter[ch] += 1

max_count = max(counter.values())
result = [ch for ch in counter if counter[ch] == max_count]

print("".join(sorted(result)))
