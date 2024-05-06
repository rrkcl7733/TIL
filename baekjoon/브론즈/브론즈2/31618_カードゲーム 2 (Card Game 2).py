from collections import Counter


input()
counter = Counter(map(int, input().split()))
for x in range(1, 200001):
    if counter[x] and counter[x+3] and counter[x+6]:
        print('Yes')
        exit()
print('No')
