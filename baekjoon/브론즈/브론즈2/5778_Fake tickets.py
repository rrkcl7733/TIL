from collections import Counter


while 1:
    n, m = map(int, input().split())
    if n < 1:
        exit()

    counter = Counter(map(int, input().split()))
    clones = sum(1 for count in counter.values() if count > 1)
    print(clones)
