from collections import Counter


for _ in range(int(input())):
    line = input()
    counts = Counter(c for c in line if c.isalpha())
    max_freq = max(counts.values())

    most_common = [ch for ch, cnt in counts.items() if cnt == max_freq]
    if len(most_common) == 1:
        print(most_common[0])
    else:
        print("?")
