from collections import Counter

numbers = [int(input()) for _ in range(int(input()))]
count = Counter(numbers)
max_freq = max(count.values())

result = min([num for num, freq in count.items() if freq == max_freq])

print(result)
