n, m = map(int, input().split())
words = [input().strip() for _ in range(n)]

count = 0
for word in words:
    if len(word) == len(set(word)) and all(ch <= chr(64 + m) for ch in word):
        count += 1

print(count)
