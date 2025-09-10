from collections import Counter

freq = Counter(input())

if len(freq) < 3:
    print(0)
else:
    sorted_counts = sorted(freq.values(), reverse=True)
    print(sum(sorted_counts[2:]))
