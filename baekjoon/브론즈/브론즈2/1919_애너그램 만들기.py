from collections import Counter


count1 = Counter(input())
count2 = Counter(input())

result = 0
for ch in range(ord('a'), ord('z')+1):
    c = chr(ch)
    result += abs(count1[c] - count2[c])

print(result)
