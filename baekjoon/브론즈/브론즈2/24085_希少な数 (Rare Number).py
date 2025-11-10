from collections import Counter


input()
count = Counter(list(map(int, input().split())))

min_freq = min(count.values())

candidates = [num for num, freq in count.items() if freq == min_freq]
print(min(candidates))
