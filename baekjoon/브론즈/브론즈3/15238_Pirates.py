n = int(input())
s = input()

alpa = [0] * 26
for i in range(n):
    alpa[ord(s[i]) - ord('a')] += 1

max_count = -1
max_index = -1
for i in range(26):
    if alpa[i] > max_count:
        max_count = alpa[i]
        max_index = i

print(chr(max_index + ord('a')), max_count)
